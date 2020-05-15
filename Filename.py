name=str(input("Input the filename:"))
loc=name.find(".")
if '.' in name:
  print("The extension of the file is:",name[loc+1:])
