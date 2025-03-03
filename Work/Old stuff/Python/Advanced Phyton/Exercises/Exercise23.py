def textcheck(zbor):
    if zbor == "":
        return {}
    rechnik = {}
    zbor = zbor.lower()
    zborovi = zbor.split()
    for zbor in zborovi:
        if zbor in rechnik:
            rechnik[zbor] = rechnik[zbor] + 1
        else:
            rechnik[zbor] = 1
    return rechnik
