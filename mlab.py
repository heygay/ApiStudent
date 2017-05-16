import mongoengine

##mongodb://<dbuser>:<dbpassword>@ds143141.mlab.com:43141/apistudent

host = "ds143141.mlab.com"
port = 43141
db_name = "apistudent"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())