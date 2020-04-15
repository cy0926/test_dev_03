from interface_app.forms.service_form import ServiceForm
from interface_app.libs.common import ErrorCode
from interface_app.models.model_ import Service
from interface_app.views.base.base_detail import MyBaseDetailView


class ServiceDetail(MyBaseDetailView):
    model = Service
    form = ServiceForm
    code = ErrorCode.common


