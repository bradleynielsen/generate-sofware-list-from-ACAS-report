import csv
import os
from datetime import date
from datetime import datetime

#config:
include_lines_without_version = False     # False will exclude lines in the plugin that do not have a version number
csv_path                      = ".\\csv"  # This is the path where you want to search
extension                     = '.csv'    # this is the extension you want to detect
results_path                  = ".\\results"

#init:
today                   = str(date.today())
now                     = datetime.now()
current_time            = now.strftime("%H%M%S")
todaycurrent_time       = today + "_" + current_time
csv_results_filename    = "software_use_table-" + todaycurrent_time + ".csv"
csv_results_filepath    = os.path.join(results_path, csv_results_filename)
software_list_all       = []
software_list_unique    = []
txt_results_filename    = "software_list-" + todaycurrent_time + ".txt"
txt_results_filepath    = os.path.join(results_path, txt_results_filename)

#create new csv fle
output_file = open(csv_results_filepath, "w", newline='')
writer      = csv.writer(output_file, delimiter=',')
writer.writerow(["software_name", "software_version", "hostname", "repository"]) #writes the headder

for root, dirs, files in os.walk(csv_path):
    for file in files:
        if os.path.splitext(file)[-1] == extension:
            file_name_path = os.path.join(root, file)
            with open(file_name_path, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    if row['Plugin'] == "20811":
                        print(row['Plugin'], " / ", row['NetBIOS Name'], row['Plugin Text'])
                        hostname    = row['NetBIOS Name']
                        plugin_text = row['Plugin Text']
                        repository  = row['Repository']

                        for pt_row in iter(plugin_text.splitlines()):
                            #get values from line and split them into name and version
                            software_line           = pt_row.strip()
                            software_values_split   = software_line.split(" [")
                            software_name           = software_values_split[0].strip()

                            #Software Version
                            if include_lines_without_version == False: # only include lines that have a version number
                                try: # software version is not uniform, mush use try/except
                                    software_version = software_values_split[1].strip().replace("version ","").replace("]","")
                                except:
                                    continue    # this will skip any line without a version
                            else:
                                try: # software version is not uniform, mush use try/except
                                    software_version = software_values_split[1].strip()
                                    software_version = software_version.replace("version ","")
                                except:
                                    software_version = ""   # this will include the line, and set version to empty string

                            writer.writerow([software_name, software_version, hostname, repository])

                            swNameVersion = software_name + " @ Version: " + software_version
                            software_list_all += [swNameVersion]


#sort the list
software_list_all.sort()

#remove duplicate software
software_list_unique = list(set(software_list_all))
software_list_unique.sort()

#write the software list to file
with open(txt_results_filepath, 'x') as txt_output_file:
    for software in software_list_unique:
           txt_output_file.write('%s\n' % software)

