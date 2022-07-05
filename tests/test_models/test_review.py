#!/use/bin/python3
""" Unitest Review class """

import pep8
from models.review import Review
import pep8

class TestReview(unittest.TestCase):
    """ Test Review using unit test"""

    def testPep8(self):
        """ pep8 linter requirements"""

        pep8stl = pep8.StyleGuide(quite=True)
        result = pep8stl.check_files(['models/review.py',
                                      'test/test_models/test_review.py'])

    def testInit(self):
        """ Test Initialization """
        self.new_instance = Review()
        self.assertIsInstance(self.new_instnce, Review)

    def testId(self):
        """ sest that uid is working """

        self.id_rev_1 = Review()
        self.id_rev_2 = Review()
        self.assertNotEqual(self.id_rev_1.id,
                            self.id_rev_2.id)

    def testCreate(self):
        """ test create is working """
        self.create_rev_1 = Review()
        self.create_rev_2 = Review()
        self.assertNotEqual(self.create_rev_1,
                            self.create_rev_2)

    def testSave(self):
        """ Test that save works """
        self.save_rev = Review()
        self.bef_save = self.save_rev.update_at
        self.save_rev.save()
        self.after_save = self.save_rev.update_at
        self.assertNotEqual(self.bef_save, self.aftr_save)

    def testDict(self):
        """ test dictionary by comparison """

        self.i_review = Review()
        self._dict = dict(self.i_review.__dict__)
        self.dict['__class__'] = "Review"
        self.dict['create_at'] =\
            self.dictionary['created_at'] =\
        self.dict['update_at'] =\
            self.dictionary['update_at'] =\
        self.assertDictEqual(self.dict, self.i_review.to_dict())



