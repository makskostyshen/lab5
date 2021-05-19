"""created by Kostyshen Maksym"""

from sys import argv
import sys
import csv
import json
import re
from Information import Information
from Builder import Builder


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
    holder = Information()

    load_data(csv_file, holder, encoding)
    settings = load_sett(json_file, encoding)
    fit(holder, settings)



def load_data(csv_file, holder, encoding) -> Information:
    """
    Upload information from the main file

    input:
        holder: object to upload information into
        csv_file - path to the main file

    output:
        holder - object with uploaded information
    """

    name = _pathname(csv_file)
    print(f"input-csv {name} : ", end="")

    holder.clear()

    with open(csv_file, encoding=encoding) as opened_file:
        csv_format = csv.reader(opened_file)
        builder = Builder(csv_format)
        builder.load_data(holder)

    print("OK")




def load_sett(sett_file: str, encoding: str) -> dict:
    """
    Upload information from the additional file

    input:
        sett_file - path to the additional file
        encoding - file's encoding
    output:
        parameters - additional file's capacity
    """

    name = _pathname(sett_file)
    print(f"input-json {name} : ", end="")

    with open (sett_file, "r", encoding=encoding) as f:
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

    dictionary = {"max_auditory": p1, "total_skips": p2}
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


def _check_sett(param: dict) -> None:
    """
    Check existent keys from the settings' file.
    """

    p1 = param["input"]["csv"]
    p2 = param["input"]["json"]
    p3 = param["input"]["encoding"]
    p4 = param["output"]["fname"]
    p5 = param["output"]["encoding"]


def fit(holder: Information, settings: dict) -> bool:
    """
    Check the correspondence between main file and additional file

        input:
            holder - object with data from the main file
            settings - object with data from the additional file

        output:
            sign of the correspondence between files
    """
    #print(holder.max_auditory)
    #print(holder.total_skips)
    if holder.max_auditory == settings["max_auditory"] and holder.total_skips == settings["total_skips"]:
        return True

    else: return False


i = Information()


#load_data("infor.csv", i, "utf-8")
#settings = load_stat("infor.json", "utf-8")
#print(fit(i, settings))

load("infor.csv", "infor.json", "utf-8")
