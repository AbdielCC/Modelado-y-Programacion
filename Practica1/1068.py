while True:
    try:
        cadena = input()
        incorrecto = False
        balance = 0
 

        for char in cadena:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            if balance < 0:
                incorrecto = True
                break

        if  incorrecto or balance != 0:
            print('incorrect')
        else:
            print('correct')

    except EOFError:
        break



