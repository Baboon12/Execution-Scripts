import subprocess

def directory_enum():
    website_url = input("Enter website URL: ")
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'dir', '-u', website_url, '-w', wordlist_path])

def subdomain_enum():
    domain = input("Enter domain: ")
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'dns', '-d', domain, '-w', wordlist_path, '--wildcard'])

def s3_enum():
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 's3', '-w', wordlist_path])

def vhost_enum():
    website_url = input("Enter website URL: ")
    wordlist_path = input("Enter path to wordlist: ")
    subprocess.run(['gobuster', 'vhost', '-u', website_url, '-w', wordlist_path])

def main():
    while True:
        print("Select an option:")
        print("1. Directory Enumeration")
        print("2. Subdomain Enumeration")
        print("3. S3 Bucket Enumeration")
        print("4. VHost Enumeration")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            directory_enum()
        elif choice == '2':
            subdomain_enum()
        elif choice == '3':
            s3_enum()
        elif choice == '4':
            vhost_enum()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
