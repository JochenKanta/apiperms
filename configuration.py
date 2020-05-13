import json

from qumulo import rest_client

QHOST='192.168.11.155'
QPORT=8000
QUSER='admin'
QPASS='Admin123'

USERS_GROUP_NAME = 'Domain Users'
ADMINS_GROUP_NAME = 'Domain Admins'

# this will get placed below the named root when running mktree.py
DIRECTORY_SKELETON = [
    'assets',
    'assets/meshes',
    'assets/textures',
    'media',
    'media/clips',
    'media/frames',
    'sim',
    'sim/data',
    'sim/caches',
]

# END OF CONFIGURATION SECTION DON'T TOUCH BELOW

RC = rest_client.RestClient(address=QHOST, port=QPORT)
RC.login(username=QUSER, password=QPASS)


def auth_id_from_name(name):
    response = RC.auth.find_identity(name=name)
    return response['auth_id']


def sid_from_name(name):
    response = RC.auth.find_identity(name=name)
    return response['sid']


with open("child_qacl.json") as child_qacl:
    CHILD_QACL = child_qacl.read()

with open("parent_qacl.json") as parent_qacl:
    PARENT_QACL = parent_qacl.read()


USERS_GROUP_AUTHID = auth_id_from_name(USERS_GROUP_NAME)
USERS_GROUP_SID = sid_from_name(USERS_GROUP_NAME)
ADMINS_GROUP_AUTHID = auth_id_from_name(ADMINS_GROUP_NAME)
ADMINS_GROUP_SID = sid_from_name(ADMINS_GROUP_NAME)


replace_dict = {
    "REPLACE_WITH_ADMINS_GROUP_AUTHID": ADMINS_GROUP_AUTHID,
    "REPLACE_WITH_ADMINS_GROUP_SID": ADMINS_GROUP_SID,
    "REPLACE_WITH_ADMINS_GROUP_NAME": ADMINS_GROUP_NAME,
    "REPLACE_WITH_USERS_GROUP_AUTHID": USERS_GROUP_AUTHID,
    "REPLACE_WITH_USERS_GROUP_SID": USERS_GROUP_SID,
    "REPLACE_WITH_USERS_GROUP_NAME": USERS_GROUP_NAME,
}


for key in replace_dict.keys():
    CHILD_QACL = CHILD_QACL.replace(key, replace_dict[key])
    PARENT_QACL = PARENT_QACL.replace(key, replace_dict[key])


CHILD_QACL = json.loads(CHILD_QACL)
PARENT_QACL = json.loads(PARENT_QACL)
