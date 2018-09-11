#
#
"""
v_2:

-Hexa dan normal yaziya cevrime sirasinda 20 diye bir shu yok ama var gozukuyo o duzeltlecek  -- duzeltildi
-Basinda isaret olan varsa artik ayri yaziliyor
- kaydirmac modulu kusursuz calisiyor.
-- satir satir yapilacak
"""








import sys
t = 0
num_shcu = sum(1 for line in open("shcu.txt"))
num_binary = sum(1 for line in open("binary.txt"))

def decimal_calc(input):
    global kaydirmac
    kaydirmac = 0
    for i in range(len(input)):
        global t
        # print(input)
        t = int(input[-1 - i])
        kaydirmac= kaydirmac + 2**int(i)*int(t)

def binlisteceviren(dosya_adi,binarylist):
    encrypt = open(dosya_adi,"r+")
    for r in range(num_binary):
        line = encrypt.readline()
        i = 0
        if str(line)[0] != "0" and str(line)[0] != "1" : #basi isaretli olan artik ayri ve shift i  kaydirmac olarak atiyor

            decimal_calc(line[1:len(line)-1])
        else:
            for x in range(len(line)//4):
                a = str(line[i])+str(line[i+1])+str(line[i+2])+str(line[i+3])
                i = i+4
                binarylist.append(a)
        binarylist.append("\n")
    encrypt.close()

def binaryconverter(binarylist,nbinarylist):
    global binary

    binary = {"0000" : "0",
              "0001" : "1",
              "0010" : "2",
              "0011" : "3",
              "0100" : "4",
              "0101" : "5",
              "0110" : "6",
              "0111" : "7",
              "1000" : "8",
              "1001" : "9",
              "1010" : "A",
              "1011" : "B",
              "1100" : "C",
              "1101" : "D",
              "1110" : "E",
              "1111" : "F",
              }
    for i in range(len(binarylist)):
        binarylist[i] =  binary[binarylist[i]]

    for i in range(0,len(binarylist),2):
        nbinarylist.append(str(binarylist[i]+str(binarylist[i+1])))

def shcuokuyucu(cevrilen,asciisys,cevrilmis):
    global sozluk
    global chiper
    chiper = []
    sozluk = {}
    encrypt = open(asciisys,"r+")
    for i in range(num_shcu):
        a = encrypt.readline().split("\t")
        chiper.append(a[0])
        sozluk.setdefault(a[1],(a[0]))
    encrypt.close()
    for i in range(len(cevrilen)):
        cevrilmis.append(sozluk[cevrilen[i]])
    # print(cevrilmis[0])



def encrypter(crypted,uncrypted,shift):
    for  i in range(len(crypted)):
        if i > len(crypted):
            i = i%len(crypted)
        t = chiper.index(crypted[i])
        uncrypted.append(crypted[(t+shift)%len(crypted)])

def encrypter_2(crypted,uncrypted,shift):
    for i  in range(len(crypted)):

        crypted[i] = chiper[(chiper.index(crypted[i])+shift)%len(chiper)]
    print(crypted)



    # encrypt.close()
    # # print(sozluk)
    # # for anahtar,deger in sozluk.items():
    # #     print("{} = {}".format(anahtar,deger))
    # for i in range(len(cevrilen)):
    #     cevrilen[i] = str(sozluk[cevrilen[i]][0])


binarylist = []
b = []
c = []
yeni = []
sonuc = []
binlisteceviren("binary.txt",binarylist)
print(binarylist)
# binaryconverter(binarylist,b)
# print(b)
# shcuokuyucu(b,"shcu.txt",c)
# print(c)
# for i in range(94):
#     encrypter_2(c,yeni,i)
