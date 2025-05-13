<script setup lang="ts">
import { ref, nextTick  } from 'vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import ProductPerformance from '@/components/dashboard/ProductPerformance.vue';
import CreateFormModal from '@/views/pages/CreateFormModal.vue'

const isModalOpen = ref(false)
const modal = ref()
const list = ref()

const refreshTabulator = () => {
  // 테이블 새로고침 로직
  list.value?.fetchMenus()
}

const openDetail = async (id : string) => {
  isModalOpen.value = true
  await nextTick()
  modal.value?.openModal(id)
}


</script>
<template>
    <CreateFormModal v-if="isModalOpen" @close="isModalOpen = false" @refresh="refreshTabulator" ref="modal"/>
    <v-row>
        <v-col cols="12" md="12">
            <UiParentCard title="메뉴 추가 하는 화면임.">
                <div class="pa-7 pt-1"><p class="text-body-1">메뉴 추가</p></div>
            </UiParentCard>
            <br/>
            <button class="add-button" @click="()=>openDetail('')">새 음식점 등록</button>
            <ProductPerformance @getOpenDetail="openDetail" ref="list"/>
        </v-col>
    </v-row>
</template>
