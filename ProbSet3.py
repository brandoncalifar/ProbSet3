import time
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

#Functions to open fresh versions of file into memory (to avoid errors with popping values); as file or Pandas dataframe
def ReadFile():
	#.csv File Opening and skipping headers; Dataframe Creation
	fhand = open("CO-OPS__8729108__wl.csv")
	data = csv.reader(fhand, delimiter=',')
	next(data)

	return data

def ReadPandas():
	pdataset = pd.read_csv("CO-OPS__8729108__wl.csv")
	pdata = pdataset.loc[:, 'Date Time':' Water Level']

	return pdata

#Problem Functions
def Problem1():

	WaterLevel = 0
	DateList = []
	LevelList = []
	WaterMaxIndex = 0
	WaterMaxDate = None
	Date = None
	WaterMax = 0 

	for row in ReadFile():
		WaterLevel = row.pop(1)

		#Skip missing data and float all Water Level entries, append data to lists
		if(WaterLevel != ""):
			WaterLevel = float(WaterLevel)
			Date = row.pop(0)
			DateList.append(Date)
			LevelList.append(WaterLevel)

	#Calculate max from list, take index of the max, and take the date&time at that index in Time list
	WaterMax = max(LevelList)
	WaterMaxIndex = LevelList.index(max(LevelList))
	WaterMaxDate = DateList.pop(WaterMaxIndex)
	
	
	print("\nMaximum recorded water level was %f feet at %s\n" % (WaterMax, WaterMaxDate))

	time.sleep(2)
	return;

def Problem2():

	WaterMax = 0 
	WaterMaxIndex = 0 
	WaterMaxDate = None

	ReadPandas()

	WaterMax = ReadPandas()[' Water Level'].max()
	WaterMaxIndex = ReadPandas()[' Water Level'].idxmax()
	WaterMaxDate = ReadPandas().iloc[WaterMaxIndex][0]
	
	print("\nMaximum recorded water level was %f feet at %s\n" % (WaterMax, WaterMaxDate))

	time.sleep(2)
	return;

def Problem3():

	DateList = []
	LevelList = []
	RateList = []
	WaterMaxIndex = 0
	WaterMaxDate = None
	WaterLevelPrev = 0
	MaxRateIndex = 0
	MaxRate = 0
	WaterLevel = 0 
	Date = None
	WaterRate = 0 
	MaxRateDate = None	

	for row in ReadFile():
		WaterLevel = row.pop(1)

		#Skip missing data and float all Water Level entries, append data to lists
		if(WaterLevel != ""):
			WaterLevel = float(WaterLevel)
			Date = row.pop(0)
			DateList.append(Date)
			LevelList.append(WaterLevel)


			if(WaterLevelPrev != 0):
				WaterRate = WaterLevel - WaterLevelPrev
				RateList.append(WaterRate)
			else:
				RateList.append(0)
			
			#Prep for next loop's calculations
			WaterLevelPrev = WaterLevel
	
	MaxRate = max(RateList)
	MaxRateIndex = RateList.index(MaxRate)
	MaxRateDate = DateList[MaxRateIndex]

	print("\nMaximum recorded rate of water level rise was %f feet per 6 minute interval at %s\n" % (MaxRate, MaxRateDate))
	time.sleep(2)
	return;

def Problem4():

	WaterLevel = 0
	DateList = []
	LevelList = []
	WaterMaxIndex = 0
	WaterMaxDate = None
	Date = None
	WaterMax = 0 
	DayList = []
	TimeList = []
	PrevDay = None
	Day = None
	DayNum = 0
	iter = 0

	#Code from Problem 1 to regenerate Date & Water Level Lists

	for row in ReadFile():
		WaterLevel = row.pop(1)

		#Skip missing data and float all Water Level entries, append data to lists
		if(WaterLevel != ""):
			WaterLevel = float(WaterLevel)
			Date = row.pop(0)
			DateList.append(Date)
			LevelList.append(WaterLevel)

	#End of code from Problem 1

	fig = plt.figure()
	plt.plot(DateList, LevelList)
	plt.ylabel('Water Level (ft)')
	plt.xlabel('Date & Time')
	print("Please wait")

	FigInp = input("Would you like to (view) the plot directly or (save) the plot to your current directory?\n:")
	if(FigInp == "save"):
		print("Saving in Progress\n")
		fig.savefig('My_Figure.png')
		print("Figure Saved")
	elif(FigInp == "view"):
		print("Plotting, check taskbar. Pop-up window may take a while to show the full plot.")
		plt.show()
	else:
		print("Invalid input")
	time.sleep(1)

	return;


#Input Request Loop

while True:

	fhand = None
	data = None	
	inp = 0
	print("Which would you like to run?\n Problem 1: Highest Water Level Line-by-Line\n Problem 2: Highest Water Level via Pandas\n Problem 3: Fastest Water Level Rise in 6-minute periods\n Problem 4: Plot water level over time\n")

	inp = input("Please enter a whole number (1 - 4), or 'done' when finished:")

	try:
		inp = int(inp)
	except:
		if(inp == "done"):
			break
		else:
			print("Invalid input")
			time.sleep(1)
			break

	if(inp == 1):
		Problem1()

	elif(inp == 2):
		Problem2()

	elif(inp == 3):
		Problem3()

	elif(inp == 4):
		Problem4()
	else:
		print("Invalid numerical input")
		time.sleep(1)
		break



	continue



