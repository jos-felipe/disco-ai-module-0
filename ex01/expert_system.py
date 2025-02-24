# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: josfelip <josfelip@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/24 10:47:12 by josfelip          #+#    #+#              #
#    Updated: 2025/02/24 11:01:38 by josfelip         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    # Check for proper command line arguments
    if len(sys.argv) != 3:
        print("Usage: python expert_system.py <min_comfort_temp> <max_comfort_temp>")
        sys.exit(1)
    
    try:
        min_comfort = float(sys.argv[1])
        max_comfort = float(sys.argv[2])
        
        if min_comfort >= max_comfort:
            print("Error: Minimum comfort temperature must be less than maximum comfort temperature")
            sys.exit(1)
    except ValueError:
        print("Error: Comfort temperatures must be numbers")
        sys.exit(1)
    
    # Initial state
    indoor_temp = None  # Will be set on first input
    heating = False
    cooling = False
    
    # Process each input (temperature)
    while True:
        try:
            # Read temperature from stdin
            external_temp = float(input().strip())
            
            # For first reading, indoor = external
            if indoor_temp is None:
                indoor_temp = external_temp
            
            # Expert system logic
            # 1. Determine if heating or cooling should be activated
            if indoor_temp < min_comfort and not heating:
                heating = True
                cooling = False
            elif indoor_temp > max_comfort and not cooling:
                cooling = True
                heating = False
            elif min_comfort <= indoor_temp <= max_comfort:
                heating = False
                cooling = False
            
            # 2. Update indoor temperature based on the current state
            if heating:
                # Heating increases indoor temp by 0.5 degrees per cycle
                indoor_temp += 0.5
            elif cooling:
                # Cooling decreases indoor temp by 0.5 degrees per cycle
                indoor_temp -= 0.5
            else:
                # When system is off, indoor temp moves 0.25 degrees toward external temp
                if abs(indoor_temp - external_temp) < 0.25:
                    indoor_temp = external_temp
                elif indoor_temp < external_temp:
                    indoor_temp += 0.25
                elif indoor_temp > external_temp:
                    indoor_temp -= 0.25
            
            # Determine current action for output
            if heating:
                action = "heating"
            elif cooling:
                action = "cooling"
            else:
                action = "nothing"
            
            # Output: external temp, action, indoor temp
            print(f"{external_temp:.1f} - {action} - {indoor_temp:.1f}")
            
        except EOFError:
            break
        except ValueError:
            print("Error: Invalid input - expected a number")
            break

if __name__ == "__main__":
    main()