<template>
  <div>
    <transition> 
    <div v-if="loading">
    <preloader/>
</div></transition>
   <div v-if="!loading"> 
    <NavbarComponent/>
    <transition name="fade" mode="out-in" appear> 
    <router-view/></transition>
   </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import NavbarComponent from "@/components/Navbar.vue";
import preloader from "@/components/preloader.vue";
export default {
  name: "App",
  components: {
    NavbarComponent,
    preloader

  },
  data() {
    return {
      loading: false,
      requestUser:null

    }
  },
  methods:{
        async setUserInfo() {
          this.loading = true;
      // add the username of the logged in user to localStorage
      const data = await apiService("/api/user/");
      const requestUser = data["username"];
      this.requestUser = data["username"];
      const id = data["id"];
      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("id", id);
      setTimeout(() => {
            this.loading = false;
          }, 2000)
    }
  },
    created() {
          this.setUserInfo()

    }

  };
</script>
<style>

.ody {

    font-family: "Quicksand", sans-serif;

}
.fade-enter-active, .fade-leave-active {
  transition: opacity 1s
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0
}



h1{
            font-size:55px;

        }

h2{
            font-size:35px;
           text-align:center;

        }
h4{
            font-size:25px;
        }

h5{
            font-size:20px;
        }
@media only screen and (max-width:700px) {
h1{
            font-size:20px;

        }
h2{
            font-size:15px;
            text-align:center;

        }
h4{
            font-size:10px;
        }
h5{
            font-size:8px;
            font-weight:300;

        }
}
  
  /*  .slide-leave-active {
        transition: opacity 1s ease;
        opacity: 0;
        animation: slide-out 1s ease-out forwards;
    }

    .slide-leave {
        opacity: 1;
        transform: translateX(0);
    }

    .slide-enter-active {
        animation: slide-in 1s ease-out forwards;
    }

    @keyframes slide-out {
        0% {
            transform: translateY(0);
        }
        100% {
            transform: translateY(-30px);
        }
    }

    @keyframes slide-in {
        0% {
            transform: translateY(-30px);
        }
        100% {
            transform: translateY(0);
        }
    }
*/
</style>
