#Author Yan Lu yfl5541@psu.edu
#Collaborator Marco Falcucci mzf5527@psu.edu
#Collaborator Samantha Nelson szn254@psu.edu
#Collaborator Finn Thompson fet5024@psu.edu
Temp = float(input("Enter temperature: "))
unit = input("Enter unit in F/f or C/c: ")
if unit == "C" or unit =="c":
  f = float((Temp*9/5)+32)
  print(f"{Temp}° in Celsius is equivalent to {f}° Fahrenheit.")
elif unit=="F" or unit=="f":
    c = float((Temp-32)*5/9)
    print(f"{Temp}° in Fahrenheit is equivalent to {c}° Celsius.")
else:
  print(f"Invalid unit ({unit}).")
  