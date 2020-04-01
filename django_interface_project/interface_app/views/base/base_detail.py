import json

from django.forms import model_to_dict
from django.views.generic import View

from interface_app.forms.service_form import ServiceForm
from interface_app.libs.common import response_failed, response_success, ErrorCode
from interface_app.models.service import Service


class MyBaseDetailView(View):
    model = Service
    form = ServiceForm
    code = ErrorCode.common

    def get(self, request, base_id, *args, **kwargs):
        """
        获取单个数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        model_data = self.model.objects.filter(id=base_id).first()
        if not model_data:
            return response_failed(code=self.code, message="数据不存在")
        return response_success(model_to_dict(model_data))

    def put(self, request, base_id, *args, **kwargs):
        """
        修改单个数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        body = request.body
        # 将得到的body数据转换成字典
        data = json.loads(body, encoding='utf-8')
        form = self.form(data)
        if not form.is_valid():
            return response_failed()

        model_data = self.model.objects.filter(id=base_id).first()
        if not model_data:
            return response_failed(code=self.code, message="数据不存在")
        model_data = self.model.objects.filter(id=base_id).update(**form.cleaned_data)
        return response_success(model_to_dict(model_data))

    def delete(self, request, base_id, *args, **kwargs):
        """
        删除单个数据
        :param request:
        :param base_id:
        :param args:
        :param kwargs:
        :return:
        """
        model_data = self.model.objects.filter(id=base_id).first()
        if not model_data:
            return response_failed(message="删除的数据不存在")
        self.model.objects.filter(id=base_id).delete()
        return response_success()
