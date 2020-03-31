from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from interface_app.forms.user_form import UserForm
# Create your views here.
import json
from interface_app.libs.common import response_failed, ErrorCode, response_success


@require_http_methods(['POST'])
def user_login(request, *args, **kwargs):
    """
    用户登录
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    # 用UserForm做字段的格式校验
    # form = UserForm(request.POST)
    # print("=========>", request.POST)
    body = request.body
    data = json.loads(body, encoding='utf-8')
    form = UserForm(data)
    if not form.is_valid():
        return response_failed()
    user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    if not user:
        return response_failed(code=ErrorCode.auth_error,
                               message="登录失败")
    else:
        login(request, user)  # 登录持久化，记录session
        return response_success()


@require_http_methods(['POST'])
def user_register(request, *args, **kwargs):
    """
    用户注册
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    # user = UserForm(request.POST)
    body = request.body
    data = json.loads(body, encoding='utf-8')
    form = UserForm(data)
    if not form.is_valid():
        # print(user.cleaned_data['username'])
        # print(user.cleaned_data['password'])
        return response_failed()

    # 先判断注册用户是否已存在
    if User.objects.filter(username=form.cleaned_data['username']).exists():

        return response_failed(code=ErrorCode.auth_error, message="用户已存在")

    user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    if not user:
        return response_failed(code=ErrorCode.auth_error, message="注册失败")
    else:
        login(request, user)
        return response_success()


@require_http_methods(['DELETE'])
def user_logout(request, *args, **kwargs):
    logout(request)
    return response_success()


@require_http_methods(['GET'])
def get_user_info(request, *args, **kwargs):
    user = request.user   # 获取当前已登录的用户信息
    if not user:
        return response_failed(code=ErrorCode.auth_error,
                               message="用户未登录")
    if user.is_authenticated:  # 判断用户是否已经通过校验，多一点判断更加保险一点
        return response_success(data={
            "id": user.id,
            "name": user.username
        })
    else:
        return response_failed(code=ErrorCode.auth_error,
                               message="用户未登录")
