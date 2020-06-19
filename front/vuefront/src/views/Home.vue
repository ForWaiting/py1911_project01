<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
<!-- 	<div>
		<button @click="requestCategoryList">请求分类列表</button>
	</div> -->
	<div class="category">
		
		<van-cell v-for="(item,index) in categorys" :key="index" :title="item.name" is-link :to="'/categorys/'+item.id + '/' " />
 
	</div>

	<div>
		<van-field v-model="categoryName" placeholder="请输入分类名" />
		<br>
		<van-button  @click="requestCreateCategory" color="#7232dd">创建分类请求</van-button>
	</div>
<!-- 	<div>
		<label for="">需要修改的分类ID</label>
		<input type="text" v-model="newCategoryId">
		<br>
		<label for="">需要修改的分类类名</label>
		<input type="text" v-model="newCategoryName" >
		<br>
		<button @click="requestModifyCategory" >修改分类</button>
	</div> -->
<!-- 	<div>
		<label for="">用户名:</label> <input type="text" v-model="username">
		<br>
		<label for="">密码:</label> <input type="text" v-model="password" >
		<br>
		<button @click="requestToken">发起请求Token</button>
	</div> -->
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data(){
	  return{
		  categorys:[],
		  categoryName:'',
		  // newCategoryName:'',
		  // newCategoryId:'',
		  
	  }
  },
  components: {
    // HelloWorld
  },
  created() {
  	this.requestCategoryList();
  },
  methods:{
	  requestCategoryList(){
		  this.$api.getCategoryList().then(res=>{
			  console.log('分类列表',res);
			  if(res.status==200){
				  this.categorys=res.data
			  }
		  }).catch(err=>{
			  console.log('出错了',err);
		  })
	  },
	  requestCreateCategory(){
		  if(this.categoryName != ''){
		  	 this.$api.createCategory({
				 name:this.categoryName
			 }).then(res=>{
				 console.log('创建了',res);
				 this.categorys.push(res.data);
				 this.categoryName = '';
			 }).catch(err=>{
				 console.log('出错了',err);
			 })
	  }else{
		  this.$toast('必须输入分类名')
		  console.log('必须输入分类名')
	  }
	},
	// requestModifyCategory(){
	// 	if(this.newCategoryId == '' || this.newCategoryName==''){
	// 		console.log('需要选择分类，命名')
	// 	}else{
	// 		this.$api.modifyCategory({
	// 			id:this.newCategoryId,
	// 			name:this.newCategoryName,
	// 		}).then(res=>{
	// 			console.log(res)
	// 		}).catch(err=>{
	// 			console.log(err)
	// 		})
	// 	}
	// },
	
	
  }
}
</script>
