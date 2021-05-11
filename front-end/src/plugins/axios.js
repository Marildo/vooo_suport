import axios from 'axios'

export default {
  install: (app, options) => {
    app.config.globalProperties.$axios = () => {
      axios.defaults.baseURL = 'http://127.0.0.1:4000/'
      return axios
    }
  }
}
