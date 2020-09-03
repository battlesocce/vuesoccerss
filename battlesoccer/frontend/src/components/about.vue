<template>
<div clas="ody">
  <div class="abt">

<center>
 <div class="card">
      <div class="card-image">
        <div class="background-image" :style="{'background-image': `url(${require('@/assets/img/card.jpg')})`}"></div>
        <div class="publication-details">
            Battle Begins
          <span class="date"><i class="fas fa-calendar-alt"></i> April 01, 2020</span>
        </div>
      </div>

      <div class="card-content">
        <h1 class="title">Battle of Takedown</h1>
        <h2 class="subtitle">Join the Real battle now</h2>
        <router-link 
        :to="{ name: 'contest'}" >
        <div class="cta1">
          <a href="">Read more &rarr;</a>
        </div></router-link>
      </div> 
 </div>

</center>
<br>
   <div class="right2">
    <h2>About</h2><br>
    Battle soccer is a real time online game challenge!!<br>Now come let's<br>Play in the real world
        <br><br><h4>If you think LOVE is the best feeling ever!!<br><br><span class="quotes"> "Try playing FootBall"</span></h4><br><br>
      </div>
  </div>
</div>
</template>
<script>
export default {
    name:"about"
}
</script>
<style scoped>
 @import '../assets/css/about.css';


.right2 {
  color:black;
  float:left;
  width:100%;
  padding:18px;
  margin-top:10px;
  text-align:center;
}

.background-image {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-size: cover;
  z-index: 0;
  transition: transform 5s;
  overflow: hidden;

}

</style>