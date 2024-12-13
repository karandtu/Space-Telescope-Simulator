# File: main.py
# Main application integrating space telescope design and black hole challenges
from telescope_design import design_telescope
from complex_calculations import model_black_hole
from consistent_theory import explore_consistent_theory
from resolving_singularities import resolve_singularities
from visualization import visualize_space_objects
from integration_logic import integrate_black_holes_and_telescope

def main():
    print("\nWelcome to the Integrated Space Telescope and Black Hole Research Application!\n")
    
    while True:
        print("Choose an option:")
        print("1. Design a Space Telescope")
        print("2. Model a Black Hole")
        print("3. Explore Consistent Theory")
        print("4. Resolve Black Hole Singularities")
        print("5. Visualize Space Objects")
        print("6. Integrate Telescope and Black Hole Challenges")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            design_telescope()
        elif choice == "2":
            model_black_hole()
        elif choice == "3":
            explore_consistent_theory()
        elif choice == "4":
            resolve_singularities()
        elif choice == "5":
            visualize_space_objects()
        elif choice == "6":
            integrate_black_holes_and_telescope()
        elif choice == "7":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
