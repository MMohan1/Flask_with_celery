from edge import celery

@celery.task(queue="default_job")
def celery_test():
    print "HJHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    return "Say Hello"

@celery.task(queue="matchingJobs")
def celery_test_kk():
    print "HJHHHHHHHHHHHHHHHHHHKKKKKKKKKKKKKKKKKKKHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    return "Say Hello KKK"