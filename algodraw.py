#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import drange, SUNDAY
from _algolist import getPracticeNumber
from lcode import getQuizCount
import datetime
import numpy as np


###################### 
### Initialize
######################
FILE_PREFIX     = "statistics"
FILE_PREFIX_SCORE     = "score"
FILE_STATISTICS = FILE_PREFIX + ".log"

FILE_IMAGE201910 = FILE_PREFIX + "_201910" + ".png"
FILE_IMAGE201911 = FILE_PREFIX + "_201911" + ".png"
FILE_IMAGE201912 = FILE_PREFIX + "_201912" + ".png"
FILE_IMAGE202001 = FILE_PREFIX + "_202001" + ".png"
FILE_IMAGE202002 = FILE_PREFIX + "_202002" + ".png"
FILE_IMAGE202003 = FILE_PREFIX + "_202003" + ".png"

FILE_IMAGE_SCORE202004 = FILE_PREFIX_SCORE + "_202004" + ".png"

DATE_FORMATTER = "%Y-%m-%d"
dates = []
values = []
scores = []

latest_date = ""

###################### 
### Write to file  
######################
def write(line):
    f = open(FILE_STATISTICS, "a+")
    f.write(line)  
    f.close()

def writePrepare(today_date, today_value):
    lcode_count = getQuizCount()
    score = 1 * lcode_count['ac_easy'] \
          + 3 * lcode_count['ac_medium'] \
          + 5 * lcode_count['ac_hard']
    line = [] 
    line.append(str(today_date))
    line.append(str(today_value))
    line.append(str(lcode_count['num_solved']))
    line.append(' | ')
    line.append(str(lcode_count['ac_easy']))
    line.append(str(lcode_count['ac_medium']))
    line.append(str(lcode_count['ac_hard']))
    line.append(' | ')
    line.append(str(score))
    line.append('\n')
    linePrint = '   '.join(line)
    return linePrint

###################### 
### Draw the graph   
######################
def draw(dates, values):
    fig, ax = plt.subplots(figsize=(14, 8))
    
    xfmt = mdates.DateFormatter("%m/%d")
    xloc1 = mdates.WeekdayLocator(SUNDAY)
    xloc2 = mdates.DayLocator()
    ax.xaxis.set_major_formatter(xfmt)
    ax.xaxis.set_minor_formatter(xfmt)
    ax.xaxis.set_major_locator(xloc1) #major: week
    ax.xaxis.set_minor_locator(xloc2) #minor: day

    ax.grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    ax.grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    ax.grid(which='major', color='#bbbbbb', axis ='y')
    ax.set_ylim(50,100) 

    plt.plot_date(dates, values,'-', marker='o')
    plt.yticks(np.arange(50, 500, step=10))
    plt.gcf().autofmt_xdate(which='both')
    for i,j in zip(dates, values):
        ax.annotate(str(j),xy=(i, j - 3))

    #2019.10
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics (2019.10)")
    ax.set_xlim(datetime.datetime(2019,10,1), datetime.datetime(2019,10,31)) 
    ax.set_ylim(50,150) 
    plt.savefig(FILE_IMAGE201910)

    #2019.11
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics (2019.11)")
    ax.set_xlim(datetime.datetime(2019,11,1), datetime.datetime(2019,11,30)) 
    plt.savefig(FILE_IMAGE201911)

    #2019.12
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics (2019.12)")
    ax.set_xlim(datetime.datetime(2019,12,1), datetime.datetime(2019,12,31)) 
    plt.savefig(FILE_IMAGE201912)

    #2020.01
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics (2020.01)")
    ax.set_xlim(datetime.datetime(2020,1,1), datetime.datetime(2020,1,31)) 
    ax.set_ylim(100,200) 
    plt.savefig(FILE_IMAGE202001)

    #2020.02
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics (2020.02)")
    ax.set_xlim(datetime.datetime(2020,2,1), datetime.datetime(2020,2,29)) 
    plt.savefig(FILE_IMAGE202002)

    #2020.03
    ax.set(xlabel="Date", ylabel="Number of Practices",
        title="Accumulative Statistics (2020.03)")
    ax.set_xlim(datetime.datetime(2020,3,1), datetime.datetime(2020,3,31)) 
    plt.savefig(FILE_IMAGE202003)

    #----------------------

    #2020.04
    plt.close()
    dates = dates[-len(scores):]
    values = values[-len(scores):]
    annotate_y_offset = 10

    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(14, 8))
    axs[0].set(xlabel="Date", ylabel="Number of Practices",
        title="Number of Quiz (2020.04)")
    axs[0].set_xlim(datetime.datetime(2020,4,1), datetime.datetime(2020,4,30)) 
    axs[0].set_ylim(100,300) #number of quiz
    axs[0].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[0].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[0].grid(which='major', color='#bbbbbb', axis ='y')
    axs[0].plot_date(dates, values,'-', marker='o')
   
    axs[1].set(xlabel="Date", ylabel="Score",
        title="Score of Quiz (2020.04)")
    #ax2.set_xlim(datetime.datetime(2020,4,1), datetime.datetime(2020,4,30)) 
    axs[1].set_ylim(300,600) #score of quiz
    axs[1].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[1].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[1].grid(which='major', color='#bbbbbb', axis ='y')
    axs[1].plot_date(dates, scores,'-', marker='*', markersize=10, color='#cc3300')

    for i,j in zip(dates, values):
        axs[0].annotate(str(j), xy=(i, j - annotate_y_offset))

    for i,j in zip(dates, scores):
        axs[1].annotate(str(j), xy=(i, j - annotate_y_offset * 2))

    plt.savefig(FILE_IMAGE_SCORE202004)
    #plt.show()

###################### 
### Read from file  
######################
def read(dates, values):
    f = open(FILE_STATISTICS, "r")
    line = f.readline()
    while line != '':  # The EOF char is an empty string
        split_line = line.split()
        if len(split_line) > 3 :  # New format 
            date_str = split_line[0] 
            file_count = split_line[1] 
            l_count_total = split_line[2] 
            l_count_easy = split_line[4] 
            l_count_medium = split_line[5] 
            l_count_hard = split_line[6] 
            l_score = split_line[8] 
            dates.append(datetime.datetime.strptime(date_str, DATE_FORMATTER)) 
            values.append(int(val_str))
            scores.append(int(l_score))
        else:
            date_str, val_str = split_line[0], split_line[1] 
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

print(">> Read from files:", FILE_STATISTICS)
read(dates, values)
latest_date = dates[-1].strftime(DATE_FORMATTER)


if str(today_date) != str(latest_date): 
    print(">> Status : NEW! This is the first log today. (latest = ", latest_date, ", today = " ,today_date, ")") 
    print(">> Wrote the log: \"" + str(today_date) + "   " + str(today_value), "\"")
    
    writeLine = writePrepare(today_date, today_value)     
    write(writeLine)

    dates.append(today_date) 
    values.append(today_value)
else:
    print(">> Status: The record is already updated today.")

print(">> Save the image:", FILE_IMAGE201910)
print(">> Save the image:", FILE_IMAGE201911)
print(">> Save the image:", FILE_IMAGE201912)
print(">> Save the image:", FILE_IMAGE202001)
print(">> Save the image:", FILE_IMAGE202002)
print(">> Save the image:", FILE_IMAGE202003)
print(">> Save the image:", FILE_IMAGE_SCORE202004)
draw(dates, values)

