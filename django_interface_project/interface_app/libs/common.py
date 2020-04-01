from django.http import JsonResponse


class ErrorCode:
    common = 1000
    auth = 1001
    service = 1002
    task = 1003


def common_response(success, data, error_code, message):
    response = {
        "data": data,
        "success": success,
        "error": {
            "code": error_code,
            "message": message
        }
    }
    return JsonResponse(response, safe=False)


def response_success(data='{}'):
    return common_response(True, data, "", "")


def response_failed(code=ErrorCode.common, message="参数错误", data='{}'):
    return common_response(False, data, code, message)
