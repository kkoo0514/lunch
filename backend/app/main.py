from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import errorcode
import os


app = FastAPI(title="FastAPI Backend")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 프로덕션에서는 특정 도메인만 허용하도록 수정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    result = []
    cnx = None
    cursor = None
    message = 'success'
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        # 2) 커넥션 생성
        cursor = conn.cursor()

        # 3) 쿼리 실행
        cursor.execute("SELECT * FROM t_place;")
        rows = cursor.fetchall()

        result = rows

    except mysql.connector.Error as err:
        # 에러 처리
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            message = "사용자 이름 또는 비밀번호 오류"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            message = "데이터베이스가 없습니다"
        else:
            message = err
    finally:
        # 4) 자원 정리
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()
    return {"message": message,"data":result}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 