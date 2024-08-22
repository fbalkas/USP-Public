import os
import pandas as pd

# Path to the directory containing source Excels and target JSONs.
excel_directory = r"C:\\Users\\cansu\\Documents\\csv_to_json\\csv_files"
excel_file = "C:\\Users\\cansu\\Documents\\csv_to_json\\csv_files\\excel_example_1.xlsx"
json_directory = r"C:\\Users\\cansu\\Documents\\csv_to_json\\json_files"


df = pd.read_excel(excel_file)
df

studentnumberraw = df.iloc[0, 0]
studentnumberarray = studentnumberraw.split(" - ")
studentnumber = studentnumberarray[0]
df.iloc[0,0] = studentnumber


#Replace each "Unnamed: 0" element with student number and JSON block number.
for ind, row in enumerate(df.itertuples(),0):
    row_id = studentnumber + " - " + f"{ind + 1 :03d}"
    df.at[ind, "Unnamed: 0"] = row_id
    #df.loc[ind,0] = row_id
print(df)

# Fill missing values with the value in the first cell

json_filename = json_directory + "//"+ studentnumber + ".json"

    # Create the full path for the JSON file
json_path = os.path.join(json_directory, json_filename)

    # Convert the DataFrame to JSON and save it
df.to_json(json_path, orient="records")