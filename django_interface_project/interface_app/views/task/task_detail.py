from interface_app.forms.task_form import TaskForm
from interface_app.libs.common import ErrorCode
from interface_app.models.model_ import Task
from interface_app.views.base.base_detail import MyBaseDetailView


class TaskDetailView(MyBaseDetailView):
    model = Task
    form = TaskForm
    code = ErrorCode.task
