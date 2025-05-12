<script setup lang="ts">
import { onMounted, ref } from 'vue';
import axios from 'axios';

const select = ref('March 2025');
const items = ref(['March 2025', 'April 2025', 'May 2025', 'June 2025']);
const item = ref()

const fetchMenus = async () => {
  try {
    const response = await axios.get('http://localhost:8000/getPlace')
    item.value = response.data.result
  } catch (error) {
    console.error('메뉴 목록을 가져오는데 실패했습니다:', error)
  }
}

onMounted(() => {
  fetchMenus()
})

</script>
<template>
    <v-card elevation="10" class="">
        <v-card-item class="pa-6">
        <div class="d-flex align-center mb-1">
                <div>
                    <h3 class="card-title"></h3>
                </div>

                <div class="ms-auto">
                    <v-select v-model="select" :items="items" hide-details density="compact"  variant="outlined" rounded="md"></v-select>
                </div>
            </div>
        <v-table class="month-table">
            <thead>
                <tr>
                    <th class="text-subtitle-1 font-weight-bold">Seq</th>
                    <th class="text-subtitle-1 font-weight-bold">Category</th>
                    <th class="text-subtitle-1 font-weight-bold">Menu</th>
                    <th class="text-subtitle-1 font-weight-bold">PlaceName</th>
                    <th class="text-subtitle-1 font-weight-bold">PriceAvg</th>
                    <th class="text-subtitle-1 font-weight-bold">Rating</th>
                    <th class="text-subtitle-1 font-weight-bold">RatingCount</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in item" :key="item.name" class="month-item">
                    <td>
                        <p class="text-15 font-weight-medium">{{ item.id }}</p>
                    </td>
                    <td>
                        <h6 class="text-body-1 text-muted">{{ item.category }}</h6>
                    </td>
                    <td>
                        <h6 class="text-subtitle-1 text-muted">{{ item.cuisine_type }}</h6>
                    </td>
                    <td>
                        <div class="">
                                <h6 class="text-subtitle-1 font-weight-bold">{{ item.name }}</h6>
                                <div class="text-13 mt-1 text-muted opacity-90">{{ item.post }}</div>
                        </div>
                    </td>
                    <td>
                        <h6 class="text-subtitle-1 text-muted">{{ item.priceAvg }}</h6>
                    </td>
                    <td>
                        <h6 class="text-subtitle-1 text-muted">{{ item.rating }}</h6>
                    </td>
                    <td>
                        <v-chip  :class="'rounded-md bg-' + item.ratingCount "   size="small" >{{
                            item.ratingCount
                        }}</v-chip>
                    </td>
                </tr>
            </tbody>
        </v-table>
        </v-card-item>
    </v-card>
</template>
