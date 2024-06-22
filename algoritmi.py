# parola palindroma 
def anagramma(str1,str2):
    if len(str2)==len(str1):
        return all(x in str2 for x in str1)
    else: return False

print(anagramma('heart','earth'))
print(anagramma('heart','earph'))