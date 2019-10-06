import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import drange, SUNDAY
from algolist import getPracticeNumber
import datetime
import numpy as np

###################### 
### Initialize
######################
FILE_STATISTICS = "statistics.log"
DATE_FORMATTER = "%Y-%m-%d"
dates = []
values = []
latest_date = ""

###################### 
### Write to file  
######################
def write(today_date, today_value):
    f = open(FILE_STATISTICS, "a+")
    f.write("\n" + str(today_date) + "   " + str(today_value))
    f.close()

###################### 
### Draw the graph   
######################
def draw(dates, values):
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics")

    xfmt = mdates.DateFormatter("%m/%d")
    xloc = mdates.WeekdayLocator(SUNDAY)
    ax.xaxis.set_major_formatter(xfmt)
    ax.xaxis.set_major_locator(xloc)
    ax.grid(True)
    ax.set_xlim(datetime.datetime(2019,9,1), datetime.datetime(2019,12,31)) 

    plt.plot_date(dates, values, '-', marker='.')
    plt.gcf().autofmt_xdate()  
    plt.show()

###################### 
### Read from file  
######################
def read(dates, values):
    f = open(FILE_STATISTICS, "r")
    line = f.readline()
    while line != '':  # The EOF char is an empty string
        split_line = line.split()
        date_str, val_str = split_line[0], split_line[1]
        # print(date_str, " -- ", val_str)
        dates.append(datetime.datetime.strptime(date_str, DATE_FORMATTER)) 
        values.append(int(val_str))
        line = f.readline()
    f.close()

# print("Today  date: ", today_date, "")
# print("Latest date: ", latest_date, "")

###################### 
### Read today info 
######################
print(">> App algodraw.py starts")
today_date = datetime.date.today()
today_value = getPracticeNumber()
print(">> Read today info: (date =", today_date, ", value =", today_value, ")")

print(">> Read from files: ", FILE_STATISTICS)
read(dates, values)
latest_date = dates[-1].strftime(DATE_FORMATTER)


if str(today_date) != str(latest_date): 
    print(">> Not updated yet: (latest = ", latest_date, ", today = " ,today_date, ")") 
    print(">> Write the following today's data into log.")
    print(">> New log: " + str(today_date) + "   " + str(today_value))
    write(today_date, today_value)
    dates.append(today_date) 
    values.append(today_value)
else:
    print(">> Already updated.")

print(">> Drawing the graph...")
draw(dates, values)