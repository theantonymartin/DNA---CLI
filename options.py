def do_job(option):
    switcher = {
        1: option1
    }

    (switcher.get(option, invalid_op))()


def option1():
    print("you are at option 1. Works na")


def invalid_op():
    print("You have selected an invalid operation.")
