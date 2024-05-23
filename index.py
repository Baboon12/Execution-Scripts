import src.metagoofil
import src.wget
import src.whatweb
import src.herschel

def main():
    while True:
        print("Select an option:")
        print("1. Running metagoofil")
        print("2. wget")
        print("3. whatweb")
        print("4. Nmap")
        print("5. Nikto")
        print("6. SqlMap")
        print("7. dnsrecon")
        print("8. dnsenum")
        print("9. dirsearch")
        print("10. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            src.metagoofil.main()
        elif choice == "2":
            src.wget.main()
        elif choice == "3":
            src.whatweb.main()
        elif choice == "4":
            src.herschel.run_nmap()
        elif choice == "5":
            src.herschel.run_nikto()
        elif choice == "6":
            src.herschel.run_sqlmap()
        elif choice == "7":
            src.herschel.run_dnsrecon()
        elif choice == "8":
            src.herschel.run_dnsenum()    
        elif choice == "9":
            src.herschel.run_dirsearch()
        elif choice == "10":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

