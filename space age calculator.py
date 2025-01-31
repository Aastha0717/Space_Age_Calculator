# Space Age Calculator: Find out your age on different planets!

def space_age(earth_years):    
    # Orbital period (in Earth years) for each planet
    planet_years = {
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Earth": 1.0,  # Just for reference
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }

    print("\n--- Space Age Calculator ---")
    print(f"Your age on Earth: {earth_years} years\n")

    # Loop through each planet and calculate age
    for planet, year_length in planet_years.items():
        planet_age = earth_years / year_length
        print(f"On {planet}, you'd be {planet_age:.2f} years old.")

# Get user input
try:
    age = float(input("Enter your age in Earth years: ").strip())
    
    if age < 0:
        print("Uh-oh! Age can't be negative. Try again.")
    else:
        space_age(age)

except ValueError:
    print("Invalid input! Please enter a number.")
