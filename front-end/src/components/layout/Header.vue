<template>
  <header>
    <img alt="Vooo logo" src="../../assets/images/logo.png" />
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/client">Clientes</router-link></li>
        <li><router-link to="/conectores">Conectores</router-link></li>
        <li><router-link to="/monitoramento">Monitoramento</router-link></li>
         <li><router-link to="/about">About</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style lang="scss" scoped>
header {
  background-color: $primary;
  display: flex;
}
img {
  margin: 0.3em;
  width: 70px;
  height: 42px;
}
nav ul {
  list-style: none;
  padding: 0;
  margin: 0.3em;
}

nav ul li {
  display: inline;
  text-align: center;
  margin: 0.1em 0.2em;
}

nav ul li a {
  background-color: #42618a;
  box-shadow: $shadow;
  color: $light;
  padding: 0.8em;
  text-decoration: none;
  display: inline-block;
  width: 130px;

  &.router-link-exact-active {
    border-bottom: 1px $accent solid;
  }
}

nav ul li a:hover {
  background-color: $light;
  color: #42618a;
}
</style>
