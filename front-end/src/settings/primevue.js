import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // 'icons
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'
import Toolbar from 'primevue/toolbar'

const primeInit = app => {
  app.use(PrimeVue)
  app.component('p-button', Button)
  app.component('p-toolbar', Toolbar)
}
export default primeInit
