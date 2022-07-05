#!/use/bin/python3
""" Unitest Review class """

import pep8
from models.base_models import BaseModel
from models.user import User
import unittest

class TestReview(unittest.TestCase):
    """ Test Review using unit test"""

    def testPep8(self):
        """ pep8 linter requirements"""

        pep8stl = pep8.StyleGuide(quite=True)
        result = pep8stl.check_files(['models/user.py',
                                      'test/test_models/test_user.py'])
        self.assertEqual(result.total_error, 0,
                "Found codes style error (and warnings)."

    def testInit(self):
        """ Test Initialization """
        self.new_instance = User()
        self.assertIsInstance(self.new_instnce, User)

    def testId(self):
        """ sest that uid is working """

        self.id_rev_1 = User()
        self.id_rev_2 = User()
        self.assertNotEqual(self.id_rev_1.id,
                            self.id_rev_2.id)

    def testCreate(self):
        """ test create is working """
        self.create_rev_1 = User()
        self.create_rev_2 = User()
        self.assertNotEqual(self.create_rev_1,
                            self.create_rev_2)

    def testSave(self):
        """ Test that save works """
        self.save_usr = User()
        self.bef_save = self.save_usr.update_at
        self.save_rev.save()
        self.after_save = self.save_rev.update_at
        self.assertNotEqual(self.bef_save, self.aftr_save)

    def testUpdate(self):
        """ check update of user works"""
        self.update_usr = User()
        self.bef_update = self.update_usr.created_at
        self.update_usr.save()
        self.aftr_update = update_usr.created_at
        self.assertEqual(self.bef_update, self.aftr_update)

    def testDict(self):
        """ test dictionary by comparison """

        self.i_User = User()
        self._dict = dict(self.i_review.__dict__)
        self.dict['__class__'] = "User"
        self.dict['create_at'] =\
                self.dict['update_at'].isoformat()
        self.dict['update_at'] =\
                self.dict['update_at'].isoformat()
        self.assertDictEqual(self.dict, self.i_user.to_dict()

    if __name__ == '__main__':
        inittest.main()

