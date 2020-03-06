import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
	islog:false
  },
 //  getters:{
	// getLog(state){
	// 	return state.islog
	// }  
  // },
  mutations: {
	  setLog(state,b){
		  state.islog=b
	  }
  },
  actions: {
  },
  modules: {
  }
})
