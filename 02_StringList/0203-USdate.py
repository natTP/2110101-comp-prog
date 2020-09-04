mname = ["","January","February","March","April","May","June","July","August","September","October","November","December"]

d = input()
date = d.split("/")
month = int(date[1])
print(mname[month],date[0] + ",",date[2])

