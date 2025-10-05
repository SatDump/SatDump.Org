This directory contains everything related to the management of the public-facing Satellite list. There are currently 5 files:

- `colors.py` This provides simple color functions for nicer printing for the other modules.
- `sat_classes.py` This contains the classes used to store & read the satellites.
- `manage_sat_list.py` This file is used internally to provide a simple TUI to add a satellite without having to bother with manual JSON. Using it is not required, but is advisable in order not to miss anything. Running it lints the satellite list on launch.
- `generate_sat_list_md.py` This generated the actual public facing markdown file, is ran using the `gen_script.sh` script at the root level of this repo.
- `sat_list.json` This file contains the actual satellite information.
