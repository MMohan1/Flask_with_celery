from edge import celery

@celery.task(queue="default")
def celery_test():
    print "HJHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    return "Say Hello TEST"

@celery.task(queue="matchingJob")
def celery_test_kk():
    print "HJHHHHHHHHHHHHHHHHHHKKKKKKKKKKKKKKKKKKKHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    return "Say Hello TEST KKK"