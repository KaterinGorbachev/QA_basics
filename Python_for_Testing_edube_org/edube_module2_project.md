# Project: Fixing a Bug in a Temperature Conversion System

#### Scenario

You’re working as a developer for "WeatherWise," an environmental data analysis platform. The platform takes temperature inputs in Celsius and converts them to Fahrenheit for users who prefer this unit. A bug report was filed indicating an issue with the conversion function for specific edge cases.

Your task is to investigate the issue based on the provided bug report, fix the code, and validate it through testing with a simple function.

Bug Report

\*\*Found On\*\*: WeatherWise Platform, Version 1.0.4

\*\*Bug ID\*\*: WW-BUG-001

\*\*Description\*\*: The function that converts Celsius to Fahrenheit returns an incorrect result when the input is 0°C.

\*\*Steps to Reproduce\*\*:  
\- Call the celsius\_to\_fahrenheit() function with 0 as input.

\*\*Expected Behavior\*\*: The function should return 32°F (as 0°C equals 32°F).

\*\*Actual Behavior\*\*: The function returns 0°F instead of 32°F.

\*\*Severity\*\*: High (Incorrect output for critical edge case)

\*\*Priority\*\*: High (Affects core temperature conversion accuracy)

\*\* Reviewed by\*\*: Andy Bugfinder Jr.

The function below is suspected of causing the bug. Review and fix it so that the correct result is returned for 0°C.

def celsius\_to\_fahrenheit(celsius):

   result \= (celsius \* 9/5) \+ 32

   

   if celsius \== 0:

      print("Temperature is freezing point.")

      return f"{0} F"

   

   if celsius \< 0:

      print("Temperature is below freezing.") 

      return f"{result} F"

   

   if celsius \> 0:

      print("Temperature is above freezing.")

      return f"{result} F"

\# Original test case showing the issue

print(celsius\_to\_fahrenheit(0))  \# Expected output: 32

def celsius\_to\_fahrenheit(celsius):

   result \= (celsius \* 9/5) \+ 32

   if celsius \== 0:

      print("Temperature is freezing point.")

   elif celsius \< 0:

      print("Temperature is below freezing.")

   else: 

      print("Temperature is above freezing.")

   return f”{result} F”

Create a stub function, temperature\_stub(), that returns 0°C to simulate input for the temperature conversion. Use this to verify the behavior of the corrected function.  
def temperature\_stub():  
    \# Stub: returns a fixed temperature to simulate sensor data  
    return 0

Write a simple test function that uses the temperature\_stub() function to simulate input and validate the output of the fixed celsius\_to\_fahrenheit() function.

**Bug Fix Report**

\*\*Bug ID\*\*: WW-BUG-001

\*\*Summary\*\*: The celsius\_to\_fahrenheit() function was returning an incorrect output of 0°F when 0°C was input, instead of the expected 32°F.

\*\*System Under Test (SUT)\*\*: WeatherWise Platform, Version 1.0.4, Temperature Conversion Module

\*\*Replication Steps\*\*:  
1\. Call the celsius\_to\_fahrenheit() function with an input of 0\.  
2\. Observe the printed message and returned result.

\*\*Root Cause Analysis\*\*: The bug was due to an incorrect return value for the edge case when celsius \== 0\. The code had a return statement that returned 0 instead of the calculated result.

\*\*Fix Description\*\*: The return statement in the block handling celsius \== 0 was corrected to return the calculated result instead of 0\.

\*\*Test Strategy\*\*:  
\- \*\*Test Environment\*\*: Local development environment, Python 3.10, Windows 11  
\- \*\*Test Steps\*\*:  
  1\. Implemented a stub function to simulate the input of 0°C.  
  2\. Called the fixed celsius\_to\_fahrenheit() function using the stub.  
  3\. Verified the output against the expected result of 32°F in fake main function.  
  4\. Conducted additional tests with positive and negative Celsius values.

\*\*Test Outcome\*\*: The test failed with the actual output of 32.0°F for 0°C when 32°F expected. 

\*\*Status\*\*: Verified and Needed requirements check.

\*\*Reviewed by/Fix by\*\*: John Tester / Jane Developer

\*\*Comments/Additional Information\*\*: 1.Due to implementation of division in the celsius\_to\_fahrenheit() function, the type of result that gives the function is float. In the requirements it is expected to get an integer 32°F as output. The error can be fixed by changing the requirements expected result or by changing the celsius\_to\_fahrenheit() function to return 32°F for 0°C.   
2.Further regression tests are recommended to ensure consistent behavior across all edge cases and temperature ranges.

    
		

