import requests
import traceback

from django.conf import settings
from datetime import datetime


def send_error_log(message) -> None:
    request = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&parse_mode=Markdown&text={}"
    request = request.format(
        settings.LOGGER_BOT_TOKEN, settings.LOGGER_CHAT_ID, message
    )
    requests.post(request)


class ErrorHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if not settings.DEBUG:
            if exception:
                message = (
                    "**Project - cura.uz**\n\n"
                    "**Error time:** {error_time}\n\n"
                    "**Error message:** {error_message}\n\n"
                    "```python\n{error_traceback}\n```"
                ).format(
                    error_time=datetime.now(),
                    error_traceback=traceback.format_exc(),
                    error_message=repr(exception),
                )
                try:
                    send_error_log(message)
                except:
                    pass
        raise exception
