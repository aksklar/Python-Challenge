#import modules
import os
import csv
import datetime
#create csv path
empInfo_csvpath = os.path.join('..', 'PyBoss\\PyBoss_RawData', 'employee_data_2.csv')
#print(empInfo_csvpath)
#create empty lists to store formatted info
empID = []
firstName = []
lastName = []
dob = []
ssn = []
state = []
#add state abbreviated dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#open csv file
with open(empInfo_csvpath, newline='', encoding='utf-8') as csvfile:
    empInfo_csvreader = csv.reader(csvfile, delimiter=',')
    #skip header
    next(empInfo_csvreader, None)
    #print(empInfo_csvreader)
    for row in empInfo_csvreader:
        #add existing employer id to empID list
        empID.append(row[0])
        #split name into two separate lists 
        nameSplit = row[1].split(' ')
        #print(nameSplit)
        #add first names into firstName list
        firstName.append(nameSplit[0])
        #add last names into lastName list
        lastName.append(nameSplit[1])
        #print(lastName)
        #change dob date format
        dobFormatted = datetime.datetime.strptime(row[2], '%Y-%m-%d')
        dobFormatted = dobFormatted.strftime('%m-%d-%Y')
        #add formatted date to dob list
        dob.append(dobFormatted)
        #print(dob)
        #split ssn
        ssnSplit = list(row[3])
        #print(ssnSplit)
        #replace first 5 numbers with asterisks
        ssnSplit[0:3] = ("*", "*", "*")
        ssnSplit[4:6] = ("*", "*")
        #create variable that will join asterisks with last four ssn numbers
        ssnFormatted = ''.join(ssnSplit)
        #print(ssnFormatted)
        #add formatted ssn to ssn list
        ssn.append(ssnFormatted)
        #create variable that will hold the abbreviated states
        stateFormatted = us_state_abbrev[row[4]]
        #print(stateFormatted)
        #add formatted states to state list
        state.append(stateFormatted)
#zip lists together
clean_empInfo = zip(empID, firstName, lastName, dob, ssn, state)
#write path for new csv to be put in
outputcsv = os.path.join('PyBoss_CleanData/clean_employee_data_2.csv')
#write in csv file
with open(outputcsv, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    #write in header row
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    #write the zipped rows
    csvwriter.writerows(clean_empInfo)