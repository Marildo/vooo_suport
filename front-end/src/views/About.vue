<template>
  <div>
    <h5>Basic</h5>
    <p-button label="Submit" />
    <p-button label="Disabled" disabled="disabled" />
    <p-button label="Link" class="p-p-button-link" />

    <h5>Icons</h5>
    <p-button icon="pi pi-check" />
    <p-button label="Submit" icon="pi pi-check" />
    <p-button label="Submit" icon="pi pi-check" iconPos="right" />

    <h5>Severities</h5>
    <p-button label="Primary" />
    <p-button label="Secondary" class="p-p-button-secondary" />
    <p-button label="Success" class="p-p-button-success" />
    <p-button label="Info" class="p-p-button-info" />
    <p-button label="Warning" class="p-p-button-warning" />
    <p-button label="Help" class="p-p-button-help" />
    <p-button label="Danger" class="p-p-button-danger" />

    <h5>Raised p-buttons</h5>
    <p-button label="Primary" class="p-p-button-raised" />
    <p-button label="Secondary" class="p-p-button-raised p-p-button-secondary" />
    <p-button label="Success" class="p-p-button-raised p-p-button-success" />
    <p-button label="Info" class="p-p-button-raised p-p-button-info" />
    <p-button label="Warning" class="p-p-button-raised p-p-button-warning" />
    <p-button label="Help" class="p-p-button-raised p-p-button-help" />
    <p-button label="Danger" class="p-p-button-raised p-p-button-danger" />

    <h5>Rounded p-buttons</h5>
    <p-button label="Primary" class="p-p-button-rounded" />
    <p-button label="Secondary" class="p-p-button-rounded p-p-button-secondary" />
    <p-button label="Success" class="p-p-button-rounded p-p-button-success" />
    <p-button label="Info" class="p-p-button-rounded p-p-button-info" />
    <p-button label="Warning" class="p-p-button-rounded p-p-button-warning" />
    <p-button label="Help" class="p-p-button-rounded p-p-button-help" />
    <p-button label="Danger" class="p-p-button-rounded p-p-button-danger" />

    <h5>Text p-buttons</h5>
    <p-button label="Primary" class="p-p-button-text" />
    <p-button label="Secondary" class="p-p-button-secondary p-p-button-text" />
    <p-button label="Success" class="p-p-button-success p-p-button-text" />
    <p-button label="Info" class="p-p-button-info p-p-button-text" />
    <p-button label="Warning" class="p-p-button-warning p-p-button-text" />
    <p-button label="Help" class="p-p-button-help p-p-button-text" />
    <p-button label="Danger" class="p-p-button-danger p-p-button-text" />
    <p-button label="Plain" class="p-p-button-text p-p-button-plain" />

    <h5>Raised Text p-buttons</h5>
    <p-button label="Primary" class="p-p-button-raised p-p-button-text" />
    <p-button
      label="Secondary"
      class="p-p-button-raised p-p-button-secondary p-p-button-text"
    />
    <p-button
      label="Success"
      class="p-p-button-raised p-p-button-success p-p-button-text"
    />
    <p-button label="Info" class="p-p-button-raised p-p-button-info p-p-button-text" />
    <p-button
      label="Warning"
      class="p-p-button-raised p-p-button-warning p-p-button-text"
    />
    <p-button label="Help" class="p-p-button-raised p-p-button-help p-p-button-text" />
    <p-button
      label="Danger"
      class="p-p-button-raised p-p-button-danger p-p-button-text"
    />
    <p-button
      label="Plain"
      class="p-p-button-raised p-p-button-text p-p-button-plain"
    />

    <h5>Outlined p-buttons</h5>
    <p-button label="Primary" class="p-p-button-outlined" />
    <p-button label="Secondary" class="p-p-button-outlined p-p-button-secondary" />
    <p-button label="Success" class="p-p-button-outlined p-p-button-success" />
    <p-button label="Info" class="p-p-button-outlined p-p-button-info" />
    <p-button label="Warning" class="p-p-button-outlined p-p-button-warning" />
    <p-button label="Help" class="p-p-button-outlined p-p-button-help" />
    <p-button label="Danger" class="p-p-button-outlined p-p-button-danger" />

    <h5>Rounded Icon p-buttons</h5>
    <p-button icon="pi pi-bookmark" class="p-p-button-rounded p-p-button-secondary" />
    <p-button icon="pi pi-search" class="p-p-button-rounded p-p-button-success" />
    <p-button icon="pi pi-user" class="p-p-button-rounded p-p-button-info" />
    <p-button icon="pi pi-bell" class="p-p-button-rounded p-p-button-warning" />
    <p-button icon="pi pi-heart" class="p-p-button-rounded p-p-button-help" />
    <p-button icon="pi pi-times" class="p-p-button-rounded p-p-button-danger" />
    <p-button icon="pi pi-check" class="p-p-button-rounded" />

    <h5>Rounded Text Icon p-buttons</h5>
    <p-button icon="pi pi-check" class="p-p-button-rounded p-p-button-text" />
    <p-button
      icon="pi pi-bookmark"
      class="p-p-button-rounded p-p-button-secondary p-p-button-text"
    />
    <p-button
      icon="pi pi-search"
      class="p-p-button-rounded p-p-button-success p-p-button-text"
    />
    <p-button
      icon="pi pi-user"
      class="p-p-button-rounded p-p-button-info p-p-button-text"
    />
    <p-button
      icon="pi pi-bell"
      class="p-p-button-rounded p-p-button-warning p-p-button-text"
    />
    <p-button
      icon="pi pi-heart"
      class="p-p-button-rounded p-p-button-help p-p-button-text"
    />
    <p-button
      icon="pi pi-times"
      class="p-p-button-rounded p-p-button-danger p-p-button-text"
    />
    <p-button
      icon="pi pi-filter"
      class="p-p-button-rounded p-p-button-text p-p-button-plain"
    />

    <h5>Rounded and Outlined Icon p-buttons</h5>
    <p-button icon="pi pi-check" class="p-p-button-rounded p-p-button-outlined" />
    <p-button
      icon="pi pi-bookmark"
      class="p-p-button-rounded p-p-button-secondary p-p-button-outlined"
    />
    <p-button
      icon="pi pi-search"
      class="p-p-button-rounded p-p-button-success p-p-button-outlined"
    />
    <p-button
      icon="pi pi-user"
      class="p-p-button-rounded p-p-button-info p-p-button-outlined"
    />
    <p-button
      icon="pi pi-bell"
      class="p-p-button-rounded p-p-button-warning p-p-button-outlined"
    />
    <p-button
      icon="pi pi-heart"
      class="p-p-button-rounded p-p-button-help p-p-button-outlined"
    />
    <p-button
      icon="pi pi-times"
      class="p-p-button-rounded p-p-button-danger p-p-button-outlined"
    />

    <h5>Badges</h5>
    <p-button type="p-button" label="Emails" badge="8" />
    <p-button
      type="p-button"
      label="Messages"
      icon="pi pi-users"
      class="p-p-button-warning"
      badge="8"
      badgeClass="p-badge-danger"
    />

    <h5>Loading</h5>
    <p-button
      type="p-button"
      label="Search"
      icon="pi pi-search"
      :loading="loading[0]"
      @click="load(0)"
    />
    <p-button
      type="p-button"
      label="Search"
      icon="pi pi-search"
      iconPos="right"
      :loading="loading[1]"
      @click="load(1)"
    />
    <p-button
      type="p-button"
      icon="pi pi-search"
      :loading="loading[2]"
      @click="load(2)"
    />
    <p-button
      type="p-button"
      label="Search"
      :loading="loading[3]"
      @click="load(3)"
    />

    <h5>Templating</h5>
    <p-button type="p-button" class="p-px-3">
      <img
        alt="logo"
        src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png"
        style="width: 1.5rem"
      />
    </p-button>
    <p-button type="p-button" class="p-p-button-outlined p-p-button-success">
      <img
        alt="logo"
        src="https://www.primefaces.org/wp-content/uploads/2020/05/placeholder.png"
        style="width: 1.5rem"
      />
      <span class="p-ml-2 p-text-bold">PrimeVue</span>
    </p-button>

    <h5>p-button Set</h5>
    <span class="p-p-buttonset">
      <p-button label="Save" icon="pi pi-check" />
      <p-button label="Delete" icon="pi pi-trash" />
      <p-button label="Cancel" icon="pi pi-times" />
    </span>

    <h5>Sizes</h5>
    <div class="sizes">
      <p-button label="Small" icon="pi pi-check" class="p-p-button-sm" />
      <p-button label="Normal" icon="pi pi-check" class="p-p-button" />
      <p-button label="Large" icon="pi pi-check" class="p-p-button-lg" />
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    const loading = ref([false, false, false])
    const load = index => {
      loading.value[index] = true
      setTimeout(() => (loading.value[index] = false), 1000)
    }

    return { loading, load }
  }
}
</script>

<style lang="scss" scoped>
.p-p-button {
  margin-right: 0.5rem;
}

.p-p-buttonset {
  .p-p-button {
    margin-right: 0;
  }
}

.sizes {
  .p-button {
    margin-bottom: 0.5rem;
    display: block;

    &:last-child {
      margin-bottom: 0;
    }
  }
}

@media screen and (max-width: 640px) {
  .p-p-button {
    margin-bottom: 0.5rem;

    &:not(.p-p-button-icon-only) {
      display: flex;
      width: 100%;
    }
  }

  .p-p-buttonset {
    .p-p-button {
      margin-bottom: 0;
    }
  }
}
</style>
