<template>
	<div class="usercenter">
		用户中心
		<div v-if="userinfo">
			用户名：{{userinfo.username}}
			<br>
			手机号：{{userinfo.telephone}}
			<br>
			邮箱：{{userinfo.email}}
			<br>
			注册日期：{{userinfo.date_joined|dateFormat}}
			<br>
			<h3>修改信息</h3>
			<van-form @submit="modifyInfo">
			  <van-field
				v-model="userinfo.username"
				name="name"
				label="用户名"
				placeholder="修改后的用户名"
			  />
			  <van-field
				v-model="userinfo.password"
				type="password"
				name="password"
				label="密码"
				placeholder="修改后的密码"
			  />
			  <van-field
				v-model="userinfo.telephone"
				name="tel"
				label="手机号"
				placeholder="修改后的手机号"
			  />
			  <van-field
				v-model="userinfo.email"
				type="email"
				name="email"
				label="邮箱"
				placeholder="修改后的邮箱"
			  />
			  <div style="margin: 16px;">
				<van-button round block type="info" native-type="submit">
				  提交修改
				</van-button>
			  </div>
			</van-form>
		</div>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				userinfo:null,
			}
		},
		created() {
			this.$api.getUserinfo().then(res=>{
				console.log(res.data)
				this.userinfo=res.data;
				this.$jsCookie.set('userinfo',res.data)
			}).catch(err=>{
				console.log('出错了');
			})
		},
		methods:{
			modifyInfo(){
				if(this.newusername == ''||this.newpassword==''||this.newtelephone==''){
					this.$toast('输入新的信息不能为空')
				}else{
					this.$api.modifyInfo({
						userinfo:this.userinfo
					}).then(res=>{
						this.$router.push('/')
						console.log('修改成功',res)
					}).catch(err=>{
						console.log('修改失败',err)
					})
				}
			}
		},
		filters:{
			dateFormat(date){
				date = new Date(date)
				return `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
			}
		},
	}
</script>

<style>
</style>
