import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.common import response_success, response_failed, ErrorCode
from interface_app.models.service import Service


class ServiceList(View):
    def get(self, request, *args, **kwargs):
        """
        获取列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        services = Service.objects.all()
        result = []
        for r in services:
            res = model_to_dict(r)
            result.append(res)
        return response_success(result)

    def post(self, request, *args, **kwargs):
        """
        创建数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        data = json.loads(body, encoding='utf-8')
        form = ServiceForm(data)
        if not form.is_valid():
            return response_failed()

        service = Service.create(**form.cleaned_data)
        if not service:
            return response_failed(code=ErrorCode.common,message="创建数据失败")
        else:
            return response_success(model_to_dict(service))
