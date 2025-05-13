from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from mysql.connector import errorcode
import os
from pydantic import BaseModel
from typing import Optional

class PlaceForm(BaseModel):
    name: str
    address: str
    phone: str
    category: str
    cuisine_type: str
    created_at: str

class PlaceRequest(BaseModel):
    id: int

app = FastAPI(title="FastAPI Backend")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 프로덕션에서는 특정 도메인만 허용하도록 수정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

@app.get("/getPlace")
async def getPlace():
    result = []
    cursor = None
    message = 'success'
    try:
        # 2) 커넥션 생성
        cursor = conn.cursor()

        # 3) 쿼리 실행
        cursor.execute("select id, name, category, cuisine_type, (select AVG(rating) from t_place_review where id = tp.id group by id) as rating, (select count(rating) from t_place_review where id = tp.id group by id) as ratingCount, (select AVG(price) from t_place_review where id = tp.id group by id) as priceAvg from t_place tp;")
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]


        result = [dict(zip(columns, row)) for row in rows]


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
    return {"message": message,"result":result}

@app.get("/getPlaceById/{id}")
async def getPlaceById(id : int):
    result = None
    cursor = None
    message = 'success'

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM t_place WHERE id = %s"
        cursor.execute(query, (id,))
        row = cursor.fetchone()

        if row:
            columns = [desc[0] for desc in cursor.description]
            result = dict(zip(columns, row))
        else:
            message = "No data found"
            result = {}

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            message = "사용자 이름 또는 비밀번호 오류"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            message = "데이터베이스가 없습니다"
        else:
            message = str(err)
    finally:
        if cursor:
            cursor.close()

    return {"message": message, "result": result}

@app.put("/savePlace/{id}")
async def save_place(id: str, place: PlaceForm):
    cursor = conn.cursor()

    query = """
            UPDATE t_place
            SET name = %s, address = %s, phone = %s, category = %s, cuisine_type = %s, created_at = %s
            WHERE id = %s \
            """
    cursor.execute(query, (place.name, place.address, place.phone, place.category, place.cuisine_type, place.created_at, id))
    message = "Place updated successfully"

    conn.commit()
    return {"message": message, "id": id}

@app.post("/savePlace")
async def create_place(place: PlaceForm):
    cursor = conn.cursor()

    query = """
            INSERT INTO t_place (name, address, phone, category, cuisine_type, created_at)
            VALUES ( %s, %s, %s, %s, %s, NOW()) \
            """
    cursor.execute(query, (place.name, place.address, place.phone, place.category, place.cuisine_type))
    conn.commit()
    return {"message": "Place inserted successfully"}