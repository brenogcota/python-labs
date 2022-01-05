def itsApproved():
    note = int(input('Type a number between 0 & 100: '))
    if note > 100 or note < 0:
        return print('the number entered is not between 0 and 100')

    if note >= 60:
        return print('Apto')
    
    print('Em construção')

itsApproved()
    