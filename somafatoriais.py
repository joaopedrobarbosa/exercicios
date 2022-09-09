from multiprocessing.resource_sharer import stop


try:
    m,n = map(int, input().split())
    aux = m ;

    while aux > 1:
        aux = aux - 1;
        m = m * aux;

    aux = n ;

    while aux > 1:
        aux = aux - 1;
        n = n * aux;

    total = m + n;

    print(total)
except EOFError:
    exit