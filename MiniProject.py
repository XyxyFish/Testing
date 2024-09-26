# Welcome message to the user
print("Welcome to the Marathon Training Tracker!")
print("Enter the time (in whole minutes) for each 5K run. Press Enter without input when done.")

runs = []  # List to store times for each run

# Loop to continuously ask for run times until the user enters nothing (presses Enter)
while True:
    run_time = input("Enter time for 5K run (in minutes): ").strip()  # Get user input and remove any extra spaces
    
    # If the user presses Enter without input, stop collecting data
    if run_time == "":
        break
    
    # Check if the input is a valid whole number (minutes)
    if run_time.isdigit():
        runs.append(int(run_time))  # Convert the input to an integer and add it to the list of runs
    else:
        # If input is invalid, prompt the user to try again
        print("Invalid input, please enter a whole number.")

# If no runs were entered, display a message and end the program
if len(runs) == 0:
    print("No runs entered. Exiting program.")
else:
    # Calculating the number of days (runs), total time, average time per run, and average time per kilometer
    num_of_days = len(runs)  # The number of runs corresponds to the number of days
    total_minutes = sum(runs)  # Total minutes is the sum of all the run times
    avg_time_per_run = total_minutes / num_of_days  # Average time per run is total minutes divided by the number of runs
    avg_minutes_per_km = total_minutes / (num_of_days * 5)  # Average time per kilometer is total time divided by total kilometers (5 km per run)

    # Displaying the calculated information to the user
    print("\nMarathon Training Summary:")
    print(f"Number of runs: {num_of_days}")
    print(f"Total minutes ran: {total_minutes}")
    print(f"Average time per 5K run (minutes): {avg_time_per_run:.2f}")
    print(f"Average minutes per kilometer: {avg_minutes_per_km:.2f}")
