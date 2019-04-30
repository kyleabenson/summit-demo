from tower_cli import get_resource
from tower_cli.exceptions import CannotStartJob
from tower_cli.conf import settings

def hello_world(request):
    request_json = request.get_json()
    if request_json and 'incident' in request_json:
        limit_value = request_json['incident']['resource_name']
        with settings.runtime_values(username='admin', password='ansible'):
            try:
                res = get_resource('job')
                # jt_list = res.list()
                launch_job = res.launch(job_template=8, monitor=True, limit=limit_value)
                return 
            except CannotStartJob:
                print('Unable to start this job')
                return    
    # elif request.args and 'message' in request.args:
    #     return request.args.get('message')
    else:
        return f'Hello World!'

