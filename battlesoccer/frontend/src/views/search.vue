<template>
<div class="ody">
  <br><br><br>
      <div id="wrap">
<input type="text" :value='search'
@input='evt=>search=evt.target.value'
  ref="search" placeholder="Search Team/Player name?">
<input id="search_submit"  type="submit">
</div><br><br><br><br><br><br>
<b-row>
<b-col cols="6" lg="3" v-for="te in filteredList" :key ="te.id">
         <router-link
        :to="{ name: 'Teamveiw', params: { id: te.id } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="te.logo + '?'+ new Date().getTime()">
    </div>
    <div class="team-content">
      <h4 class="name">{{te.teamname| capitalize}}</h4>
     </div> <br>
             <ul class="social">
            <li><b href="" class="fa fa-facebook" aria-hidden="true"></b></li>
            <li><b href="" class="fa fa-instagram" aria-hidden="true"></b></li>
        </ul>
</div></router-link>
</b-col>
</b-row>

<b-row>
<b-col cols="6" lg="3" v-for="p in filteredListplayer" :key ="p.id">
          <router-link
        :to="{ name: 'playerpage', params: { player: p } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="p.pic + '?'+ new Date().getTime()">
    </div>
    <div class="team-content">
      <h4 class="name">{{p.player| capitalize}}</h4>
     </div> <br>
             <ul class="social">
            <li><b href="" class="fa fa-facebook" aria-hidden="true"></b></li>
            <li><b href="" class="fa fa-instagram" aria-hidden="true"></b></li>
        </ul>
</div></router-link>
</b-col>
</b-row>
</div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "search",
data() {
    return {
      search:null,
      teamsearch: [],
      player:[],
      show:null
    }
},
 computed: {
    filteredList() {
      return this.teamsearch.filter(teams => {
        return teams.teamname.toLowerCase().match(this.search.toLowerCase())
      })
    },
    filteredListplayer() {
      return this.player.filter(players => {
        return players.player.toLowerCase().match(this.search.toLowerCase())
      })
    }
  },
     methods: {
       focusInput() {
      this.$refs.search.focus();
    },
getTeamData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/team/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.teamsearch = data;

          } else {
            this.team = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
      getplayerData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/player/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.player = data;
          } else {
            this.player = null;
            this.setPageTitle("404 - Page Not Found")
          }
        })
    },
     },
  created() {
    this.getTeamData()
    this.getplayerData()

    },
  mounted() {
    this.focusInput();
  },
}
</script>


<style scoped>
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        


}
.ody {

    font-family: "Quicksand", sans-serif;
        text-decoration: none;
        


}
@import '../assets/css/userprofile.css';

#wrap {
  margin: 15px 15px;
  display: inline-block;
  position: relative;
  height: 60px;
  float: right;
  padding: 0;
  position: relative;
}


input[type="text"] {
  height: 60px;
  font-size: 35px;
  display: inline-block;
  font-weight: 100;
  border: none;
  outline: none;
  color: #555;
  padding: 30px;
  padding-right: 5px;
  position: absolute;
  top: 0;
  right: 0;
  background: none;
  z-index: 1;
  transition: width 0.4s cubic-bezier(0, 0.795, 0, 1);
  cursor: pointer;
  width:550px;
  z-index: 0;
  border-bottom: 1px solid #bbb;
  cursor: text;
}



@media only screen and (max-width:550px) {

   input[type="text"] {
     font-size: 18px;
      width:320px;
     padding-right:3px;
  }

  .close {
  margin-left:10px;
}
}

input[type="submit"] {
  height: 47px;
  width: 43px;
  display: inline-block;
  color: red;
  float: right;
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAADNQTFRFU1NT9fX1lJSUXl5e1dXVfn5+c3Nz6urqv7+/tLS0iYmJqampn5+fysrK39/faWlp////Vi4ZywAAABF0Uk5T/////////////////////wAlrZliAAABLklEQVR42rSWWRbDIAhFHeOUtN3/ags1zaA4cHrKZ8JFRHwoXkwTvwGP1Qo0bYObAPwiLmbNAHBWFBZlD9j0JxflDViIObNHG/Do8PRHTJk0TezAhv7qloK0JJEBh+F8+U/hopIELOWfiZUCDOZD1RADOQKA75oq4cvVkcT+OdHnqqpQCITWAjnWVgGQUWz12lJuGwGoaWgBKzRVBcCypgUkOAoWgBX/L0CmxN40u6xwcIJ1cOzWYDffp3axsQOyvdkXiH9FKRFwPRHYZUaXMgPLeiW7QhbDRciyLXJaKheCuLbiVoqx1DVRyH26yb0hsuoOFEPsoz+BVE0MRlZNjGZcRQyHYkmMp2hBTIzdkzCTc/pLqOnBrk7/yZdAOq/q5NPBH1f7x7fGP4C3AAMAQrhzX9zhcGsAAAAASUVORK5CYII=)
  center center no-repeat;
  text-indent: -10000px;
  border: none;
  position: absolute;
  top: 0;
  right: 0;
  z-index: 0;
  cursor: pointer;
  opacity: 0.4;
  cursor: pointer;
  transition: opacity 0.4s ease;

}



input[type="submit"]:hover {
  opacity: 0.8;
}

</style>