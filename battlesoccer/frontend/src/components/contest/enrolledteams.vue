<template>
    <div>
      <br><br>
       <div class="container"><br>
<h1>Team Enrolled</h1>  </div> 
<br>
<div class="container">
<div class=row>
<div class="col-6 col-lg-3" v-for="teamd in team" :key="teamd.id">
        <router-link
        :to="{ name: 'Teamveiw', params: { id: teamd.own.id } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="teamd.own.logo + '?'+ new Date().getTime()">
         </div>

    <div class="team-content">
      <h4 class="name">{{teamd.own.teamname| capitalize}}</h4>
    </div>

  </div>
        </router-link>
</div>
</div>
</div><br><br><br>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
    name:"enrolledteams",
      data() {
    return {
      team: [],
    }
      },
 
      methods: {
      getTeamData() {
      // get the details of a question instance from the REST API and call setPageTitle
      let endpoint = `/api/contest/`;
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
    this.getTeamData()
  }

}

</script>

<style scoped>
  .ody a{

    font-family: "Quicksand", sans-serif;
    text-decoration: none;

    

}
</style>