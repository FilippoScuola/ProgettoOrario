ORARIO = []
#ORARIO[0] = orario delle classi del primo prof
#ORARIO[1] = orario delle classi del secondo prof
#...

INDICE_ORARIO = []
#INDICE_ORARIO[0] = Giorni dal 'lun' al 'ven'
#INDICE_ORARIO[1] = Ore di lezione dal '1' al '8'

NOMI = []

SPAZIO = [""]
file_dati = '.\\file\\OrarioTabellaGlobale.csv'

def CreaOrario():
    '''
        Genera una lista che contiene tutti gli orari degli insegnanti
       
        e un'altra che contiene tutti i giorni di lezione degli insegnanti
       
        Returns: lista con orari dei professori
    '''
    USCITA = False

    file = open(file_dati,'r')


    while not(USCITA):
       
            r = file.readline().strip().split(',')
            if r == SPAZIO:
                USCITA = True
            else:
                ORARIO.append(r[1:])
           
        #rimuove dalla lista orario il giorno e il numero delle ore e le aggiunge alla lista indice_orario
    INDICE_ORARIO.append(ORARIO.pop(0))
    INDICE_ORARIO.append(ORARIO.pop(0))

    file.close()
    return ORARIO

def CreaListaNomi():
    '''
        Genera una lista che contiene tutti i nomi dei professori

        Returns: lista con nomi dei professori
       
    '''    
   
    file = open(file_dati,'r')

    USCITA = False

    while not(USCITA):
       
        r = file.readline().strip().split(',')
        if r == SPAZIO:
                USCITA = True
        else:
            NOMI.append(r[0].strip())  

    NOMI.pop(0)
    NOMI.pop(0)
    file.close()
    return NOMI

def ElencoDocentiClasse(classe):
    '''
        Questa funzione crea un nuovo file di testo, chiamato Docenti classe{Determinata classe inserita in input}.txt, dove all'interno ci saranno tutti i nomi dei docenti di una data classe
        il file di testo si troverà nella cartella corrispettiva denominata "file",
        e un'altra tutti igiorni di lezione degli insrgnanti.
   
        Arguments: Riceve come argomento una determinata classe
       
    '''    
    USCITA = False
    elenco_docenti = []
    file = open(file_dati,'r')

    r = file.readline().strip().split(',')
    while not(USCITA):
        if r == SPAZIO:
            USCITA = True
        else:
            if classe in r:
                elenco_docenti.append(r[0].strip())
       
        r = file.readline().strip().split(',')

    file.close()
    file = open(f".\\file\\Docenti_classe{classe}.txt",'w')
    for elemento in elenco_docenti:
        file.write(str(elemento).strip() + "\n")

    file.close()

def OrarioDocente(docente,dizionario):
    '''
        Questa funzione scrive su un nuovo file di testo chiamato Orario{nome del docente inserito via input}.txt il quale si trova nella cartella apposita denominata "file",
         l'oarario di un determinato docente.
   
        Arguments: Docente, Dizionario
       
    '''
   

    file = open(f'.\\file\\Orario{docente}.txt','w')

   
    file.write(str(INDICE_ORARIO[0]).strip() + "\n")
    file.write(str(INDICE_ORARIO[1]).strip() + "\n")
    file.write(str(dizionario[docente]).strip())

    file.close()

    

def OreADisposizione(docente,dizionario):
    '''
        Questa funzione scrive all'interno del file di testo OreADisposizione_{nome del docente inserito via input}.txt che si trova nell'apposita cartella denominata "file",
         le ore a disposizione di un insegnante.
   
        Arguments: Docente, dizionario
       
    '''  
    orario_docente = dizionario[docente]

    while ' ' in orario_docente:
        orario_docente.remove(' ')

    D = orario_docente.count('D')

    file = open(f".\\file\\OreADisposizione_{docente}.txt",'w')
    file.write(f"{docente} ha {D} ore a disposizione")
    file.close()
    
def OraSpecifica(Giorno,Ora):
    
    '''
        Questa funzione scrive all'interno del file OraSpecifica{Giorno}{Ora}.txt il quale si trova nell'apposita cartella denominata "file",
        il numero di docenti che hanno lezione in un dato giorno inserito precedentemente in input in una data ora
        
        Arguments: Giorno, Ora

    '''
    
    indice_ore = {"Lunedi":0, "Martedi":8, "Mercoledi":16, "Giovedi":24, "Venerdi":32}

    indice = indice_ore[Giorno] + int(Ora)
    docenti_ora_giorno = []
    cont = 0

    file = open(file_dati,'r')
    r = file.readline().strip().split(',')
    r = file.readline().strip().split(',')

    r = file.readline().strip().split(',')

    while r != SPAZIO:
        if r[indice] != '   ':
            docenti_ora_giorno.append(str(r[0]).strip())
            cont += 1
        r = file.readline().strip().split(',')

    file.close()
    
    file = open(".\\file\\OraSpecifica.txt",'w')
    for elemento in docenti_ora_giorno:
        file.write(elemento + "\n")
    file.write(f"Il numero di professori a lezione il {Giorno} alla {Ora} ora sono {cont}")

    file.close()

