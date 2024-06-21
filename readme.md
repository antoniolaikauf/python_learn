# Python

## Enviroment 
 per creare un ambiente di lavoro si usa **py -m venv nome_ambiente**,
 si usano gli ambienti di lavoro per staccarsi dal globale e installare
 e fare cose che si vuole (per esempio se si volesse istallare una versione
 piu vecchia di una libreria , o se si volesse avere solo poche librerie
 essendo che nella globale ci sono tante librerie già installate )
 invece per attivare il tuo ambinete di lavoro bisogna attivare il file activate
 nella cartella script es. **.\enviroment\Scripts\Activate** se si volesse uscire invece
 si scrive nel terminale **deactivate**

 ## Esecuzione codice 
 ci possono essere due metodo di eseguire il codice: uno da **direttamente dall IDE** l'altro tramite il **terminale** nel seguente modo: si scrive python e il nome del file python 

 ## Caratteristiche python 
 una delle caratteristiche di python è **l'indentazione** con lo spazio, se io scrivessi  print('cisidj') e questa linea di codice non è attaccata al lato sinistro e c'è dello spazio quando si esegue il codice uscirà un errore  ![](img/Screenshot%202024-06-15%20153450.png).

 Python per comunicare con il computer utilizza un tipo di codifica chiamato **unicode** cosi che il compilatore trasforma il codice in stringe di bit 0 o 1 

 ## Data type 
 Un data type è un attributo associato a un pezzo di dato che dice al computer come interpetrare il suo valore.
 Per determinare il nome di una variabile si usa la funzione **type()** .
 I vari tip di dati in python sono:
 1. Numeric
    1. integer 
    2. float
    3. complex number 
 2. Boolean
 3. Dictionary
 4. Set (è una conllezione di dati non ripetitivi e non ordinati)
 5. Sequence 
    1. string 
    2. list
    3. tuples

Per cambiare il tipo di dato python ha due metodi **implicito** ed **esplicito** 

## Funzione di Print()
la funzione di print ha delle keywords che possono essere validate come argomento aggiuntivo, questi possono essere **object**, **sep**, **end**, esiste anche un file dove vengono stampati i valori, quello di default è **STD** 

es Set. 

![](img/Screenshot%202024-06-15%20170155.png)

## Operatori 
- operatori matematici  + - * / 
- operatori logici or and not 

Gli operatori sono seguiti da **condizioni** che controllano il flow del tuo programma che decidono cosa eseguire o cosa non eseguire.

Le condizioni potrebberro lavorare bene quando sono poche ma quando sono tante il codice inizia a diventare molto lungo e complesso quindi si usa **match** che è stato introdotto nella versione 3.10.

Con match si possono combinare varie condizioni con l'operatore or 

![](img/Screenshot%202024-06-18%20154427.png)

## Funzioni 
Per utilizare la funzione la sintassi è  def seguita dal nome della funzione, un argomento molto importante sono i vari tipi di scope (l'ambito di visibilità di una certa variabile, o l'insieme di variabili utilizzate all'interno di una funzione) sono **local**, **enclosing**, **global**, **built-in**

built-in e global sono accessibili ovunque invece enclosing e local no

![](img/Screenshot%202024-06-20%20143532.png)

Lo scopo dello scope è quello di proteggere la variabile, in modo che non venga modificata da altre parti del codice.

Nelle funzioni si possono passare i parametri come tutti gli altri linguaggi di programmazione, ma se si volesse passare molti parametri al posto di crease un parametro per ogni elemento passato alla funzione si può usare *args, che avrà le proprietà dei tuple essendo un tuple 

## strutture dati 
permette di organizzare e di disporre i suoi dati per eseguire operazioni su di esse. Queste strutture dati possono essere **Mutabili** o **Immutabili**.

Python dispone di 4 stutture dati:

1. tuple 
  - possono contenere qualsiasi tipo di dato ma la differesza con il set è che non si possono modificare i valori dentro ai tuple quindi sono immutabili 
2. elenco 
   - possono contenere qualsiasi tipo di dato 
3. dizionario 
   - si basano sulle key e non sull'index, all'interno non ci possno essere due key uguali 
4. set 
  - i set non permettono di avere valori duplicati, con i set si possono fare diverse operazione matematiche tra due set come l'unione l'intersezione e la differenza tra due insiemi 

inoltre pyhton permette di creare la propria struttura dati come **Stack**, **Queue**, **Tree**

La differenza tra quali strutture di dati scegliere va in base alla **dimensione**, **velocità**, **prestazione**

## Errori

Ci sono due tipi di errori 

- errori di sintassi
  - causati principalmente dai sviluppatori segnalati principalmente dal IDE 
- eccezioni 
  - succedono durante l'esecuzione del codice

per modificare il messaggio di errore si usa **try** o **except** nel except si possno ottenere le informazini dell'eccezione usando la classe e as e 

![](img/Screenshot%202024-06-21%20144617.png)

## funzioni file
Ci sono tre tipi di funzioni per gestire i file **open** **close** **with**

- open 
  1. reading 
     - per leggere righe nel file si usa readlines 
  2. creating
  3. writing 
     - per scrivere linee si usa il metodo writelines

si può leggere e gestire i file in python in testo o in un formato binario 

## Librerie
 - time : calcolare il tempo di eecuzione 


# Links 
- https://docs.python.org/3/library/functions.html funzioni di python 

- https://realpython.com/python-data-structures/ strutture dati 

- https://pythonbasics.org/try-except/ try e except

- https://realpython.com/python-conditional-statements/