<template>
  <div class="ody">
<div class="profile-page">
    <div v-if='team.coverpic'>
<v-lazy-image :src="team.coverpic"  class="responsive"
    src-placeholder="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTDjsRb3qChxX4vFIFiN5-V3b4MyeaOzdywNg&usqp=CAU"
     style="margin-top:65px;" />    </div>
    <div class="main main-raised">
		<div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar" v-if='team.logo'>
                            <v-lazy-image :src="team.logo" class="img-raised rounded-circle img-fluid"
    src-placeholder="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR508iDAmSEkkOWUuK7SsEbpflpVR1TKl1ljQ&usqp=CAU"
     />
                          </div>
	                        <div class="name">
	                            <h3 style="font-size:5vw;">{{team.teamname | capitalize}}</h3>
<router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'matchplayed',params: {id:id} }"
        ><i class="fa fa-info"></i></router-link>
        <router-link class="btn btn-just-icon btn-link btn-twitter"
        :to="{ name: 'gallery',params: {id:id} }"
        ><i class="fa fa-file-video-o"></i></router-link>	                        </div>
	                    </div>
    	            </div>
                </div>
                    <h3 style="font-size:3vw;"><center>{{team.teamquotes| capitalize}}</center></h3>
                <br><br>
            </div>
		</div>
    </div>
</div>
<br>
<div class="container-sm">
  <br>
        <b-row>
         <Playerveiw
        v-for="player in team.players"
        :player="player"
        :key="player.id"
      />
      </b-row>
</div>
        </div> 
</template>

<script>
import { apiService } from "@/common/api.service.js";
import Playerveiw from "@/components/profileplayer.vue";
export default{
  name: "Teamveiw",
     components: {
    Playerveiw
  },
  data() {
    return {
      team: {},
      id:null
    }
  },
   methods: {
      getTeamData() {
      // get the details of a question instance from the REST API and call setPageTitle
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
    },
   }, 
 created() {
this.id = this.$route.params.id;
    this.getTeamData()
    },

}

</script>
<style scoped>
@import '../assets/css/details.css';
.ody{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
@media screen and (max-width:600px) {

.profile-page .profile img {
    max-width: 120px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}
}
.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}



.upload-btn-wrapper input[type=file] {
  font-size: 100px;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}



 .v-lazy-image {
    filter: blur(20px);
    transition: filter 0.8s;
  }
  .v-lazy-image-loaded {
    filter: blur(0);
  }
</style>
