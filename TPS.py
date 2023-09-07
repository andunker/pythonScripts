import datetime
from datetime import timedelta


def set_rate_limit(numeber_of_request, tps):
    executions = 0
    lost_requests = 0

    now_time = datetime.datetime.now()
    exp_time = now_time + timedelta(seconds=1)
    
    ext_exp_time = now_time + timedelta(seconds=1)

    for _ in range(numeber_of_request):
        now_time = datetime.datetime.now()
        if exp_time > now_time:
            if executions < tps:
                #print("Hello world")
                executions = executions + 1
            else:
                #print("Rate limited")
                lost_requests = lost_requests + 1
        else:
            exp_time = now_time + timedelta(seconds=1)
            executions = 0

     
    while lost_requests != 0:
        if ext_exp_time <  datetime.datetime.now():
            print(lost_requests)
            lost_requests = set_rate_limit(lost_requests, tps)
    
    return lost_requests


tps = 3
result = set_rate_limit(1000, tps)
print(result)