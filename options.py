def do_job(option):
    return (switcher.get(option, invalid_op))[0]()


def option1():
    print("you are at option 1. Works na")
    return True


def invalid_opfunc():
    print("You have selected an invalid operation.")
    return False


switcher = {
    1: [option1, "Option 1"]
}

invalid_op = [invalid_opfunc, "Invalid Operation"]
