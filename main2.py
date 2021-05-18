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


def process(sett_file: str) -> Information:
    """
    Read file with settings and process data
    input:
        sett_file - path to the file with settings
    output:
        Ya ne znaiu!!!!
    """
    parameters = sett_read(sett_file)
    print("ok")


def load(csv_file, json_file, encoding) -> Information:
    """
    Upload input data
    input:
        csv_file - path to the main file
        json_file - path to the additional file
    output:
        hzzzz
    """
    Inform = Information()
    print("ok")
    # load csv
    # load json
    # check

def load_data(csv_file, information, encoding) -> Information:
    """
    Upload information from the main file
    input:
        information: object to upload infomation into
        csv_file - path to the main file
    output:
        hzzzz
    """
    print("ok")
    # load csv
    # load json
    # check


def load_stat(sett_file: str, encoding: str) -> dict:
    """
    Upload information from the additional file

    input:
        sett_file - path to the additional file
        encoding - file's encoding
    output:
        parameters - additional file's capacity
    """

    name = _pathname(path)
    print(f"input-json {name} : ", end="")

    with open (path, "r", encoding=encoding) as f:
        parameters = json.load(f)
        dictionary = check_sett(parameters)
        print("OK")
        return dictionary


def check_sett(param: dict) -> dict:
    """
    Check existent keys from the additional file
    and return a changed dictionary
    """
    p1 = param["найбільший номер аудиторії"]
    p2 = param["кількість записів у файлі"]

    dictionary = {"max_auditory": p1, "rows_number": p2}
    return dictionary


def sett_read(sett_file: str) -> dict:
    """
    Open, read and analyse the settings' file.

    input:
        sett_file - setting file's path
    output:
        param - settings file's capacity.
    """

    name = _pathname(sett_file)
    print(f"ini {name} : ", end="")

    with open(path, "r") as f:
        param = json.load(f)
        _check_sett(param)
        print("OK")
        return param


def _pathname(path: str) -> str:
    """
    Single out file`s name from the path.
    """

    pattern = r"[^\\^\/]*\.[^.]*"
    name = re.search(pattern, path).group()
    return name


def fit(information: Information, settings: dict) -> bool:
    """
    Check the correspondence between main file and additional file
    :param information:
    :param settings:
    :return:
    """