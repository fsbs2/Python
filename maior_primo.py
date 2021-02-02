def ehPrimo(num):
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1

    if divisores == 2:
        return True
    else:
        return False

def maior_primo(x):
    sent=True
    y=0
    while sent:
        if ehPrimo(x):
            y = x
            sent = False
        else:
             x=x-1
    return y
        
     


