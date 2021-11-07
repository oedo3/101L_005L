import csv

def reported_date_dict(data):
    return dict_column(data,'Reported_Date')

def offense_dict(data):
    return dict_column(data,"Offense")

def report_month_dict():
    file_list = read_in_file('CrimeDataSmall.csv')
    month_dict = reported_month_dict(file_list)
    return month_dict

def reported_month_dict(data):
    dict_ex = {}
    for i in data[1:]:
        temp = i[1][0:2]
        if temp in dict_ex:
            dict_ex[temp]+=1
        else:
            dict_ex[temp]=1
    return dict_ex

def dict_column(data,name):
    dict_ex = {}
    n = data[0].index(name)
    for i in data[1:]:
        if i[n]in dict_ex:
            dict_ex[i[n]]+=1
        else:
            dict_ex[i[n]]=1
    return dict_ex

def read_in_file(fname):
    data = []
    try:
        f = open(fname,'r',encoding='UTF-8')
    except:
        return -1
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
    f.close()
    return data
def offense_by_zip(data):
    dict_ex={}
    for i in data[1:]:
        temp = i[7]
        if temp in dict_ex:
            temp_dict = dict_ex[temp]
            if i[13] in temp_dict:
                temp_dict[i[13]]+=1
            else:
                temp_dict[i[13]] = 1
        else:
            dict_ex[temp] = {i[13]:1}
    return dict_ex
def main():
    while True:
        file_name = input("Enter the name of the crime data file > ")
        data = read_in_file(file_name)
        if(data==-1):
            print(f"Could not find the file specified. {file_name} not found")
        else:
            break
    month = reported_month_dict(data)
    print(month)
    month_max = max(month,key=month.get)
    print(f"The month with the highest # of crimes is  {month} with {month_max} offenses")
    offense = offense_dict(data)
    crime_max = max(offense,key=offense.get)
    print(f"The offense with the highest # of crimes is {offense_dict} with {crime_max} offenses")
    offense = offense_by_zip(data)
    print()
    while(True):
        offense = input("Enter an offense : ")
        if offense not in offense:
            print("Not a valid offense, please try again")
        else:
            break
    print(offense, " offense by Zip Code")
    print("Zip Code\t\t\t# Offenses")
    for k,v in offense.items():
        print(k, "\t\t\t\t\t", v.str())

if __name__ == "__main__":
    main()