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

es Set. ![](img/Screenshot%202024-06-15%20170155.png)

## Operatori 
- operatori matematici  + - * / 
- operatori logici or and not 

Gli operatori sono seguiti da **condizioni** che controllano il flow del tuo programma che decidono cosa eseguire o cosa non eseguire.

Le condizioni potrebberro lavorare bene quando sono poche ma quando sono tante il codice inizia a diventare molto lungo e complesso quindi si usa **match** che è stato introdotto nella versione 3.10.

Con match si possono combinare varie condizioni con l'operatore or 

![](img/Screenshot%202024-06-18%20154427.png)

## Funzioni 
L e funzioni per essere dichiarate con la key def seguita dal nome della funzione, i vari tipi di scope (l'ambito di visibilità di una certa variabile, o l'insieme di variabili utilizzate all'interno di una funzione) sono **local** **enclosing** **global** **built-in**

built-in e global sono accessibili ovunque invece enclosing e local no 

![](img/Screenshot%202024-06-20%20143532.png)

Lo scopo dello scope è quello di proteggere la variabile, in modo che non venga modificata da altre parti del codice.

## Librerie
 - time : calcolare il tempo di eecuzione 


# Links 
- https://docs.python.org/3/library/functions.html funzioni di python 

- https://realpython.com/python-conditional-statements/