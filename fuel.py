batteries=[50,30,4,45,12,18,30]
minimum_battery_power=20
usable_battery_power=0
usable_battery_count=0
for battery in batteries:
    if battery>=minimum_battery_power:
        usable_battery_power+=battery
        usable_battery_count+=1
print(f"There are {usable_battery_count} batteries which can be used to generate,{usable_battery_power}")
