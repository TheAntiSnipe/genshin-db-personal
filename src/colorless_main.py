import json

class TalentCostCalculator:
    def __init__(self):
        # talent_material_cost_json = open("talent_material_cost.json", "r")
        self.talent_material_cost_dict = {"Mora":{"0":12500,"1":17500,"2":25000,"3":30000,"4":37500,"5":120000,"6":260000,"7":450000,"8":700000},"Talent books(uncommon)":{"0":3,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0},"Talent books (rare)":{"0":0,"1":2,"2":4,"3":6,"4":9,"5":0,"6":0,"7":0,"8":0},"Talent books (epic)":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":4,"6":6,"7":12,"8":16},"Mob drops(common)":{"0":6,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0},"Mob drops(uncommon)":{"0":0,"1":3,"2":4,"3":6,"4":9,"5":0,"6":0,"7":0,"8":0},"Mob drops(rare)":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":4,"6":6,"7":9,"8":12},"Boss material":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":1,"6":1,"7":2,"8":2},"Crowns":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":1}}

        list_of_material_types = [
            "Mora",
            "Talent books(uncommon)",
            "Talent books (rare)",
            "Talent books (epic)",
            "Mob drops(common)",
            "Mob drops(uncommon)",
            "Mob drops(rare)",
            "Boss material",
            "Crowns",
        ]
        list_of_material_quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.cumulative_material_dict = dict(
            zip(list_of_material_types, list_of_material_quantities)
        )

        # * cumulative_material_dict holds the current sum of all resources
        # * needed. Updates in aggregate_cumulative_cost for each talent.
        # * Used in determine_total_costs_and_display after all iterations of
        # * aggregate_cumulative_cost finish.

    # * Four methods:
    # *    1. validate_level_input
    #         Validates input level against a whitelist
    #         and resorts to a fallback if this isn't followed.
    # *    2. aggregate_cumulative_cost
    #        Handles dataframe aggregation and summation with
    #        cumulative_material_dict.
    # *    3. determine_total_costs_and_display
    #        Handles method calls to aggregate_cumulative_cost and displays
    #        output UI.
    # *    4. run_talent_material_calculator
    #        Handles UI display and sends initial and final talent values to
    #        determine_total_costs_and_display.

    def validate_level_input(self,whitelist,input_data,fallback):
        if input_data in whitelist:
            return int(input_data)
        else:
            return fallback

    def aggregate_cumulative_cost(self, initial_level, final_level):
        for index in range(initial_level - 1, final_level - 1):
            # * The json data is zero-indexed
            for key in list(self.cumulative_material_dict.keys()):
                # Update for the values associated with each key in the
                # cumulative_material_dict

                self.cumulative_material_dict[key] += self.talent_material_cost_dict[
                    key
                ][str(index)]

    def determine_total_costs_and_display(
        self,
        initial_talent_values,
        final_talent_values,
    ):

        for index in range(3):
            self.aggregate_cumulative_cost(
                initial_talent_values[index],
                final_talent_values[index],
            )
        for key, value in self.cumulative_material_dict.items():
            if value != 0:
                # * If something is not required, don't display it.
                print("Total "
                    + key
                    + " needed: "
                    + str(int(value))
                )

    def run_talent_material_calculator(self):
        print("\nMy character has current talent levels: (press anything if 1)")
        whitelist = [str(i) for i in range(2,11)]
        fallback = 1
        aa_initial = input("Auto-attack talent: ")
        aa_initial = self.validate_level_input(whitelist,aa_initial,fallback)
        e_initial = input("Elemental skill talent: ")
        e_initial = self.validate_level_input(whitelist,e_initial,fallback)
        q_initial = input("Elemental burst talent: ")
        q_initial = self.validate_level_input(whitelist,q_initial,fallback)
        initial_talent_values = [aa_initial, e_initial, q_initial]

        print("\nI need talent levels: (press anything if 10)")
        whitelist = [str(i) for i in range(1,10)]
        fallback = 10
        aa_final = input("Auto-attack talent: ")
        aa_final = self.validate_level_input(whitelist,aa_final,fallback)
        e_final = input("Elemental skill talent: ")
        e_final = self.validate_level_input(whitelist,e_final,fallback)
        q_final = input("Elemental burst talent: ")
        q_final = self.validate_level_input(whitelist,q_final,fallback)
        final_talent_values = [aa_final, e_final, q_final]
        print("\nThus, for",initial_talent_values,"to",final_talent_values,"I need:")

        self.determine_total_costs_and_display(
            initial_talent_values,
            final_talent_values,
        )


