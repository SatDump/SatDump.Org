"""This file generates the .md file that contains all satellites"""

from datetime import datetime, timezone
import json
from sat_classes import *

# from pprint import pprint

SAT_LIST = open("../sat-list/sat_list.json", "r")
OUTPUT_FILE = open("Satellite-List.md", "w")

OUTPUT_FILE.write("---\ntitle: Satellite list\nicon: fas fa-book\norder: 4\n---\n\n")

OUTPUT_FILE.write(
    """<style>
th,td {
  text-align: center;
}
</style>
"""
)

OUTPUT_FILE.write(
    """This site contains all satellites currently decodable by SatDump, including descriptions of each of their downlinks. 

Credits for sample data/FFT images: Meti, Lego11, Aang23, Seler1500, R1chae

Every signal will have a colored marker next to the name depicting its last known status:
- 🟢 Active
- 🔴 Failed/Inoperative
- 🔵 Operational but disabled
- 🟡 Unknown

"""
)


OUTPUT_FILE.write("_Last updated: " + str(datetime.now(timezone.utc)) + "_\n\n")
OUTPUT_FILE.write("_Currently maintained by: Meti_\n\n")


failed_generations = 0

for sat_raw in sorted(json.load(SAT_LIST), key=lambda x: x.get("name", "")):

    try:
        sat = Satellite(**sat_raw)
    except TypeError as e:
        print(f"Generation failed! Malformed dict?")
        print(f"Error: {e}")
        print("JSON:", sat_raw)

        OUTPUT_FILE.write("\n\n# WARNING: GENERATION FAILED!!! MALFORMED SATELLITE?\n")
        OUTPUT_FILE.write(f"Exception: `{e}` <br>JSON:<br>```")
        OUTPUT_FILE.write(str(sat_raw))
        OUTPUT_FILE.write("```\n\n")

        failed_generations += 1
        continue

    OUTPUT_FILE.write(sat.to_markdown())
    OUTPUT_FILE.write("\n\n")

    print(f"Generated {sat.name}")


SAT_LIST.close()
OUTPUT_FILE.close()

if failed_generations == 0:
    print("Succesfully generated satellite list!")
else:
    print("Failed to generate some satellites!")