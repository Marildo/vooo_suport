<template>
  <Toolbar>
    <template #right>
      <InputText
        type="text"
        v-model="search"
        placeholder="Search"
        class="input_search"
      />

      <p-button
        type="button"
        label="Buscar"
        :icon="state.inputIcon"
        iconPos="right"
        @click="toSearch()"
      />
    </template>
  </Toolbar>
  <div>
    <h1>Clientes</h1>
    <button @click="loadClients()">Load</button>
    <div>
      <DataTable :value="state.clients" responsiveLayout="scroll" showGridlines>
        <Column
          v-for="col in columns"
          :key="col.id"
          :field="col.field"
          :header="col.title"
        ></Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive, ref } from 'vue'
import axios from 'axios'
import Toolbar from 'primevue/toolbar'
import InputText from 'primevue/inputtext'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

export default {
  name: 'Client',
  components: {
    DataTable,
    Column,
    Toolbar,
    InputText
  },

  setup () {
    const search = ref('')

    onMounted(() => {
      loadClients()
    })

    const state = reactive({
      clients: [],
      inputIcon: 'pi pi-search'
    })

    const columns = [
      { field: 'id', title: 'Id' },
      { field: 'name', title: 'Nome' }
    ]

    function loadClients () {
      console.log('clicked')
      axios
        .get('http://127.0.0.1:4000/client')
        .then(response => response.data)
        .then(data => (state.clients = data))
        .catch(erros => console.log(erros))
    }

    function toSearch () {
      console.log('inputIcon: ', state.inputIcon)
      state.inputIcon = 'pi pi-spin pi-spinner'
      setTimeout(() => (state.inputIcon = 'pi pi-search'), 1000)
      console.log('inputIcon: ', state.inputIcon)
    }

    return {
      state,
      columns,
      loadClients,
      toSearch,
      search
    }
  }
}
</script>

<style scoped>
.input_search {
  width: 30vw;
}
</style>
