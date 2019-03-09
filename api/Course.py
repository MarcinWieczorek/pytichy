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
                num=tds[0].text,
                name=tds[1].text.strip(),
                uid=tr.findAll('td')[2].find('a').attrs['href'][10:-1],
                deadline=tr.findAll('td')[4].text.strip(),
            ))

        return ex_list

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.course_uid)
