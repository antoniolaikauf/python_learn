# Python

Python è un linguaggio molto popolare grazie alla sua varietà di pacchetti open-source, inoltre consente ai sui svilupptori di strutturare il loro codice in molti modi, i tre paradigmi (che si rifersice allo stile di scrittura del programma) in python sono :
- **Orientati agli oggetti** è il modello principale (creazione di oggetti e classi). Questo paradigma è stato inventato da Alan Kay.

  -  Le quattro proprietà per OOP sono:
     - Astrazione
     - Ereditarietà (sia singola che multipla), esistono funzioni utili quando si lavora con l'ereditarietà **issubclass()** e **isinstance()** **super()**
     ci sono 4 tipi di ereditarietà:
       - ereditarietà semplice
       - ereditarietà multipla (in cui il figlio eredita da due classi diverse)
       - livello multiplo di ereditarietà (in cui una classe figlia eredita da un padre, ma fa anche da padre per un altra classe )
       - eredità gerarchica che è come un tree 
       
       se si volesse vedere la gerarchia della classe print(nomeClasse.mro()).
       invece per altri dettagli print(help(nomeClasse))

     - Incapsulamento
     - Polimorfismo

   - I tre procedimenti per questo sono:
       - dichiarare una classe 
       - inizializare l'istanza
       - dichiarare l'istanza 

- **Procedurali** si basa sulla creazione di funzioni
- **Funzionali**  utilizzo di funzioni pure es. map, filter. Queste funzioni è come se vivessero dentro le variabili e quindi si richiamano come .nomeFunzione()

Python consente modelli di programmazione orientati agli oggetti, procedurali e funzionali

Inoltre python aderisce al **MRO** Ordine di risoluzione dei metodi che determina l'esecuzione del flusso.

Con python non hai bisogno di allocare la memoria per una variabile con malloc e poi liberarla con free (non esistono neanche i puntatori) perché lo fa già in automatico dato che è un **high-level language**. Questo ricade sulle performance perché Python ha più funzioni e caratteristiche rispetto a **low-level languages**.

Un altro beneficio di Python è che non ha il problema di **integer overflow** poiché la memoria viene gestita automaticamente. Se facessimo un'operazione in C in cui il numero supera i 4 miliardi, avremmo l'integer overflow, che causerebbe risultati numerici errati.

Una convenzione di Python è quella di utilizzare main per le funzioni e evocare tutte le funzioni all'interno di esso.
La funzione main si evoca alla fine del tuo codice in modo tale che la funzione main stia in cima al codice, rendendo visibile la parte importante del codice.
Un altro aspetto importante è che senza la funzione main, se il codice venisse importato come modulo, quel codice verrebbe eseguito cosache non succederebbe aggiungendo condizione.

## Ambiente  
 per creare un ambiente di lavoro si usa **py -m venv nome_ambiente**,
 si usano gli ambienti di lavoro per staccarsi dal globale e installare
 e fare cose che si vuole (per esempio se si volesse istallare una versione
 piu vecchia di una libreria , o se si volesse avere solo poche librerie
 essendo che nella globale ci sono tante librerie già installate )
 invece per attivare il tuo ambinete di lavoro bisogna attivare il file activate
 nella cartella script es. **.\enviroment\Scripts\Activate** se si volesse uscire, invece
 si scrive nel terminale **deactivate**

 ## Esecuzione codice 
 ci possono essere due metodi per eseguire il codice: uno direttamente **dall'IDE** e l'altro tramite il **terminale** nel seguente modo: si scrive python e il nome del file Python.

 ## Caratteristiche python 
una delle caratteristiche di Python è **l'indentazione** con lo spazio. Se scrivessi print('cisidj') e questa linea di codice non è allineata al lato sinistro e c'è dello spazio, quando si esegue il codice uscirà un errore. 

![](img/Screenshot%202024-06-15%20153450.png).

