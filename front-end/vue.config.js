module.exports = {
  css: {
    loaderOptions: {
      sass: {
        prependData: `
            @import "@/css/app.variables.scss";
          `
      }
    }
  }
}
