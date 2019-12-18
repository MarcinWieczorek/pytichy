#!env python3

import os
from time import sleep
from typing import Dict, List

from api import TichyAPI
import webbrowser
import sys

ARG_EXPAND = {
    'c': 'course',
    'e': 'exercise',
    'l': 'list',
}

options: Dict = {
    'open-browser': False,
    'list': False,
}


def get_arg(option_key: str, **kwargs):
    try:
        val = options[option_key]
    except KeyError:
        print("Specify value with --" + option_key)
        exit(1)
        return

    if option_key == 'course':
        try:
            return kwargs['courses'][int(val)]
        except IndexError:
            print("Invalid course index.")
            exit(1)
    if option_key == 'exercise':
        try:
            return kwargs['exercises'][int(val)]
        except IndexError:
            print("Invalid exercise index.")
            exit(1)
    else:
        return bool(val)


if __name__ == '__main__':
    username = 'MarcinWieczorek'
    password = 'HASLOTUTAJ'
    tichy = TichyAPI()
    r = tichy.login(username, password)

    argv: List = []
    key = None
    next_val = False
    for arg in sys.argv[1:]:
        if arg.startswith('--'):
            arg = arg[2:]
            if '=' in arg:
                split = arg.split('=')
                key = split[0]
                value = split[1]
            else:
                key = arg
                value = True
            options[key] = value
        elif arg.startswith('-'):
            arg = arg[1:]
            for c in arg:
                options[ARG_EXPAND[c]] = True
                key = c
                next_val = True
        else:
            if next_val:
                options[ARG_EXPAND[key]] = arg
                next_val = False
                continue
            argv.append(arg)

    cmd = argv[0]
    courses = tichy.list_courses()
    if cmd in 'course':
        if get_arg('list'):
            for i, c in enumerate(courses):
                print('[%d] %s' % (i, c.name))
    elif cmd in 'exercise':
        c = get_arg('course', courses=courses)
        if get_arg('list'):
            exercises = c.exercise_list()
            for e in exercises:
                print('[%2d] %s' % (e.num, e.name))
    elif cmd in ('send', 's'):
        c = get_arg('course', courses=courses)
        exercises = c.exercise_list()
        e = get_arg('exercise', exercises=exercises)
        file = argv[1]
        if not os.path.exists(file):
            print("No such file:", file)
            exit(1)

        solution = e.send_file(file, 2)
        # solution = e.list_solutions()[0]
        print("Waiting for results...")
        wait_cycles: int = 0
        while wait_cycles < 10:
            wait_cycles += 1
            sleep(0.5)
            solution.fetch_data()

            if not list(filter(lambda t: t.status == 'Sprawdzany', solution.tests)):
                break
        print("Date: %s\nResult: %s\nPoints: %4.2f\n" % (solution.date, solution.status, solution.points))

        if get_arg('open-browser'):
            webbrowser.open(solution.get_url())

        print("Id | Result         | Time (s)    | Memory (kB)")
        for i, test in enumerate(solution.get_tests()):
            print("%2d | %-14s | %4s / %-4s | %s / %s" % (
                i, test.status,
                test.time, test.time_limit,
                test.memory, test.memory_limit
            ))
    else:
        print("Unknown command")
        exit(1)
