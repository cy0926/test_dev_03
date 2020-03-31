import { postRequest, getRequest} from "./common";

export const login = function (username, password) {
    return postRequest('user/login/',{   //登录
        username:username,
        password:password
    })
};

export const logout = function () {
    return deleteRequest('user/logout/')   //退出登录
};

export const register = function (username, password) {
    return postRequest('user/register/', {   //注册
        username: username,
        password: password
    })
};

export const getLoginUserInfo = function () {
    return getRequest('user/info/')
    
};