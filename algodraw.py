#!/usr/local/bin/python3

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import drange, SUNDAY

from algolist import getPracticeNumber
from algolist import showQuizListFromDir
from lcode import getQuizCount
from lcode import showQuizListFromLeetcode

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
FILE_IMAGE_SCORE202005 = FILE_PREFIX_SCORE + "_202005" + ".png"

DATE_FORMATTER = "%Y-%m-%d"
dates = []
values = []      #file quiz number
leetnumber = []  #leetcode quiz number
easyNumber = []
mediumNumber =[]
hardNumber = []
leetscore = []  #leetcode score 
leetscore = []  #leetcode score 


latest_date = ""

###################### 
### Write to file  
######################
def write(line):
    f = open(FILE_STATISTICS, "a+")
    f.write(line)
    f.close()

def writePrepare(today_date, today_value, today_lcode, score):
    line = [] 
    line.append(sf(str(today_date)))
    line.append(sf(str(today_value)))
    line.append(sf(str(today_lcode['num_solved'])))
    line.append(sf(' | '))
    line.append(sf(str(today_lcode['ac_easy']),5))
    line.append(sf(str(today_lcode['ac_medium']),5))
    line.append(sf(str(today_lcode['ac_hard']),4))
    line.append(sf(' | '))
    line.append(sf(str(score)))
    line.append('\n')
    linePrint = ''.join(line)
    return linePrint

###################### 
### Draw the graph   
######################
def draw(dates, values):
    fig, ax = plt.subplots(figsize=(14, 7))

    # vertical dividers (week, day)
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

    # tilt the date in x-axis
    plt.gcf().autofmt_xdate(which='both')

    # add the annotation of the values 
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
    
    dates = dates[-len(leetscore):]
    values = values[-len(leetscore):]

    annotate_y_offset = 12

    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(14, 14))
    axs[0].set(xlabel="Date", ylabel="Number of Problems",
        title="Number of Problems (2020.04)")
    axs[0].set_title("Number of Problems (2020.04)", fontweight = 'bold')

    axs[0].set_xlim(datetime.datetime(2020,4,1), datetime.datetime(2020,4,30)) 
    axs[0].set_ylim(0,300) #number of quiz
    axs[0].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[0].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[0].grid(which='major', color='#bbbbbb', axis ='y')

    y_stack = np.row_stack([easyNumber, mediumNumber, hardNumber])
    axs[0].stackplot(dates, y_stack, colors=['#5cb85c', '#f0ad4e', '#d9534f'])
    #axs[0].plot_date(dates, values,'-', marker='o')
    axs[0].plot_date(dates, leetnumber,'-', marker='o', color='black')

    axs[1].set(xlabel="Date", ylabel="Score",
        title="Score (2020.04)")
    #ax2.set_xlim(datetime.datetime(2020,4,1), datetime.datetime(2020,4,30)) 
    axs[1].set_title("Score (2020.04)", fontweight = 'bold')
    axs[1].set_ylim(350,600) #score of quiz
    axs[1].grid(which='major', color='k', axis ='x', linestyle='-', linewidth=1.5)
    axs[1].grid(which='minor', color='#bbbbbb', axis ='x', linestyle=':', linewidth=1)
    axs[1].grid(which='major', color='#bbbbbb', axis ='y')
    axs[1].plot_date(dates, leetscore,'-', marker='*', markersize=10, color='#cc3300')

    xfmt = mdates.DateFormatter("%m/%d")
    xloc1 = mdates.WeekdayLocator(SUNDAY)
    xloc2 = mdates.DayLocator()
    axs[0].xaxis.set_major_formatter(xfmt)
    axs[0].xaxis.set_major_locator(xloc1) #major: week
    axs[0].xaxis.set_minor_formatter(xfmt)
    axs[0].xaxis.set_minor_locator(xloc2) #minor: day

    plt.gcf().autofmt_xdate(which='both')

    # leetcode number
    # for i,j in zip(dates, leetnumber):
    #     axs[0].annotate(str(j), xy=(i, j + annotate_y_offset - 5))
    for i in range(len(leetnumber)):
        axs[0].annotate(leetnumber[i]  , xy=(dates[i], leetnumber[i] + annotate_y_offset - 5), fontweight = 'bold')
        axs[0].annotate(hardNumber[i]  , xy=(dates[i], leetnumber[i] - annotate_y_offset - 0), fontsize = 9)
        axs[0].annotate(mediumNumber[i], xy=(dates[i], easyNumber[i] + mediumNumber[i] - annotate_y_offset - 3), fontsize = 9)
        axs[0].annotate(easyNumber[i]  , xy=(dates[i], easyNumber[i] - annotate_y_offset - 3),fontsize = 9)

    
    # leetcode score
    for i,j in zip(dates, leetscore):
        axs[1].annotate(str(j), xy=(i, j - annotate_y_offset * 1.5))

    plt.savefig(FILE_IMAGE_SCORE202004)


    axs[0].set(xlabel="Date", ylabel="Number of Problems",
        title="Number of Quiz (2020.05)")
    axs[0].set_title("Number of Problems (2020.05)", fontweight = 'bold')

    axs[1].set(xlabel="Date", ylabel="Score",
        title="Score of Quiz (2020.05)")
    axs[1].set_title("Score (2020.05)", fontweight = 'bold')
    axs[0].set_xlim(datetime.datetime(2020,5,1), datetime.datetime(2020,5,31)) 
    plt.savefig(FILE_IMAGE_SCORE202005)
    #plt.show()

