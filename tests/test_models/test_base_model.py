#!/usr/bin/python3
import os
import unittest
from models.base_model import BaseModel


class BaseModelClass(unittest.TestCase):
    def test_save(self):
        base = BaseModel()
        created_at = base.created_at
        update_at = base.updated_at
        base.save()
        self.assertNotEqual(update_at, base.updated_at)
        self.assertEqual(created_at, base.created_at)

    def test_to_dict(self):
        base = BaseModel()
        temp = {}
        temp['id'] = self.id
        temp['__class__'] = base.__class__.__name__
        temp['created_at'] = base.created_at.isoformat()
        temp['updated_at'] = base.updated_at.isoformat()
        self.assertEqual(temp, base.to_dict())

    def test_save(self):
        base = BaseModel()
        try:
            os.remove('file.json')
        except Exception:
            pass
        base.save()
        self.assertTrue(os.path.exists('file.json'))
