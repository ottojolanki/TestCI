import unittest
from runsimpleapp import runsimpleapp_getoutput


class TestSimpleApp(unittest.TestCase):

    def setUp(self):
        pass

    def test_runsimpleapp_emptyinput(self):
        self.assertEqual(runsimpleapp_getoutput(input_str='', sleep_int=5), '')

    def test_runsimpleapp_nonemptyinput(self):
        self.assertEqual(runsimpleapp_getoutput(input_str='there is input',
                                                sleep_int=5), 'there is input')


if __name__ == "__main__":
    unittest.main()