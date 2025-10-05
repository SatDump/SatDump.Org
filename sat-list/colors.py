"""This file contains helper funcs to allow pretty colored UI"""

class ANSII_ESCAPE:
    """Some ANSII color escape codes"""
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    GRAY = "\033[3;90m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ENDC = "\033[0m"


def orange(msg: str) -> str:
    return ANSII_ESCAPE.WARNING + msg + ANSII_ESCAPE.ENDC


def red(msg: str) -> str:
    return ANSII_ESCAPE.FAIL + msg + ANSII_ESCAPE.ENDC


def blue(msg: str):
    return ANSII_ESCAPE.OKBLUE + msg + ANSII_ESCAPE.ENDC


def green(msg: str):
    return ANSII_ESCAPE.OKGREEN + msg + ANSII_ESCAPE.ENDC

def gray(msg: str):
    return ANSII_ESCAPE.GRAY + msg + ANSII_ESCAPE.ENDC

# Direct prints

def warn(msg: str):
    print(orange(msg))

def error(msg: str):
    print(red(msg))

def info(msg: str):
    print(blue(msg))

def good(msg: str):
    print(green(msg))
