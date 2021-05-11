import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from './plugins/axios'

import primeInit from './settings/primevue'

const app = createApp(App)
app.use(store)
app.use(router)
app.use(axios)
primeInit(app)
app.mount('#app')

export default app
