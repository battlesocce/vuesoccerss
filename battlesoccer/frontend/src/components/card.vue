<template>
<div clas="ody">
  <div class="container"><br>
<h1>Contest Update</h1></div>
<div class="container mt-5">
  <div class="row">
    <div class="col-12">
      <article class="blog-card">
        <div class="blog-card__background">
          <div class="card__background--wrapper">
            <div class="card__background--main" :style="{'background-image': `url(${require('@/assets/img/card.jpg')})`}">             
             <div class="card__background--layer"></div>
            </div>
          </div>
        </div>
        <div class="blog-card__head">
          <span class="date__box">
            <span class="date__day">11</span>
            <span class="date__month">JAN</span>
          </span>
        </div>
        <div class="blog-card__info">
          <h2>Battle Takedown</h2>
            <br>
          <p>
              Football is much more than just a game where you score a goal or win a match. It's a relationship where only love prevails. Love for the colours you wear, for that crest you touch right above your heart when you pray and for those boots you lace up in the hope that your legs pump harder than your heart does.
          </p>
          <router-link 
        :to="{ name: 'contest'}" class="btn1 btn1--with-icon"><i class="btn1-icon fa fa-long-arrow-right"></i>READ MORE</router-link>
        </div>
      </article>
    </div>
  </div>
</div>
</div>
</template>

<script>
export default {
  name: "card",
}
</script>


<style scoped>


@import '../assets/css/card.css';

</style>