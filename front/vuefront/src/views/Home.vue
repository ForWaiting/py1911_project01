<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
	<div>
		<button @click="requestCategoryList">发起请求分类列表</button>
	</div>
	<div>
		<label for="">用户名:</label> <input type="text" v-model="username">
		<br>
		<label for="">密码:</label> <input type="text" v-model="password" >
		<br>
		<button @click="requestToken">发起请求Token</button>
	</div>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
	  return{
		  username:'admin',
		  password:'123456'	
	  }
  },
  components: {
    // HelloWorld
  },
  methods:{
	  requestCategoryList(){
		  // console.log('点击了按钮')
		  this.$http({
			  method:'get',
			  url:'http://127.0.0.1:8000/api/v1/categorys/',
		  }).then(res=>{
			  console.log('分类列表',res);
		  }).catch(err=>{
			  console.log('发生错误',err);
		  })
	  },
	  requestToken(){
		  this.$http({
			  method:'post',
			  url:'http://127.0.0.1:8000/tokenlogin/',
			  data:{
				  username:this.username,
				  password:this.password,
			  }
		  }).then(res=>{
			  console.log('得到Token',res)
		  }).catch(err=>{
			  console.log('发生错误',err)
		  })
	  }
  }
}
</script>
