import email
from os import sep
from pickle import TRUE
from turtle import color
from colorama import Fore

mahsulotlar = [
    {
        'Sabzavot va mevalar':{
            'Sabzavotlar':[
                ['Karam', '1 kg', 5490],
                ['Bodring', '1 kg', 29990],
                ['Sabzi', '1 kg', 9490]
            ],
            'Mevalar':[
                ['Anor', '1 kg', 27990],
                ['Olma', '1 kg', 16990],
                ['Apelsin', '1 kg', 17990]
            ],
            'Ko\'katlar':[
                ['Petrushka', '1 bog\'', 990],
                ['Ko\'k piyoz', '1 bog\'', 1690],
                ['Yalpiz', '1 bog\'', 2490]
            ],
            'Quritilgan mevalar':[
                ['Bodom', '1 kg', 85990],
                ['Pista', '1 kg', 99990],
                ['Yang\'oq', '1 kg', 46990]
            ]
        }
    },
    {
        'Ichimliklar':{
            'Sharbatlar':[
                ['Dena',' 1 dona', 9990],
                ['Bliss', '1 dona', 12990]
            ],
            'Salqin ichimliklar':[
                ['Sprite', '1 dona', 9990],
                ['Fanta', '1 dona', 11990]
            ],
            'Energetik ichimliklar':[
                ['Flash', '1 dona', 7490],
                ['RedBull', '1 dona', 18490]
            ]
        }
    },
    {
        'Go\'sht va go\'sht mahsulotlari':{
            'Mol go\'shti':[
                ['Mol jigari', '1 kg', 53990],
                ['Qovurg\'a', '1 kg', 53990]
            ],
            'Qo\'y go\'shti':[
                ['Qiyma', '1 kg', 58990],
                ['Qo\'y bo\'yni', '1 kg', 77990]
            ],
            'Parranda go\'shti':[
                ['Tovuq soni', '1 kg', 41990],
                ['Tovuq qanoti', '1 kg', 36990]
            ]
        }
    }
]

user = [
    ['behruz@gmail.com',12345],
    ['abs@gmail.com',54321]
]

xaridlar_savati = []

def main():
    while True:
        print('Korzinka online shopping.')
        print('1.Harid qilish')
        print('2.Xaridlar savati')
        print('3.Sotuvchi')
        nomer = int(input('Nomer kiriting : '))
        if nomer == 1:
            while True:
                ins = 1
                for x in mahsulotlar:
                    for y in x:
                        print(ins,'.',y,sep='')
                    ins += 1
                print(ins,'.Orqaga',sep='')
                nomer = int(input('Nomer kiriting : '))
                if nomer == ins:
                    break
                else:
                    turi = mahsulotlar[nomer - 1]
                    for x in turi.values():
                        ins = 1
                        for y in x:
                            print(ins,'.',y,sep='')
                            ins += 1
                        print(ins,'.Orqaga',sep='')
                        nomer = int(input('Nomer kiriting : '))
                        if nomer == ins:
                            break
                        else:
                            for y in x.values():
                                if nomer == 1:
                                    ins = 1
                                    for z in y:
                                        print(ins,'.',f'{z[0]} -> {z[1]} -> {z[2]} so\'m',sep='')
                                        ins += 1
                                    print(ins,'.Orqaga',sep='')
                                    nomer = int(input('Nomer kiriting : '))
                                    if nomer == ins:
                                        break
                                    else:
                                        nomi = y[nomer - 1]
                                        print(nomi[0])
                                        miqdor = float(input(f'Miqdorini kiriting ({nomi[1][2:]}) : '))
                                        puli = nomi[2] * miqdor
                                        nomi1 = [nomi[0], f'{miqdor} {nomi[1][2:]}', puli]
                                        xaridlar_savati.append(nomi1)
                                        print(f'{nomi[0]} savatga saqlandi.')
                                        break
                                nomer -= 1
        elif nomer == 2:
            pul = float(input('Mablag\'ingizni kiriting : '))
            while True:
                jami:float = 0
                for x in xaridlar_savati:
                    jami += x[2]
                if pul - jami >= 0:
                    print( Fore.GREEN,'Sizning pulingiz yetarlicha.', Fore.RESET)
                    print('')
                    print('           Karzinka.uz ')
                    print('Korzinka online shopping xarid cheki.')
                    print('---------------------------------------')
                    for x in xaridlar_savati:
                        print(f'{x[0]}  -> {x[1]} --> {x[2]} so\'m ')
                    print('---------------------------------------')
                    print(f'**jami                   {jami} so\'m')
                    break
                else:
                    print(Fore.RED, f'Sizga {jami - pul} so\'m pul yetmayapdi', Fore.RESET)
                    print('Ro\'yxatdan bazilarini olib tashlang.')
                    ins = 1
                    for x in xaridlar_savati:
                        print(ins,f'. {x[0]} -> {x[1]} -> {x[2]} so\'m ')
                        ins = ins + 1
                    nomer = int(input('Nomer kiriting : '))
                    xaridlar_savati.pop(nomer - 1)
            break
        elif nomer == 3:
            email = input('Emailni kiriting : ')
            password = int(input('Parolni kiriting : '))
            for x in user:
                if email == x[0] and password == x[1]:
                    print('Kabenitizga xush kelibsiz.')
                    print(mahsulotlar[0]['Sabzavot va mevalar'][0])

            else:
                print('Email yoki parol xato.')
            break
        else:
            print('Bunday amal yoq.')

def run():
    main()


if __name__ == '__main__':
    run()