# move into crime_data folder
os.chdir('./crime_data')

# get list of files and folders in cwd
all_items = os.listdir()
# regex pattern to identify the folders containing data (they have 
# a data format e.g. '2020-01')
pattern = re.compile(r'\A\d+-\d+\Z')
# filter list of items to just the folders we want to open
folders = [item for item in all_items if pattern.match(item)]

# regex pattern to identify the csv files (ends in  '.csv')
pattern = re.compile(r'.+\.csv\Z')
crime_data = pd.DataFrame()

for folder in folders:
    # move cwd into the folder
    os.chdir('./' + folder)
    # get list of files and folders in cwd
    all_items = os.listdir()
    # filter list of items to just the csv files we want to open
    csv_files = [item for item in all_items if pattern.match(item)]
    
    # Loop through csv files
    for csv in csv_files: 
        # Load csv file into pandas
        data = pd.read_csv(csv)
        # Add rows of csv file to crime_data dataframe 
        crime_data = pd.concat([crime_data, data], 
                               ignore_index = True)
    
    # move cwd back to crime_data folder
    os.chdir('..')  


# move cwd back to main project folder
os.chdir('..')
# Save combined data to csv 
crime_data.to_csv('all_crime_data.csv', index = False)