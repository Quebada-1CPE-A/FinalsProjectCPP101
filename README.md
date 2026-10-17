# Simulated Device Monitoring and Alert System
 
**Student Name:** Luiza Regino Quebada
**Student Number:** 2600681
**Section:** 1CPE - A
 
## Project Description
This project serves as a system for monitoring temperatures.  It gives you the readings, lets you add a new reading, and changes it summary for every number you add. It shall only accept integers; any string are considered invalid, and must input a different value. This prohject's objective is to apply all the knowledge learned throughout the whole course.
 
## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings
 
## Requirements
- Python 3 (no external packages)
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)
 
## Sample Output
SIMULATED DEVICE MONITORING SYSTEM
-----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 9
Invalid choice. Please select a valid option.
SIMULATED DEVICE MONITORING SYSTEM
-----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 4
MONITORING SUMMARY
------------------
Number of readings: 5
Total of readings: 160
Average temperature: 32.00 °C
Minimum temperature: 28 °C
Maximum temperature: 37 °C

NORMAL:    2 (40.00%)
WARNING:    2 (40.00%)
CRITICAL:    1 (20.00%)

Overall Status: ATTENTION REQUIRED
SIMULATED DEVICE MONITORING SYSTEM
-----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 5
Thank you for using the Device Monitoring System.
 
## Test Cases
I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md.
 
## Known Limitations
- Does not have a design like website yet.
- Does not have an option where user chooses not to input and goes back in the menu instead without inputs.
 
## Reflection
I enjoyed doing this code. The hardest part so far was the determining whether the user's input is an integer or not. I had to rely on the module, but at the same time I learned a lot from it. I shall improve my knowledge on the syntax better.
