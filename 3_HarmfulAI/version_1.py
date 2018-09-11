#
#
#
#
#
#
import sys


num_shcu = sum(1 for line in open("shcu.txt"))
num_binary = sum(1 for line in open("binary.txt"))
def binlisteceviren(dosya_adi,binarylist):
    encrypt = open(dosya_adi,"r+")
    line = encrypt.readline()
    i = 0
    for x in range(len(line)//4):
        a = str(line[i])+str(line[i+1])+str(line[i+2])+str(line[i+3])
        i = i+4
        binarylist.append(a)

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

def shcuokuyucu(cevrilen,asciisys):
    global sozluk
    global chiper
    chiper = []
    sozluk = {}
    encrypt = open(asciisys,"r+")
    for i in range(num_shcu):
        a = encrypt.readline().split("\t")
        chiper.append(a[0])
        sozluk.setdefault(a[1],(a[0],a[2]))


def encrypter(crypted,uncrypted,shift):
    for  i in range(len(crypted)):
        if i > len(crypted):
            i = i%len(crypted)
        t = chiper.index(crypted[i])
        uncrypted.append(crypted[(t+shift)%len(crypted)])





    encrypt.close()
    # print(sozluk)
    # for anahtar,deger in sozluk.items():
    #     print("{} = {}".format(anahtar,deger))
    for i in range(len(cevrilen)):
        cevrilen[i] = str(sozluk[cevrilen[i]][0])


binarylist = []
b = []
sonuc = []
# for i in range(num_binary):
binlisteceviren("binary.txt",binarylist)
binaryconverter(binarylist,b)
print(b)
# print(b)
shcuokuyucu(b,"shcu.txt")
print(b)
# print(b)
# for i in range(num_shcu):
#     encrypter(b,sonuc,i)
#     print(sonuc)
#     sonuc = []
