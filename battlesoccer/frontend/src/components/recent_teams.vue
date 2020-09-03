<template>
<b-row>
<b-col  v-for="teamd in teamdata" :key="teamd.id" cols="6" sm="6" md="3" lg="3">
        <router-link
        :to="{ name: 'Teamveiw', params: { id: teamd.id } }"
        >
  <div class="our-team">
    <div class="picture">
      <img :src="teamd.logo + '?'+ new Date().getTime()">
         </div>

    <div class="team-content">
      <h4 class="name">{{teamd.teamname| capitalize}}</h4>
    </div>

  </div>
        </router-link>
</b-col>
</b-row>
</template>

<script>


export default{
name: "recentteam",
props: {
    teamdata: {
      type: Array,
      required: true
    },
    }
}

</script>

<style scoped>
@import '../assets/css/userprofile.css';
.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}
</style>
