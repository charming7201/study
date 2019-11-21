import Myunittest


class TestA(Myunittest.TestCase):

    def test_show(self):
        self.assertEqual('i','i')


Myunittest.main()
