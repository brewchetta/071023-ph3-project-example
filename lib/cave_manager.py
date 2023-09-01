from lib.models import CaveProperty
from colorama import Fore
import time

class CaveManager:

    ###
    # This lists out possible prompts in a green color for users
    MENU_PROMPTS=f"""{Fore.GREEN}
        1. Search for cave
        2. Purchase cave
        3. Rent a cave
        4. Speak to a live cave manager
        5. Exit
        {Fore.RESET_ALL}
        """
    ###
    
    ###
    # This variable will be used throughout the application
    user_input = ""
    ###


    ###
    # The run method is the "entry point" for the application
    def run(self):
        CaveProperty.create_table()
        print("Welcome to Cave Manager 10,000 B.C.!")
        self.main_menu()
    ###


    ###
    # The main_menu loops on itself until somebody inputs "5" a.k.a. exits the application
    def main_menu(self):
        while self.user_input != "5":
            print(self.MENU_PROMPTS)            
            self.user_input = input(">>> ")

            possible_inputs={
                "1": self.search_for_cave,
                "2": self.purchase_cave,
                "3": self.rent_cave,
                "4": self.speak_to_cave_manager,
                "5": self.exit_cave,
            }

            # we are checking here to see whether the user picked an input from our possible inputs
            # if so we run the input
            if self.user_input in possible_inputs:
                possible_inputs[self.user_input]()
            else:
                print("Invalid input you caveperson, try again...")
        ###


    ###
    # solicits input for cave name and gives option to purchase the cave
    def search_for_cave(self):
        print("What is the name of the cave you're looking for?")
        self.user_input = input(">>> ")

        found_property = CaveProperty.select_by_name(self.user_input)

        print("Searching for cave...")
        time.sleep(1)
        print("Querying our database...")
        time.sleep(1)
        print("Asking local cavepeople...")
        time.sleep(1)
        print("Hunting and gathering...")
        time.sleep(1)


        if found_property:
            print(f"Found! Would you like to purchase {found_property.name} for {found_property.price_in_rocks}?")
            self.user_input = input(">>> ")

            if self.user_input == "yes":
                self.purchase_cave()
            else:
                print("Sending you back to the main menu...")

        else:
            print("No property found with that name")
    ###

    ###
    # would ideally build these out more...
    def purchase_cave(self):
        print("Congratulations on your new purchaseeeeee!!!!!!!")

    def rent_cave(self):
        pass

    def speak_to_cave_manager(self):
        pass

    def exit_cave(self):
        print("See ya later gator!")
    ###