nossaString = "*NEGRITO*";
novaString = ''
aux = 0;
for i in list(nossaString):
    if (i == '*' and aux == 0):
        i = '<br>';
        aux = 1;
    elif (i == '*' and aux == 1):
        i = '</br>';
        aux = 0;

    novaString += i;
print(novaString);