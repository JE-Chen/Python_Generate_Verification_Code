import unittest

import JEVerificationCode


class GenerateVerification(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @staticmethod
    def testGenerate():
        JEVerificationCode.GenerateVerificationCode().generate_code_only_string(5)


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(GenerateVerification))
    unittest.TextTestRunner(verbosity=2).run(suite)
