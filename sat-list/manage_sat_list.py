"""This file exists to internally manage the satellite list, to make it a bit less tedious to add/edit stuff"""

import json
import sys
from pprint import pprint
from sat_classes import *
from colors import *

SAT_LIST = []


def update_sat_list() -> None:
    """Loads the satellite list from the .json file"""

    with open("sat_list.json", "r") as file:
        raw_data = json.load(file)

    global SAT_LIST
    # Resets for writing
    SAT_LIST = []

    for sat in raw_data:
        try:
            SAT_LIST.append(Satellite(**sat))

        except TypeError as e:
            error("Satellite list has an invalid element!!!")
            print("Problematic dict: ")
            pprint(sat)

            print(red(f"Exception: {e}"))
            print("Please fix before running this file or the markdown generator!")

            sys.exit(1)

    print(gray(f"Loaded {len(SAT_LIST)} satellite(s)"))


def write_sat_list() -> None:
    """Writes to the satellite list from the local SAT_LIST variable"""

    out = "[\n"
    for sat in SAT_LIST:
        out += sat.to_JSON()
        out += ",\n"

    # Ensures we don't have a trailing comma
    out = out[:-2] + "\n]"

    with open("sat_list.json", "w") as file:
        file.write(out)


def get_input(
    message: str, default: str = "", case_sensitive=False, options: list[str] = []
) -> str:  # pyright: ignore[reportReturnType]
    """Gets input with some additional functionality, exists gracefully if 'q' is entered

    Args:
        message (str): The message to prompt the user with
        default (str, optional): The default choice if the input is "".
        case_sensitive (bool, optional): Whether to NOT apply .lower() to the result. Defaults to False.
        options (list[str], optional): Possible choices. Unused by default.

    Returns:
        str: User choice
    """
    while 1:
        print(blue(message))

        prompt = ">"
        if default:
            prompt = f"[{default}] >"

        choice = input(prompt)

        if choice == "":
            return default

        if choice.lower() in ["q", "quit"]:
            sys.exit()

        if options and choice not in options:
            error("Invalid input! Options: " + str(options))
            continue

        if not case_sensitive:
            return choice.lower()

        return choice


def confirm(msg: str, info: str = "", default: bool = True) -> bool:  # type: ignore
    """Prompts user to confirm something (Yes/No)

    Args:
        msg (str): Message to prompt with
        info (str, optional): Additional header message
        default (bool, optional): What to return if no input is given. Defaults to True.

    Returns:
        bool: User choice
    """

    while 1:

        if info:
            pprint(info)

        inp = get_input(f"{msg} [Y]es/[N]o")

        if inp in ["y", "yes"]:
            return True
        if inp in ["n", "no"]:
            return False
        if inp == "":
            return default
        if inp in ["q", "quit"]:
            sys.exit()

        error("Invalid input!")


def find_satellite(query: int | str) -> list[Satellite]:
    """Gets a satellite from the sat_list dictionary by NORAD or name

    Args:
        query (int | str): NORAD ID or name
    """
    matches = []

    try:
        for sat in SAT_LIST:
            # Only one should exist. ValueError is thrown if it is not an integer
            if sat.norad == int(query):
                return [sat]

    except ValueError:
        pass

    # If query were NORAD, it would have been found already. Look in names
    for sat in SAT_LIST:
        if str(query).lower() in sat.name.lower():
            matches.append(sat)

    return matches


def choose_satellite() -> Satellite | None:
    """Prompts user to select a satellite via NORAD or name

    Returns:
        Satellite: The desired satellite
    """
    matches = []
    while 1:
        query = get_input("Please enter satellite [NORAD]/[name] or [C]ancel")
        if query == "c":
            return

        matches = find_satellite(query)

        if len(matches) > 5:
            warn("More than 5 satellites found, truncating list...")
            matches = matches[:5]

        if not matches:
            error(f"No satellites have such a NORAD/name! Try again?")
            continue

        if len(matches) == 1:

            if confirm(
                f"Only 1 satellite matched - {matches[0].name}, proceed?",
                "y",
            ):
                return matches[0]

            continue

        good(f"Found {len(matches)} satellites! Please choose one:")

        while 1:
            sat_index = 1

            for sat in matches:
                print(blue(f"{sat_index}. {sat.name}"))
                sat_index += 1

            choice = get_input("Please choose satellite to edit [#]\n")

            try:
                choice = int(choice)

                if choice <= len(matches):
                    return matches[choice - 1]

                error("Please enter a valid number")

            except ValueError:
                error("Please enter a valid number")


def redo_dict(inp: dict):
    """Prompts user to redo all keys in the input dict. Used when undoing things

    Args:
        inp (dict): The working dict
    """
    while 1:
        if len(inp) == 0:
            error("Nothing to undo!")
            return

        if len(inp) == 1:
            key = list(inp.keys())[0]
            inp[key] = get_input(f"{key}:")
            return

        while 1:
            index = 1
            for step in list(inp):
                print(f"{index}. {step}")
                index += 1

            choice = get_input(
                "Please choose which attribute to input [#]/[D]one", default="d"
            )

            if choice[0] == "d":
                return

            try:
                choice = int(choice)

                if choice > len(inp):
                    error("Invalid input!")
                    continue

                step = list(inp)[choice - 1]
                inp[step] = get_input(f"{step}:")

            except ValueError as e:
                error("Invalid input!")


