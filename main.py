import pandas
from colored import fore, style


def talent_determine(
    initial_level, final_level, initial_dataframe, cumulative_material_dictionary
):
    # Always summate from "initialLevel-1" to "finalLevel-1"
    final_dataframe = initial_dataframe.iloc[initial_level - 1 : final_level - 1].sum()
    material_dictionary = final_dataframe.to_dict()
    for key, value in material_dictionary.items():
        cumulative_material_dictionary[key] += value


def determine_total_costs(
    initial_talent_values,
    final_talent_values,
    initial_dataframe,
    cumulative_material_dictionary,
):
    talent_determine(
        initial_talent_values[0],
        final_talent_values[0],
        initial_dataframe,
        cumulative_material_dictionary,
    )
    talent_determine(
        initial_talent_values[1],
        final_talent_values[1],
        initial_dataframe,
        cumulative_material_dictionary,
    )
    talent_determine(
        initial_talent_values[2],
        final_talent_values[2],
        initial_dataframe,
        cumulative_material_dictionary,
    )


def talent_material_calculator():
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
    cumulative_material_dictionary = dict(zip(materials, quantities))
    initial_dataframe = pandas.read_csv("talent_material_cost.csv")

    print(fore.GREEN_1 + "My character has current talent levels:")
    aa_initial = int(input(fore.LIGHT_YELLOW + "Auto-attack talent: "))
    e_initial = int(input(fore.LIGHT_YELLOW + "Elemental skill talent: "))
    q_initial = int(input(fore.LIGHT_YELLOW + "Elemental burst talent: "))
    initial_talent_values = [aa_initial, e_initial, q_initial]

    print(fore.GREEN_1 + "\nI need talent levels:")
    aa_final = int(input(fore.LIGHT_YELLOW + "Auto-attack talent: "))
    e_final = int(input(fore.LIGHT_YELLOW + "Elemental skill talent: "))
    q_final = int(input(fore.LIGHT_YELLOW + "Elemental burst talent: "))
    final_talent_values = [aa_final, e_final, q_final]
    print(fore.GREEN_1 + "\nThus, I need:")

    determine_total_costs(
        initial_talent_values,
        final_talent_values,
        initial_dataframe,
        cumulative_material_dictionary,
    )

    for key, value in cumulative_material_dictionary.items():
        if value != 0:
            print(
                fore.LIGHT_MAGENTA
                + "Total "
                + key
                + " needed: "
                + fore.GREEN
                + str(int(value))
                + fore.WHITE
            )


def mora_for_exp_calculator():
    print(fore.GREEN_1 + "I have the following EXP book quantities: ")
    uncommon_exp_books = int(input(fore.LIGHT_GREEN + "Uncommon books: "))
    rare_exp_books = int(input(fore.LIGHT_BLUE + "Rare books: "))
    epic_exp_books = int(input(fore.MAGENTA + "Epic books: "))
    total_mora_required = (
        200 * uncommon_exp_books + 1000 * rare_exp_books + 4000 * epic_exp_books
    )
    print(
        fore.LIGHT_YELLOW
        + "Thus, I need "
        + str(total_mora_required)
        + " mora"
        + fore.WHITE
    )


def find_total_cost_of_levels(current_level, required_level, initial_dataframe):
    # Index start corresponds to (current_level-1)th value. Index end corresponds to this too.
    final_dataframe = initial_dataframe.iloc[current_level - 1 : required_level].sum()
    dataframe_dict = final_dataframe.to_dict()
    for key, value in dataframe_dict.items():
        if value != 0:
            if key != "EXP needed":
                print(fore.LIGHT_MAGENTA + key + ":" + fore.GREEN + str(value))
            else:
                final_exp_required = round(value / 20000, 2)
                print(
                    fore.LIGHT_MAGENTA
                    + "EXP books needed in terms of epic EXP books: "
                    + fore.GREEN
                    + str(final_exp_required)
                    + fore.WHITE
                )


def level_resource_calculator():
    initial_dataframe = pandas.read_csv("character_levelup_ascend_cost.csv")
    print(fore.GREEN_1 + "My character is currently at: ")
    print(fore.LIGHT_YELLOW + "1> Level 1")
    print(fore.LIGHT_YELLOW + "2> Level 20")
    print(fore.LIGHT_YELLOW + "3> Level 40")
    print(fore.LIGHT_YELLOW + "4> Level 50")
    print(fore.LIGHT_YELLOW + "5> Level 60")
    print(fore.LIGHT_YELLOW + "6> Level 70")
    print(fore.LIGHT_YELLOW + "7> Level 80")
    print(
        fore.YELLOW_1
        + """(We are assuming your character hasn't been ascended at that level. 
        If you select 20, your character should be 20/20, not 20/40.)"""
    )
    current_level = int(input(fore.GREEN + "Enter the corresponding number: "))

    print(fore.GREEN_1 + "I want my character to be: ")
    print(fore.LIGHT_YELLOW + "1> Level 20")
    print(fore.LIGHT_YELLOW + "2> Level 40")
    print(fore.LIGHT_YELLOW + "3> Level 50")
    print(fore.LIGHT_YELLOW + "4> Level 60")
    print(fore.LIGHT_YELLOW + "5> Level 70")
    print(fore.LIGHT_YELLOW + "6> Level 80")
    print(fore.LIGHT_YELLOW + "7> Level 90")
    required_level = int(input(fore.GREEN + "Enter the corresponding number: "))
    if required_level < current_level:
        print(
            fore.RED
            + "Your required level cannot be lower than your current level. Exiting."
        )
    else:
        find_total_cost_of_levels(current_level, required_level, initial_dataframe)


def exp_book_aggregator():
    print(fore.GREEN_1 + "I have the following EXP book quantities: ")
    uncommon_exp_books = int(input(fore.LIGHT_GREEN + "Uncommon books: "))
    rare_exp_books = int(input(fore.LIGHT_BLUE + "Rare books: "))
    epic_exp_books = int(input(fore.MAGENTA + "Epic books: "))
    epic_book_aggregate = epic_exp_books + rare_exp_books / 4 + uncommon_exp_books / 20
    print(
        fore.LIGHT_MAGENTA
        + "\nThis equates to: "
        + fore.GREEN
        + str(epic_book_aggregate)
        + " hero's wit"
        + fore.WHITE
    )


def main():
    option = int(
        input(
            fore.LIGHT_MAGENTA
            + style.BOLD
            + """\tEnter what you want to do with the database:
            1. Figure out talent level resource requirements.
            2. Figure out how much mora you need for some EXP quantity.
            3. Figure out character level+ascension resource requirements.
            4. Convert uncommon, rare and epic EXP books' EXP values to values relative to epic EXP books. 
            5. Exit.\n"""
            + style.RESET
        )
    )
    if option == 1:
        talent_material_calculator()
    if option == 2:
        mora_for_exp_calculator()
    if option == 3:
        level_resource_calculator()
    if option == 4:
        exp_book_aggregator()


if __name__ == "__main__":
    main()
