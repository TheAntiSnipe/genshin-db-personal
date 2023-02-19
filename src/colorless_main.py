import json


class TalentCostCalculator:
    def __init__(self):
        talent_material_cost_json = open("talent_material_cost.json", "r")
        self.talent_material_cost_dict = json.load(talent_material_cost_json)

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

    # * Three methods:
    # *    1. run_talent_material_calculator
    #        Handles UI display and sends initial and final talent values to
    #        determine_total_costs_and_display.
    # *    2. determine_total_costs_and_display
    #        Handles method calls to aggregate_cumulative_cost and displays
    #        output UI.
    # *    3. aggregate_cumulative_cost
    #        Handles dataframe aggregation and summation with
    #        cumulative_material_dict.

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
                print("Total " + key + " needed: " + str(int(value)))

    def run_talent_material_calculator(self):
        print("\nMy character has current talent levels:")

        aa_initial = int(input("Auto-attack talent: "))
        e_initial = int(input("Elemental skill talent: "))
        q_initial = int(input("Elemental burst talent: "))
        initial_talent_values = [aa_initial, e_initial, q_initial]

        print("\nI need talent levels:")
        aa_final = int(input("Auto-attack talent: "))
        e_final = int(input("Elemental skill talent: "))
        q_final = int(input("Elemental burst talent: "))
        final_talent_values = [aa_final, e_final, q_final]
        print("\nThus, I need:")

        self.determine_total_costs_and_display(
            initial_talent_values,
            final_talent_values,
        )


class BasicCalculationFunctions:
    #  This class covers functions that do simple calculations and don't pull from
    #  any of the csv files.

    # * Two methods:
    # *     1. mora_for_exp_calculator
    #         Handles the second option, gives the number of mora needed
    #         for a given number of EXP books.
    # *     2. exp_book_aggregator
    #         Handles the conversion of various EXP book types to a standardized
    #         "hero's wit equivalent" format.

    def mora_for_exp_calculator(self):
        print("\nI have the following EXP book quantities: ")
        uncommon_exp_books = int(input("Uncommon books: "))
        rare_exp_books = int(input("Rare books: "))
        epic_exp_books = int(input("Epic books: "))
        # * Cost per uncommon book is 200 mora.
        # * Cost per rare book is 1000 mora.
        # * Cost per epic book is 4000 mora.
        total_mora_required = (
            200 * uncommon_exp_books + 1000 * rare_exp_books + 4000 * epic_exp_books
        )
        print("\nThus, I need " + str(total_mora_required) + " mora")

    def exp_book_aggregator(self):
        print("\nI have the following EXP book quantities: ")
        uncommon_exp_books = int(input("Uncommon books: "))
        rare_exp_books = int(input("Rare books: "))
        epic_exp_books = int(input("Epic books: "))
        epic_book_aggregate = (
            epic_exp_books + rare_exp_books / 4 + uncommon_exp_books / 20
        )
        print("\nThis equates to: " + str(epic_book_aggregate) + " hero's wit")


class LevelingCostCalculator:
    def __init__(self):
        ascend_cost_json = open("character_levelup_ascend_cost.json", "r")
        self.ascend_cost_dict = json.load(ascend_cost_json)

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
    # *     1. level_resource_calculator
    #         Handles UI display and sends the current and required level
    #         values to find_total_cost_of_levels
    # *     2. find_total_cost_of_levels
    #          Aggregates total resources needed and displays output UI.

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
                    print(
                        "EXP books needed in terms of epic EXP books: "
                        + str(final_exp_required)
                    )

    def level_resource_calculator(self):
        print("\nMy character is currently at: ")
        print("1> Level 1")
        print("2> Level 20")
        print("3> Level 40")
        print("4> Level 50")
        print("5> Level 60")
        print("6> Level 70")
        print("7> Level 80")
        print(
            """\n(We are assuming your character hasn't been ascended at that level. 
If you select 20, your character should be 20/20, not 20/40.)\n"""
        )
        current_level = int(input("Enter the corresponding number: "))

        print("I want my character to be: ")
        print("1> Level 20")
        print("2> Level 40")
        print("3> Level 50")
        print("4> Level 60")
        print("5> Level 70")
        print("6> Level 80")
        print("7> Level 90")
        required_level = int(input("\nEnter the corresponding number: "))
        if required_level < current_level:
            print(
                "Your required level cannot be lower than your current level. Exiting."
            )
        else:
            start_level = [1, 20, 40, 50, 60, 70, 80]
            end_level = [20, 40, 50, 60, 70, 80, 90]
            print(
                "\nMaterials required to level a character from "
                + str(start_level[current_level - 1])
                + " to "
                + str(end_level[required_level - 1])
                + ":\n"
            )
            self.find_total_cost_of_levels(current_level, required_level)


class MainMenu:
    def display_option_list(self):
        option = int(
            input(
                """\nEnter what you want to do with the database:
1. Figure out talent level resource requirements.
2. Figure out how much mora you need for some EXP quantity.
3. Figure out character level + ascension resource requirements.
4. Convert uncommon, rare and epic EXP books' EXP values to values relative to epic EXP books. 
5. Exit.

Enter the corresponding number: """
            )
        )
        calculation_functions = BasicCalculationFunctions()
        talent_cost_calculator = TalentCostCalculator()
        leveling_cost_calculator = LevelingCostCalculator()
        if option == 1:
            talent_cost_calculator.run_talent_material_calculator()
        elif option == 2:
            calculation_functions.mora_for_exp_calculator()
        elif option == 3:
            leveling_cost_calculator.level_resource_calculator()
        elif option == 4:
            calculation_functions.exp_book_aggregator()
        elif option == 5:
            exit("Thank you for using GI-DB!")
        else:
            print(
                "Invalid option, please select an option between 1 and 5. You selected",
                option,
            )

def main():
    newMenu = MainMenu()
    while True:
        newMenu.display_option_list()

if __name__ == "__main__":
    newMenu = MainMenu()
    while True:
        newMenu.display_option_list()
