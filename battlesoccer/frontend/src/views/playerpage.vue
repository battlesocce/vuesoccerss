<template>
<div class="ody">
  
    <br><br><br><br><br><br>
<div class="profile-page">
     <div class="main main-raised">
		<div class="profile-content">
            <div class="container">
                <div class="row">
	                <div class="col-md-6 ml-auto mr-auto">
        	           <div class="profile">
	                        <div class="avatar" v-if="players.pic">     
                            <v-lazy-image :src="players.pic" class="res"
    src-placeholder="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR508iDAmSEkkOWUuK7SsEbpflpVR1TKl1ljQ&usqp=CAU"
     />
                        </div>
                         <div class="name">
	                            <h2 style="margin-top:-50px;">{{players.player| capitalize}}</h2></div>
        	        <router-link v-if="isUser" class='router-link' 
            :to="{ name: 'Addplayer',
             params: { id: players.id } }"
             ><i class="fa fa-edit btn btn-just-icon btn-twitter"  style="margin-top:-60px" ></i>
            </router-link>
            <div v-if="isUser"  class="upload-btn-wrapper">
  <button class="btn"><i class="fa fa-camera btn btn-just-icon btn-twitter"></i></button>
  <input type="file" name="myfile"  v-on:input="onchange"/>
</div>  
                  </div>
                </div>
            </div>
     <center><h4 v-if="players.description">{{players.description|capitalize}}</h4></center><br>
    <center><h2 style="margin-top:-10px">Team_{{players.teamname|capitalize}}</h2></center>
<br><br>
    <div class="wrap text-center">
    <div class="col-lg-2 cols=6">
    <h3> Age </h3><br><h4> {{players.age| capitalize}} </h4><br><hr><br>
    </div>
     <div class="col-lg-2 cols=6">
    <h3> Profession </h3><br><h4> {{players.profession| capitalize}} </h4><br><hr><br>
    </div>
    <div class="col-lg-4">
    </div>
         <div class="col-lg-2 cols=6">
    <h3> Position </h3><br><h4> {{players.position| capitalize}} </h4><br><hr><br>
    </div>
         <div class="col-lg-2 cols=6">
    <h3> Liked_by </h3><br><h4> {{players.likes_count| capitalize}} </h4><br><hr><br>
    </div>
    <br><br>
    </div>
	    </div>
    </div>
</div> 
    </div>
    
</div>
</template>

<script>
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js"
import { apiService } from "@/common/api.service.js";
export default {
  name: "playerpage",
    data() {
    return {
      players:{},
     pic: null,
     userid:null
    }}, 
  props: {
    player: {
      type: Object,
      required: false
    }
  },

  computed: {
    isUser() {    
      return this.player.own.user == this.userid
    }
  },
methods: {
onchange() {
  this.pic=event.target.files[0]
 event.target.value = '';
if (!this.pic) {
        this.error = "You can't send an empty question!";
      }  else {
      const formData = new FormData()
     formData.append('pic',this.pic)
     axios.put( `/api/playerpic/${this.player.id }/`,
  formData,
  {
    headers: {
         "Access-Control-Allow-Origin" : "*",
        'Content-Type': 'multipart/form-data',
        "X-CSRFTOKEN": CSRF_TOKEN

    }
  }
)
.then(function(){
  console.log('SUCCESS!!');
})
.catch(function(){
  console.log('FAILURE!!');
});
setTimeout(() => {
 this.getplayerData()
        },2000)
      }
    },
      getplayerData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/player/${this.player.id}/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.players = data;
          } else {
            this.players = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    }
},
    created() {
   this.userid = window.localStorage.getItem("id");
    this.getplayerData()

    }    
}
</script>


<style scoped>
@import '../assets/css/details.css';

.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
.profile-page .profile img {
    max-width: 250px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}
.res{
	width:25%;
	height:auto;
	margin: auto;
	border-radius: 5%;


}
.wrap {
	display: flex;
	flex-wrap: wrap;
	margin-right:-15px;
	margin-left:-15px;
  }


@media screen and (max-width:600px) {
    .res{
	width:40%;
	height:auto;
	margin: auto;
	border-radius: 5%;

}

.profile-page .profile img {
    max-width: 180px;
    width: 100%;
    margin: 0 auto;
    -webkit-transform: translate3d(0,-40%,0);
    -moz-transform: translate3d(0,-40%,0);
    -o-transform: translate3d(0,-40%,0);
    -ms-transform: translate3d(0,-40%,0);
    transform: translate3d(0,-40%,0);
}
.wrap {
	display: flex;
	flex-wrap: wrap;
	margin-right:-15px;
	margin-left:-15px;
  }

}
.responsive{
width:100%;
height:auto;

}

.upload-btn-wrapper {
  position: relative;
  overflow: hidden;
  display: inline-block;
}



.upload-btn-wrapper input[type=file] {
  font-size: 80px;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
}

</style>