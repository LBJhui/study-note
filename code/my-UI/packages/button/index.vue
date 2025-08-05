<template>
  <div :class="tClass">
    <button>
      <slot></slot>
    </button>
  </div>
</template>

<script lang="ts">
export default {
  name: 't-button',
}
</script>

<script lang="ts" setup>
import { computed } from 'vue'

const props = defineProps({
  type: {
    type: String,
    default: '',
  },
})
const tClass = computed(() => {
  return [ 't-button', props.type ? `t-button-${ props.type }` : '' ]
})

</script>

<style lang="scss" scoped>
button {
  background: none;
  border: 0;
  cursor: pointer;
  outline: none;

  &:hover, &:focus {
    opacity: 0.8;
  }
}

.t-button {
  button {
    border: 1px solid #b4b0b0;
    border-radius: 4px;
    padding: 12px 24px;
  }
}

.t-button-success {
  button {
    background: #0eac77;
  }
}

.t-button-warning {
  button {
    background: #f9a825;
  }
}
</style>
