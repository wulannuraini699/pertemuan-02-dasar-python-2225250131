KELVIN_OFFSET = 273.15

celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print(f"Suhu dalam Fahrenheit : {fahrenheit}")
print(f"Suhu dalam Kelvin     : {kelvin}")