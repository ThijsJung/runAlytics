def get_runs():
    pass


def get_run(run_id):
    pass


def delete_run(run_id):
    pass


def upload_run(event, context):
    pass

# def get_runs(event, context):
#     db_runs = table.scan(ProjectionExpression='run_id')
#     runs = list()
#     if db_runs['Items']:
#         runs = [run['run_id'] for run in db_runs['Items']]
#     body = json.dumps(runs)
#     return dict(statusCode=200, body=body, headers={'Access-Control-Allow-Origin': '*'})

# def get_run_data(event, context):
#     run_id = str(event['pathParameters']['run_id'])
#     run_data = table.get_item(Key={'run_id': run_id})
#     body = json.dumps(run_data, cls=DecimalEncoder)

#     return dict(statusCode=200, body=body, headers={'Access-Control-Allow-Origin': '*'})
