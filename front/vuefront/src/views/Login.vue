<template>
	<div class="login">
<!-- 		<div>
			<label for="">用户名:</label> <input type="text" v-model="username">
			<br>
			<label for="">密码:</label> <input type="text" v-model="password" >
			<br>
			<button @click="requestToken">发起请求Token</button>
		</div> -->
		<van-form @submit="requestToken">
		  <van-field
		    v-model="username"
		    name="用户名"
		    label="用户名"
		    placeholder="用户名"
		    :rules="[{ required: true, message: '请填写用户名' }]"
		  />
		  <van-field
		    v-model="password"
		    type="password"
		    name="密码"
		    label="密码"
		    placeholder="密码"
		    :rules="[{ required: true, message: '请填写密码' }]"
		  />
		  <div style="margin: 16px;">
		    <van-button round block type="info" native-type="submit">
		      提交
		    </van-button>
		  </div>
		</van-form>
	</div>
</template>

<script>
	export default{
		data(){
			return {
				username:'admin',
				password:'123456',
			}
		},
		methods:{
			requestToken(){
			  this.$api.getToken({
				  username:this.username,
				  password:this.password,
			  }).then(res=>{
				  console.log('得到Token',res)
				  this.$jsCookie.set('refresh',res.data.refresh);
				  this.$jsCookie.set('access',res.data.access);
				  this.$jsCookie.set('username',this.username);
				  this.$router.push('/');
				  this.$store.commit('setLog',true)
			  }).catch(err=>{
				  console.log('发生错误',err)
				  this.$toast('登录错误')
			  })
			},
		}
	}
</script>

<style>
</style>
