import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.common import response_failed, response_success, ErrorCode
from interface_app.models.service import Service


class ServiceDetail(View):
    def get(self, request, service_id, *args, **kwargs):
        """
        获取单个数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        service = Service.objects.filter(id=service_id).first()
        if not service:
            return response_failed(code=ErrorCode.common, message="数据不存在")
        return response_success(model_to_dict(service))

    def put(self, request, service_id, *args, **kwargs):
        """
        修改单个数据
        :param request:
        :param service_id:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        # 将得到的body数据转换成字典
        data = json.loads(body, encoding='utf-8')
        form = ServiceForm(data)
        if not form.is_valid():
            return response_failed()

        service = Service.objects.filter(id=service_id).first()
        if not service:
            return response_failed(code=ErrorCode.common, message="数据不存在")
        service = Service.objects.filter(id=service_id).update(**form.cleaned_data)
        return response_success(model_to_dict(service))

    def delete(self, request, service_id, *args, **kwargs):
        """
        删除单个数据
        :param request:
        :param service_id:
        :param args:
        :param kwargs:
        :return:
        """
        service = Service.objects.filter(id=service_id).first()
        if not service:
            return response_failed(message="删除的数据不存在")
        Service.objects.filter(id=service_id).delete()
        return response_success()
