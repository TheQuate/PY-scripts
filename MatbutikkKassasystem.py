matvarer_priser = {
    "eple": 8,
    "havregryn": 32,
    "brød": 25,
    "melk": 12
}

handlekurv = []

def LeggTil(vare):
    if vare in matvarer_priser:
        handlekurv.append(vare)
        print(f"{vare} ble lagt til i handlekurven.")
    else:
        print("Varen finnes ikke i listen over matvarer.")

def FjernVare(vare):
    if vare in handlekurv:
        handlekurv.remove(vare)
        print(f"{vare} ble fjernet fra handlekurven.")
    else:
        print("Varen er ikke i handlekurven.")

def Handlekurv():
    print("Handlekurv:")
    for vare in handlekurv:
        print(f"- {vare}: {matvarer_priser[vare]} kroner")
