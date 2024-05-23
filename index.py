import src.metagoofil
import src.wget
import src.whatweb

def main():
    while True:
        print("Select an option:")
        print("1. Running metagoofil")
        print("2. wget")
        print("3. whatweb")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            src.metagoofil.main()
        elif choice == "2":
            src.wget.main()
        elif choice == "3":
            src.whatweb.main()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

