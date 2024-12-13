import math

def calculate_telescope_parameters():
    print("Welcome to the Space Telescope Simulator!")
    
    # Input parameters
    diameter = float(input("Enter the primary mirror diameter (in meters): "))
    focal_length = float(input("Enter the focal length (in meters): "))
    wavelength = float(input("Enter the observing wavelength (in micrometers): "))
    
    # Convert wavelength to meters
    wavelength_m = wavelength * 1e-6

    # Calculate resolution (Rayleigh criterion)
    resolution = 1.22 * (wavelength_m / diameter)

    # Calculate magnification assuming a 25mm eyepiece
    eyepiece_focal_length = 0.025  # in meters
    magnification = focal_length / eyepiece_focal_length

    # Print results
    print(f"\n--- Telescope Specifications ---")
    print(f"Primary Mirror Diameter: {diameter} meters")
    print(f"Focal Length: {focal_length} meters")
    print(f"Observing Wavelength: {wavelength} micrometers")
    print(f"Angular Resolution: {resolution:.6f} radians")
    print(f"Magnification (with 25mm eyepiece): {magnification:.1f}x\n")

def simulate_observation():
    print("Simulating Deep-Sky Observations...")

    objects = {
        "1": {"name": "Andromeda Galaxy", "distance": 2.537e6, "description": "A spiral galaxy approximately 2.5 million light-years away."},
        "2": {"name": "Whirlpool Galaxy", "distance": 23e6, "description": "A classic spiral galaxy located 23 million light-years away."},
        "3": {"name": "Black Hole (M87*)", "distance": 53.5e6, "description": "A supermassive black hole located in the galaxy M87, 53.5 million light-years away."}
    }

    print("Choose an object to observe:")
    for key, obj in objects.items():
        print(f"{key}. {obj['name']}")

    choice = input("Enter the number of the object: ")
    if choice in objects:
        obj = objects[choice]
        print(f"\nObserving {obj['name']}...")
        print(f"Distance: {obj['distance']:.2e} light-years")
        print(f"Description: {obj['description']}\n")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculate_telescope_parameters()
    simulate_observation()
