import bs4

from api.Exercise import Exercise


class Course:
    def __init__(self, tichy, uid, name):
        self.tichy = tichy
        self.course_uid = uid
        self.name = name

    def exercise_list(self):
        r = self.tichy.session.get("{}/course/{}/".format(self.tichy.BASE_URL, self.course_uid))
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        ex_list = []

        for tr in soup.find('table').findAll('tr')[1:]:
            tds = tr.findAll('td')
            ex_list.append(Exercise(
                course=self,
                num=int(tds[0].text),
                name=tds[1].text.strip(),
                uid=tr.findAll('td')[1].find('a').attrs['href'][10:-1],
                deadline=tds[3].text.strip(),
            ))

        return ex_list

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.course_uid)
