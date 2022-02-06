#get the file and read it 
name = input("Enter file name: ") 
text = open(name, "r") 

#to store data 
hours = dict() 

#find hours and calculate how many times are used 
for line in text: 
    if line.startswith("From "): 
        x = line.split() 
        time = x[5].split(":")
        hour = time[0]
        hours[hour] = hours.get(hour, 0) + 1 

#print the hours and how many times are repeated 
for key, value in hours.items(): 
    print(key, value)