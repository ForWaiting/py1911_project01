<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">首页</router-link> |
	  <span  v-if="!islog" >
		<router-link to="/login/">登录</router-link>|
		<router-link to="/regist/">注册</router-link>
	  </span>
	  
	  <span v-else >
	  		<router-link to="/usercenter/">用户:{{$jsCookie.get('username')}}</router-link>|
	  		<span @click="logout">退出</span>
	  </span>
	  
	  
    </div>
    <router-view/>
  </div>
</template>

<script>
	export default{
		data(){
			return{
				
			}
		},
		computed:{
			islog(){
				// return this.$store.getters.getLog
				return this.$store.state.islog
			}
		},
		methods:{
			logout(){
				this.$router.push('/')
				this.$jsCookie.remove('username')
				this.$jsCookie.remove('userinfo')
				this.$jsCookie.remove('refresh')
				this.$jsCookie.remove('access')
				this.$store.commit('setLog',false)
			}
		}
	}
</script>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
