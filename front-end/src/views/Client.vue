<template>
  <p-toolbar>
    <template #right>
      <p-combobox
        v-model="state.selectedsearchTypes"
        :options="searchTypes"
        optionLabel="name"
        optionvalue="code"
        class="combo_type"
      >
      </p-combobox>
      <p-inputText
        type="text"
        v-model="state.search"
        placeholder="Digite sua busca"
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
        v-if="state.pagination"
        v-model:first="state.first"
        :rows="limit"
        :totalRecords="state.totalClients"
        @page="loadClients($event)"
      >
        <template #right="slotProps">
          Page: {{ slotProps.state.page }} First:
          {{ slotProps.state.first }} Rows: {{ slotProps.state.rows }} Total:
          {{ state.totalClients }}
        </template>
      </p-paginator>
    </div>
  </div>
</template>

<script>
import { onMounted, reactive } from 'vue'
import { readAllClient } from '@/services/api_services'

export default {
  name: 'Client',
  components: {},

  setup () {
    const columns = [
      { field: 'id', title: 'Id' },
      { field: 'name', title: 'Nome' },
      { field: 'document.number', title: 'CNPJ' },
      { field: 'aggregator.name', title: 'Agregador' }
    ]

    const searchTypes = [
      { type: '1', name: 'Id' },
      { type: '2', name: 'CNPJ' },
      { type: '3', name: 'Nome' },
      { type: '4', name: 'EC' },
      { type: '5', name: 'Matriz' },
      { type: '6', name: 'Conector' }
    ]

    let limit = 10

    const state = reactive({
      search: '',
      selectedsearchTypes: searchTypes[0],
      clients: [],
      inputIcon: 'pi pi-search',
      totalClients: 0,
      pagination: true
    })

    onMounted(() => {
      limit = 10
      loadClients({ page: 0 })
    })

    function loadClients (payload) {
      readAllClient({ ...payload, limit })
        .then(response => {
          state.clients = response.data.data
          state.totalClients = response.data.total
        })
        .catch(erros => console.log(erros))
        .finally(() => {
          state.inputIcon = 'pi pi-search'
        })
    }

    function toSearch () {
      state.pagination = false
      const { type } = state.selectedsearchTypes
      loadClients({ page: 0, search: state.search, type })
    }

    return {
      state,
      columns,
      searchTypes,
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
  height: 37px;
  margin-right: 0.5em;
}

.combo_type {
  height: 37px;
  margin-right: 0.5em;
}
</style>
