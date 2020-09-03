<template>
<div class="ody">
<nav class="nav">
        <div class="contain">
            <div class="logo">
                 <router-link 
        :to="{ name: 'Home' }"
        >Battle Soccer</router-link>        
            </div> 
        <router-link 
        :to="{ name: 'search' }"
        ><li class="fa fa-search  btn btn-just-icon btn-twitter" style="float:right; margin-right:70px; margin-top:13px;"></li></router-link> 
              <div id="mainListDiv" class="main_list">
                <ul class="navlinks">


        <li class="tog"><router-link v-if="requestUser"
        :to="{ name: 'Userprofile' }" 
        >Profile</router-link>

        <div v-if="!requestUser"><a class="tog" style="cursor:default;">Guest</a></div>
        </li>
        
<li><router-link class="tog "
        :to="{ name: 'contest' }"
        >Contest</router-link></li>

         <li><router-link class="tog "
        :to="{ name: 'Highlight' }"
        >Highlights</router-link></li>

          <li><router-link class="tog"
        :to="{ name: 'rankpage' }"
        >Rankboard</router-link></li>

        <li><router-link class="tog"
        :to="{ name: 'aboutpage' }"
        >About</router-link></li>

      <li><div v-if="requestUser" class="tog">
      <a href="/accounts/logout/">Log out</a></div>

      <div v-if="!requestUser" class="tog">
      <a href="/accounts/logout/">Sign In</a></div></li>

                </ul>
            </div>
            <span class="navTrigger">
                <i></i>
                <i></i>
                <i></i>
            </span>
        </div>
    </nav>
    </div>
</template>

<script>
import $ from 'jquery'
import { apiService } from "@/common/api.service.js";
export default {
  name: "NavbarComponent",
    data() {
    return {
      requestUser:null  
    }},
  methods: {
    async setUserInfo() {
      const data = await apiService("/api/user/");
      this.requestUser = data["username"];
    }
    },
  mounted () {
              $(window).scroll(function() {
            if ($(document).scrollTop() > 50) {
                $('.nav').addClass('affix');
                console.log("OK");
            } else {
                $('.nav').removeClass('affix');
            }
        });
 $('.navTrigger').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();
});

 $('.tog').click(function () {
    $(this).toggleClass('active');
    console.log("Clicked menu");
    $("#mainListDiv").toggleClass("show_list");
    $("#mainListDiv").fadeIn();
});

},
created() {
    this.setUserInfo()
    },
};

</script>

<style>
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        color:inherit;


}

.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        color:inherit;


}
@import '../assets/css/navbar.css';
</style>