import axios from 'axios'
axios.defaults.withCredentials = true  //这句话代表没每次发送请求，都带上cookie

// 定义后端域名
const backendHost = "http://127.0.0.1:8000/api/"

export const postRequest = function (path, data={}) {
    return axios.post(backendHost + path, data)
};

export const getRequest = function (path, data={}) {
    return axios.get(backendHost + path, {
        params: data
    })
};

export const putRequest = function (path, data={}) {
    return axios.put(backendHost + path, data)
    
};

export const deleteRequest = function (path, data={}){
    return axios.dlete(backendHost + path, data)
};

export const patchRequest = function (path, data={}){
    return axios.patch(backendHost + path, data)
};

