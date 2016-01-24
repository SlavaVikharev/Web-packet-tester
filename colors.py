HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def header(text):
    return HEADER + text + ENDC


def ok_blue(text):
    return OKBLUE + text + ENDC


def ok_green(text):
    return OKGREEN + text + ENDC


def warning(text):
    return WARNING + text + ENDC


def fail(text):
    return FAIL + text + ENDC


def bold(text):
    return BOLD + text + ENDC


def underline(text):
    return UNDERLINE + text + ENDC