###################### 
### Read from file  
######################
def read():
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
            values.append(int(file_count))
            leetscore.append(int(l_score))
            leetnumber.append(int(l_count_total))
            easyNumber.append(int(l_count_easy))
            mediumNumber.append(int(l_count_medium))
            hardNumber.append(int(l_count_hard))
        elif len(split_line) == 2:
            date_str, val_str = split_line[0], split_line[1] 
            dates.append(datetime.datetime.strptime(date_str, DATE_FORMATTER)) 
            values.append(int(val_str))
        else:
            break
        line = f.readline()
    f.close()

def sf(s, num=6):
    s = str(s)
    return f'{s:>{num}}'

###################### 
### Print info 
######################

showQuizListFromDir()       #from local repo
showQuizListFromLeetcode()  #from leetcode

###################### 
### Read today info 
######################
print(">> Read from files:", FILE_STATISTICS)
read()
latest_date = dates[-1].strftime(DATE_FORMATTER)
today_date = datetime.date.today()

# New data
if str(today_date) != str(latest_date): 
    print(">> Status : NEW! (latest = ", latest_date, ", today = " ,today_date, ")") 
    
    #Get data 
    today_lcode = getQuizCount()      # Get leetcode data
    today_value = getPracticeNumber() # Get local data
    
    #Update data in memory (4 lists)
    dates.append(today_date)
    values.append(today_value)
    leetnumber.append(today_lcode['num_solved'])
    score = 1 * today_lcode['ac_easy'] \
        + 3 * today_lcode['ac_medium'] \
        + 5 * today_lcode['ac_hard']
    leetscore.append(score)

    #Update data in file
    writeLine = writePrepare(today_date, today_value, today_lcode, score)    
    #print(writeLine)
    write(writeLine)
else:
    print(">> Status: Existed date.")

print(">> Save the image:", FILE_IMAGE201910)
print(">> Save the image:", FILE_IMAGE201911)
print(">> Save the image:", FILE_IMAGE201912)
print(">> Save the image:", FILE_IMAGE202001)
print(">> Save the image:", FILE_IMAGE202002)
print(">> Save the image:", FILE_IMAGE202003)
print(">> Save the image:", FILE_IMAGE_SCORE202004)
print(">> Save the image:", FILE_IMAGE_SCORE202005)
draw(dates, values)