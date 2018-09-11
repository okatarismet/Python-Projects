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
 Mission 00 tamamen bitti       25 kasim 00:56
 Mission 01 basladi             25 kasim 13:15   13:26
                                         17:28
 Mission 01 ilk kisim tamam
 Mission 01 geri encrypt yapilacak.
|**********************************************************************;
"""
import sys
hurap = sys.argv[1]
shcu = sys.argv[2]
virus = sys.argv[3]
t = 0
num_shcu = sum(1 for line in open(shcu))
num_binary = sum(1 for line in open(hurap))
num_virus = sum(1 for line in open(virus))
hex_ler = []
crypt_ler = []
u = ""
list_a = []


son = []
broken_list = []
def decimal_calc(input):
    global shifter
    shifter = 0
    input = list(input)
    for i in range(len(list(input))):
        global t
        if input[i] == "0":
            input[i] = "1"
        elif input[i] == "1":
            input[i] = "0"
    for i in range(len(list(input))):
        t = int(input[-1 - i])
        shifter= shifter + 2 ** int(i) * int(t)
    shifter = -(shifter + 1)
def ters_hex(inlist,outlist):
    for i in range(len(inlist)):
        if len(inlist[i])>0:
            for x in range(len(inlist[i])):
                list_a.append(reverse_dict[inlist[i][x]])
            outlist.append("".join(list_a))
            list_a.clear()
    print("")
    print("--- hex of encrypted code ---")
    print("-----------------------------")
    print("")

    for i in range(len(outlist)):
        print(outlist[i])

def binlisteceviren(filename, binarylist):
    line = encrypt.readline()
    i = 0

    if str(line)[0] != "0" and str(line)[0] != "1" :
        decimal_calc(line[1:len(line)-1])
    else:
        for x in range(len(line)//4):
            a = str(line[i])+str(line[i+1])+str(line[i+2])+str(line[i+3])
            i = i+4
            binarylist.append(a)
def binaryconverter(binarylist,nbinarylist):
    global binary
    binarylist1 = []
    binary = {"0000" : "0","0001" : "1","0010" : "2","0011" : "3","0100" : "4","0101" : "5","0110" : "6","0111" : "7","1000" : "8","1001" : "9","1010" : "A","1011" : "B","1100" : "C","1101" : "D","1110" : "E","1111" : "F",}
    for i in range(len(binarylist)):
        binarylist1.append(binary[binarylist[i]])
    for i in range(0,len(binarylist),2):
        nbinarylist.append(str(binarylist1[i]+str(binarylist1[i+1])))
    binarylist.clear()
def encrypt_printer():
    c = []

    print("--- encrypted code ---")
    print("----------------------")
    print("")
    for r in range(num_binary):
        binlisteceviren(hurap, nbinarylist)
        binaryconverter(nbinarylist, c)
        sonuc = []
        shcuokuyucu(c, shcu, sonuc)
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
        binlisteceviren(hurap,nbinarylist)
        binaryconverter(nbinarylist,c)
        hex_ler.append("".join(c))
        if len(c) > 0 :
            print("".join(c))
        c = []
    encrypt.close()
def shcuokuyucu(cevrilen, asciisys, trans):
    global dicttt
    global chiper
    global reverse_dict
    chiper = []
    dicttt = {}
    reverse_dict = {}
    encrypt = open(asciisys,"r+")
    for i in range(num_shcu):
        a = encrypt.readline().split("\t")
        chiper.append(a[0])
        dicttt[a[1]] = a[0]
        reverse_dict[a[0]] = a[1]
    encrypt.close()
    for i in range(len(cevrilen)):
        trans.append(dicttt[cevrilen[i]])
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

def encypt_yazdiran(uncrypted,kaydirmac):
    print("")
    print("--- decrypted code ---")
    print("----------------------")
    print("")
    for i in range(num_binary):
        encrypter_2(list(crypt_ler[i]),uncrypted,kaydirmac)
        if len(uncrypted[i]) > 0:
            print(uncrypted[i])

def encrypter_2_ters(crypted,uncrypted,shift):
    for i  in range(len(crypted)):

        crypted[i] = chiper[(chiper.index(crypted[i])-shift)%len(chiper)]
    uncrypted.append("".join(crypted))

def encypt_yazdiran_ters(uncrypted,kaydirmac):
    print("")
    print("--- decrypted code ---")
    print("----------------------")
    print("")
    for i in range(num_binary):

        encrypter_2_ters(list(uncrypted[i]),son,kaydirmac)
        if len(son[i]) > 0:
            print(son[i])

def degistirilmis_yazdiran(cozulmus):
    for x in range(len(cozulmus)):
        virus_codes = open(virus, "r")

        for i in range(num_virus):
            a = virus_codes.readline().split(":")
            a[1] = a[1].strip("\n")
            cozulmus[x] = cozulmus[x].replace(a[0], a[1])
            a = []
        virus_codes.close()
    print("")
    print("*********************")
    print("     Mission 01      ")
    print("*********************")
    print("")

    for i in range(len(cozulmus)):
        broken_list.append(cozulmus[i])
        if len(cozulmus[i]) > 0:
            print(cozulmus[i])


def cart_curt():
    for i in range(len(hex_yazilacak)):
        for x in range(len(hex_yazilacak[i])):
            list_a.append(list(binary.keys())[list(binary.values()).index(hex_yazilacak[i][x])])
        list_c.append("".join(list_a))
        list_a.clear()
    print("")
    print("--- bin of encrypted code ---")
    print("-----------------------------")
    print("")
    for i in range(len(list_c)):

        print(list_c[i])


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
hex_yazilacak = []
list_c= []
# BU KISIMDA PRINT YAPILIYOR
print("*********************")
print("     Mission 00      ")
print("*********************")
print("")
encrypt = open(hurap,"r") # encrypt_printer ile bitisiktir
hex_printer()
print("")
encrypt = open(hurap,"r") # hex_printer ile bitisiktir
encrypt_printer()

encypt_yazdiran(cozulmus, shifter)
virus_codes = open(virus,"r")
degistirilmis_yazdiran(cozulmus)
encypt_yazdiran_ters(broken_list, -shifter)
# print(son)
# print(ters_sozluk)
ters_hex(son,hex_yazilacak)
cart_curt()