#!/usr/bin/env python

import configuration

from unittest import TestCase


# {'domain': 'ACTIVE_DIRECTORY', 'auth_id': '21474836992', 'uid': None, 'gid': None, 'sid': 'S-1-5-21-3759427542-666250840-780413923-512', 'name': 'DEMO\\Domain Admins'}
# {'domain': 'ACTIVE_DIRECTORY', 'auth_id': '21474836993', 'uid': None, 'gid': None, 'sid': 'S-1-5-21-3759427542-666250840-780413923-513', 'name': 'DEMO\\Domain Users'}

#ACES_WITH_NULL = [{"rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "WRITE_EA", "WRITE_ATTR", "WRITE_ACL", "CHANGE_OWNER", "WRITE_GROUP", "DELETE", "EXECUTE", "MODIFY", "EXTEND", "DELETE_CHILD", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-512", "uid": null, "auth_id": "21474836992", "gid": null, "domain": "ACTIVE_DIRECTORY", "name": "Domain Admins"}, "flags": ["OBJECT_INHERIT", "CONTAINER_INHERIT"], "type": "ALLOWED"}, {"flags": [], "rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "EXECUTE", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-513", "uid": null, "domain": "ACTIVE_DIRECTORY", "gid": null, "name": "Domain Users", "auth_id": "21474836993"}, "type": "ALLOWED"}]
ACES_WITH_NONE = [{"rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "WRITE_EA", "WRITE_ATTR", "WRITE_ACL", "CHANGE_OWNER", "WRITE_GROUP", "DELETE", "EXECUTE", "MODIFY", "EXTEND", "DELETE_CHILD", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-512", "uid": None, "auth_id": "21474836992", "gid": None, "domain": "ACTIVE_DIRECTORY", "name": "Domain Admins"}, "flags": ["OBJECT_INHERIT", "CONTAINER_INHERIT"], "type": "ALLOWED"}, {"flags": [], "rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "EXECUTE", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-513", "uid": None, "domain": "ACTIVE_DIRECTORY", "gid": None, "name": "Domain Users", "auth_id": "21474836993"}, "type": "ALLOWED"}]
ACES_WITH_DOMAIN = [{"rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "WRITE_EA", "WRITE_ATTR", "WRITE_ACL", "CHANGE_OWNER", "WRITE_GROUP", "DELETE", "EXECUTE", "MODIFY", "EXTEND", "DELETE_CHILD", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-512", "uid": None, "auth_id": "21474836992", "gid": None, "domain": "ACTIVE_DIRECTORY", "name": "DEMO\\Domain Admins"}, "flags": ["OBJECT_INHERIT", "CONTAINER_INHERIT"], "type": "ALLOWED"}, {"flags": [], "rights": ["READ", "READ_EA", "READ_ATTR", "READ_ACL", "EXECUTE", "SYNCHRONIZE"], "trustee": {"sid": "S-1-5-21-3759427542-666250840-780413923-513", "uid": None, "domain": "ACTIVE_DIRECTORY", "gid": None, "name": "DEMO\\Domain Users", "auth_id": "21474836993"}, "type": "ALLOWED"}]


class TestConfiguration(TestCase):
    def test_expand_identity(self):
        result = configuration.RC.auth.find_identity(name=configuration.USERS_GROUP_NAME)
        print(result)
        self.assertTrue(False)

    def test_auth_id_from_name(self):
        target = '21474836993'
        result = configuration.auth_id_from_name(configuration.USERS_GROUP_NAME)
        self.assertEqual(target, result)
        target = '21474836992'
        result = configuration.auth_id_from_name(configuration.ADMINS_GROUP_NAME)
        self.assertEqual(target, result)


class TestAcl(TestCase):
    def test_fs_set_acl_v2(self):
        configuration.RC.fs.set_acl_v2(path='/test', acl=configuration.PARENT_QACL)