#!/usr/bin/python3
import unittest
from models.review import Review


class ReviewTest(unittest.TestCase):
    def test_attribute(self):
        review = Review()
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")