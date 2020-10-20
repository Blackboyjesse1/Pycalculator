print("Welkom bij PyCalculator")
First = input("Typ het eerste getal: ")
Second = input("Typ tweede getal: ")
benodig = input("delen, keer, plus of min? ")
if benodig == "delen":
    print(float(First) / float(Second))
if benodig == "keer":
    print(float(First) * float(Second))
if benodig == "plus":
    print(float(First) + float(Second))
if benodig == "min":
    print(float(First) - float(Second))
bye_bye = input("Typ iets om af te sluiten. ")
