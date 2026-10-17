# Test Cases – Simulated Device Monitoring and Alert System
 
Tested by: Quebada, Luiza R.        Date: Oct. 17, 2026
 
| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Five readings | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading added successfully. | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Rejected; displays "Invalid input. Try again." | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Rejected; displays "Invalid reading. Try again." | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Rejected; displays "Invalid reading. Try again." | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | 30 degrees, classified as WARNING | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | 35 degrees, classified as Warning. | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Total of 160, average of 32, minimum of 28, mmaximum of 37, 2 normal count, 2 warning count, 1 critical count | Pass |
| TC09 | Enter 9 | Error message; menu shown again | Lets the user reinput; displays "Invalid choice, please select a valid option." | Pass |
| TC10 | Choose 5 | Exit message; program ends | Exits the program; displays "Thank you for using the Device Monitoring System. "| Pass |

 
## Bugs Found and Fixed
- It usually had a problem at the is_integer(), I couldn't figure out how to make it detect without using the isdigit command. So I had to look at the module, and ask for AI on how the code worked. Now I understood that it needed len commands as well as logic to even make it work. 
- Another issue I was also struggling with as a beginner coder is the syntax of commands. Like using loops when not needed, not defining a variable before making the command, etc. I have learned it with help of AI, I both learned and utilized it.

