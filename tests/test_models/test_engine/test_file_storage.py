import unittest
from models.engine.file_storage import FileStorage


class FileStorageTest(unittest.TestCase):
    def test_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_reload(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)