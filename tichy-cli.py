#!env python3

import os

from api import TichyAPI
import webbrowser
import sys

if __name__ == '__main__':
    username = 'MarcinWieczorek'
    password = 'HASLOTUTAJ'
    tichy = TichyAPI()
    r = tichy.login(username, password)

    cmd = sys.argv[1]
    courses = tichy.list_courses()
    if cmd in ('courses', 'c'):
        for i, c in enumerate(courses):
            print('[%d] %-40s (%s)' % (i, c.name, c.course_uid))
    elif cmd in ('exercises', 'e'):
        c = courses[int(sys.argv[2])]
        exercises = c.exercise_list()
        for e in exercises:
            print('[%2d] %-30s (%s)' % (e.num, e.name, e.uid))
    elif cmd in ('send', 's'):
        c = courses[int(sys.argv[2])]
        exercises = c.exercise_list()
        e = exercises[int(sys.argv[3])]
        file = sys.argv[4]
        if not os.path.exists(file):
            print("No such file:", file)
            exit(1)

        solution = e.send_file(file, 2)
        print("Solution:", solution)
        for solution in e.list_solutions():
            print("Solution:", solution)

        solution = e.list_solutions()[0]
        solution.fetch_data()
        print("Solution:", solution)

        webbrowser.open(solution.get_url())

        for test in solution.get_tests():
            print(test)
    else:
        print("Unknown command")
        exit(1)
