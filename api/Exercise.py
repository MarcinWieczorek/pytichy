import bs4

from . import Course
from .Solution import Solution


class Exercise:
    def __init__(self, course, num, name, uid, deadline):
        self.course: Course = course
        self.num = num
        self.name = name
        self.uid = uid
        self.deadline = deadline

    def exercise_send(self, code, language):
        send_url = "{}/exercise/{}/send/".format(self.course.tichy.BASE_URL, self.uid)
        token = self.course.tichy.csrf_get(send_url)
        r = self.course.tichy.session.post(send_url, data={
            'csrfmiddlewaretoken': token,
            'src': code,
            'language': language,
        })

        if r.status_code != 200:
            return None

        solution_uid = r.url.replace(self.course.tichy.BASE_URL, "")[10:-1]
        return Solution(
            exercise=self,
            uid=solution_uid,
        )

    def exercise_send_file(self, exercise_uid, path):
        f = open(path, 'r')
        code = f.read()
        self.exercise_send(exercise_uid, code)

    def list_solutions(self):
        solutions = []
        r = self.course.tichy.session.get("{}/exercise/{}/solutions/".format(self.course.tichy.BASE_URL, self.uid))

        soup = bs4.BeautifulSoup(r.content, "html.parser")

        for tr in soup.find('table', {'class': 'solution-list'}).findAll('tr')[1:]:
            tds = tr.findAll('td')
            solutions.append(Solution(
                exercise=self,
                uid=tds[1].find('a').attrs['href'][10:-1].split('/')[1],
                date=tds[1].text.strip(),
                status=tds[2].text.strip(),
                points=tds[3].text.strip(),
            ))

        return solutions

    def __str__(self) -> str:
        return "[{}] {} ({})".format(self.num, self.name, self.uid)
