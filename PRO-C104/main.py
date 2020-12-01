import csv
from collections import Counter

#importing the csv file into a list
with open("SOCR-HeightWeight.csv",newline='') as f:
    CsvReader = csv.reader(f)
    csvData = list(CsvReader)

# taking out the heading from the csvData cause we don't need the heading
csvData.pop(0)

sum_of_weight = 0
weights = []

for i in csvData:
   index, height, weight = i
   sum_of_weight += float(weight)
   weights.append(weight)

number_of_records = int(index)
weights.sort()

def Mean():
    mean = sum_of_weight/number_of_records
    print("The Mean(Average) of all the weight is -->" + str(mean))

def Median():
    if number_of_records % 2 == 0:
        median1 = float(weights[number_of_records//2])
        median2 = float(weights[number_of_records//2 - 1])
        median = (median1 + median2)/2
    else:
        median = float(weights[number_of_records//2])
    print("The Median of all the weights is --> "+ str(median))

def Mode():
    data = Counter(weights)

    mode_data_for_range = {
        "75-85":0,
        "85-95":0,
        "95-105":0,
        "105-115":0,
        "115-125":0,
        "125-135":0,
        "135-145":0,
        "145-155":0,
        "155-165":0,
        "165-175":0,
    }

    for height, occurence in data.items():
        if 75< float(height) <85:
            mode_data_for_range["75-85"]+=occurence
        elif 85<float(height)<95:
            mode_data_for_range["85-95"]+=occurence
        elif 95<float(height)<105:
            mode_data_for_range["95-105"]+=occurence
        elif 105<float(height)<115:
            mode_data_for_range["105-115"]+=occurence
        elif 115<float(height)<125:
            mode_data_for_range["115-125"]+=occurence
        elif 125<float(height)<135:
            mode_data_for_range["125-135"]+=occurence
        elif 135<float(height)<145:
            mode_data_for_range["135-145"]+=occurence
        elif 145<float(height)<155:
            mode_data_for_range["145-155"]+=occurence
        elif 155<float(height)<165:
            mode_data_for_range["155-165"]+=occurence
        elif 165<float(height)<175:
            mode_data_for_range["165-175"]+=occurence

    mode_range,mode_occurence = 0,0
    for range, occurence in mode_data_for_range.items():
        if occurence>mode_occurence:
            mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
    mode = float((mode_range[0]+mode_range[1])/2)
    print("Mode is -->"+ str(mode))
Mean()
Median()
Mode()
