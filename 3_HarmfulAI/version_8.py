#
#
"""
|**********************************************************************;
 Project           : cs,assignment3

 Program name      : assignment3.py

 Author            : ismet

 Date created      : 20100816

 Purpose           : a thing

 Revision History  :

  Revision (Date in YYYYMMDD format)        Date        Author      Ref
 20100818    smithb      1      Removed subjects with who have not been dosed per spec.
 11:32       ismet              114 line da kaldim print i sep ile yapmayi dusunuyorum
 25 kasim 00:02                 print islemi kusursuz calisiyor
 shift ile encrypt yapilacak    25 kasim 00:02   00:37
 decimal_calc calismiyor        25 kasim 00:37   00:56
 Mission 00 tamamen bitti

|**********************************************************************;
"""








import sys
t = 0
num_shcu = sum(1 for line in open("shcu.txt"))
num_binary = sum(1 for line in open("binary.txt"))
hex_ler = []
crypt_ler = []
u = ""

def decimal_calc(input):
    global kaydirmac
    kaydirmac = 0
    input = list(input)
    for i in range(len(list(input))):
        global t
        # print(input)
        if input[i] == "0":
            input[i] = "1"
        elif input[i] == "1":
            input[i] = "0"
    for i in range(len(list(input))):
        t = int(input[-1 - i])
        kaydirmac= kaydirmac + 2**int(i)*int(t)
    kaydirmac = -(kaydirmac+1)
    # print(kaydirmac,"kaydirmac")
def binlisteceviren(dosya_adi,binarylist):
    line = encrypt.readline()
    i = 0
    # print(line)
    # print("girdi")
    if str(line)[0] != "0" and str(line)[0] != "1" : #basi isaretli olan artik ayri ve shift i  kaydirmac olarak atiyor
        decimal_calc(line[1:len(line)-1])
        # print("AAAAAAAAAASASASDSADFASDFASFASFASDF")

    else:
        for x in range(len(line)//4):
            a = str(line[i])+str(line[i+1])+str(line[i+2])+str(line[i+3])
            i = i+4
            binarylist.append(a)
    # print(binarylist)
def binaryconverter(binarylist,nbinarylist):
    global binary
    binarylist1 = []
    # print(binarylist1)
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
        binarylist1.append(binary[binarylist[i]])
    for i in range(0,len(binarylist),2):
        nbinarylist.append(str(binarylist1[i]+str(binarylist1[i+1])))


    # print(binary)



    binarylist.clear()

def encrypt_printer():
    c = []
    print("--- encrypted code ---")
    print("----------------------")
    print("")


    for r in range(num_binary):
        binlisteceviren("binary.txt", nbinarylist)
        binaryconverter(nbinarylist, c)
        sonuc = []
        shcuokuyucu(c, "shcu.txt", sonuc)
        crypt_ler.append("".join(sonuc))
        if len(c) > 0 :
            print("".join(sonuc))
        c = []
    encrypt.close()

def hex_printer():
    c = []
    print("--- hex of encrypted code ---")
    print("-----------------------------")
    print("")
    for r in range(num_binary):
        binlisteceviren("binary.txt",nbinarylist)
        binaryconverter(nbinarylist,c)
        hex_ler.append("".join(c))
        if len(c) > 0 :
            print("".join(c))

        c = []
    encrypt.close()


def shcuokuyucu(cevrilen,asciisys,cevrilmis):
    global sozluk
    global chiper
    chiper = []
    sozluk = {}
    encrypt = open(asciisys,"r+")
    for i in range(num_shcu):
        a = encrypt.readline().split("\t")
        chiper.append(a[0])
        sozluk[a[1]] = a[0]
        # print("AAAAAA",a[1])
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

        crypted[i] = chiper[(chiper.index(crypted[i])-shift)%len(chiper)]
    uncrypted.append("".join(crypted))

def encypt_yazdiran():
    print("")
    print("--- decrypted code ---")
    print("----------------------")sdad
    print("")
    for i in range(num_binary):
        encrypter_2(list(crypt_ler[i]), cozulmus,kaydirmac)
        if len(cozulmus[i]) > 0:
            print(cozulmus[i])




    # encrypt.close()"
    # # print(sozluk)
    # # for anahtar,deger in sozluk.items():
    # #     print("{} = {}".format(anahtar,deger))
    # for i in range(len(cevrilen)):
    #     cevrilen[i] = str(sozluk[cevrilen[i]][0])
hex = ""
encrypted = ""
decrypted = ""
binarylist = []
nbinarylist = []
binarylist1 = []
b = []
c = []
yeni = []
sonuc = []
cart = []
cozulmus =[]

# BU KISIMDA PRINT YAPILIYOR
print("*********************")
print("     Mission 00      ")
print("*********************")
print("")
encrypt = open("binary.txt","r+") # encrypt_printer ile bitisiktir
hex_printer()
print("")
encrypt = open("binary.txt","r+") # hex_printer ile bitisiktir
encrypt_printer()
# print("hexler ",u)
# print("c",c)
# encrypter_2(u,-91)
# print(chiper)
encypt_yazdiran()

