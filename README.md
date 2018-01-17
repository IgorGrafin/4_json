# Prettify JSON

Reads JSON file and prints in console in human-readable format.

# Quickstart

You have to start program with json-file as a parameter. See the following example.

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

$ python pprint_json.py in.json

```
Launching on Windows via CMD or PowerShell is the same. 

Save json as file for example from [here](https://devman.org/media/filer_public/1d/32/1d32132e-efa4-4a6c-bd32-312acc3710ad/alco_shops.json). Put it's path as a parameter. The out put will be look something like this:

```
[
    {
        "Cells": {
            "ClarificationOfWorkingHours": null,
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 555-55-55"
                }
            ],
            "TypeService": "realization",
            "WorkingHours": [
                {
                    "DayOfWeek": "Monday",
                    "Hours": "09:30-22:30"

    }
]
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
