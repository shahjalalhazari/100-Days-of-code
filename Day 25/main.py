import csv
##################
with open("weather_data.csv") as weather_data:
    datas = weather_data.readlines()
    for data in datas:
        data.split()
        print(data)
##################


#####################
# In previous day we're done this task in above method.
# But right now this method will not going to work.
# For that we need to import Python's library called CSV.
with open("weather_data.csv") as weather_data:
    datas = csv.reader(weather_data)
    temps = []
    for data in datas:
        if data[1] != "temp":
            temps.append(int(data[1]))
    print(temps)
#######################


# We're done our task successfully.
# But we can do it more easy way.
# For that we have to import another library called PANDAS.

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(data["temp"].mean())  # Get average of all temps
print(data.temp.max())  # Get maximum temp
print(data["temp"].min())  # Get minimum temp


#  Get Data from columns
print(data["condition"])  # 'condition' is column heading, and it should be same as column heading.
print(data.day)

#  Get Data form row
print(data[data.day == "Monday"])
print(data[data["day"] == "Friday"])

#  Get a row of data that has maximum temp
print(data[data.temp == data.temp.max()])

#  Get condition or any value of a particular row.
day = data[data.day == "Thursday"]
print(day.condition)

#  Get temp in Fahrenheit
day_temp = int(day.temp)
temp_in_f = day_temp * 9/5 + 32
print(temp_in_f)

#  Create a DataFrame from scratch
data_dict = {
    "Students": ["Emon", "Rubayet", "Shahjalal", "Rubayed"],
    "scores": [89, 95, 80, 75]
}
data = pandas.DataFrame(data_dict)
#  Now we to create a CSV file with datas
data.to_csv("new_data.csv")
print(data)


data = pandas.read_csv("Central_Park_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_color_count)
print(red_color_count)
print(black_color_count)


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color_count, red_color_count, black_color_count]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Fur Color Count.csv")
