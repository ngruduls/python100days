
import pandas

#data = pandas.read_csv("weather_data.csv")
#print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict["day"])
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in Columsn
# print(data["condition"])
# print(data.condition)

#Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# # get row
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#create DataFrame from scratch
#Primary Fur Color
#dataframe
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
