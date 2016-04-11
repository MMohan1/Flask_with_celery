from flask import Flask
from kombu import Exchange, Queue
from celery import Celery
app = Flask(__name__)

app.config["CELERY_QUEUES"] = (
    Queue('defaultt', Exchange('defaultt'), routing_key='defaultt'),
    Queue('matchingJob', Exchange('matchingJob'), routing_key='matchingJob'),
    Queue('bulk_resume_upload', Exchange('bulk_resume_upload'), routing_key='bulk_resume_upload')
)


def make_celery(flaskapp):
    # basic configuration
    celery_broker_uri = 'amqp://hirealchemy:hirealchemy@localhost:5672/hirealchemy'
    celeryinit = Celery(flaskapp.import_name, broker=celery_broker_uri)
    celeryinit.conf.update(flaskapp.config)
    taskbase = celeryinit.Task

    class ContextTask(taskbase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return taskbase.__call__(self, *args, **kwargs)

    celeryinit.Task = ContextTask
    return celeryinit
    
celery = make_celery(app)

from flask_test.router import routes
from flask_test.tasks import basetask
