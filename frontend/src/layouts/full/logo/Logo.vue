<script setup>
import Logo from "@/assets/images/logos/logo.png";

</script>
<template>
  <div class="logo" style="text-align: center;">
      <RouterLink to="/">
          <img :src="Logo" alt="logo" />
      </RouterLink>
  </div>
</template>
