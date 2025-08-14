def convert_temperature():
    u = input("Select one (Celsius(c), Fahrenheit(f), Kelvin(k))\n").strip().lower()
    if u not in 'cfk': print("Invalid input."); return
    try:
        v = float(input(f"Enter {('Celsius','Fahrenheit','Kelvin')['cfk'.index(u)]} val="))
    except: print("Invalid value."); return
    t = input("Enter which val you want to convert (c,f,k)\n").strip().lower()
    if t not in 'cfk': print("Invalid input."); return
    if u == t: print(f"Output={v} (no conversion needed)"); return
    if u+t == 'cf': r = v*9/5+32; s = "Celsius converted into Fahrenheit"
    elif u+t == 'ck': r = v+273.15; s = "Celsius converted into Kelvin"
    elif u+t == 'fc': r = (v-32)*5/9; s = "Fahrenheit converted into Celsius"
    elif u+t == 'fk': r = (v-32)*5/9+273.15; s = "Fahrenheit converted intoc"
    elif u+t == 'kc': r = v-273.15; s = "Kelvin converted into Celsius"
    elif u+t == 'kf': r = (v-273.15)*9/5+32; s = "Kelvin converted into Fahrenheit"
    else: print("Conversion not supported."); return
    print(f"{s} is {int(round(r))}")

if __name__ == "__main__":
    convert_temperature()


