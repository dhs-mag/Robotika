<template>
  <div class="home">

    <Sonar/>
    <Control/>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import Sonar from '@/components/Sonar.vue';
import Control from '@/components/Control.vue';

@Component({
  components: {
    Sonar,
    Control,
  },
})
export default class Home extends Vue {}
</script>
