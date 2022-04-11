import unittest
from recorder import Recorder
from remember import Remember


class Test(unittest.TestCase):
    def setUp(self):
        self.remember = Remember()
        self.recorder = Recorder()

    def test_write_to_recorder(self):
        data = {"message": "asdadsa", "title": "dsfsfds"}

        self.assertTrue(self.recorder.save(data))

    def test_remember(self):
        self.remember.remember()


if __name__ == "__main__":
    unittest.main()
