import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import primeInit from './settings/primevue'

const app = createApp(App)
app.use(store)
app.use(router)
primeInit(app)
app.mount('#app')
