<template>
   <div class="ody">
       <br><br><br>
    <div class="container">
    <h1 class="display-4">Register Your Team Here</h1>   
     <form>
<br>
<div class="form-group">
  <label for="usr">Team_name:</label>
  <input type="text"   class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">admin_name:</label>
  <input type="text"  class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">admin_contact:</label>
  <input type="text"  class="form-control" id="usr">
</div>

      <br>
<button type="submit" class="btn btn-dark">Register</button>
<br><br><br>
    </form>
  </div>
  </div>
</template>

<script>
export default {
    name:"joincontest",
}

</script>

<style scoped>
  
@media only screen and (max-width:700px) {
h1{
            font-size:35px;

        }
h2{
            font-size:15px;
            text-align:center;

        }
h4{
            font-size:10px;
        }
h5{
            font-size:8px;
            font-weight:300;

        }
}


</style>