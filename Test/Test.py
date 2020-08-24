from Core.Code_Core import Code_Core

g = Code_Core()
Code = g.Generate.Generate_Base64_Image(True)
print(Code[0])
print(Code[1])

print(g.Generate.Generate_Code_OnlyString(5))

