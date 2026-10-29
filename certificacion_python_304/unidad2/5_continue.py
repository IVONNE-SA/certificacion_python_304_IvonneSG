for contador in range(1,11):
    #1. contador =1 1%2 ==0 -->Sílo imprime
    #2. contador =2 2%2 ==0 -->Si lo imprime
    #3. contador =3 3%2 ==0 -->Sí lo imprime
    #4. contador =4 4%2 ==0 -->Sí lo imprime
    if contador % 2 != 0:
        continue
    print(contador)