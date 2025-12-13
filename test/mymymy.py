
def cow(count):
    if count//10%10 == 1:
        return f'{count} коров'
    elif count%10 == 1:
        return f'{count} корова'
    elif count%10 == 2 or count%10 == 3 or count%10 == 4:
        return f'{count} коровы'
    return f'{count} коров'
