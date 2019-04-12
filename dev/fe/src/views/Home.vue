<template>
  <div class="home">

    <Sonar/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Sonar from '@/components/Sonar.vue';

@Component({
  components: {
    Sonar,
  },
})
export default class Home extends Vue {}
</script>