class BasicCalculationFunctions:
    #  This class covers functions that do simple calculations and don't pull from
    #  any of the csv files.

    # * Three methods:
    # *     1. take_integer
    #          Persistently takes input until user enters an int.
    # *     2. exp_input
    #          Common input handler for 2 and 3.
    # *     3. mora_for_exp_calculator
    #         Handles the second option, gives the number of mora needed
    #         for a given number of EXP books.
    # *     4. exp_book_aggregator
    #         Handles the conversion of various EXP book types to a standardized
    #         "hero's wit equivalent" format.
    def take_integer(self,text,fallback):
        value = input(text)
        while(not value.isdigit()):
            value = input(fallback)
        return value
    
    def exp_input(self):
        print("\nI have the following EXP book quantities: ")
        text = "Uncommon books: "
        fallback = "Please enter an integer for uncommon books: "
        uncommon_exp_books = int(self.take_integer(text,fallback))
        text = "Rare books: "
        fallback = "Please enter an integer for rare books: "
        rare_exp_books = int(self.take_integer(text,fallback))
        text = "Epic books: "
        fallback = "Please enter an integer for epic books: "
        epic_exp_books = int(self.take_integer(text,fallback))
        return uncommon_exp_books,rare_exp_books,epic_exp_books

    def mora_for_exp_calculator(self):
        uncommon,rare,epic = self.exp_input()
        # * Cost per uncommon book is 200 mora.
        # * Cost per rare book is 1000 mora.
        # * Cost per epic book is 4000 mora.
        total_mora_required = (
            200 * uncommon + 1000 * rare + 4000 * epic
        )
        print("\nThus, I need "
            + str(total_mora_required)
            + " mora"
        )

    def exp_book_aggregator(self):
        uncommon,rare,epic = self.exp_input()
        epic_book_aggregate = (
            epic + rare / 4 + uncommon / 20
        )
        print("\nThis equates to: "
            + str(epic_book_aggregate)
            + " hero's wit"
        )


