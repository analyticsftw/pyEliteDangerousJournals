# pyEliteDangerousJournals 
Python scripts to pulls data from [Elite:Dangerous](https://elitedangerous.com/) player journals/logs as a CSV file.  The CSV output file can then be consumed for further processing.  

In the original use case, the script logged the total number of lightyears travelled and the amount of fuel scooped during the first [Distant Worlds Expedition](https://elite-dangerous.fandom.com/wiki/Distant_Worlds). 

The export mechanism can easily be adapted to suit other needs.

In its current version, the bodies.csv export file is used in a [data science project using R](https://github.com/analyticsftw/EDSMR).

## Usage 

Before you start, look at the `config.py` file to make sure you correctly set the location of your journal files.

From your shell / terminal, run:
```shell
python journals.py
```

The script will output a file named `bodies.csv` in the same directory as the `journals.py` script unless specified otherwise.

## Requirements
Use Python v3.7 or later

No particular library requirement (uses basic libs such as `csv`, `os`, `json`...)