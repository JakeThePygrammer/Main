def librarysystem(priceofbook,isuserborrowing,userbalance):
    if userbalance >= priceofbook:
        if isuserborrowing == False:
            return True
        else:
            return False
    else:
        if isuserborrowing == False:
            return 403
        else:
            return False

def evennumbers(numbers):
    newlist = []
    removednumbers = []
    for number in numbers:
        if int(number) % 2 == 0:
            newlist.append(number)
        else:
            removednumbers.append(number)
    return f"New list : {newlist}, removed numbers : {removednumbers}"