<template>
<b-col cols="6" sm="6" md="3" lg="3"  >
  <div class="our-team">
    <router-link
        :to="{ name: 'playerpage', params: { player: player} }"
        >
    <div class="picture">
      <img :src="player.pic + '?'+ new Date().getTime()">
    </div></router-link>
    <div class="team-content">
      <h4 class="name">{{player.player| capitalize}}</h4>
      <h5 class="tit">{{player.age| capitalize}}</h5>
      <h5 class="tit">{{player.profession| capitalize}}</h5>

<table>
    <tr>
            <td><p
            class="fa fa-heart" 
            style="font-size:20px;"
            @click="toggleLike"
            :class="{
              'fa fa-heart': userLikedPlayer,
              'fa fa-heart-o': !userLikedPlayer
              }"
            ></p><strong>&nbsp;{{ likesCounter }}</strong>
            </td>

          
         </tr>
</table>
     </div> 
             <ul class="social">
            <li><b href="" class="fa fa-facebook" aria-hidden="true"></b></li>
            <li><b href="" class="fa fa-instagram" aria-hidden="true"></b></li>
        </ul>
             </div>

</b-col>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Playerveiw",
  props: {
    player: {
      type: Object,
      required: true
    },
  },
    data() {
    return {
      userLikedPlayer: this.player.user_has_voted,
      likesCounter: this.player.likes_count,
      pic: null,
      error: null,
      ran:null
    }
  },
  methods: {
  toggleLike() {
      this.userLikedPlayer=== false
        ? this.likePlayer()
        : this.unLikePlayer()
    },
    likePlayer() {
      this.userLikedPlayer = true;
      this.likesCounter += 1;
      let endpoint = `/api/playerlike/${ this.player.id }/like/`;
      apiService(endpoint, "POST")
    },
    unLikePlayer() {
      this.userLikedPlayer = false;
      this.likesCounter -= 1;
      let endpoint = `/api/playerlike/${ this.player.id }/like/`;
      apiService(endpoint, "DELETE")
    },
    
  }     
}
</script>


<style scoped>
.fa-heart-o {
  color:red;
  cursor: pointer;
}

.fa-heart {
  color: red;
  cursor: pointer;
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

.router-link {
  color: inherit;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
  width: 100%;
  border: 0px solid #ddd;
}
th, td {
  text-align: center;
  padding: 10px;
}


</style>