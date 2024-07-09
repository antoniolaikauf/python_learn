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

ci possono essere delle flag cosi che modifichi il comportamento del comando 
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed

'''