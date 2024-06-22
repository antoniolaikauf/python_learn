# parola palindroma 
def anagramma(str1,str2):
    if len(str2)==len(str1):
        return all(x in str2 for x in str1)
    else: return False

print(anagramma('heart','earth'))
print(anagramma('heart','earph'))


# Definire una funzione che riceva come argomenti due stringhe s1 e s2 contenenti la prima una frase
# e la seconda una sequenza di lettere qualsiasi; la funzione dovrà restituire il numero di occorrenze
# della stringa s2 all’interno della frase s1 (senza usare la funzione predefinita count). Si assuma per
# semplicità che tutte le lettere delle due stringhe siano minuscole. Per esempio, se s1 ="questo è
# un esercizio difficilissimo" e s2 ="ci", la funzione dovrebbe restituire il valore 2, in quanto in s1 sono presenti due occorrenze della sequenza di lettere "ci" ("questo è un esercizio
# difficilissimo")

def string(s1,s2):
    count=0
    for x in  s1.split():
        if s2 in x:count+=1
    return count 
print(string('questo è un esercizio difficilissimo','ci'))


# Definire una funzione che riceva come argomenti due liste che si assumono avere la stessa lunghezza,
# contenenti i voti (numeri interi compresi tra 0 e 30) conseguiti da un certo insieme di studenti nelle
# due prove di un esame. Posizioni corrispondenti nelle due liste si riferiscono allo stesso studente.
# La funzione dovrà restituire il valore True se tutti gli studenti hanno superato entrambe le prove;
# in caso contrario dovrà restituire il valore False.
# Per esempio, se le liste fossero [21, 28, 26] e [23, 27, 28], la funzione dovrebbe restituire True,
# mentre se le liste fossero [21, 28, 26] e [23, 12, 28] la funzione dovrebbe restituire False.