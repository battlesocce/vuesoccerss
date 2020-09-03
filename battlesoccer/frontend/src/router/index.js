import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Teamedit from "../views/teamedit.vue";
import Addplayer from "../views/addplayer.vue";
import Userprofile from "../views/userprofile.vue";
import Highlight from "../views/highlights.vue";
import rankpage from "../views/rankpage.vue";
import aboutpage from "../views/aboutpage.vue";
import Teamveiw from "../views/teamprofileveiw.vue";
import matchplayed from "../views/matchplayed.vue";
import gallery from "../views/gallery.vue";
import playerpage from "../views/playerpage.vue";
import contest from "../views/contest.vue";
import search from "../views/search.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },

  {
    path: "/Userprofile",
    name: "Userprofile",
    component: Userprofile,
    props: true

  },

  {
    path: "/Teamveiw/:id",
    name: "Teamveiw",
    component: Teamveiw
  },

  {
    path: "/gallery/:id",
    name: "gallery",
    component: gallery
  },

  {
    path: "/matchplayed/:id",
    name: "matchplayed",
    component: matchplayed
  },

  {
    path: "/aboutpage",
    name: "aboutpage",
    component: aboutpage
  },

  {
    path: "/rankpage",
    name: "rankpage",
    component: rankpage
  },


  {
    path: "/Highlight",
    name: "Highlight",
    component: Highlight
  },


  {
    path: "/search",
    name: "search",
    component: search
  },




  // {
  //   path: "/about/",
  //   name: "About",
  //   component: About
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   //component: () =>
  //   //import(/* webpackChunkName: "about" */ "../views/About.vue"),
  // },

  
  {
      path: "/Teamedit/:id",
      name: "Teamedit",
      component: Teamedit,
      props: true
    },

    {
      path: "/contest/",
      name: "contest",
      component: contest,
    },

  {
      path: "/addplayer/:id?/",
      name: "Addplayer",
      component: Addplayer,
      props: true
    },

    {
      path: "/playerpage/:player",
      name: "playerpage",
      component: playerpage,
      props: true
    },



];

const router = new VueRouter({
  mode: "history",
  //base: process.env.BASE_URL,
  routes,

  
});


export default router;
