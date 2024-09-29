import runner as r
import unittest as u


class RunnerTest(u.TestCase):
    def test_walk(self):
        self.obj_1 = r.Runner('Antilopa')
        [self.obj_1.walk() for i in range(9)]  # Here we make a mistake. Change to range(10) and it'll work well.
        self.assertEqual(self.obj_1.distance, 50)

    def test_run(self):
        self.obj_2 = r.Runner('Lopa')
        [self.obj_2.run() for j in range(10)]
        self.assertEqual(self.obj_2.distance, 100)

    def test_challenge(self):
        self.obj_3 = r.Runner('Joka')
        self.obj_4 = r.Runner('Boka')
        [self.obj_3.run() for k in range(10)]
        [self.obj_4.walk() for l in range(10)]
        self.assertNotEqual(self.obj_3.distance, self.obj_4.distance)
