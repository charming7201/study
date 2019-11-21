from survey import AnonymousSurvey
import Myunittest



class TestAnonymousSurvey(Myunittest.TestCase):
    '''针对AnonymousSurvey类的测试'''
    def test_show(self):
        self.assertEqual('i','i')
    def test_store_single_response(self):
        question = 'what language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')

        self.assertIn('english',my_survey.responses)

Myunittest.main()
