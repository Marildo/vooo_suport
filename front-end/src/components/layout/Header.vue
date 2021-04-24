<template>
  <header>
    <img alt="Vooo logo" src="../../assets/images/logo.png" />
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/about">Clientes</router-link></li>
        <li><router-link to="/">Conectores</router-link></li>
        <li><router-link to="/">Monitoramento</router-link></li>
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
  margin:  0.1em 0.2em;
}

nav ul li a {
  background-color: #42618a;
  box-shadow: 0px 0px 3px 1px rgba(152,193,217,0.38);
  color: $light;
  padding: 0.8em;
  text-decoration: none;
  display: inline-block;
  width: 100px;
}

nav ul li a:hover {
  background-color: $light;
  color: #42618a;
  border-bottom: 1px $accent solid;
}
</style>
