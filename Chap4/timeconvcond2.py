second_per_minute = 60

second_per_hour = 60 * second_per_minute

seconds = int(input("Please enter the number of seconds: "))

hours = seconds // second_per_hour

seconds = seconds % second_per_hour

minutes = seconds // second_per_minute

seconds = seconds % second_per_minute

if hours > 0:
    print(hours, end="")

    if hours == 1:
        print(" hours ", end="")
    else:
        print(" hours ", end="")

if minutes > 0:
    print(minutes, end="")

    if minutes == 1:
        print(" minute ", end="")
    else :
        print(" minutes ", end="")

if seconds > 0 or (hours == 0 and minutes == 0 and seconds == 0):
    print(seconds, end="")

    if seconds == 1:
        print(" second ", end="")
    else:
        print(" seconds ", end="")

print()
