while True:
    try:
        m,n = map(int, input().split())
    except EOFError:
        break
    aux = m ;

    if(m == 0):
        m = 1
    
    if(n==0):
        n =1

    while aux > 1:
        aux = aux - 1;
        m = m * aux;

    aux = n ;

    while aux > 1:
        aux = aux - 1;
        n = n * aux;

    total = m + n;

    print(total)
