<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'
import CreateFormModal from './CreateFormModal.vue'

interface Menu {
  id: string
  name: string
  votes: string
  category: string
  cuisine_type: string
}

const modal = ref()
const menus = ref<Menu[]>([])
const isModalOpen = ref(false)

const fetchMenus = async () => {
  try {
    const response = await axios.get('http://localhost:8000/getPlace')
    menus.value = response.data.result
  } catch (error) {
    console.error('메뉴 목록을 가져오는데 실패했습니다:', error)
  }
}

const deleteMenu = async (id: string) => {
  try {
    await axios.post('http://localhost:8000/deletePlace', { id })
    menus.value = menus.value.filter(menu => menu.id !== id)
  } catch (error) {
    console.error('메뉴 삭제에 실패했습니다:', error)
  }
}

const refreshTabulator = () => {
  // 테이블 새로고침 로직
}

const openDetail = (id : id) => {
  isModalOpen.value = true
  modal.value?.openModal(id)
}

onMounted(() => {
  fetchMenus()
})
</script>

<template>
  <createFormModal v-if="isModalOpen" @close="isModalOpen = false" @refresh="refreshTabulator" ref="modal"/>
  <div class="place-list">
    <div class="header-actions">
      <button class="add-button" @click="openDetail">새 음식점 등록</button>
    </div>
    
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>번호</th>
            <th>대분류</th>
            <th>소분류</th>
            <th>상호명</th>
            <th>별점</th>
            <th>관리</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(menu, index) in menus" :key="menu.id" @click="openDetail(menu.id)">
            <td>{{ index + 1 }}</td>
            <td>{{ menu.name }}</td>
            <td>{{ menu.category }}</td>
            <td>{{ menu.cuisine_type }}</td>
            <td>{{ menu.votes }}</td>
            <td>
              <button class="delete-button" @click="deleteMenu(menu.id)">삭제</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.place-list {
  padding: 20px;
}

.header-actions {
  margin-bottom: 20px;
  display: flex;
  justify-content: flex-end;
}

.add-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s;
}

.add-button:hover {
  background-color: #45a049;
}

.table-container {
  overflow-x: auto;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
}

th, td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f8f9fa;
  color: #333;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 14px;
}

tr:hover {
  background-color: #f5f5f5;
}

.delete-button {
  background-color: #dc3545;
  color: white;
  padding: 6px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
  transition: background-color 0.3s;
}

.delete-button:hover {
  background-color: #c82333;
}

/* 반응형 디자인 */
@media screen and (max-width: 768px) {
  .place-list {
    padding: 10px;
  }

  th, td {
    padding: 8px 10px;
    font-size: 14px;
  }

  .add-button {
    padding: 8px 16px;
    font-size: 13px;
  }

  .delete-button {
    padding: 4px 8px;
    font-size: 12px;
  }
}
</style> 