import pytest
import  addition

def test_add():
    assert addition.add(4,5) == 9

def test_sub():
    assert addition.sub(4,5) == -1


'''
occhio alla sintassi deve essere per forza test_nome della funzione che vuoi verificare sia corretta 
La keyword asset viene usata per debuggare il codice e ti permette di testare se una codizione ritorna true usando questo comando 
pytest Test\test_addition.py
'''