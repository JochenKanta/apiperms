from unittest import TestCase

from qumulo import rest_client
from qumulo.lib.request import RequestError

QHOST='192.168.11.155'
QPORT=8000
QUSER='admin'
QPASS='Admin123'

RC = rest_client.RestClient(address=QHOST, port=QPORT)
RC.login(username=QUSER, password=QPASS)

try:
    RC.fs.create_directory(name='test_set_acl', dir_path='/')
except RequestError as e:
    if "fs_entry_exists_error" in str(e):
        print("WARNING: Directory exists")

CONTROL_DEFAULT = ['PRESENT', 'AUTO_INHERIT']
ACES_WITH_DOMAIN = [{"rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "WRITE_EA", "WRITE_ATTR", "WRITE_ACL", "CHANGE_OWNER", "WRITE_GROUP", "DELETE", "EXECUTE", "MODIFY", "EXTEND", "DELETE_CHILD", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-512", "uid": None, "auth_id": "21474836992", "gid": None, "domain": "ACTIVE_DIRECTORY", "name": "DEMO\Domain Admins"}, "flags": ["OBJECT_INHERIT", "CONTAINER_INHERIT"], "type": "ALLOWED"}, {"flags": [], "rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "EXECUTE", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-513", "uid": None, "domain": "ACTIVE_DIRECTORY", "gid": None, "name": "DEMO\Domain Users", "auth_id": "21474836993"}, "type": "ALLOWED"}]

ACES_SIMPLE = [{"rights": ["READ"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-512", "uid": None, "auth_id": "21474836992", "gid": None, "domain": "ACTIVE_DIRECTORY", "name": "DEMO\Domain Admins"}, "flags": ["OBJECT_INHERIT", "CONTAINER_INHERIT"], "type": "ALLOWED"}]
ACES_SIMPLER = [{"rights": ["READ"], "trustee": {"name": "DEMO\Domain Admins"}, "flags": ["OBJECT_INHERIT", "CONTAINER_INHERIT"], "type": "ALLOWED"}]

with open("parent_qacl.json") as parent_qacl:
    PARENT_QACL = parent_qacl.read()
ACL_V2 =


class TestSetAcl(TestCase):
    def test_set_acl(self):
        RC.fs.set_acl(path='/test', aces=ACES_WITH_DOMAIN, control=CONTROL_DEFAULT)

    def test_set_simple_acl(self):
        RC.fs.set_acl_v2(path='/test', aces=ACES_SIMPLER,
                      control=CONTROL_DEFAULT)