Python per comunicare con il computer utilizza un tipo di codifica chiamato **Unicode**, così che il compilatore trasforma il codice in stringhe di bit 0 o 1.

 ## Data type 
 Un data type è un attributo associato a un pezzo di dato che dice al computer come interpetrare il suo valore.
Per determinare il tipo di una variabile si usa la funzione **type()**.
 I vari tip di dati in Python sono:
 1. Numeric (sono immutabili come le stringhe)
    - integer (Memoria allocata generalmente 28 bytes)
    - float (Memoria allocata generalmente 24 bytes)
    - complex number 
 2. Boolean (Memoria allocata 28 bytes)
 3. Dictionary
 4. Set (è una conllezione di dati non ripetitivi e non ordinati)
 5. Sequence 
    - string (Memoria allocata se unicode (4 bytes per carattere) o ascii(49n byte che sarebbe un overhead + un byte per ogni carattere)) le stringhe sono immutabili (quando si modifica una stringa python non modificherà quella stringa che hai salvato nella memoria ma creerà una nuova variabile associata a quel nome e la salverà nella memoria e l'altra variabile rimmarrà nella memoria) inoltre le stringe sono liste di caratteri quindi si può utilizzare [i] per ottenere un singolo carattere 
    - list  Nelle liste invece si possono cambiare i valori al suo interno quindi non hanno la proprietà delle stringhe di essere immutabili 
    - tuples

A differenza di altri linguaggi che hanno piu tipi di dati in base al valore delle variabile (es in c si hanno anche i double) in python non c'è bisogno perchè fornisce gia lui una grande quantita di bit a disposizione della variabile.

Quando si combinano cose insieme si formano le **espressioni** che sarebbe l'insieme di operandi e operatori, nelle espressioni sono valide **stringhe  + stringhe**, **stringhe operatore * numero**, **numero operatore numero** le altre come **stringhe + numero** causeranno un errore perchè python controlla il typo della variabile (type checking) è non si può fare la somma di un numero e di una stringa.


Per cambiare il tipo di dato python ha due metodi **implicito** ed **esplicito** 

## Funzione di Print()
 La funzione di print ha delle keywords che possono essere passate come argomenti aggiuntivi, queste possono essere **object**, **sep**, **end**

il valore di default è '\n' in end e la keyword end permette di sovrascrivere '\n' in modo tale che si possa avere un output orizzontale 

es Sep. 

![](img/Screenshot%202024-06-15%20170155.png)

## Operatori 
- operatori matematici  +, -, *, **, %, / (la divisione ritorna sempre un float) lordine in cui vengon svolti sono **, % >> /, * >> +, -
- operatori logici or and not 

Gli operatori sono seguiti da **condizioni** che controllano il flow del tuo programma che decidono cosa eseguire o cosa non eseguire.

Le condizioni potrebbero funzionare bene quando sono poche, ma quando sono tante, il codice inizia a diventare molto lungo e complesso, quindi si usa **match**, introdotto nella versione 3.10.

Con match si possono combinare varie condizioni con l'operatore or 

![](img/Screenshot%202024-06-18%20154427.png)

## Funzioni 
Per utilizare la funzione la sintassi è def seguita dal nome della funzione, un argomento molto importante sono i vari tipi di scope (l'ambito di visibilità di una certa variabile, o l'insieme di variabili utilizzate all'interno di una funzione) sono **local**, **enclosing**, **global**, **built-in**

![](img/Screenshot%202024-06-20%20143532.png)


 Quando si chiama una funzione essa crea un mini enviroment che è completamente separato dal main enviroment infatti nei due enviroment si possono avere variabili con lo stesso nome ma non interferiscono tra di loro, quando avviene la call della funzione il main enviroment viene messo in attesa per far eseguire le opreazione del enviroment della funzione una volta appena la funzione ritorna un valore l'enviroment della funzione scompare 

![](img/Screenshot%202024-07-08%20171647.png)

Lo scopo dello scope è quello di proteggere la variabile, in modo che non venga modificata da altre parti del codice.

Nelle funzioni si possono passare i parametri come tutti gli altri linguaggi di programmazione, ma se si volesse passare molti parametri al posto di crease un parametro per ogni elemento passato alla funzione si può usare *args, che avrà le proprietà dei tuple essendo un tuple 

i due tipi di funzione possono essere tradizionali o pure, le funzioni pure sono funzioni che non cambiano o non hanno nessun effetto su variabili, data, set, oltre il suo proprio ambito es. se si avesse una variabile globale, le funzioni pure non riuscirebbero a modificarla. 

Quando nella funzione non facciamo ritornare nulla da essa pyhton metterà da solo **return None** 

![](img/Screenshot%202024-07-08%20144626.png)

anche se non c'è scritto None viene compunque ritornato dalla funzione 

## strutture dati 
permette di organizzare e di disporre i suoi dati per eseguire operazioni su di esse. Queste strutture dati possono essere **Mutabili** o **Immutabili**.

Python dispone di 4 stutture dati:

1. tuple 
   
    possono contenere qualsiasi tipo di dato ma la differesza con il set è che non si possono modificare i valori dentro ai tuple quindi sono immutabili 
2. elenco 
   
    possono contenere qualsiasi tipo di dato.
   
    modo sbagliato di modificare una lista 

   ![](img/Screenshot%202024-07-10%20084952.png)

   perchè **la funzione append non ritorna niente come valore** e quindi quando si fa il print di L si perde il collegamento nella memoria e ritorna none (oltre ad append ci sono anche remove), ciclare su liste che vengono modificate all'interno del ciclo tramite append o remove potrebbe portare a un malfunzionamento del codice.

   ![](img/Screenshot%202024-07-10%20111355.png)
   
    Ci sono alcune funzioni che modificano la lista e ritornano il valore e una di queste è Pop quindi L=L.pop(2) è corretta come sintassi 
3. dizionario 
   
   si basano sulle key e non sull'index, all'interno non ci possno essere due key uguali e le key devono essere immutabili, python nel salvare un dizionario nella memoria esegue una **hash function sulla key** e trasforma la key in un numero che punterà al valore nella memoria che fa riferimento a quella key, quindi le key devono essere **immutabili** per questo 
4. set 
   
   i set non permettono di avere valori duplicati, con i set si possono fare diverse operazione matematiche tra due set come l'unione l'intersezione e la differenza tra due insiemi 

inoltre pyhton permette di creare la propria struttura dati come **Stack**, **Queue**, **Tree**

La scelta delle strutture di dati dipende da  **dimensione**, **velocità**, **prestazione**.

negli oggetti che sono mutabili se non diciamo noi a pyhton di creare una copia di quel oggetto e cambiassimo 
un oggetto cambierà anche l'altro questo perche ci sono due nomi che puntano alla stessa posizione di memoria 

![](img/Screenshot%202024-07-10%20112443.png)

per creare una copia si può usare la funzione copy() **ma creerà solo una shallow copy** (crea una solo copia di un livello nell'ogetto mutabile)

![](img/Screenshot%202024-07-10%20114047.png) 

nella foto se si avese modificato solo nel primo livello quindi c[0] avrebbe modificato solo la copia ma già nel secondo livello di profondità non si ha più una copia e quindi entrambi vengono modificati



### Le comprensioni 
Le comprensioni in python sono un modo per creare una nuova sequenza da una sequenza gia esistente o crearen uno nuovo direttamente
**[expression for variable_name in iterable]**
esistono quattro tipi di comprensione:
1. comprensione di liste 
2. comprensione di dizionari
3. comprensioni di set
4. comprensioni di generatori 

## Errori

Ci sono due tipi di errori 

- errori di sintassi
  - causati principalmente dai sviluppatori segnalati principalmente dal IDE 
- eccezioni 
  - succedono durante l'esecuzione del codice

per modificare il messaggio di errore si usa **try** o **except** nel except si possno ottenere le informazini dell'eccezione usando la classe e as e, inoltre insieme a try ed except esistono altri due blocchi uno **finally** che viene eseguito sia se c'è un errore o no e l'altro è **else** che viene eseguito solo se non ci sono errori

Tutti i tipi di errori si possono trovare  [qui](https://www.w3schools.com/python/python_ref_exceptions.asp)

![](img/Screenshot%202024-06-21%20144617.png)

Questa immagine fa riferimento agli errori e il percorso dove trovare l'errore, in questo esempio si parte dalla funzione main in riga 171 per poi passare alla funzione altezza nel loop a riga 162 e per poi passare a riga 168 nell'input per poi dire cosa ha causato l'errore

![](img/Screenshot%202024-06-30%20155837.png)


In python esiste l'errore chiamato **floating point error** in cui rende difficile le comparazioni tra numeri con la virgola, questo perchè per il computer è più facile convertire numeri che sono in base 10 in base 2, 

![](img/Screenshot%202024-07-07%20112422.png)

## Funzioni file
Ci sono tre tipi di funzioni per gestire i file **open** **close** **with**

open 
  - reading 
     - per leggere righe nel file si usa readlines 
  - creating
  - writing 
     - per scrivere linee si usa il metodo writelines

si può leggere e gestire i file in python in testo o in un formato binario

## Lambda 

la funzione lambda è una funzione piu compatta e anonima (cioè che non bisogna dare un nome), una funzione lambda può prendere qualsiasi argomento ma può avere solo una espressione

![](img/Screenshot%202024-07-01%20094835.png)

nell'immagine i due argomenti sono a e b e l'espressione ne ha solo una a * b

## Moduli
I moduli permettono di fare cose piu potenti a python, sono blocchi di codice che aggiungono funzionalita al tuo codice cosi che non hai bisogno di ricustruire sempre ogni cosa.

La sintassi per utilizzare un modulo è import, se un modello non è presente nella libreria standard chiamata built in module allora bisogna installare quel modello grazie a **pip**, ma qualsiasi file python può diventare un modello 

 - time: calcolare il tempo di eecuzione 
 - random: scegliere random scelte 
 - pdb: per debuggare 
 - abc:  utilizzato per abstract delle classi
 - ctypes: Fornisce tipi di dati compatibili con il C
 - cs50: libreria classe cs50 harvard
 - sys: Principalmente lo si usa per accedere agli argomenti del terminale.
 - csv: manipola data o file 
 - os: permette di accedere al sistema operativo
 - flask: framework back-end
 - math: operazioni matematiche
 - pytorch, tensorflow, keras: per ML
 - numpy: calcolo scientifico 
 - pandas: lavorare e manipolare dati
 - unittest: test per software 
 - PyTest: test per software 
 - Dateutil: date 
 - matplotlob: grafici


## databese 
Per usufruire di un database bisogna aver istallato **sqlite3**, se si volesse istallarlo **sudo apt install sqlite3** questo è il comnado per l'istallazione se si usa ubuntu, e nel terminale **sqlite3 nomeDatabase.db** in modo tale da iniziare la creazione del tuo database.
Si hanno delle funzioni base in sqlite AVG, COUNT, DISTINCT, LOWER, MAX, MIN, UPPER e le keywords sono WHERE, LIKE, ORDER BY, LIMMIT, GROUP BY.

Una caratteristica molto importante è la creazione di **indexes** che sono strutture dati che aumentano l'efficienza nell accedere alle tabele nel database (permettono di aumentare la velocità delle query)

frameworks usato per il database quindi back-end è **flask** (è più un microframeworks) o **Django** (Django può essere usando anche per il front-end), per usare flask prima bisognerebbe installarlo con **pip install flask** e se si usa linux il comando da eseguire è **sudo apt install python3-pip** una volta fatto questo bisogna fornire una **FLASK APP** che sarebbe il tuo file, il comando è export FLASK_APP=[YOUR_APP_FILE].py e dopo per attivare il server **flask run**

## Algoritmi

Possono avere **tempo costante** in cui non bisogna iterare su nessun componente e quindi il tempo non cambia, **tempo lineare** in cui il tempo cresce in base all'input, **tempo logaritmo** il tempo necessario per eseguire un algoritmo cresce in modo logaritmico rispetto alle dimensioni dell'input.

per calcolare il tempo necessario per un algoritmo ad essere completato si usa la notazione big **O** o **limite superiore** che ci aiuta a rispondere a delle domande Come cambia il tempo di esecuzione di un algoritmo quando i dati di ingresso diventano più grandi? Come scala un algoritmo con l'aumento delle dimensioni dell'input?

PS. la grandezza dell'elemento non inluenza il tempo.
ES. se un elemento è 1 o 100000000000 non inluenza l'algoritmo 

**quando riportiamo la complessità di una funzione/algoritmo la riportiamo rispetto all'input non ad altri valori**

### Esempi di O

- tempo costante 
   - negli algoritmi con complessità temporale costante, il tempo di esecuzione rimane sempre costante e non dipende dall'input es. accedere ad un elemento di un array o un loop con un range sempre fisso che non dipenda da un elemento che può variare è costante 
- tempo lineare 
   - negli algoritmi con complessità temporale lineare il tempo di esecuzione cresce in base alla grandezza dell'input es. cercare elementi dentro ad un array
- tempo quadratico 
   - negli algoritmi con complessità quadratica, i tempi di esecuzione crescono con il quadrato delle dimensioni dell'ingresso es. un ciclo dentro ad un altro ciclo ( un nested loop).
- tempo logaritmico 
   - negli algoritmi con complessità logaritmica, i tempi di esecuzione creascono logaritmicamente con la dimensione dei dati di ingresso 
- tempo esponenziale 
   - negli algoritmi con complessità esponenziale, i tempi di esecuzione crescono esponenzialmente rispetto all'input  es. se avessi tre funzioni che come output possono avere 3 valori output sarebbe 3**3 quindi 27 possibili combinazioni 

**L'omega Ω** o **limite ineriore** rappresenta il best case, quindi se si usasse un binary search il best case sarebbe **Ω(1)** perchè nei miglior casi si trova a meta.

Nel buble sort Ω(n)(limite inferiore) perchè deve fare a prescindere un ciclo per controllare invece O(n**2) (upper bount/limite superiore)

Se si volesse calcolare le operazioni necessarie per completare un pezzo di codice bisogna contare quante operazioni deve fare quel codice 

es 

y=0

for i in range(x): <br />
  y+=1 <br />

in questo ciclo c'è:
 1. prima oprazione  y=0 
 2. associare i ad un elemento nel range 
 3. y+=1 è composta da 2 oparazione quella della somma e qualla dell'associazione perche
 si associa e poi si somma  y = y + 1

 e tutte queste operazioni sono eseguite **x** volte, quindi per calcolare le operazioni che ci vorranno per questo codice 1 + (x) * (2 + 1) = **3x + 1**, ma di questa funzione ci concentriamo solo sul termine dominante quindi in questa funzione è **X** cioè è il termine che cresce più rapidamente quando x tende a infinito.

     


## test 
[vedi file](./Test/test_addition.py)


![](img/Screenshot%202024-07-09%20151102.png)

Per vedere se i test sono tutti passati bisogna vedere in parte al percorso del file che si ha testato se ci sono solo puntini allora i test sono passati 

# Links 
- https://docs.python.org/3/library/functions.html funzioni di python 

- https://realpython.com/python-data-structures/ strutture dati 

- https://pythonbasics.org/try-except/ try e except

- https://pynative.com/python/file-handling/ gestione file 

- https://realpython.com/python-conditional-statements/

- https://it.wikipedia.org/wiki/Complessit%C3%A0_temporale complessità temporale 

- https://www.knowledgehut.com/blog/programming/python-map-list-comprehension comprensione

- https://www.geeksforgeeks.org/python-oops-concepts/ OOP

- https://www.programiz.com/python-programming/modules moduli

- https://testdriven.io/blog/modern-tdd/ sviluppo test 

- https://docs.pytest.org/en/7.1.x/ pytest