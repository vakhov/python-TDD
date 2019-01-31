from django.test import TestCase

class SmokeTest(TestCase):
    """smoke test"""

    def test_bad_math(self):
        """тест: неправильные математические подсчёты"""
        self.assertEqual(1 + 1, 3)
