import os

import uwsgidecorators
from django.core.wsgi import get_wsgi_application

import api.sentry as sentry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

application = get_wsgi_application()

sentry.initialize()


@uwsgidecorators.postfork
def preload():
    from api.core.task_runner import Runner

    if os.getenv("API_TASK_RUNNER_ENABLED") == "True":
        Runner.instance()
