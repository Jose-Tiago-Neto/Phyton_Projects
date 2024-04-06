#Import library to create random temperatures 
import random
#generate random temperatures per day
daily_temperature = [random.randint(0,35) for _ in range(0,30)]
print(daily_temperature)

#Find the lowest, highest, below 10 and above 20 temperatures 

temp_min = daily_temperature[0]
temp_min_day = 1
for day, temp in enumerate(daily_temperature, 1):
    if temp < temp_min:
        temp_min = temp
        temp_min_day = day
print("Day with the lowest temperature:", temp_min_day)

temp_max_day = [0]
temp_max = daily_temperature[0]
for day, temp in enumerate(daily_temperature, 1):
    if temp > temp_max:
       temp_max = temp
       temp_max_day = day
print("Day with the highest temperature:", temp_max_day)


for day, temp in enumerate(daily_temperature):
    if temp > 20:
       print ("Temperature above 20: Day:", day, "Temperature", temp)
for day, temp in enumerate(daily_temperature):
    if temp < 10:
       print ("temperature below 10: Day:", day, "Temperature:", temp)

# The days where the temperature increased from the day before 
temp_days_increased = []

for day in range(1, len(daily_temperature)):
    if daily_temperature[day] > daily_temperature[day - 1]:
        temp_days_increased.append(day + 1) 

print("Days where the temperature increased from the day before:", temp_days_increased)


# The days where the temperature was hotter than any of the days previous in the month.

more_hot_than_previous_days = []

if len(daily_temperature) > 0:
    day_max_temp = daily_temperature[0]
    for day in range(1, len(daily_temperature)):
        if daily_temperature[day] > day_max_temp:
            more_hot_than_previous_days.append(day + 1)  
            day_max_temp = daily_temperature[day]

print("Temperature was hotter than any of the days previous in the month:", more_hot_than_previous_days)

#generate the random rainfall per day       
daily_rainfall = [random.randint(0,10) for _ in range(0,30)]
print(daily_rainfall)
bad_wheater = 1
average_wheater = 1
good_wheater = 1
#record the amount of bad weather, temperature below 10 and rainfall above 3mm.

for temp, rainfall in zip(daily_temperature, daily_rainfall):
    if temp < 10 and rainfall > 3:
       bad_wheater += 1
print (bad_wheater,"Bad weather days.")
       
for temp, rainfall in zip(daily_temperature, daily_rainfall):       
    if 10 < temp < 18 and 1 < rainfall > 5:
       average_wheater += 1
print (average_wheater, "Average weather days.") 
       
for temp, rainfall in zip(daily_temperature, daily_rainfall):   
    if temp > 18 and rainfall < 1:
       good_wheater += 1
print (good_wheater,"Good weather days.")
       