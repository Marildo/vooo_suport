import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // 'icons
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'
import Toolbar from 'primevue/toolbar'
import InputText from 'primevue/inputtext'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'

const primeInit = app => {
  app.use(PrimeVue)
  app.component('p-button', Button)
  app.component('p-toolbar', Toolbar)
  app.component('p-inputText', InputText)
  app.component('p-dataTable', DataTable)
  app.component('p-column', Column)
}
export default primeInit
