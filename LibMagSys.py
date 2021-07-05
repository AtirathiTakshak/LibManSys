def BookReg():
    lolpan = open('books.txt','a+')
    x = input('book no.- ')
    y = x.split(' ')
    for i in range(1,int(y[1])+1):
        pan = y[0]+','
        lolpan.write(pan)
    lolpan.close()

def HirerReg():
    with open('books.txt','r') as lopa:
        alt = lopa.read()
    with open('books.txt','w+') as lopa:
        ola = alt.split(',')
        alter = input('name book date: ')
        altrr = alter.split(' ')
        if altrr[1] not in ola:
            print('no such book available. Enter some other book name')
            alter = input('name book date: ')
        altrr = alter.split(' ')
        ola.remove(altrr[1])
        winto = ''
        for i in ola:
            winto+=i+','
        lopa.write(winto.strip(',')+',')
    with open('hirer.txt','r') as mudra:
        bhar = mudra.read()
    with open('hirer.txt','w+') as mudra:
        chinto = ''
        for j in bhar.split(','):
            chinto+=j+','
        mudra.write(chinto+alter+',')

def BookBack():
    wps = input('name book: ')
    with open('hirer.txt','r') as hire:
        data = hire.read()
        RDdata = data.split(',')
    with open('hirer.txt','w+') as hire:
        wpso = wps.split(' ')
        for i in RDdata:
            a = i.split(' ')
            if a[0]==wpso[0] and a[1]==wpso[1]:
                global dante
                dante = a[2] #date
                RDdata.remove(i)
        for j in RDdata:
            hell = ''
            hell+=j+','
        hire.write(hell+',')
        ########################################
        
        ########################################
    with open('book.txt','a+') as buk:
        buk.write(wpso[1]+',')


alpha = input('what do you want to do? \n-register book \n-register hirer \n-take book back \n\n\n')
while alpha not in ['register book','register hirer','take book back']:
    alpha = input('what do you want to do? \n-register book \n-register hirer \n-take book back \n\n\n')
if alpha == 'register book':
    BookReg()
elif alpha == 'register hirer':
    HirerReg()
elif alpha == 'take book back':
    BookBack()