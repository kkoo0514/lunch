<script setup lang="ts">
import { ref } from 'vue'

interface Menu {
  id: number
  name: string
  votes: number
}

const menus = ref<Menu[]>([])
const newMenu = ref('')
const drawer = ref(true)
const rail = ref(true)

const addMenu = () => {
  if (newMenu.value.trim()) {
    menus.value.push({
      id: Date.now(),
      name: newMenu.value.trim(),
      votes: 0
    })
    newMenu.value = ''
  }
}

const deleteMenu = (id: number) => {
  menus.value = menus.value.filter(menu => menu.id !== id)
}

const voteMenu = (id: number) => {
  const menu = menus.value.find(menu => menu.id === id)
  if (menu) {
    menu.votes++
  }
}
</script>

<template>
  <div>
    <!-- 사이드바 -->
    <aside>
      <div>
        <img src="https://randomuser.me/api/portraits/men/85.jpg" alt="Profile" />
        <span v-if="!rail">점심 메뉴 추천</span>
        <button @click.stop="rail = !rail">메뉴</button>
      </div>

      <nav>
        <a href="#">홈</a>
        <a href="#">히스토리</a>
        <a href="#">설정</a>
      </nav>
    </aside>

    <!-- 메인 컨텐츠 -->
    <div>
      <!-- 헤더 -->
      <header>
        <button @click="drawer = !drawer">메뉴</button>
        <h1>오늘 점심 뭐 먹지?</h1>
      </header>

      <!-- 메인 컨텐츠 영역 -->
      <main>
        <!-- 메뉴 목록 -->
        <div>
          <div v-for="menu in menus" :key="menu.id">
            <div>
              <h3>{{ menu.name }}</h3>
              <button @click="deleteMenu(menu.id)">삭제</button>
            </div>
            <div>
              <span>{{ menu.votes }}표</span>
              <button @click="voteMenu(menu.id)">투표하기</button>
            </div>
          </div>
        </div>

        <!-- 새 메뉴 추가 -->
        <div>
          <h2>새 메뉴 추가</h2>
          <div>
            <input
              v-model="newMenu"
              type="text"
              placeholder="메뉴 이름"
              @keyup.enter="addMenu"
            />
            <button @click="addMenu">추가</button>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>
