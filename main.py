import pandas
from colorama import Fore, init

init()


class TalentCostCalculator:
    def __init__(self):
        self.initial_dataframe = pandas.read_csv("talent_material_cost.csv")
        materials = [
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
        quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cumulative_material_dictionary = dict(zip(materials, quantities))
        # * cumulative_material_dictionary holds the current sum of all resources
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
    #        cumulative_material_dictionary.

    def aggregate_cumulative_cost(self, initial_level, final_level):
        # Always summate from "initialLevel-1" to "finalLevel-1"th index in
        # the dataframe.

        aggregated_dataframe = self.initial_dataframe.iloc[
            initial_level - 1 : final_level - 1
        ].sum()
        material_dictionary = aggregated_dataframe.to_dict()
        for key, value in material_dictionary.items():
            # * Add resources to the cumulative dictionary
            #   We want to find out the requirements for each talent
            #   and add them together, then display them.
            # * cumulative_material_dictionary holds these sum values
            # * and updates after each iteration of this function.

            self.cumulative_material_dictionary[key] += value

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
        for key, value in self.cumulative_material_dictionary.items():
            if value != 0:
                # * If something is not required, don't display it.
                print(
                    Fore.MAGENTA
                    + "Total "
                    + key
                    + " needed: "
                    + Fore.GREEN
                    + str(int(value))
                    + Fore.WHITE
                )

    def run_talent_material_calculator(self):
        print(Fore.GREEN + "\nMy character has current talent levels:")

        aa_initial = int(input(Fore.LIGHTYELLOW_EX + "Auto-attack talent: "))
        e_initial = int(input(Fore.LIGHTYELLOW_EX + "Elemental skill talent: "))
        q_initial = int(input(Fore.LIGHTYELLOW_EX + "Elemental burst talent: "))
        initial_talent_values = [aa_initial, e_initial, q_initial]

        print(Fore.GREEN + "\nI need talent levels:")
        aa_final = int(input(Fore.LIGHTYELLOW_EX + "Auto-attack talent: "))
        e_final = int(input(Fore.LIGHTYELLOW_EX + "Elemental skill talent: "))
        q_final = int(input(Fore.LIGHTYELLOW_EX + "Elemental burst talent: "))
        final_talent_values = [aa_final, e_final, q_final]
        print(Fore.LIGHTCYAN_EX + "\nThus, I need:")

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
        print(Fore.GREEN + "\nI have the following EXP book quantities: ")
        uncommon_exp_books = int(input(Fore.GREEN + "Uncommon books: "))
        rare_exp_books = int(input(Fore.CYAN + "Rare books: "))
        epic_exp_books = int(input(Fore.MAGENTA + "Epic books: "))
        # * Cost per uncommon book is 200 mora.
        # * Cost per rare book is 1000 mora.
        # * Cost per epic book is 4000 mora.
        total_mora_required = (
            200 * uncommon_exp_books + 1000 * rare_exp_books + 4000 * epic_exp_books
        )
        print(
            Fore.LIGHTYELLOW_EX
            + "\nThus, I need "
            + str(total_mora_required)
            + " mora"
            + Fore.WHITE
        )

    def exp_book_aggregator(self):
        print(Fore.GREEN + "\nI have the following EXP book quantities: ")
        uncommon_exp_books = int(input(Fore.BLUE + "Uncommon books: "))
        rare_exp_books = int(input(Fore.CYAN + "Rare books: "))
        epic_exp_books = int(input(Fore.MAGENTA + "Epic books: "))
        epic_book_aggregate = (
            epic_exp_books + rare_exp_books / 4 + uncommon_exp_books / 20
        )
        print(
            Fore.MAGENTA
            + "\nThis equates to: "
            + Fore.GREEN
            + str(epic_book_aggregate)
            + " hero's wit"
            + Fore.WHITE
        )


class LevelingCostCalculator:
    def __init__(self):
        self.initial_dataframe = pandas.read_csv("character_levelup_ascend_cost.csv")

    # * Two methods:
    # *     1. level_resource_calculator
    #         Handles UI display and sends the current and required level
    #         values to find_total_cost_of_levels
    # *     2. find_total_cost_of_levels
    #          Aggregates total resources needed and displays output UI.

    def find_total_cost_of_levels(self, current_level, required_level):
        # Index start corresponds to (current_level-1)th value. Index end corresponds to this too.

        final_dataframe = self.initial_dataframe.iloc[
            current_level - 1 : required_level
        ].sum()
        dataframe_dict = final_dataframe.to_dict()
        for key, value in dataframe_dict.items():
            if value != 0:
                # * We need a separate piece of logic when displaying
                # * the EXP needed section.
                if key != "EXP needed":
                    print(Fore.MAGENTA + key + ":" + Fore.GREEN + str(value))
                else:
                    # * One epic book is 20000 EXP, we round it to
                    # * double precision.
                    final_exp_required = round(value / 20000, 2)
                    print(
                        Fore.MAGENTA
                        + "EXP books needed in terms of epic EXP books: "
                        + Fore.GREEN
                        + str(final_exp_required)
                        + Fore.WHITE
                    )

    def level_resource_calculator(self):
        print(Fore.GREEN + "\nMy character is currently at: ")
        print(Fore.LIGHTYELLOW_EX + "1> Level 1")
        print(Fore.LIGHTYELLOW_EX + "2> Level 20")
        print(Fore.LIGHTYELLOW_EX + "3> Level 40")
        print(Fore.LIGHTYELLOW_EX + "4> Level 50")
        print(Fore.LIGHTYELLOW_EX + "5> Level 60")
        print(Fore.LIGHTYELLOW_EX + "6> Level 70")
        print(Fore.LIGHTYELLOW_EX + "7> Level 80")
        print(
            Fore.LIGHTYELLOW_EX
            + """\n(We are assuming your character hasn't been ascended at that level. 
If you select 20, your character should be 20/20, not 20/40.)\n"""
        )
        current_level = int(input(Fore.GREEN + "Enter the corresponding number: "))

        print(Fore.GREEN + "I want my character to be: ")
        print(Fore.LIGHTYELLOW_EX + "1> Level 20")
        print(Fore.LIGHTYELLOW_EX + "2> Level 40")
        print(Fore.LIGHTYELLOW_EX + "3> Level 50")
        print(Fore.LIGHTYELLOW_EX + "4> Level 60")
        print(Fore.LIGHTYELLOW_EX + "5> Level 70")
        print(Fore.LIGHTYELLOW_EX + "6> Level 80")
        print(Fore.LIGHTYELLOW_EX + "7> Level 90")
        required_level = int(input(Fore.GREEN + "\nEnter the corresponding number: "))
        if required_level < current_level:
            print(
                Fore.RED
                + "Your required level cannot be lower than your current level. Exiting."
            )
        else:
            start_level = [1, 20, 40, 50, 60, 70, 80]
            end_level = [20, 40, 50, 60, 70, 80, 90]
            print(
                Fore.LIGHTCYAN_EX
                + "\nMaterials required to level a character from "
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
                Fore.LIGHTBLUE_EX
                + """\nEnter what you want to do with the database:
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
            exit(Fore.LIGHTGREEN_EX + "Thank you for using GI-DB!")
        else:
            print(
                "Invalid option, please select an option between 1 and 5. You selected",
                option,
            )


if __name__ == "__main__":
    newMenu = MainMenu()
    while True:
        newMenu.display_option_list()
