import sys
import traceback
from src.utils.console import print_header, print_success, print_error, print_info, prompt_input, print_warning
from src.utils.logger import log

# Import all applications
from src.apps import (
    calculator,
    number_guessing,
    contact_book,
    file_renamer,
    password_checker,
    yt_downloader,
    weather_app,
    chatbot
)

def show_menu():
    print_header("Python CLI Projects Collection")
    print_info("Please select an application to run:")
    print("1. Simple Calculator")
    print("2. Number Guessing Game")
    print("3. Contact Book")
    print("4. File Renaming Automation")
    print("5. Password Strength Checker")
    print("6. YouTube Video Downloader")
    print("7. Weather App (OpenWeather API)")
    print("8. Simple Rule-Based Chatbot")
    print("9. Exit")
    print()

def main():
    log.info("Starting Python CLI Projects application.")
    while True:
        try:
            show_menu()
            choice = prompt_input("Enter your choice (1-9): ").strip()
            
            if choice == '1':
                log.info("Running Simple Calculator.")
                calculator.run()
            elif choice == '2':
                log.info("Running Number Guessing Game.")
                number_guessing.run()
            elif choice == '3':
                log.info("Running Contact Book.")
                contact_book.run()
            elif choice == '4':
                log.info("Running File Renaming Automation.")
                file_renamer.run()
            elif choice == '5':
                log.info("Running Password Strength Checker.")
                password_checker.run()
            elif choice == '6':
                log.info("Running YouTube Video Downloader.")
                yt_downloader.run()
            elif choice == '7':
                log.info("Running Weather App.")
                weather_app.run()
            elif choice == '8':
                log.info("Running Chatbot.")
                chatbot.run()
            elif choice == '9':
                print_success("Thank you for using the Python CLI Projects Collection. Goodbye!")
                log.info("Exiting application normally.")
                sys.exit(0)
            else:
                print_error("Invalid choice. Please enter a number between 1 and 9.")
                
        except KeyboardInterrupt:
            print_warning("\nOperation cancelled by user. Returning to main menu...")
            log.warning("KeyboardInterrupt caught in main loop.")
        except Exception as e:
            print_error(f"An unexpected error occurred: {e}")
            log.error(f"Unexpected error: {traceback.format_exc()}")
            print_info("Returning to main menu...")

if __name__ == "__main__":
    main()
