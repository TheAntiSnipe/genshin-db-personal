# genshin-db-personal

Just a WIP of a personal database for Genshin Impact.
Currently, we have the following features:

1. A talent material calculator. Uses `talent_material_cost.csv` as an input file and tells you how many materials you need to get a three-set of talents from level x to level y. ![Example](https://media.discordapp.net/attachments/780657122589278239/859620593095933952/exper1.png)
2. A mora calculator. Given the number of books of each type, calculates the total mora needed to blow them all on a character. ![Example](https://media.discordapp.net/attachments/780657122589278239/859620596639072256/exper2.png)
3. A comprehensive levelup calculator. Uses `character_levelup_ascend_cost.csv` as an input file and tells you how much mora, boss mats, local specialities, and talent books (in hero's wit aggregation form -- It tells you how many Hero's Wit you would need, in fractions) ![Example](https://cdn.discordapp.com/attachments/780657122589278239/859620597931311134/exper3.png)
4. A calculator that converts multiple EXP book types into hero's wit aggregation form - Standardization for easy calculation work.![Example](https://cdn.discordapp.com/attachments/780657122589278239/859620598124511253/exper4.png)

This is my personal Swiss-army knife of tools that I use when I boost characters from a certain level to another.

Only dependencies are `pandas` and `colorama`.

Have fun!
