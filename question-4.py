def timeToSeconds():
    hours = int(input('Type number of hours: ')) * 3600
    minutes = int(input('Type number of minutes: ')) * 60
    seconds = int(input('Type number of seconds: '))

    result = hours + minutes + seconds
    print(result)

timeToSeconds()