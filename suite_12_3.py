import unittest as u
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest


def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper


# For tests_12_1.py
class RunnerTest(u.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_example(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_another_example(self):
        self.assertEqual(1 + 1, 2)


# For tests_12_2.py
class TournamentTest(u.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_tournament_feature(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_another_tournament_feature(self):
        self.assertEqual(2 * 2, 4)


test_suite = u.TestSuite()

test_suite.addTests(u.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(u.TestLoader().loadTestsFromTestCase(TournamentTest))

if __name__ == '__main__':
    runner = u.TextTestRunner(verbosity=2)
    runner.run(test_suite)
