from . import Exercise


class Solution:
    def __init__(self, exercise, uid, date, status, points):
        self.exercise: Exercise = exercise
        self.uid = uid
        self.date = date
        self.status = status
        self.points = points

    def __str__(self) -> str:
        return "{} - {}, {} points. ({})".format(self.date, self.status, self.points, self.uid)
