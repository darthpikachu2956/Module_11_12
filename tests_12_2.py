import runner_and_tour as r
import unittest as u


class TournamentTest(u.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.obj_osama = r.Runner('Osama', 10)
        self.obj_andrew = r.Runner('Andrew', 9)
        self.obj_nick = r.Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        print("Tournament Results:")
        for result in cls.all_results:
            name_result = {place: runner.name for place, runner in result.items()}
            print(name_result)

    def testOsamaAndNick(self):
        tournament = r.Tournament(90, self.obj_osama, self.obj_nick)
        result = tournament.start()
        last_runner = max(result.keys(), key=int)
        self.assertTrue(result[last_runner] == 'Nick')
        self.all_results.append(result)

    def testAndrewAndNick(self):
        tournament = r.Tournament(90, self.obj_andrew, self.obj_nick)
        result = tournament.start()
        last_runner = max(result.keys(), key=int)
        self.assertTrue(result[last_runner] == 'Nick')
        self.all_results.append(result)

    def testOsamaAndAndrewAndNick(self):
        tournament = r.Tournament(90, self.obj_osama, self.obj_andrew, self.obj_nick)
        result = tournament.start()
        last_runner = max(result.keys(), key=int)
        self.assertTrue(result[last_runner] == 'Nick')
        self.all_results.append(result)


if __name__ == '__main__':
    u.main()
