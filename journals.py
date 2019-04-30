"""
    A simple script to pull data from Elite: Dangerous journal files.
    In this simple configuration, the script only pulls star data

    This kind of extract is used in another project based on R.
    See https://github.com/analyticsftw/EDSMR

"""
__author__      = "Julien Coquet"
__copyright__   = "Copyright 2016, MIT License"

# Import libraries
import config
import csv
import fnmatch
import json
import os


# DEfining the main function
def main():

    # Define path to journal files
    # See config.py for details / finetuning
    path = config.journalSettings['path']

    # Define CSV header for export
    csv_header = ["system", "body", "is star", "type", "temp", "radius", "absMagnitude", "solMass", "spectralClass", "luminosity"]

    # Define output file
    fp = open('bodies.csv', 'w')

    # Create file pointer and write CSV header
    writer = csv.writer(fp)
    writer.writerow(csv_header)

    i = 0

    # Walk through each journal file
    for fileItem in os.listdir(path):
        star_system = ""
        if fnmatch.fnmatch(fileItem, 'Journal*.log'):
            with open(path+"/"+fileItem, encoding='utf-8') as file:
                star_system = ""
                # Grab each line in the journal file
                lines = file.readlines()

                for line in lines:
                    # Initialize / reset variables

                    star_type = ""
                    star_name = ""
                    star_class = ""
                    star_mass = ""
                    star_radius = ""
                    star_magnitude = ""
                    star_temp = ""
                    star_luminosity = ""

                    # This variable will contain the output for each line, once processed
                    csv_body=[]

                    # Process each line as JSON
                    this_line = json.loads(line)

                    # The FSDJump event contains at least the system name
                    if this_line['event'] == 'FSDJump':
                        star_system = this_line["StarSystem"]

                    # The Scan event contains most star data
                    if this_line['event'] == 'Scan':
                        if "StarType" not in this_line:
                            star_type = "Misc"
                            continue
                        else:
                            star_type = this_line['StarType']
                        if "BodyName" not in this_line:
                            continue
                        else:
                            star_name = this_line['BodyName']

                            # If no star system is available, generate it by popping the last element in the body name
                            if star_system == "":
                                if star_system in star_name:
                                    star_system = star_name
                                else:
                                    starBits = star_name.split(" ")
                                    starBits = starBits[0:-1]
                                    star_system = " ".join(starBits)

                        if "Subclass" not in this_line:
                            star_class=""
                        else:
                            star_class = str(this_line['Subclass'])
                        if "StellarMass" not in this_line:
                            star_mass = "NA"
                        else:
                            star_mass = str(this_line['StellarMass'])
                        if "Radius" not in this_line:
                            star_radius = "NA"
                        else:
                            star_radius = str(this_line['Radius'])
                        if "AbsoluteMagnitude" not in this_line:
                            star_magnitude = "NA"
                        else:
                            star_magnitude = str(this_line['AbsoluteMagnitude'])
                        if "SurfaceTemperature" not in this_line:
                            star_temp = "NA"
                        else:
                            star_temp = str(this_line['SurfaceTemperature'])
                        if "Luminosity" not in this_line:
                            star_luminosity = "NA"
                        else:
                            star_luminosity = this_line['Luminosity']

                    # start building the output string
                    if star_system == "" or star_name == "":
                        continue
                    csv_body.append(star_system)
                    csv_body.append(star_name)
                    if star_type == "Misc":
                        csv_body.append("Not a Star")
                    else:
                        csv_body.append("Star")
                    csv_body.append(star_type)
                    csv_body.append(star_temp)
                    csv_body.append(star_radius)
                    csv_body.append(star_magnitude)
                    csv_body.append(star_mass)
                    csv_body.append(star_type + star_class)
                    csv_body.append(star_luminosity)

                    # Output line to CSV
                    writer.writerow(csv_body)


# Initialize the script
if __name__ == '__main__':
    main()
