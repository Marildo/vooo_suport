<template>
  <p-toolbar>
    <template #right>
      <p-inputText
        type="text"
        v-model="state.search"
        placeholder="Id | CNPJ| Nome | EC "
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
  </p-toolbar>
  <div>
    <h1>Clientes</h1>
    <button @click="loadClients({page:3})">Load</button>
    <div>
      <p-dataTable
        :value="state.clients"
        responsiveLayout="scroll"
        showGridlines
      >
        <p-column
          v-for="col in columns"
          :key="col.id"
          :field="col.field"
          :header="col.title"
        ></p-column>
      </p-dataTable>
      <p-paginator
        v-model:first="state.first"
        :rows="limit"
        :totalRecords="state.totalClients"
        @page="loadClients($event)"
      >
          <template #right="slotProps">
        Page: {{slotProps.state.page}}
        First: {{slotProps.state.first}}
        Rows: {{slotProps.state.rows}}
        Total: {{state.totalClients}}
    </template>
      </p-paginator>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import axios from 'axios'

export default {
  name: 'Client',
  components: {},

  setup () {
    onMounted(() => {
      loadClients({ page: 0 })
    })

    const limit = 10

    const state = reactive({
      search: '',
      clients: [],
      inputIcon: 'pi pi-search',
      totalClients: 0
    })

    const columns = [
      { field: 'id', title: 'Id' },
      { field: 'name', title: 'Nome' }
    ]

    function loadClients (event) {
      const { page } = event
      const url = 'http://127.0.0.1:4000/client'
      axios
        .get(url, { params: { page, limit } })
        .then(response => response.data)
        .then(response => {
          state.clients = response.data
          state.totalClients = response.total
        })
        .catch(erros => console.log(erros))
    }

    function toSearch () {
      state.inputIcon = 'pi pi-spin pi-spinner'
      setTimeout(() => (state.inputIcon = 'pi pi-search'), 1000)
    }

    return {
      state,
      columns,
      limit,
      loadClients,
      toSearch
    }
  }
}
</script>

<style scoped>
.input_search {
  width: 30vw;
  margin-right: 0.5em;
}
</style>
