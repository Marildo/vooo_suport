<template>
  <div>
    <p-dataTable
      :value="state.connectors"
      responsiveLayout="scroll"
      showGridlines
      :globalFilterFields="['name']"
      v-model:filters="filters"
    >
      <template #header>
        <div class="table-header">
          <span class="p-input-icon-left">
            <i class="pi pi-search" />
            <p-inputText
              v-model="filters['global'].value"
              placeholder="Pesquisa"
            />
          </span>
          <p-button
            type="button"
            icon="pi pi-filter-slash"
            label="Limpar"
            @click="clearFilter()"
          />
        </div>
      </template>
      <p-column
        v-for="col in columns"
        :key="col.id"
        :field="col.field"
        :header="col.title"
      ></p-column>
    </p-dataTable>
  </div>
</template>

<script>
import { onMounted, reactive, ref } from 'vue'
import { readAllConnector } from '@/services/api_services'
import { FilterMatchMode, FilterOperator } from 'primevue/api'
export default {
  name: 'Connector',

  setup () {
    const columns = [
      { field: 'connector_id', title: 'Id' },
      { field: 'name', title: 'Nome' },
      { field: 'type.name', title: 'Tipo' }
    ]

    const filters = ref({
      global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      name: {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
      }
    })

    const state = reactive({
      connectors: []
    })

    const clearFilter = () => {
      filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        name: {
          operator: FilterOperator.AND,
          constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        }
      }
    }

    onMounted(() => {
      readAllConnector()
        .then(resp => {
          state.connectors = resp.data
        })
        .catch(erros => console.log(erros))
    })

    return {
      columns,
      state,
      filters,
      clearFilter
    }
  }
}
</script>
<style lang="scss" scoped>
.table-header {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  padding: 0.3em;
}

.table-header input {
  margin-right: 0.8em;
  height: 40px;
}
</style>
