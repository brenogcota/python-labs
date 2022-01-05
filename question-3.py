def formatSeconds():
    totalSec = int(input('Type number of seconds: '))
    hours = int((totalSec / 3600) % 24)
    minutes = int((totalSec / 60) % 60)
    seconds = int(totalSec % 60)

    result = f'{hours} horas, {minutes} min e {seconds} segundos'
    print(result)

formatSeconds()