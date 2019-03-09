from api import Course, Solution


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
        # token = self.course.tichy.session.cookies['csrftoken']
        r = self.course.tichy.session.post(send_url, data={
            'csrfmiddlewaretoken': token,
            'src': code,
            'language': language,
        })
        print(r)

        if r.status_code != 200:
            return None

        solution_uid = r.url.replace(self.course.tichy.BASE_URL, "")[10:-1]
        print("Solution uid:", solution_uid)
        return Solution(
            exercise=self,
            uid=solution_uid,
        )

    def exercise_send_file(self, exercise_uid, path):
        f = open(path, 'r')
        code = f.read()
        self.exercise_send(exercise_uid, code)

    def __str__(self) -> str:
        return "[{}] {} ({})".format(self.num, self.name, self.uid)
