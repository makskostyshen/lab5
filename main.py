"""created by Kostyshen Maksym"""

from sys import argv
import sys
import csv
import json
import re
from Class import Information


def pr_exec() -> None:
    """
    Output information about executor.
    """

    print("Kostyshen Maksym, K12")
    print("80 variant")

def pr_cond() -> None:
    """
    Output information about conditions of a task.
    """

    print("Use the data from the semester register and find students, who skipped more than 15 lectures.")
    print("Write required information about them to the definite file in the definite order.")


def cmd_read() -> str:
    """
    Read and analyse command line. Return the path of the settings' file.
    If input is wrong - abort the programme.
    """

    if (len(argv) != 2):
        sys.exit("***** program aborted *****")
    path = argv[1]
    return path

def _check_sett(param: dict) -> None:
    """
    Check existent keys from the settings' file.
    """

    p1 = param["input"]["csv"]
    p2 = param["input"]["json"]
    p3 = param["input"]["encoding"]
    p4 = param["output"]["fname"]
    p5 = param["output"]["encoding"]


def _pathname(path: str) -> str:
    """
    Single out file`s name from the path.
    """

    pattern = r"[^\\^\/]*\.[^.]*"
    name = re.search(pattern, path).group()
    return name


def sett_read(path: str) -> dict:
    """
    Open, read and analyse the settings' file.

    input:
        path - file's path
    output:
        param - settings file's capacity.
    """

    name = _pathname(path)
    print(f"ini {name} : ", end="")

    with open(path, "r") as f:
        param = json.load(f)
        _check_sett(param)
        print("OK")
        return param


def _row_check(row: str, pattern: list) -> list:
    """
    Check the correspondence between the row and the pattern.
    """

    limit = len(row)
    #print(row)
    for i in range(limit):
        re.fullmatch(pattern[i], row[i]).group()

def row_head_check(row: list) -> None:
    """
    Check the accuracy of headers' row.
    """

    head = ["предмет", "прізвище", "день тижня", "пара", "аудиторія", "вид занять",
            "навчальний тиждень", "курс", "код групи", "ім'я"]
    _row_check(row, head)


def row_info_check(row: list) -> None:
    """
    Check the accuracy of information row.
    """

    week_pat = re.compile(r"[0-1][0-8]|[0-9]")  # тут питаннячко щодо коомпіляції і навіщо вона треба тут саме
    audi_pat = re.compile(r"\d+")               # типу функція буде викликатись багато разів.
    day_pat = re.compile(r"[0-5]")              # Кожен раз буде наново компілюватись?
    pair_course_pat = re.compile(r"[0-4]")
    type_pat = re.compile(r"Lecture|практ.|8|Лаб.")
    subj_pat = re.compile(r"\S[\d 'a-zA-Zа-яА-Я-]{4,22}\S")
    group_pat = re.compile(r"\S[\da-zA-Zа-яА-Я-]{,2}\S")
    names_pat = re.compile(r"\S[a-zA-Zа-яА-Я-]{4,18}\S")

    info = [subj_pat, names_pat, day_pat, pair_course_pat, audi_pat,
                type_pat, week_pat, pair_course_pat, group_pat, names_pat]

    _row_check(row, info)



def csv_read(path: str, encod: str) -> Information:
    """
    Open, read and analyse the file with main information.
    Return it structured

    input:
        path - path to the file
        encod - file's encoding
    output:
        infor - object with the main information got structured
    """

    name = _pathname(path)
    print(f"input-csv {name} : ", end="")

    with open (path, "r", encoding=encod) as f:
        r = csv.reader(f)
        row_index = 0
        for row in r:
            if(row_index):
                row_info_check(row)
            else: row_head_check(row)
            row_index += 1

        print("OK")

def _check_json(param: dict) -> None:
    """
    Check existent keys from the additional file.
    """
    p1 = param["найбільший номер аудиторії"]
    p2 = param["кількість записів у файлі"]


def json_read(path: str, encod: str) -> dict:
    """
    Open, read and analyse the file with additional information.

    input:
        path - path to the file
        encod - file's encoding
    output:
        param - additional file's capacity
    """

    name = _pathname(path)
    print(f"input-json {name} : ", end="")

    with open (path, "r", encoding=encod) as f:
        param = json.load(f)
        _check_json(param)
        print("OK")
        return param



def main(): pass



pr_exec()
pr_cond()
print("*****")

path = cmd_read()


try:
    param = sett_read(path)
    csv_read(param["input"]["csv"], param["input"]["encoding"])
    json_read(param["input"]["json"], param["input"]["encoding"])
except BaseException as e:
    print("UPS", "***** program aborted *****", e, sep="\n")
