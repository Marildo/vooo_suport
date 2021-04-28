<template>
  <div>
    <h1>Clientes</h1>
    <button @click="loadClients()">Load</button>
    <div>
      <DataTable :value="state.clients" responsiveLayout="scroll" showGridlines>
        <Column field="id" header="Id"></Column>
        <Column field="name" header="Name" aling=""></Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import axios from 'axios'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

export default {
  name: 'Client',
  components: {
    DataTable,
    Column
  },

  setup () {
    onMounted(() => {
      // loadClients()
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
