<template>
  <div class="wrapper">
    <!-- <div class="wrapper" :class="{'nav-open': $sidebar.showSidebar}"> -->

    <side-bar :background-color="backgroundColor">
      <sidebar-link to="/knowledgegraph/fields">
        <i class="tim-icons icon-vector"></i>
        <p>Knowledge Graph</p>
      </sidebar-link>
      <sidebar-link to="/nodefeeds">
        <i class="tim-icons icon-paper"></i>
        <p>Node Feeds</p>
      </sidebar-link>
    </side-bar>

    <div class="main-panel" :data="backgroundColor">
      <top-navbar></top-navbar>
      <dashboard-content @click.native="toggleSidebar"></dashboard-content>
      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./DashboardContent.vue";
// import SidebarShare from "./SidebarSharePlugin.vue";
// import MobileMenu from "./MobileMenu.vue";
import SideBar from "@/components/SidebarPlugin/SideBar.vue";
import SidebarLink from "@/components/SidebarPlugin/SidebarLink.vue";
// import { DropDown } from "@/components/index";

export default {
  components: {
    TopNavbar,
    DashboardContent,
    ContentFooter,
    // DropDown,
    // MobileMenu,
    SideBar,
    SidebarLink
    // SidebarShare
  },
  data() {
    return {
      backgroundColor: "green"
    };
  },
  computed: {
    isRTL() {
      return this.$rtl.isRTL;
    }
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
};
</script>
