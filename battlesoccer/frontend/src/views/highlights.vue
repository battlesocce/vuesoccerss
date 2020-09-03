<template>
<div class="ody">
 <br><br><br><br>
 <div class="container">
    <h1>Hightlights</h1>   
 </div><br>
        <div v-for = "video in highligths"
        :key="video.pk">
        <div class="videocover">
              <div class="embed-responsive embed-responsive-1by1">
  <iframe class="embed-responsive-item" :src="video.highlight"
   allow="accelerometer; autoplay;loop;mute;encrypted-media; gyroscope; picture-in-picture" allowfullscreen
   ></iframe>
</div>
    <router-link
        :to="{ name: 'Teamveiw', params: { id: video.own.id} }"
        >  
 <center><h4>{{video.teamname| capitalize}}</h4></center></router-link><br>
          </div></div>
</div>
</template>

<script>

import { apiService } from "@/common/api.service.js";
export default{
  name: "Highlight",
  data() {
    return {
      highligths: [],
    }
  },
   methods: {
      gethighligthsData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/highlights/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.highligths = data;
          } else {
            this.highligths = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
    },
  created() {
    this.gethighligthsData()
    }
}
</script>
<style scoped>
.ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;
}
.videocover {
  color:black;
overflow:hidden;
  float:left;
  width:25%;
  padding: 0 4px;
}

iframe{
width:100%;
height:auto;
margin:auto;
font-size:35px;
}


@media only screen and (max-width:950px) {
   .videocover {
    width:100%;
  }
}


</style>