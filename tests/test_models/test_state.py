#!/usr/bin/python3
import unittest
from models.state import State


class StateTest(unittest.TestCase):
    def test_attribute(self):
        state = State()
        self.assertEqual(state.name, "")