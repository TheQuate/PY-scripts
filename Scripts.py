from datetime import datetime


def personliginfo(Navn, Alder, Hobbyer):
    print(f"Hei, jeg heter {Navn} og jeg er {Alder}. Mine favoritt hobbyer er {Hobbyer} ")

    if Alder > 16:
        print('Du er gammel nok til å øvelseskjøre')

    for H in Hobbyer:
        print(f"En av mine hobbyer er {H}")

Navn = ('Joakim')

Alder = 2023-2006

Hobbyer = ["Data", "IT", "Musikk", "Lego"]

personliginfo(Navn, Alder, Hobbyer)

from datetime import datetime

def dager_til_bursdag(bursdagsdato):
    i_dag = datetime.now()

    tid_til_bursdag = bursdagsdato - i_dag

    dager_til = tid_til_bursdag.days

    return dager_til

bursdagsdato = datetime(2024, 3, 21) 
dager_til = dager_til_bursdag(bursdagsdato)

print(f"Min bursdag er om: {dager_til} dager")


def textfil(filnavn, innhold):
    try: 
        with open(filnavn, 'w') as fil:
            fil.write('\n'.join(innhold))
        print(f"Tekstfilen '{filnavn}' ble opprettet og data ble skrevet.")
    except Exception as e:
        print(f"Feil ved oppretting av tekstfil: {e}")


filnavn = 'liste.txt'
tekst_innhold = Hobbyer

textfil(filnavn, tekst_innhold)


with open(filnavn, 'r') as fil:

    for linje in fil:
        print(linje.strip())

