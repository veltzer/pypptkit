"""Behavioural tests for pypptkit's file helpers."""

import os
import tempfile
import unittest

from pypptkit import utils


class EnsureDirTests(unittest.TestCase):
    def test_creates_missing_parent(self):
        with tempfile.TemporaryDirectory() as d:
            target = os.path.join(d, "a", "b", "file.txt")
            utils.ensure_dir(target)
            self.assertTrue(os.path.isdir(os.path.join(d, "a", "b")))

    def test_no_error_when_parent_exists(self):
        with tempfile.TemporaryDirectory() as d:
            target = os.path.join(d, "file.txt")
            utils.ensure_dir(target)
            self.assertTrue(os.path.isdir(d))

    def test_bare_filename_is_noop(self):
        # dirname of a bare name is "", which ensure_dir must skip
        utils.ensure_dir("bare_name_no_dir")
        self.assertFalse(os.path.isdir(""))


class TouchTests(unittest.TestCase):
    def test_creates_new_file(self):
        with tempfile.TemporaryDirectory() as d:
            target = os.path.join(d, "new.txt")
            utils.touch(target)
            self.assertTrue(os.path.isfile(target))

    def test_updates_mtime_of_existing_file(self):
        with tempfile.TemporaryDirectory() as d:
            target = os.path.join(d, "existing.txt")
            with open(target, "w", encoding="utf-8") as fh:
                fh.write("payload")
            os.utime(target, (1000, 1000))
            utils.touch(target)
            self.assertGreater(os.stat(target).st_mtime, 1000)
            # content must be preserved for an existing file
            with open(target, encoding="utf-8") as fh:
                self.assertEqual(fh.read(), "payload")


class TouchMkdirTests(unittest.TestCase):
    def test_creates_dirs_and_file(self):
        with tempfile.TemporaryDirectory() as d:
            target = os.path.join(d, "x", "y", "z.txt")
            utils.touch_mkdir(target)
            self.assertTrue(os.path.isfile(target))

    def test_many_creates_all(self):
        with tempfile.TemporaryDirectory() as d:
            names = [os.path.join(d, f"sub{i}", f"f{i}.txt") for i in range(3)]
            utils.touch_mkdir_many(names)
            for name in names:
                self.assertTrue(os.path.isfile(name))


if __name__ == "__main__":
    unittest.main()
