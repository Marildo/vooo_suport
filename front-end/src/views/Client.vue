<template>
  <div>
    <h1>Clientes</h1>
    <button @click="loadClients()">Load</button>
  </div>
</template>

<script>
import { onMounted } from 'vue'
export default {
  name: 'Client',
  setup () {
    onMounted(() => {
      console.log('mountend')
    })

    function loadClients () {
      console.log('clicked')
      return 1
    }

    return {
      loadClients
    }
  }
}
</script>
