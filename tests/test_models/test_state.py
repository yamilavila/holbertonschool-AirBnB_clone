#!/use/bin/python3
""" Unitest Review class """

from models.state import State
import unittest
import pep8


class TestCity(unittest.TestCase):
    """ Test Review using unit test"""

    def testPep8(self):
        """ pep8 linter requirements"""

        pep8stl = pep8.StyleGuide(quite=True)
        result = pep8stl.check_files(['models/state.py',
                                      'test/test_models/test_state.py'])

    def testInit(self):
        """ Test Initialization """
        self.new_state = State()
        self.assertIsInstance(self.new_instnce, State)

    def testId(self):
        """ sest that uid is working """

        self.id_rev_1 = State()
        self.id_rev_2 = State()
        self.assertNotEqual(self.id_rev_1.id,
                            self.id_rev_2.id)

    def testCreate(self):
        """ test create is working """
        self.create_rev_1 = State()
        self.create_rev_2 = State()
        self.assertNotEqual(self.create_rev_1.created_at,
                            self.create_rev_2.created_at)

    def testSave(self):
        """ Test that save works """
        self.save_rev = State()
        self.bef_save = self.save_state.update_at
        self.save_state.save()
        self.after_save = self.save_state.update_at
        self.assertNotEqual(self.bef_save, self.aftr_save)

    def testDict(self):
        """ test dictionary by comparison """

        self.i_state = State()
        self._dict = dict(self.i_state.__dict__)
        self.dict['__class__'] = "State"
        self.dict['create_at'] =\
                self.dict['create_at'].isoformat()
        self.dict['update_at'] =\
                self.dict['update_at'].isoformat()
        self.assertDictEqual(self.dict, self.i_state.to_dict())

    if __name__ == '__main__':
        unittest.main()
