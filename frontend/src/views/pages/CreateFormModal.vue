<template>
    <div class="modal-backdrop" >
      <div class="modal-container">
        <div class="modal-header">상세보기</div>
  
        <div class="modal-body">
            <input type="hidden" style="display:none" v-model="form.id"/>
            <table class="modal-table">
      <tbody>
        <tr>
          <th><label>상호</label></th>
          <td><input type="text" v-model="form.name" /></td>

          <th><label>주소</label></th>
          <td><input type="text" v-model="form.address" /></td>
        </tr>

        <tr>
          <th><label>전화번호</label></th>
          <td><input type="text" v-model="form.phone" /></td>

          <th><label>대분류</label></th>
          <td>
            <select v-model="form.category" >
              <option label="한식" value="한식"/>
              <option label="중식" value="중식"/>
              <option label="일식" value="일식"/>
              <option label="양식" value="양식"/>
              <option label="기타" value="기타"/>
            </select>
          </td>
        </tr>

        <tr>
          <th><label>소분류</label></th>
          <td><input type="text" v-model="form.cuisine_type" /></td>
          <th><label>등록일</label></th>
          <td><input type="date" v-model="form.created_at" disabled /></td>
        </tr>


      </tbody>
    </table>
        </div>
  
        <div class="modal-footer">
          <button class="btn btn-save" @click="save">저장</button>
          <button class="btn btn-cancel" @click="close">취소</button>
        </div>
      </div>
    </div>
  </template>
  
  
<script setup>
import axios from 'axios'
import { reactive, defineExpose,defineEmits } from 'vue'
// import { useStore } from 'vuex'
// import { useRouter } from 'vue-router'

// const store = useStore()
// const router = useRouter()

const form = reactive({
  id: '',
  name: '',
  address:'',
  phone:'',
  category:'',
  cuisine_type: '',
  created_at: '',
})

const emit = defineEmits(['close'])
const close = () => emit('close')

const openModal = async (id) => {
    const response = await axios.get('http://10.1.31.189:8000/getPlaceById/'+id )
    form.id = id
    form.name = response.data.result.name
    form.address = response.data.result.address
    form.phone = response.data.result.phone
    form.category = response.data.result.category
    form.cuisine_type = response.data.result.cuisine_type
    form.created_at = response.data.result.created_at
    
}

defineExpose({ openModal });

const save = async() => {
  try {
    let response = null;
    if (form.id) {
      // 수정
      response = await axios.put(`http://10.1.31.189:8000/savePlace/${form.id}`, form)
    } else {
      // 생성
      response = await axios.post('http://10.1.31.189:8000/savePlace', form, {
        headers: {
          'Content-Type': 'application/json',
        }
      })
    }
    if(response.status == 200){
      alert('저장되었습니다.')
      emit('refresh')
      close()
    }
  } catch (error) {
    if (error.response && error.response.status === 401) {
      alert(error.response.message)
      // store.dispatch('logout')  // Vuex 상태 관리
      // router.push('/login')  // 로그인 페이지로 리디렉션
    }else{
      alert('오류가 발생했습니다.')
      console.error('데이터 가져오기 실패:', error)
    }
  }
}

</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
}

.modal-container {
  background: white;
  width: 900px;
  max-height: 95vh;
  overflow-y: auto;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.modal-header {
  background: #2d3748;
  color: white;
  padding: 16px;
  font-size: 1.1rem;
  font-weight: bold;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.modal-body {
  padding: 24px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.modal-table label {
  font-weight: 600;
  margin-bottom: 6px;
  font-size: 0.9rem;
}

.modal-table {
  width: 100%;
}

.modal-table input,
.modal-table select,
.modal-table textarea {
  padding: 8px;
  font-size: 0.9rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.modal-table textarea {
  resize: none;
  height: 80px;
}

.modal-table input:disabled {
  background-color: #f3f3f3;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  padding: 16px 24px;
  border-top: 1px solid #eee;
}

.btn {
  padding: 8px 20px;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  font-weight: bold;
}

.btn-save {
  background-color: #3182ce;
  color: white;
}

.btn-save:hover {
  background-color: #2563eb;
}

.btn-cancel {
  background-color: #e53e3e;
  color: white;
}

.btn-cancel:hover {
  background-color: #c53030;
}
</style>
