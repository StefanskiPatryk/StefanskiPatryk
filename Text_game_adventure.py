print("Welcome in text adventure game")
print("####MENU####")
print("1.Wizard")
print("2.Warior=")
print("3.Druid")
cs=int(input("Choose you class :"))
name=input("Name your character:")
print(f"Your character name is: {name}")
print("There you go, you have your first mission. Choose 1 of them")
print("1.Rescue guy from canion")
print("2.Find diamond")    
mission1=int(input("Choose you first mission: "))
while mission1 == 1:
    print("You are going to the canion close to your city")
    print("Then, when you are closer to canion, you hear some noises, that's sounds like HELPP!!")
    print("You are coming closer to the noisees, and you are looking for someon that is calling for help")
    print("When you finally see the person that is calling for help, you are going straight to that person")
    print("On your way is coming big black cat with 3 heads")
    print("Legends say if you hit correct one you will win with enemy")
    hs=int(input("Cat wants to fight, which head you want to hit?1-3 :"))
    if hs==1:
        print("Not this time, try your luck next time.")
        break
    elif hs ==2:
        print("Not this time, try your luck next time.")
        break
    else:
        print("You are lucky, you hit the correct one ;)")
        print("You helped Kamil get out of the canion :)")
        break
        

while mission1 == 2:
    print("You are going to the mine looking for the diamond")
    print("When you finally came dip in mine you see some creatures that are making noises")
    print("You are coming closer and see 3 creatures that are ready to fight")
    print("You need to pick correct scheme to fight them to go further")
    print("1.  1,2,3")
    print("2.  3,2,1")
    print("3.  2,1,3")
    sch=int(input("Pick 1-3 to attack creatures: "))
    if sch == 1:
        print("Not this time, try your luck next time.")
        break
    elif sch == 2:
        print("You picked correct scheme, congratulations you won with creatures")
        print("After a looooonggg time of looking for this diamond you see ... nothing")
        print("After long time you are coming out of mine")
        print("You are going home after a long, hard, boring day")
        print("After a little walk to home you see something that is shining at the ground.")
        print("Then you find out you found diamond :)")
        print("Sooo, this all day of searching was worth it")
        print("You are rich :)")
        break
        
    else:
        print("Not this time, try your luck next time.")
        break
   
   






