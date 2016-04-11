from edge import app
from edge.flask_test.tasks.basetask import celery_test
from edge.flask_test.tasks.basetask import celery_test_kk
@app.route('/say/hello')
def rest_autosource_count():
    # celery_test.apply_async(queue='default',
    #                         routing_key='default')
    celery_test.delay()
    return "Hello RAJA"

@app.route('/say/hello/kk')
def rest_autosource_count_kk():
    # celery_test.apply_async(queue='default',
    #                         routing_key='default')
    celery_test_kk.delay()
    return "Hello RAJA KK"