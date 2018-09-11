print("-----------------------------------")
print("Welcome to S-400 air defence system")
print("-----------------------------------")



radar_cordinate = {"x":0,"y":0,"z":0}
misille_cordinate = {"x":int(input("Misille launchers x cordinate:")),"y":int(input("Misille launchers y cordinate:")),"z":int(input("Misille launchers z cordinate:"))}

seconds = 00
minutes = 00
hours = 00
misille_speed = int(input("Misille speed:"))
jet_speed = int(input("Jet speed:"))
jet_cordinate = {"x":int(input("Jet x cordinate:")),"y":int(input("Jet y cordinate:")),"z":int(input("Jet z cordinate:"))}
jet_cordinate_for_misille = {"x":jet_cordinate["x"]-misille_cordinate["x"],"y":jet_cordinate["y"]-misille_cordinate["y"],"z":jet_cordinate["z"]-misille_cordinate["z"]}
print(100*"\nmisille fired")
while seconds != 12312312:
    jet_cordinate_for_misille = {"x": jet_cordinate["x"] - misille_cordinate["x"],
                                 "y": jet_cordinate["y"] - misille_cordinate["y"],
                                 "z": jet_cordinate["z"] - misille_cordinate["z"]}

    # if int(seconds) < 10 :
    #     seconds = "0"+ str(seconds)
    if jet_cordinate_for_misille["x"]>35 or jet_cordinate_for_misille["x"]<-35:
        if jet_cordinate_for_misille["x"]>0:
            artilacak_deger_X = misille_speed
        elif jet_cordinate_for_misille["x"] <0:
            artilacak_deger_X = -misille_speed
        else:
            artilacak_deger_X = 0
    else:
        artilacak_deger_X = jet_cordinate_for_misille["x"]+jet_speed

    if jet_cordinate_for_misille["y"]>35 or jet_cordinate_for_misille["y"]<-35:

        if jet_cordinate_for_misille["y"]>0:
            artilacak_deger_Y = misille_speed
        elif jet_cordinate_for_misille["y"] <0:
            artilacak_deger_Y = -misille_speed
        else:
            artilacak_deger_Y = 0
    else:
        artilacak_deger_Y = jet_cordinate_for_misille["y"]+jet_speed

    if jet_cordinate_for_misille["z"]>35 or jet_cordinate_for_misille["z"]<-35:

        if jet_cordinate_for_misille["z"]>0:
            artilacak_deger_Z = misille_speed
        elif jet_cordinate_for_misille["z"] <0:
            artilacak_deger_Z = -misille_speed
        else:
            artilacak_deger_Z = 0
    else:
        artilacak_deger_Z = jet_cordinate_for_misille["z"]+jet_speed

    print(str(hours)+":"+str(minutes)+":"+str(seconds))

    # print("misille to jet", jet_cordinate_for_misille)
    if misille_cordinate["x"] != jet_cordinate_for_misille["x"]:
        misille_cordinate["x"] += artilacak_deger_X
    jet_cordinate["x"] += jet_speed
    if misille_cordinate["y"] != jet_cordinate_for_misille["y"]:
        misille_cordinate["y"] += artilacak_deger_Y
    jet_cordinate["y"] += jet_speed
    if misille_cordinate["z"] != jet_cordinate_for_misille["z"]:
        misille_cordinate["z"] += artilacak_deger_Z
    jet_cordinate["z"] += jet_speed
    print("Misille cordinate is", misille_cordinate)
    print("Jet cordinate is", jet_cordinate)




    if misille_cordinate == jet_cordinate:

        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("KABOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOMMMMMMMM")
        print("\n\n Jet succesfully eliminated in "+str(hours)+":"+str(minutes)+":"+str(seconds)+" seconds")

        break
    seconds += 1
    if seconds >= 60:
        seconds -= 60
        minutes+=1
    if minutes >= 60:
        minutes-=60
        hours +=1

    prt = misille_cordinate["x"]**150000
