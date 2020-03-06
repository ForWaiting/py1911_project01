import jsCookie from 'js-cookie'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000';

// 拦截请求
axios.interceptors.request.use(function (config) {
    // Do something before request is sent
	if(jsCookie.get('access')){
		config.headers.Authorization = `Bearer ${jsCookie.get('access')}`
	}
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });

// 拦截响应
axios.interceptors.response.use(function (response) {
    // Do something with response data
    return response;
  }, function (error) {
    // Do something with response error
	if(error.response.status== 401){
		// 根据refresh重新请求access
		console.log('认证失败');
		window.location.href='#/login/'
		jsCookie.remove('access');
		jsCookie.remove('refresh');
		jsCookie.remove('username');
		jsCookie.remove('userinfo');
	}
    return Promise.reject(error);
  });
  
  
  
export const getCategoryList = ()=>{
	return axios.get('/api/v1/categorys/')
}

export const getCategoryDetail = (param)=>{
	return axios.get(`/api/v1/categorys/${param.id}/`)
}

export const createCategory = (param)=>{
	return axios.post('/api/v1/categorys/',param)
}

export const modifyCategory = (param)=>{
	return axios.put(`/api/v1/categorys/${param.id}/`,param)
}

export const getToken = (param)=>{
	return axios.post('/tokenlogin/',param,)
}

export const getUserinfo = (param)=>{
	return axios.get('/getuserinfo/',param,)
}

export const regist = (param)=>{
	return axios.post('/api/v1/users/',param,)
}

export const modifyInfo = (param)=>{
	console.log(param)
	return axios.patch(`/api/v1/users/${param.userinfo.id}/`,param.userinfo)
}