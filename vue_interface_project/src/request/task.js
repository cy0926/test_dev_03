import { postRequest, getRequest, deleteRequest, putRequest} from "./common";

export const getAllTasks = function () {
    return getRequest('tasks/')   // 获取所有的服务
};


export const addTask = function (data) {
    return postRequest('tasks/', data)  //添加Task
      
};

export const getSingleTask  = function (taskId) {
    return getRequest(`task/${taskId}/`)   //获取单个服务
    
};

export const updateTask = function(taskId, data){
    return putRequest(`task/${taskId}/`, data)  //更新服务
};

export const deleteTask = function(taskId){
    return deleteRequest(`task/${taskId}/`)
}