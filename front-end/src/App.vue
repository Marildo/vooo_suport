<template>
  <div id="app">
    <Header />
    <main>
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/layout/Header'
import Footer from '@/components/layout/Footer'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },

  setup () {
    return { }
  }
}
</script>

<style lang="scss">
*{
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  line-height: 1;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
main{
    min-height: 88vh;
}
#app {
  text-align: center;
  color: #2c3e50;
}
</style>
