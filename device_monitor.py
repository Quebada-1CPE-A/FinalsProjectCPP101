readings = [28, 31, 35, 37, 29]

def view_readings(readings):
    print("CURRENT READINGS")
    print("----------------")
    for i in range(len(readings)):
        reading = readings[i]
        print(f"Reading {i + 1}: {reading} °C")

def is_integer(value):
    if len(value) == 0:
        return False
    start = 0
    if value[0] == "-":
        start = 1
    if start == len(value):
        return False
    for index in range(start, len(value)):
        if value[index] not in "0123456789":
            return False
    return True




def add_new_number(value):
    while True:
        new_reading = input("Enter new reading: ")
        if len(new_reading) == 0:
            print("Blank is invalid. Try again.")
        elif not is_integer(new_reading):
            print("Invalid input. Try again.")
        else:
            new_reading_int = int(new_reading)
            if new_reading_int > 100 or new_reading_int < 0:
                print("Invalid reading. Try again.")
            else:
                value.append(new_reading_int)
                print("Reading added successfully.")
                break


def reading_class(reading):
    if reading < 30:
        return "NORMAL"
    elif reading >= 30 and reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"
    

def monitor_summary(readings):
    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings: {len(readings)}")
    total = 0
    for reading in readings:
        total += reading
    print(f"Total of readings: {total}")
    print(f"Average temperature: {total / len(readings):.2f} °C")

    highest_reading = readings[0]
    lowest_reading = readings[0]
    for reading in readings:
        if reading > highest_reading:
            highest_reading = reading
        if reading < lowest_reading:
            lowest_reading = reading
    print(f"Minimum temperature: {lowest_reading} °C")
    print(f"Maximum temperature: {highest_reading} °C")


def count_readings(values):
    normal_count = 0
    warning_count = 0
    critical_count = 0
    for reading in values:
        class_r = reading_class(reading)
        if class_r == "NORMAL":
            normal_count += 1
        elif class_r == "WARNING":
            warning_count += 1
        elif class_r == "CRITICAL":
            critical_count += 1
    return normal_count, warning_count, critical_count



def reading_count(readings):
    normal_count, warning_count, critical_count = count_readings(readings)
    print(f"NORMAL: {normal_count:>4} ({100 * normal_count / len(readings):.2f}%)")
    print(f"WARNING: {warning_count:>4} ({100 * warning_count / len(readings):.2f}%)")
    print(f"CRITICAL: {critical_count:>4} ({100 * critical_count / len(readings):.2f}%)")

def overall_status(normal_count, warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def get_choice(lowest, highest):
        print("SIMULATED DEVICE MONITORING SYSTEM")
        print("-----------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")
        choice = input("Enter choice: ")
        if len(choice) == 0:
            print("Empty is invalid. Try again.")
        elif not is_integer(choice):
            print("Must be an integer. Try again.")
        elif int(choice) > highest or int(choice) < lowest:
            print("Invalid choice. Please select a valid option.")
        elif int(choice) not in [1, 2, 3, 4, 5]:
            print("Invalid choice. Please select a valid option.")
        else:
            return int(choice)

def main():
    while True:
        choice = get_choice(1,5)
        if choice == 1:
            view_readings(readings)
            print()
        elif choice == 2:
            add_new_number(readings)
            print()
        elif choice == 3:
            for reading in readings:
                classification = reading_class(reading)
                print(f"{reading} °C -> {classification}")
            print()
        elif choice == 4:
            monitor_summary(readings)
            print()
            normal_count, warning_count, critical_count = count_readings(readings)
            reading_count(readings)
            print()
            print(f"Overall Status: {overall_status(normal_count, warning_count, critical_count)}")
        elif choice == 5:
            print("Thank you for using the Device Monitoring System.")
            break


main()