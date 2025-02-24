import sys
import time
import math
import random

def get_temperature(hour, season):
    """
    Calculate temperature based on hour of day and season
    Using a sine wave with different parameters for each season
    """
    # Season parameters: (min_temp, max_temp)
    season_params = {
        "winter": (-5, 5),
        "spring": (5, 18),
        "summer": (15, 30),
        "autumn": (5, 15)
    }
    
    try:
        min_temp, max_temp = season_params[season.lower()]
    except KeyError:
        print(f"Invalid season. Choose from: {', '.join(season_params.keys())}")
        sys.exit(1)
    
    # Calculate base temperature using sine function
    # The sine wave peaks at around 2-3 PM (hour 14-15)
    amplitude = (max_temp - min_temp) / 2
    mid_temp = min_temp + amplitude
    # Shift the sine wave so it's coldest around 5 AM
    phase_shift = 5
    temperature = mid_temp + amplitude * math.sin(math.pi * (hour - phase_shift) / 12)
    
    # Add small random variation (-0.5 to +0.5)
    temperature += random.uniform(-0.5, 0.5)
    
    return round(temperature, 2)

def main():
    if len(sys.argv) != 2:
        print("Usage: python environment.py <season>")
        print("Seasons: winter, spring, summer, autumn")
        sys.exit(1)
    
    season = sys.argv[1]
    
    # Handle numeric input (1=winter, 2=spring, 3=summer, 4=autumn)
    if season.isdigit():
        seasons = ["winter", "spring", "summer", "autumn"]
        try:
            season = seasons[int(season) - 1]
        except (IndexError, ValueError):
            print("If using numbers, please provide a number from 1 to 4")
            sys.exit(1)
    
    # Simulate a full day (24 hours) in 48 seconds (30 min intervals)
    for i in range(48):
        hour = i / 2  # Convert to hours (0 to 23.5)
        temperature = get_temperature(hour, season)
        print(temperature)
        time.sleep(1)  # Wait for 1 second

if __name__ == "__main__":
    main()