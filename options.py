def do_job(option, cur, con):
    return (switcher.get(option, invalid_op))[0](cur, con)


def option1(cur, con):
    print("you are at option 1. Works na")
    return True


def invalid_opfunc(cur, con):
    print("You have selected an invalid operation.")
    return False


switcher = {
    1: [option1, "Option 1"]
}

invalid_op = [invalid_opfunc, "Invalid Operation"]
