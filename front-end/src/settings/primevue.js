import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // 'icons
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'

const primeInit = app => {
  app.use(PrimeVue)
  app.component('p-button', Button)
}
export default primeInit
