import os
import sys

def display_menu():
    print("""
    ██████╗ ██╗     ██╗      █████╗ ███╗   ███╗ █████╗     ███╗   ██╗███████╗████████╗
    ██╔═══██╗██║     ██║     ██╔══██╗████╗ ████║██╔══██╗    ████╗  ██║██╔════╝╚══██╔══╝
    ██║   ██║██║     ██║     ███████║██╔████╔██║███████║    ██╔██╗ ██║█████╗     ██║   
    ██║   ██║██║     ██║     ██╔══██║██║╚██╔╝██║██╔══██║    ██║╚██╗██║██╔══╝     ██║   
    ╚██████╔╝███████╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║    ██║ ╚████║███████╗   ██║   
     ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝   
    """)
    print("Welcome to OllamaNet!")
    print("Please choose an option:")
    print("1. Run CLI version (run_terminal.py)")
    print("2. Start API server (run_api.py)")
    print("3. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            print("Starting CLI version...")
            os.system('python3 run_terminal.py')
        elif choice == '2':
            print("Starting API server...")
            os.system('python3 run_api.py')
        elif choice == '3':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()