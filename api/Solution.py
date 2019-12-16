import bs4
import json

from . import Exercise


class Solution:
    class Test:
        def __init__(self, exercise, uid, index, status, test_size, time, time_limit, memory, memory_limit):
            self.exercise = exercise
            self.uid = uid
            self.index = index
            self.status = status
            self.test_size = test_size
            self.time = time
            self.time_limit = time_limit
            self.memory = memory
            self.memory_limit = memory_limit

        def __str__(self):
            return "[{}] {} Time: {}/{}s, Memory: {}/{}KB ({})"\
                .format(self.index, self.status, self.time, self.time_limit, self.memory, self.memory_limit, self.uid)

        def update(self):
            r = self.exercise.tichy.session.get("{}/tr_status/{}/".format(self.exercise.tichy.BASE_URL, self.uid))
            j = json.loads(r.content)
            print(j)

    def __init__(self, exercise, uid, date, status, points):
        self.exercise: Exercise = exercise
        self.uid = uid
        self.date = date
        self.status = status
        self.points = points
        self.tests = []
        self.tichy = self.exercise.course.tichy

    def __str__(self) -> str:
        return "{} - {}, {} points. ({})".format(self.date, self.status, self.points, self.uid)

    def fetch_data(self):
        r = self.tichy.session.get("{}/solution/{}/{}/".format(self.tichy.BASE_URL, self.exercise.uid, self.uid))
        soup = bs4.BeautifulSoup(r.content, "html.parser")

        for tr in soup.find(id='results_table').find('tbody').findAll('tr'):
            tds = tr.findAll('td')
            self.tests.append(Solution.Test(
                exercise=self,
                uid=tr.attrs['id'][3:],
                index=tds[0].text,
                status=tds[1].text.strip(),
                test_size=tds[2].text.strip(),
                time=tds[3].text.strip(),
                time_limit=float(tds[4].text.strip()[:-2].replace(',', '.')),
                memory=tds[5].text.strip(),
                memory_limit=int(tds[6].text.strip()[:-3])
            ))

    def get_tests(self):
        return self.tests

    def get_url(self):
        return "{}/solution/{}/{}/".format(self.tichy.BASE_URL, self.exercise.uid, self.uid)
