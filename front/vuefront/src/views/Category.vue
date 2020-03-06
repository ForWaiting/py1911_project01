<template>
	<div class="category">
		<van-nav-bar
		  title="分类"
		  left-text="返回"
		  left-arrow
		  @click-left="onClickLeft"
		/>
		<div v-if="category">
			<b>分类ID</b> <span v-text="category.id"></span>
			<br>
			<b>分类名字</b> <span v-text="category.name"></span>
			<ul>
				<li v-for="(item,index) in category.goods" :key='index' > {{item.name}}</li>
			</ul>
		</div>
		
	</div>
</template>

<script>
	export default{
		data(){
			return{
				category:null,
			}
		},
		created() {
			this.$api.getCategoryDetail({
				id:this.$route.params.id
			}).then(res=>{
				console.log('分类',res)
				this.category = res.data
			}).catch(err=>{
				console.log('出错了',err)
			})
		},
		methods: {
		    onClickLeft() {
		      this.$router.go(-1);
		    },
			
		}
	}
	
</script>

<style>
</style>
