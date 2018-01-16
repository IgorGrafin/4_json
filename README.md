# Prettify JSON

Reads JSON file and prints in console in human-readable format. For example:

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

# Quickstart

You have to start program with json-file as a parameter. See the following example.

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>

$ python pprint_json.py in.json

```
Launching on Windows via CMD or PowerShell is the same. 
The example file (in.json) is included in this project. 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
