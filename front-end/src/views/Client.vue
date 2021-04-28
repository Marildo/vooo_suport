<template>
  <div>
    <h1>Clientes</h1>
    <button @click="loadClients()">Load</button>

    {{ state.clients }}
  </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import axios from 'axios'

export default {
  name: 'Client',
  setup () {
    onMounted(() => {
      loadClients()
    })

    const state = reactive({
      clients: []
    })

    function loadClients () {
      console.log('clicked')
      axios
        .get('http://127.0.0.1:4000/client')
        .then(response => response.data)
        .then(data => (state.clients = data))
        .catch(erros => console.log(erros))
    }

    return {
      loadClients,
      state
    }
  }
}
</script>
