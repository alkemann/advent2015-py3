from Reindeer import Reindeer

class SolutionFourteen:
    def __init__(self):
        self.winners = []
        self.longest_distance = 0;
        self.time = 0

    def run_deers(self, deers, duration = 10):
        for t in range(0, duration):
            self.time += 1
            for d in deers:
                d.second()
                if d.distance > self.longest_distance:
                    self.winners = [d]
                    self.longest_distance = d.distance
                elif d.distance == self.longest_distance and d not in self.winners:
                    self.winners.append(d)
            for w in self.winners:
                w.score += 1

    def which_deer_traveled_furthest(self, deers):
        winner = 0
        longest_distance = 0
        for d in deers:
            if d.distance > longest_distance:
                winner = d
                longest_distance = d.distance

        return winner

    def whch_deer_scored_most(self, deers):
        winner = 0
        points = 0
        for d in deers:
            if d.score > points:
                winner = d
                points = d.score

        return winner
