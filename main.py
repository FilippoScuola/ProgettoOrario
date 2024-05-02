import funzioni
import funzioni.Functions

def main():

    funzioni.Functions.CreaOrario()
    funzioni.Functions.CreaListaNomi()
    dizionario = dict(zip(funzioni.Functions.CreaListaNomi(),funzioni.Functions.CreaOrario()))
    funzioni.Functions.ElencoDocentiClasse(str(input("Inserisci classe di cui vuoi sapere gli insegnanti: ").upper()))
    funzioni.Functions.OrarioDocente(str(input("Inserisci nome docente di cui vuoi sapere l'orario: ").upper()),dizionario)
    funzioni.Functions.OreADisposizione(str(input("Inserisci nome docente di cui vuoi sapere le ore a disposizione: ").upper()),dizionario)
    funzioni.Functions.OraSpecifica(input("Inserisci giorno: ").capitalize(),input("Inserisci ora: ").capitalize())

main()  