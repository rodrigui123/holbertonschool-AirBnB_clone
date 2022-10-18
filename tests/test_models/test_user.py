#!/usr/bin/python3
import os
import unittest
from models.user import User


class UserTest(unittest.TestCase):
    def test_attribute(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")