import { postRequest, getRequest, deleteRequest, putRequest} from "./common";

export const getAllServices = function () {
    return getRequest('services/')   // 获取所有的服务
};


export const addService = function (data) {
    return postRequest('services/', data)  //添加service
      
};

export const getSingleService  = function (serviceId) {
    return getRequest(`service/${serviceId}/`)   //获取单个服务
    
};

export const updateService = function(serviceId,data){
    return putRequest(`service/${serviceId}/`, data)  //更新服务
};

export const deleteService = function(serviceId){
    return deleteRequest(`service/${serviceId}/`)
}