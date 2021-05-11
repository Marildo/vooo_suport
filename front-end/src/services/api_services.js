import app from '../main'
const axios = app.config.globalProperties.$axios()

const readAllClient = payload => {
  const { page, search, type, limit } = payload
  return axios.get('client', { params: { page, limit, type, search } })
}

const readAllConnector = () => {
  return axios.get('connector')
}

export { readAllClient, readAllConnector }
