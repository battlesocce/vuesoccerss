<template>
<div class="ody">
    <div class="container text-center"><b> 
        <div class="row fixed-bottom" style="background-color:white; "  >
               
 <div class="col-3 col-lg-3">
      <div style="margin-bottom:10px; margin-top:15px; cursor:pointer;"
       v-on:click="setActive('appmain')" :class="{ active: isActive('appmain') }"
      @click="selectedComponent = 'appmain'">Contest Details</div> </div>

 <div class="col-3 col-lg-3" >
     <div style="margin-bottom:10px; margin-top:15px; cursor:pointer"
      v-on:click="setActive('appbattlestation')" :class="{ active: isActive('appbattlestation') }"
      @click="selectedComponent = 'appbattlestation'">Battle Station</div></div>

 <div class="col-3 col-lg-3">
      <div style="margin-bottom:10px; margin-top:15px; cursor:pointer"
       v-on:click="setActive('appenrolledteams')" :class="{ active: isActive('appenrolledteams') }"
       @click="selectedComponent = 'appenrolledteams'" >Team Enrolled</div></div>

 <div class="col-3 col-lg-3">
     <div style="margin-bottom:10px; margin-top:15px; cursor:pointer"
      v-on:click="setActive('appjoincontest')" :class="{ active: isActive('appjoincontest') }"
     @click="selectedComponent = 'appjoincontest'" >Join contest</div></div>

     </div></b>
     </div> 
<br>

                <transition name="slide" mode="out-in">
                <component :is="selectedComponent"/>
                </transition>            
</div>
</template>

<script>

import mainpage from '@/components/contest/mainpage.vue';
import battlestation from '@/components/contest/battlestation.vue';
import enrolledteams from '@/components/contest/enrolledteams.vue';
import joincontest from '@/components/contest/joincontest.vue';

export default {
    name:"contest",
      data: function() {
          return {
              selectedComponent: 'appmain',
              activeItem: 'appmain'
          }
        },
        components: {
            appmain: mainpage,
            appbattlestation: battlestation,
            appenrolledteams: enrolledteams,
            appjoincontest: joincontest
        },
        methods: {
    isActive: function (menuItem) {
      return this.activeItem === menuItem
    },
    setActive: function (menuItem) {
      this.activeItem = menuItem // no need for Vue.set()
    }
  }
}
</script>

<style scoped>
.active{
    color: red;

}

   .slide-leave-active {
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



</style>