def insert_value(key: str, sat: dict):
    """Prompts user to insert key into the sat dict, can undo on request

    Args:
        key (str): Key to insert
        sat (dict): The dict to insert into
    """
    while 1:
        inp = get_input(f"{key}:", case_sensitive=True)

        if inp == "u":
            redo_dict(sat)
            continue

        sat[key] = inp

        return


def build_satellite() -> Satellite:
    """Builds a Satellite object

    Returns:
        Satellite | None: The satellite object if we created one
    """
    # Debug purposes. Broken right now...
    # return Satellite("Meteor M2-3", 57145, "Roscosmos", "2020", "2026", "Bad deployment", [{"name": "LRPT", "polarization": "RHCP", "image": "test", "description": "compressed imagery","frequency": "137.9 MHz", "imagery": [{"name": "test", "url": "test", "credit": "test"}]}]) # type: ignore

    sat = {}
    sat_params = ["name", "norad", "agency", "start", "end", "description"]

    print(gray("If you make a mistake at any point, type [U]ndo to go back"))

    for param in sat_params:
        insert_value(param, sat)

    while 1:
        pprint(sat)
        if confirm("Does that look good to you?"):
            break

        redo_dict(sat)

    # Base dir is done, move onto signals

    signals = []
    current_signal = {}
    signal_params = [
        "name",
        "frequency",
        "polarization",
        "symbolrate",
        "image",
        "description",
    ]

    good(
        "You will now be propmted information for the signals the satellite broadcasts"
    )
    print(gray("If you make a mistake at any point, type [U]ndo to go back"))

    while 1:

        # First signal
        if len(current_signal) == 0:
            for param in signal_params:
                insert_value(param, current_signal)

        # Any extra ones if we so desire
        elif len(signals) != 0:

            if not confirm("Do you want to add another signal?"):
                break

            current_signal = {}

            for param in signal_params:
                insert_value(param, current_signal)

        pprint(current_signal)

        if not confirm("Do the signal params look good to you?"):
            redo_dict(current_signal)
            continue

        # Handling for sample imagery
        if confirm("Do you want to add sample imagery?"):
            sample_imagery = []
            current_image = {}

            while 1:
                # If there isn't an image, create one
                if len(current_image) == 0:
                    for img_param in ["name", "url"]:
                        insert_value(img_param, current_image)

                pprint(current_image)

                if not confirm("Does the current image look good to you?"):
                    redo_dict(current_image)

                sample_imagery.append(current_image)
                current_image = {}

                if not confirm("Add another sample image? [Y]es/[N]o", "y"):
                    break

            current_signal["imagery"] = sample_imagery

        else:
            current_signal["imagery"] = []

        # Handling for signal status
        current_signal["status"] = get_input(
            "What's the status of this signal? [A]ctive/[I]noperational (permanently off)/[D]isabled (operational but off)/[U]nknown",
            options=["a", "i", "d", "u"],
        )

        signals.append((current_signal))

    sat["signals"] = signals

    return Satellite(**sat)


def main():
    """Main event loop"""

    print("Satellite list helper script made by Meti/Cpt-Dingus")
    print("v0.1 2025-10-05")

    while 1:
        update_sat_list()

        print(
            "1. Show satellite\n2. Edit satellite\n3. Add satellite\n4. Remove satellite"
        )
        warn("This tool is still WIP! Editing is not implemented yet")

        action = get_input("Please choose action [#]/[Q]uit")
        match action.lower():
            case "1":
                print(choose_satellite())
                continue

            # Edit
            case "2":
                warn("Beware I haven't tested this yet!!!")

                sat = choose_satellite()
                if not sat:
                    continue
                pprint(sat)
                choice = get_input(
                    "What to edit? [B]ase dict/[S]ignal dict", options=["e", "s"]
                )[0]

                if choice == "e":
                    while 1:
                        redo_dict(sat.to_JSON())  # type: ignore
                        pprint(sat)
                        if confirm("Does that look good to you?"):
                            break
                # Signal editing
                else:
                    signal_choice = get_input(
                        "What to edit? [S]ignal dict/[I]magery", options=["s", "i"]
                    )[0]

                    if signal_choice == "i":
                        print("not implemented yet sorry, check the raw json out")
                        continue

                    index = 1
                    for sig in sat.signals:
                        print(f"{index}. {sig}")
                        index += 1

                    while 1:
                        sig_index = get_input("Which signal to edit?")

                        try:
                            sig_index = int(sig_index)

                        except ValueError:
                            error("Please enter a valid int!")

                        redo_dict(sat.signals[sig_index].to_JSON())  # type: ignore

            # Add
            case "3":
                SAT_LIST.append(build_satellite())
                write_sat_list()

                continue

            # Remove
            case "4":
                sat = choose_satellite()
                if not sat:
                    continue
                if confirm(f"Are you sure you want to remove `{sat.name}`?"):
                    SAT_LIST.remove(sat)
                    write_sat_list()
                    good(f"`{sat.name} was removed!")

                continue

        print(red("Invalid choice!"))


if __name__ == "__main__":
    main()
