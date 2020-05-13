#!/usr/bin/env python

"""
These unittests should all pass once your configuration is correct for your
environment
"""

import configuration

from pprint import pprint
from unittest import TestCase


class TestConfiguration(TestCase):
    def test_expand_identity(self):
        result = configuration.RC.auth.find_identity(name=configuration.USERS_GROUP_NAME)
        print(result)

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
