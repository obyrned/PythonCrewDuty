print("Crew members are not permitted to consume alcohol within 12 hours of reporting for duty.")
print("A crew member is required to have at least 10 hours of rest in their hotel room.")
print("If rest is less than 10 hours, the crew member should contact Crew Sked for reassignment.")

from datetime import datetime
currentDateAndTime = datetime.now()

currentTime = currentDateAndTime.strftime("%H:%M")
print("The current time is", currentTime)

import datetime

invalid = True

while (invalid):
    # Get a valid user input for the report time.
    print("What is your report time? (Ex. 06:30)")
    userInput = input(">> ")

# For example, this will convert 6:30 to an array of [6, 30].
    alarmTime = [int(n) for n in userInput.split(":")]

# Validate the time entered to be between 0 and 24 (hours) or 0 and 60 (minutes)
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] >= 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False

# Number of seconds in an Hour, Minute, and Second
seconds_hms = [3600, 60, 1]
# Convert the alarm time to seconds
alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)])

now = datetime.datetime.now()
currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

if secondsUntilAlarm < 0:
    secondsUntilAlarm += 86400 # number of seconds in a day

#Report time in seconds.
print("You have %s until your report time" % datetime.timedelta(seconds=secondsUntilAlarm))
partyTimeSeconds = secondsUntilAlarm - 43200

#Are you under cutoff? / Min rest
if secondsUntilAlarm > 42199:
    print("You have %s until cutoff. Meet your crew for happy hour." % datetime.timedelta(seconds=partyTimeSeconds))
elif (secondsUntilAlarm >= 36000) and (secondsUntilAlarm <= 43200):
    print("Better get to bed.")
else:
    print("Contact Crew Sked for reassignment.")