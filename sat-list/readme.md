This directory contains everything related to the management of the public-facing Satellite list. There are currently 5 files:

- `sat_list.json` This file contains the actual satellite information.
- `sat_classes.py` This contains the classes used to store & read the satellites.
- `generate_sat_list_md.py` This generated the actual public facing markdown file, is ran using the `gen_script.sh` script at the root level of this repo.

For internal management:
- `colors.py` This provides simple color functions for nicer printing for the other modules.
- `manage_sat_list.py` This file is used internally to provide a simple TUI to add a satellite without having to bother with manual JSON. Using it is not required, but is advisable in order not to miss anything. Running it lints the satellite list on launch.

The structure of satellites is as follows:

```json
{
    "name": "Name of the satellite",
    "norad": "NORAD ID of the satellite",
    "agency": "Satellite operators/agency",
    "start": "Launch date",
    "end": "EOL date",
    "description": "A description of the satelite",
    "signals": [
        {
            "name": "Name of signal",
            "status": "Activity status: [a]ctive/[i]noperational/[d]isabled/[u]nknown",
            "frequency": "Center frequency of signal",
            "polarization": "Signal downlink polarization",
            "symbolrate": "Symbol rate of signal",
            "image": "Name of the FFT screenshot found in assets/sat-list/fft",
            "description": "A brief description of the signal, i.e. when it is transmitted, where it dumps to, what it contains etc.",
            "data": [
                {
                    "name": "Name of the data",
                    "preview": "Optional link to a lower resolution, possibly cropped version of sample data",
                    "raw": "Link to the raw thing. If there is no preview, this is shown instead.
                }
            ]
        }
    ]
}
```


