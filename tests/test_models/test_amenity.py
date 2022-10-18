#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class AmenityTest(unittest.TestCase):
    def test_attribute(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")