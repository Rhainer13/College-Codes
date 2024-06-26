# Name: Mata, Rhainer Matheuz P.
# BSIT II-1
# Created: March 10 2024

# displays a guide to the user
print("\nVehicle\t\tFirst Rate\t\t\tSecond Rate\n\n"
      "CAR\t\t0.00/hr first 3 hours\t\t1.50/hr after 3 hours\n"
      "TRUCK\t\t1.00/hr first 2 hours\t\t2.30/hr after 2 hours\n"
      "BUS\t\t2.00/hr first hour\t\t3.70/hr after first hr\n")

print("Guide:\n> C for car\n> T for truck\n> B for bus\n")

vehicle_type = input("\tType of Vehicle: ").lower()

hour_entered = 0
minute_entered = 0
hour_left = 0
minute_left = 0
hour_stayed = 0
hour_stayed_display = 0
minute_stayed = 0

# checks if the vehicle inputted is valid
if vehicle_type == "c" or vehicle_type == "t" or vehicle_type == "b":
    hour_entered = int(input("\t(0-24) Hour vehicle entered: "))
    minute_entered = int(input("\t(0-60) Minute vehicle entered: "))

    # checks if the hour and minute entered is valid
    if (hour_entered >= 0 and hour_entered <= 24) and (minute_entered >= 0 and minute_entered <= 60):
        if hour_entered != 0 and hour_entered != 24:
            hour_left = int(input("\t(0-24) Hour vehicle left lot: "))
            minute_left = int(input("\t(0-60) Minute vehicle left lot: "))

            # checks if the hour and minute entered is valid
            if (hour_left >= 0 and hour_left <= 24) and (minute_left >= 0 and minute_left <= 60):

                # checks if the vehicle should be towed
                if hour_entered < hour_left:
                    hour_stayed = hour_left - hour_entered
                    hour_stayed_display = hour_stayed

                    if minute_entered > minute_left:
                        minute_stayed = (60 + minute_left) - minute_entered
                        hour_stayed = hour_stayed - 1
                        hour_stayed_display = hour_stayed
                    else:
                        minute_stayed = abs(minute_left - minute_entered)

                else:
                    print("\n(WARNING) YOUR VEHICLE HAS BEEN TOWED")
                    hour_stayed = (24 - hour_entered)
                    hour_stayed_display = hour_stayed
                    # minute_stayed = 60 - minute_entered

                    hour_left = 24
                    minute_left = 0
                    minute_stayed = 0
            else:
                print("\n(WARNING) INVALID TIME")
        else:
            print("\n(WARNING) NO MIDNIGHT PARKING")
            # test
    else:
        print("\n(WARNING) INVALID TIME")
else:
    print("\n(WARNING) INVALID VEHICLE")

vehicle_name = ""
total_fee = 0

# rounds off the hour if minute stayed is more than 0
if minute_stayed > 0:
    hour_stayed += 1

# calculates the fee for each respective vehicle
if vehicle_type == "c":
    vehicle_name = "CAR"
    if hour_stayed > 3:
        total_fee = (hour_stayed-3) * 1.50

elif vehicle_type == "t":
    vehicle_name = "TRUCK"
    if hour_stayed <= 2:
        total_fee = hour_stayed * 1
    elif hour_stayed > 2:
        total_fee = ((hour_stayed-2) * 2.30) + 2

elif vehicle_type == "b":
    vehicle_name == "BUS"
    if hour_stayed <= 1:
        total_fee = hour_stayed * 2
    elif hour_stayed > 1:
        total_fee = ((hour_stayed-1) * 3.70) + 2

# displays the result
print("\n\n\tPARKING LOT CHARGE\n")
print(f"Type of Vehicle\t\t{vehicle_name}")
print(f"TIME-IN\t\t\t{hour_entered:02}:{minute_entered:02}")
print(f"TIME-OUT\t\t{hour_left:02}:{minute_left:02}")
print("\t\t\t-----")
print(f"PARKING TIME\t\t{hour_stayed_display:02}:{minute_stayed:02}")
print(f"ROUNDED TOTAL\t\t{hour_stayed}")
print("\t\t\t-----")
print(f"TOTAL CHARGE\t\t{total_fee:.2f}\n")