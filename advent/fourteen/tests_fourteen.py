import unittest

from Reindeer import Reindeer
from SolutionFourteen import SolutionFourteen


class TestOneSolution(unittest.TestCase):
    def test_floor_counter(self):
        description = "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
        comet = Reindeer(description)
        self.assertEquals(description, comet.__str__())

        description = "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
        dancer = Reindeer(description)
        self.assertEquals(description, dancer.__str__())

    def test_seconds(self):
        description = "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
        dancer = Reindeer(description)
        dancer.second()
        self.assertEquals(16, dancer.distance)
        self.assertEquals(10, dancer.stamina_left)
        dancer.second()
        self.assertEquals(32, dancer.distance)
        self.assertEquals(9, dancer.stamina_left)

    def test_run_deers_for_20_seconds(self):
        comet = Reindeer("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        dancer = Reindeer("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
        deers = [comet, dancer]

        solver = SolutionFourteen()
        solver.run_deers(deers, 20)

        self.assertFalse(comet.flying)
        self.assertEquals(140, comet.distance)
        self.assertEquals(0, comet.stamina_left)
        self.assertEquals(127 - 10, comet.rest_left)

        self.assertFalse(dancer.flying)
        self.assertEquals(176, dancer.distance)
        self.assertEquals(0, dancer.stamina_left)
        self.assertEquals(162 - 9, dancer.rest_left)

    def test_run_deers_for_1000_seconds(self):
        comet = Reindeer("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        dancer = Reindeer("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
        deers = [comet, dancer]

        solver = SolutionFourteen()
        solver.run_deers(deers, 1000)
        self.assertFalse(comet.flying)
        self.assertFalse(dancer.flying)

        self.assertEqual(1120, comet.distance)
        self.assertEqual(1056, dancer.distance)

    def test_who_traveled_farthest(self):
        comet = Reindeer("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        dancer = Reindeer("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
        deers = [comet, dancer]

        solver = SolutionFourteen()
        solver.run_deers(deers, 1000)

        winner = solver.which_deer_traveled_furthest(deers)
        self.assertEqual(comet, winner)

    def test_score_system(self):
        comet = Reindeer("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        dancer = Reindeer("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
        deers = [comet, dancer]
        solver = SolutionFourteen()
        solver.run_deers(deers, 1)
        self.assertEqual(0, comet.score)
        self.assertEqual(1, dancer.score)

        solver.run_deers(deers, 9)
        self.assertEqual(0, comet.score)
        self.assertEqual(10, dancer.score)

        solver.run_deers(deers, 130)
        self.assertEqual(1, comet.score)
        self.assertEqual(139, dancer.score)

    def stest_who_scored_most_points(self):
        comet = Reindeer("Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.")
        dancer = Reindeer("Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.")
        deers = [comet, dancer]
        solver = SolutionFourteen()
        solver.run_deers(deers, 1000)

        self.assertEqual(dancer, solver.whch_deer_scored_most(deers))
        self.assertEqual(689, dancer.score)
        self.assertEqual(312, comet.score)
