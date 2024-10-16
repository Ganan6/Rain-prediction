import matplotlib.pyplot as plt

#Using manhatton distance
# Training Data Examples for rain and no_rain
rain_temp,rain_humidity = [45,55,55],[60,65,55]
no_rain_temp,no_rain_humidity=[35,50,40],[45,30,35]
# Unknown new data point that needs to be labeled for rain or no rain
new_data_temp = int(input("Enter temperature in F: "))
new_data_humidity = int(input("Enter humidity % "))

# Plot the data points for rain / no_rain and unknown new data
plt.scatter(rain_temp,rain_humidity,marker='^')
plt.scatter(no_rain_temp,no_rain_humidity,marker='o')
plt.scatter(new_data_temp,new_data_humidity,marker='x')
plt.legend(["rain","no_rain","new data"])
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.show()

# Simple distance based approach to lable the unknown new data point
rain=0
no_rain=0
sz=len(rain_temp)
for i in range(sz):
  rain+=abs(rain_temp[i]-new_data_temp)
  rain+=abs(rain_humidity[i]-new_data_humidity)
  no_rain+=abs(no_rain_temp[i]-new_data_temp)
  no_rain+=abs(no_rain_humidity[i]-new_data_humidity)
print("Distance to Rain data (Manhattan Distance) =", rain)
print("Distance to No Rain data (Manhattan Distance) = ", no_rain)

# Print the label of unknown new data point based on the total distance to each group
if rain < no_rain:
  print("It is going to RAIN")
else:
  print("It is NOT going to Rain")

#Using eucalidean distance
# Unknown new data point that needs to be labeled for rain or no rain
# Training Data Examples for rain and no_rain are mentioned above
# Simple distance based approach to label the unknown new data points are mentioned above

rain_euc=0
no_rain_euc=0
sz1=len(rain_temp)
for i in range(sz1):
  rain=0
  rain+=(abs(rain_temp[i]-new_data_temp))**2
  rain+=(abs(rain_humidity[i]-new_data_humidity))**2
  rain_euc+=((rain)**(1/2))
  no_rain=0
  no_rain+=(abs(no_rain_temp[i]-new_data_temp))**2
  no_rain+=(abs(no_rain_humidity[i]-new_data_humidity))**2
  no_rain_euc+=((no_rain)**(1/2))
# print("Distance to Rain data =", rain_euc)
# print("Distance to No Rain data = ", no_rain_euc)
print(f"distance to rain (Eucalidean) {rain_euc}")
print((f"distance to No rain (Eucalidean) {no_rain_euc}"))
# Print the label of unknown new data point based on the total distance to each group
if rain_euc < no_rain_euc:
  print("RAIN")
else:
  print("NO RAIN")