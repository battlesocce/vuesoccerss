<template>
<div class="ody">
<br><br><br>
<div class="aboutus-section">
            <div class="container">
                <div class="row">
                    <div class="col-md-3 col-sm-12 col-12">
                        <div class="aboutus">
                            <h2 class="aboutus-title">About Us</h2>
                            <p class="aboutus-text"> Hey Battlewarriors!  We are the first and foremost organisation to create a realistic battle environment to make different teams who have a passion for football battle it out in our Battlestation.</p>
                            <p class="aboutus-text">Our battlestations are to be placed allover India soon.But now we are currently operating in madurai.</p>
                            <div v-if="flag">    
                               <a v-on:click="onclick" class="aboutus-more" >read more</a>
                            </div>
                            <div v-else>
                               <p class="aboutus-text"> Register now and join us soon to participate in the tournaments conducted and get featured iin our highligts.Lots of prizes awaiting register soon.</p>
                               <div v-on:click="onclick" class="aboutus-more" style="cursor:pointer;"  >read less</div>
                            </div>   
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-12 col-12">
                        <div class="aboutus-banner">
                            <img src="@/assets/img/aboutc.jpg" alt="" style="width:100%">
                        </div>
                    </div>
                    <div class="col-md-5 col-sm-12 col-12">
                        <div class="feature">
                            <div class="feature-box">
                                <div class="clearfix">
                                    <div class="iconset">
                                        <span class="glyphicon glyphicon-cog icon"></span>
                                    </div>
                                    <div class="feature-content"><br>
                                        <h4>Our Motto</h4>
                                        <p>To unite all the passionate Battlewarriors to play football in the Battlestations near to them.And engage them in a fierce battle that delights the eyes of the perceivers.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="feature-box">
                                <div class="clearfix">
                                    <div class="iconset">
                                        <span class="glyphicon glyphicon-cog icon"></span>
                                    </div>
                                    <div class="feature-content">
                                        <h4>Features</h4>
                                        <p>On becoming our member you enjoy some of the most cool features.Win battles continously,earn reputation and get featured on our global rankboard. </p>
                                    </div>
                                </div>
                            </div>
                            <div class="feature-box">
                                <div class="clearfix">
                                    <div class="iconset">
                                        <span class="glyphicon glyphicon-cog icon"></span>
                                    </div>
                                    <div class="feature-content">
                                        <h4>Support</h4>
                                        <p>Our customer support team is always happy in assisting you.our customer support is available 24/7.
                                        Feel free to contact us at support@battlesoccer.in</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</div>

</template>

<script>

export default{
    name: "aboutpage",
    data() {
      return {
         flag: true
      }
    },
    methods: {
       onclick() {
        this.flag=!this.flag
       }
    }

}
</script>

<style scoped>

.ody a{

    font-family: "Quicksand", sans-serif;
        text-decoration: none;


}

.aboutus-section {
    padding: 90px 0;
}
.aboutus-title {
    font-size: 30px;
    letter-spacing: 0;
    line-height: 32px;
    margin: 0 0 39px;
    padding: 0 0 11px;
    position: relative;
    text-transform: uppercase;
    color: #000;
}
.aboutus-title::after {
    background: #fdb801 none repeat scroll 0 0;
    bottom: 0;
    content: "";
    height: 2px;
    left: 0;
    position: absolute;
    width: 54px;
}
.aboutus-text {
    color: #606060;
    font-size: 13px;
    line-height: 22px;
    margin: 0 0 35px;
}

a:hover, a:active {
    color: #ffb901;
    text-decoration: none;
    outline: 0;
}
.aboutus-more {
    border: 1px solid #fdb801;
    border-radius: 25px;
    color: #fdb801;
    display: inline-block;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0;
    padding: 7px 20px;
    text-transform: uppercase;
}
.feature .feature-box .iconset {
    background: #fff none repeat scroll 0 0;
    float: left;
    position: relative;
    width: 18%;
}
.feature .feature-box .iconset::after {
    background: #fdb801 none repeat scroll 0 0;
    content: "";
    height: 150%;
    left: 43%;
    position: absolute;
    top: 100%;
    width: 1px;
}

.feature .feature-box .feature-content h4 {
    color: #0f0f0f;
    font-size: 18px;
    letter-spacing: 0;
    line-height: 22px;
    margin: 0 0 5px;
}

.feature .feature-box .feature-content {
    float: left;
    padding-left: 28px;
    width: 78%;
}
.feature .feature-box .feature-content h4 {
    color: #0f0f0f;
    font-size: 18px;
    letter-spacing: 0;
    line-height: 22px;
    margin: 0 0 5px;
}
.feature .feature-box .feature-content p {
    color: #606060;
    font-size: 13px;
    line-height: 22px;
}
.icon {
    color : #f4b841;
    padding:0px;
    font-size:40px;
    border: 1px solid #fdb801;
    border-radius: 100px;
    color: #fdb801;
    font-size: 28px;
    height: 70px;
    line-height: 70px;
    text-align: center;
    width: 70px;
}

</style>


