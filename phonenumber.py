import phonenumbers
from phonenumbers import timezone, geocoder, carrier

#phone number as input from user
number = input("Enter your number (with +254): ")

#parsing the string input to phonenumber format
phone = phonenumbers.parse(number)

#getting the timezone of the user
time = timezone.time_zones_for_number(phone)

#determining the company's phonenumber
car = carrier.name_for_number(phone, "en")

#getting country information
reg = geocoder.description_for_number(phone, "en")

# printing the output
print("Details :")
print(phone)
print(time)
print(car)
print(reg)
