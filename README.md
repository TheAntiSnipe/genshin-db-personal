# genshin-db-personal

Just a personal database for Genshin Impact.
Currently, we have the following features:

1. A talent material calculator. Tells you how many materials you need to get a three-set of talents from level x to level y. ![Example](https://media.discordapp.net/attachments/780657122589278239/859620593095933952/exper1.png)
2. A mora calculator. Given the number of books of each type, calculates the total mora needed to blow them all on a character. ![Example](https://media.discordapp.net/attachments/780657122589278239/859620596639072256/exper2.png)
3. A comprehensive levelup calculator. Tells you how much mora, boss mats, local specialities, and talent books (in hero's wit aggregation form -- It tells you how many Hero's Wit you would need, in fractions) ![Example](https://cdn.discordapp.com/attachments/780657122589278239/859620597931311134/exper3.png)
4. A calculator that converts multiple EXP book types into hero's wit aggregation form - Standardization for easy calculation work.![Example](https://cdn.discordapp.com/attachments/780657122589278239/859620598124511253/exper4.png)

This is my personal Swiss-army knife of tools that I use when I boost characters from a certain level to another.

Only dependency is `colorama`.

You can also choose to use `colorless_main.py` in case your command line doesn't support colored output.

### Running normally in Python
1. Navigate to src/
2. Choose to run either colorless_main.py or main.py. If you're running main.py, you'll need colorama installed. To do this, `pip install colorama`.
3. Enjoy!

### Getting the snap file

I've also made snap installations for both the colorless and colored distributions! The colored one is up in the snap store: https://snapcraft.io/genshin-resource-calc

If you wish to set up the colored distribution on your own,

1. Make sure snapcraft is installed.
2. Navigate to the project directory, and type in `snapcraft --use-lxd`
3. After the install process is done, it will generate a `.snap` file with its name starting with `genshin-resource-calc_`. You can run this snap locally with `sudo snap install <name from end of step 2> --dangerous`. The dangerous keyword only exists because this is a local install!
4. You should be able to run the code on your command line with `genshin-resource-calc`!

Setting up an uncolored distribution is also easy.

1. Go to setup.py and manage the comments as mentioned in lines 14-15 and 19-20.
2. Follow the same process as stated above! This generates a snap without the pretty colors.

 Have fun!
