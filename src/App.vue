<template>
  <div id="app">
    <main role="main" class="container">
      <a-nav></a-nav>
      <resume-container></resume-container>
    </main>
    <aFooter></aFooter>
  </div>
</template>

<script>
import aNav from './components/partials/aNav';
import aFooter from './components/partials/aFooter';
import resumeContainer from './components/resumeContainer';

export default {
  name: 'app',
  components: {
    aNav,
    resumeContainer,
    aFooter,
  },
};
</script>