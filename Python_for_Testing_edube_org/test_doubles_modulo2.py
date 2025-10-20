def celsius_to_fahrenheit(celsius):
   # Converting function corrected
   result = (celsius * 9/5) + 32
   if celsius == 0:
      print("Temperature is freezing point.")
   elif celsius < 0:
      print("Temperature is below freezing.")
   else: 
      print("Temperature is above freezing.")
   return f"{result} F"

def temperature_stub():
    # Stub: returns a fixed temperature to simulate sensor data
    return 0

def celsius_fahrenheit_converter(): 
   # Fake converter main function
   user_input = temperature_stub()   
   fahrenheit = celsius_to_fahrenheit(user_input)
   expected = "32.0 F"
   if fahrenheit == expected: 
       print(f"Test passed! Correct output: {fahrenheit}")
   else:
       print(f"Test failed. Expected: {expected} but got: {fahrenheit}")


celsius_fahrenheit_converter() 
### Need to be checked celsius_to_fahrenheit(celsius) for result type as integer or float