class LevelingCostCalculator:
    def __init__(self):
        self.ascend_cost_dict = {
    "Mora": {
        "0": 24200,
        "1": 135800,
        "2": 156000,
        "3": 231000,
        "4": 319200,
        "5": 402400,
        "6": 804800
    },
    "Crystal fragment (uncommon)": {
        "0": 0,
        "1": 1,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    },
    "Crystal fragment (rare)": {
        "0": 0,
        "1": 0,
        "2": 3,
        "3": 6,
        "4": 0,
        "5": 0,
        "6": 0
    },
    "Crystal fragment (epic)": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 3,
        "5": 6,
        "6": 0
    },
    "Crystal fragment (legendary)": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 6
    },
    "Boss material": {
        "0": 0,
        "1": 0,
        "2": 2,
        "3": 4,
        "4": 8,
        "5": 12,
        "6": 20
    },
    "Local speciality": {
        "0": 0,
        "1": 3,
        "2": 10,
        "3": 20,
        "4": 30,
        "5": 45,
        "6": 60
    },
    "Mob drops(common)": {
        "0": 0,
        "1": 3,
        "2": 15,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    },
    "Mob drops(uncommon)": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 12,
        "4": 18,
        "5": 0,
        "6": 0
    },
    "Mob drops(rare)": {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 12,
        "6": 24
    },
    "EXP needed": {
        "0": 120175,
        "1": 578325,
        "2": 579100,
        "3": 854125,
        "4": 1195925,
        "5": 1611875,
        "6": 3423125
    }
}

        list_of_material_types = [
            "Mora",
            "Crystal fragment (uncommon)",
            "Crystal fragment (rare)",
            "Crystal fragment (epic)",
            "Crystal fragment (legendary)",
            "Boss material",
            "Local speciality",
            "Mob drops(common)",
            "Mob drops(uncommon)",
            "Mob drops(rare)",
            "EXP needed",
        ]
        list_of_material_quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cumulative_material_dict = dict(
            zip(list_of_material_types, list_of_material_quantities)
        )

    # * Two methods:
    # *     1. find_total_cost_of_levels
    #          Aggregates total resources needed and displays output UI.
    # *     2. level_resource_calculator
    #         Handles UI display and sends the current and required level
    #         values to find_total_cost_of_levels

    def find_total_cost_of_levels(self, current_level, required_level):
        for index in range(current_level-1, required_level):
            for key in list(self.cumulative_material_dict.keys()):
                self.cumulative_material_dict[key] += self.ascend_cost_dict[key][
                    str(index)
                ]

        for key, value in self.cumulative_material_dict.items():
            if value != 0:
                # * We need a separate piece of logic when displaying
                # * the EXP needed section.
                if key != "EXP needed":
                    print(key + ":" + str(value))
                else:
                    # * One epic book is 20000 EXP, we round it to
                    # * double precision.
                    final_exp_required = round(value / 20000, 2)
                    print("EXP books needed in terms of epic EXP books: "
                        + str(final_exp_required)
                    )

    def level_resource_calculator(self):
        valid_starts = [str(i) for i in range(2,8)]
        valid_ends = [str(i) for i in range(1,7)]
        print("\nMy character is currently at: ")
        print("Any key > Level 1")
        print("2 > Level 20")
        print("3 > Level 40")
        print("4 > Level 50")
        print("5 > Level 60")
        print("6 > Level 70")
        print("7 > Level 80")
        print("""\n(We are assuming your character hasn't been ascended at that level. 
If you select 20, your character should be 20/20, not 20/40.)\n"""
        )
        current_level = input("Enter the corresponding number: ")
        if current_level not in valid_starts:
            current_level = 1
        else:
            current_level = int(current_level)

        print("I want my character to be: ")
        print("1 > Level 20")
        print("2 > Level 40")
        print("3 > Level 50")
        print("4 > Level 60")
        print("5 > Level 70")
        print("6 > Level 80")
        print("Any key > Level 90")
        required_level = input("\nEnter the corresponding number: ")
        if required_level not in valid_ends:
            required_level = 7
        else:
            required_level = int(required_level)
        if required_level < current_level:
            print("Your required level cannot be lower than your current level. Exiting."
            )
        else:
            start_level = [1, 20, 40, 50, 60, 70, 80]
            end_level = [20, 40, 50, 60, 70, 80, 90]
            print("\nMaterials required to level a character from "
                + str(start_level[current_level - 1])
                + " to "
                + str(end_level[required_level - 1])
                + ":\n"
            )
            self.find_total_cost_of_levels(current_level, required_level)


class MainMenu:
    def display_option_list(self):
        option = input("""\nEnter what you want to do with the database:
1. Figure out talent level resource requirements.
2. Figure out how much mora you need for some EXP quantity.
3. Figure out character level + ascension resource requirements.
4. Convert uncommon, rare and epic EXP books' EXP values to values relative to epic EXP books. 

Press any other key to exit.

Enter the corresponding number: """
            )
        calculation_functions = BasicCalculationFunctions()
        talent_cost_calculator = TalentCostCalculator()
        leveling_cost_calculator = LevelingCostCalculator()
        if option == '1':
            talent_cost_calculator.run_talent_material_calculator()
        elif option == '2':
            calculation_functions.mora_for_exp_calculator()
        elif option == '3':
            leveling_cost_calculator.level_resource_calculator()
        elif option == '4':
            calculation_functions.exp_book_aggregator()
        else:
            exit("Thank you for using GI-DB!")

def main():
    newMenu = MainMenu()
    while True:
        newMenu.display_option_list()

if __name__ == "__main__":
    newMenu = MainMenu()
    while True:
        newMenu.display_option_list()
