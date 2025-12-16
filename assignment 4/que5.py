converters = [
    lambda t: t * 1000,                  
    lambda kg: kg * 1000,                
    lambda g: g * 1000,                  
    lambda mg: mg / 453592.37            
]
tonnes = float(input("Enter weight in tonnes: "))
kg = converters[0](tonnes)
grams = converters[1](kg)
mg = converters[2](grams)
pounds = converters[3](mg)
print("Weight in kilograms:", kg, "kg")
print("Weight in grams:", grams, "gm")
print("Weight in milligrams:", mg, "mg")
print("Weight in pounds:", pounds, "lbs")
