<template>
<body>
 <br><br><br>
 <div class="container">
    <h1 class="display-4">Gallery</h1>   
 </div>
    <br>
        <div v-for = "video in team.videos"
        :key="video.pk">
<div class="videocover">
              <div class="embed-responsive embed-responsive-1by1">
  <iframe class="embed-responsive-item" :src="video.highlight" 
   allow="accelerometer; autoplay;loop; encrypted-media; gyroscope; picture-in-picture" allowfullscreen
   ></iframe>
</div>
</div>
          </div>

</body>
</template>

<script>

import { apiService } from "@/common/api.service.js";
export default{
  name: "gallery",
  data() {
    return {
      team: {},
    }
  },
  methods: {
      getgallery() {
      let endpoint = `/api/team/${this.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.team = data;
          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
   },
 created() {
    this.id = this.$route.params.id;
    this.getgallery()
    },
}
</script>
<style scoped>
.videocover {
  color:black;
overflow:hidden;
  float:left;
  width:25%;
  padding: 0 4px;
}

video{
width:100%;
margin:auto;
font-size:35px;
}


@media only screen and (max-width:950px) {
   .videocover {
    width:100%;
  }
}


</style>
