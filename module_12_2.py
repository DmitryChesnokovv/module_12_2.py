import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", speed=10)
        self.andrey = Runner("Andrey", speed=9)
        self.nick = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results["Usain vs Nick"] = {k: str(v) for k, v in results.items()}
        self.assertTrue(str(results[max(results.keys())]) == "Nick")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["Andrey vs Nick"] = {k: str(v) for k, v in results.items()}
        self.assertTrue(str(results[max(results.keys())]) == "Nick")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["Usain vs Andrey vs Nick"] = {k: str(v) for k, v in results.items()}
        self.assertTrue(str(results[max(results.keys())]) == "Nick")


if __name__ == "__main__":
    unittest.main()
