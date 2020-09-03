<template>
<div class="ody">
<div v-if="rank3.own">
    <br><br><br>
          <div class="container"><br>
<h1 class="display-4">Rankpage</h1></div><br>
<div class="container-sm">
<div class="row text-center">

<b-col cols="4">
<br><br><br><br><br><br>
<h3>2</h3>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank2.own.id } }"
        >
 <img :src="rank2.own.logo" class="respo"/><br><br>
<h5>{{rank2.own.teamname|capitalize}}</h5></router-link>
</b-col>

<b-col cols="4">
<h3>1</h3><br>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank1.own.id } }"
        >
<img :src="rank1.own.logo" class="resp"/><br><br>
<h5>{{rank1.own.teamname|capitalize}}</h5></router-link>
</b-col>

<b-col cols="4">
<br><br><br><br><br><br>
<h3>3</h3>
<router-link
        :to="{ name: 'Teamveiw', params: { id: rank3.own.id } }"
        >
<img :src="rank3.own.logo" class="respo"/><br><br>
<h5>{{rank3.own.teamname|capitalize}}</h5></router-link>
</b-col>

<hr>
<br><br>
</div>
</div>
          <div class="container-sm"><br><br>
              <b-row align-v="center">
                  <b-col cols="4" ><h2>Team</h2></b-col>
              <b-col cols="8"> 
      <b-row align-v="center">
        <b-col cols="4" ><b><h5>Goals</h5></b></b-col>
          <b-col cols="4" ><b><h5>Play</h5></b></b-col>
          <b-col cols="4" ><b><h5>Won</h5></b></b-col>
     </b-row>
</b-col>
              </b-row>
<hr>
<div v-for="ranks in teamdata" :key="ranks.id">
                <b-row align-v="center">
                  <b-col cols="4">
                <router-link
        :to="{ name: 'Teamveiw', params: { id: ranks.own.id } }"
        >    
                 <h2>{{ranks.own.teamname|capitalize}}</h2><br>
                <img :src="ranks.own.logo" class="respo"/>
                </router-link>
                </b-col>
              <b-col cols="8">
      <b-row align-v="center">
         <b-col cols="4" ><h4>{{ranks.teamgoals}}</h4></b-col>
         <b-col cols="4" ><h4>{{ranks.matchs_played}}</h4></b-col>
         <b-col cols="4" ><h4>{{ranks.match_won}}</h4></b-col>
</b-row>
              </b-col>
              </b-row>
              <hr>
              </div>

</div>
</div>
</div>

</template>

<script>

import { apiService } from "@/common/api.service.js";

export default{
    name: "rankpage",

    data() {
    return {
    teamdata:[],
      teamrank:[],
      rank1:{},
      rank2:{},
      rank3:{},
    }
    },
methods: {

    getTeamRank() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/teamrank/`;
      apiService(endpoint)
        .then(data => {
          if (data) {
            this.loading = true;
            this.teamrank = data;
            this.teamdata=this.teamrank
            this.teamrank=this.teamrank.slice(0,4)
            this.rank1=this.teamrank[0];
            this.rank2=this.teamrank[1];
            this.rank3=this.teamrank[2];
          } 
          else {
            this.setPageTitle("404 - Page Not Found")
          }
        })    
    },
},
created()
{
  this.getTeamRank()
},

}


</script>

<style scoped>
@import '../assets/css/teamrank.css';
.ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;

    

}
</style>
