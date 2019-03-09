import requests
import bs4

from .Course import Course


class TichyAPI:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.BASE_URL = "https://tichy.umcs.lublin.pl"

    def login(self, username, password):
        token = self.csrf_get(self.BASE_URL + "/accounts/login/")
        r = self.session.post(self.BASE_URL + "/accounts/login/", data={
            'username': username,
            'password': password,
            'csrfmiddlewaretoken': token,
            'next': '',
        })

        return str(r.content).find("Witam") != -1

    def list_courses(self):
        r = self.session.get(self.BASE_URL + "/course")
        soup = bs4.BeautifulSoup(r.content, "html.parser")

        course_list = []

        ul = soup.find("ul", {'class': 'course-list'})

        for li in ul.findAll('li'):
            name = li.text.strip()
            uid = li.find('a')['href']
            course_list.append(Course(
                tichy=self,
                uid=uid[8:-1],
                name=name,
            ))

        return course_list

    def csrf_get(self, url):
        get = self.session.get(url)
        soup = bs4.BeautifulSoup(get.content, "html.parser")
        token = soup.find("input").attrs['value']
        return token
