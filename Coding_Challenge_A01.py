symbols = {"carbon":"C","oxygen":"O","hydrogen":"H","chlorine":"Cl"}

chemicals = {"carbon":["C",["[O2] oxygen","CO2","Carbon Dioxide"],
                       ["[4H] hydrogen","CH4","Methane"],
                       ["[4Cl] chlorine","CCl4","Carbon tetrachloride"]],
             "hydrogen":["H",["[O2] oxygen","2 H2O","Water"],
                        ["[Cl] chlorine","HCl","Hydrochloric Acid"],
                        ["[C] carbon","CH4","Methane"]],
             "chlorine":["Cl",["[O2] oxygen","2 Cl2O","Dichlorine Monoxide"],
                         ["[H] hydrogen","HCl","Hydrochloric Acid"],
                         ["[C] carbon","CCl4","Carbon tetrachloride"]]}

x = input("Chemical 1: ")
y = input("Chemical 2: ")
count = 0

for chem1 in chemicals.keys():
    if x.lower() == chem1 and x != y:
        for chem2 in chemicals[x.lower()][1:]:
            if chem2[0].split()[1] == y.lower():
                print(f"[{chemicals[x.lower()][0]}] {chem1.capitalize()} + {chem2[0].split()[0]} {chem2[0].split()[1].capitalize()} = {chem2[1]} ({chem2[2]})")
                count += 1
        break
    elif y.lower() == chem1 and x != y:
        for chem2 in chemicals[y.lower()][1:]:
            if chem2[0].split()[1] == x.lower():
                print(f"[{chemicals[y.lower()][0]}] {chem1.capitalize()} + {chem2[0].split()[0]} {chem2[0].split()[1].capitalize()} = {chem2[1]} ({chem2[2]})")
                count += 1
        break
    elif x.lower() == y.lower() and x.lower() != "carbon":
        print(f"[{symbols[x.lower()]}] {x.lower().capitalize()} + [{symbols[x.lower()]}] {x.lower().capitalize()} = [{symbols[x.lower()]}2]")
        count += 1
        break
    else:
        continue

if count == 0: print("Chemical Equation is not permissible.")
        
