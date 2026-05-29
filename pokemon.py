#Raymond Chen and Dominic Brogni
#pokemon.py
#Our First Pokemon Game Ever

#Init
import random

#Functions
def bulbasaur(): #Bulbasaur ASCII art
    print((r"                                          /\n"))
    print((r"                       _,.------....___,.' ',.-.\n"))
    print((r"                    ,-'          _,.--\"        |\n"))
    print((r"                  ,'         _.-'              .\n"))
    print((r"                 /   ,     ,'                   `\n"))
    print((r"                .   /     /                     ``.\n"))
    print((r"                |  |     .                       \\.\\\n"))
    print((r"      ____      |___._.  |       __               \\ `.\n"))
    print((r"    .'    `---\"\"       ``\"-.--\"'`  \\               .  \\\n"))
    print((r"   .  ,            __               `              |   .\n"))
    print((r"   `,'         ,-\"'  .               \\             |    L\n"))
    print((r"  ,'          '    _.'                -._          /    |\n"))
    print((r" ,`-.    ,\".   `--'                      >.      ,'     |\n"))
    print((r". .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'\n"))
    print((r"||:, .           ,'  ;  /  / \\ `        `.    .      .'/\n"))
    print((r"j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /\n"))
    print(("/ L:_  |                 .  \"' :_;                `.'.'\n"))
    print((".    \"\"'                  \"\"\"\"\"'                    V\n"))
    print((r"`.                                 .    `.   _,..  `\n"))
    print((r"  `,_   .    .                _,-'/    .. `,'   __  `\n"))
    print((r"   ) \\`._        ___....----\"'  ,'   .'  \\ |   '  \\  .\n"))
    print((r"  /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |\n"))
    print((r" .   _  `\"\"'--.._____..--\"   ,             '         |\n"))
    print((r" | .\" `. `-.                /-.           /          ,\n"))
    print((r" | `._.'    `,_            ;  /         ,'          .\n"))
    print((r".'          /| `-.        . ,'         ,           ,\n"))
    print((r"'-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'\n"))
    print((r"`\"^--'..'   '-`-^-'\"--    `-^-'`.''\"\"\"\"\"`.,^.`.--' mh\n"))
    print(("\n"))
    print(("\n"))
def ivysaur(): #Ivysaur ASCII art
    print((r"                              ,'\"`.,./.\n"))
    print((r"                            ,'        Y',\"..\n"))
    print((r"                          ,'           \\  | \\\n"))
    print((r"                         /              . |  `\n"))
    print((r"                        /               | |   \\\n"))
    print((r"           __          .                | |    .\n"))
    print((r"      _   \\  `. ---.   |                | j    |\n"))
    print((r"     / `-._\\   `Y   \\  |                |.     |\n"))
    print((r"    _`.    ``    \\   \\ |..              '      |,-'\"\"7,....\n"))
    print((r"    l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.\n"))
    print((r"    `-..     `-.  : :     |/ `   ' \"\\,' | _  /          '-'    /___\n"))
    print((r"     \\\"\"' __.,.-`.: :        /   /._    l'.,'\n"))
    print((r"      `--,   _.-' `\".           /__ `'-.' '         .\n"))
    print((r"      ,---..._,.--\"\"\"\"\"\"\"--.__..----,-.'   .  /    .'   ,.--\n"))
    print((r"      |                          ,':| /    | /     ;.,-'--      ,.-\n"))
    print((r"      |     .---.              .'  :|'     |/ ,.-='\"-.`\"`' _   -.'\n"))
    print((r"      /    \\    /               `. :|--.  _L,\"---.._        \"----'\n"))
    print((r"    ,' `.   \\ ,'           _,     `''   ``.-'       `-  -..___,'\n"))
    print((r"   . ,.  .   `   __     .-'  _.-           `.     .__    \\\n"))
    print((r"   |. |`        \"  ;   !   ,.  |             `.    `.`'---'\n"))
    print((r"   ,| |C\\       ` /    | ,' |(]|            -. |-..--`\n"))
    print((r"  /  \"'--'       '      /___|__]        `.  `- |`.\n"))
    print((r" .       ,'                   ,   /       .    `. \\\n"))
    print((r"   \\                      .,-'  ,'         .     `-.\n"))
    print((r"    x---..`.  -'  __..--'\"/\"\"\"\"\"  ,-.      |   |   |\n"))
    print((r"   / \\--._'-.,.--'     _`-    _. ' /       |     -.|\n"))
    print((r"  ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|\n"))
    print((r" .  _,'         '\"-----\"\"      |    `   | /  ,'    ;\n"))
    print((r" |-'  .-.    `._               |     `._// ,'     /\n"))
    print((r"_|    `-'   _,' \"`--.._________|        `,'    _ /.\n"))
    print(("//\\   ,-._.'\"/\\__,.   _,\"     /_\\__/`. /'.-.'.-/_,`-' mh\n"))
    print(("`-\"`\"' v'    `\"  `-`-\"              `-'`-`  `'\n"))
def venusaur(): #Venusaur ASCII art
    print((r"                          _._       _,._\n"))
    print((r"                       _.'   `. ' .'   _`.\n"))
    print((r"               ,\"\"\"/`\"\"-.-.,/. ` V'\\-,`.,--/\"\"\".\"-..\n"))
    print((r"             ,'    `...,' . ,\\-----._|     `.   /   \\\n"))
    print((r"            `.            .`  -'`\"\" .._   :> `-'   `.\n"))
    print((r"           ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L\n"))
    print((r"          .    \\_ -'   `-'     ..      `.-' `.`-.'_ .|\n"))
    print((r"          |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.\n"))
    print((r"          `.,' ,  |   |  `.  /'/,,.\\/  |    \\|   |\n"))
    print((r"               `  `---'    `j   .   \\  .     '   j\n"))
    print((r"             ,__`\"        ,'|`'\\_/`.'\\'        |\\-'-, _,.\n"))
    print((r"      .--...`-. `-`. /    '- ..      _,    /\\ ,' .--\"'  ,'\".\n"))
    print((r"    _'-\"\"-    --  _`'-.../ __ '.'`-^,_`-\"\"\"\"---....__  ' _,-`\n"))
    print((r"  _.----`  _..--.'        |  \"`-..-\" __|'\"'         .\"\"-. \"\"'--.._\n"))
    print((r" /        '    /     ,  _.+-.'  ||._'   \"\"\"\". .          `     .__\\\n"))
    print((r"`---    /        /  / j'       _/|..`  -. `-`\\ \\   \\  \\   `.  \\ `-..\n"))
    print((",\" _.-' /    /` ./  /`_|_,-\"   ','|       `. | -'`._,   L  \\ .  `.   |\n"))
    print(("`\"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .\n"))
    print((r"  /  '| /.,/   \\--.._ `-,' ,          .  '`.'  __,., '  ''``._ \\ \\`,'\n"))
    print((r" /_,'---  ,     \\`._,-` \\ //  / . \\    `._,  -`,  / / _   |   `-L -\n"))
    print((r"  /       `.     ,  ..._ ' `_/ '| |\\ `._'       '-.'   `.,'     |\n"))
    print((r" '         /    /  ..   `.  `./ | ; `.'    ,\"\" ,.  `.    \\      |\n"))
    print((r"  `.     ,'   ,'   | |\\  |       \"        |  ,'\\ |   \\    `    ,L\n"))
    print((r"  /|`.  /    '     | `-| '                  /`-' |    L    `._/  \\\n"))
    print((r" / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`\n"))
    print((r"'-\"\"-'_|    `. `.__,._____     .    _,        ____ ,-  j     \".-'\"'\n"))
    print((r"       \\      `-.  \\/.    `\"--.._    _,.---'\"\"\\/  \"_,.'     /-'\n"))
    print((r"        )        `-._ '-.        `--\"      _.-'.-\"\"        `.\n"))
    print((r"       ./            `,. `\".._________...\"\"_.-\"`.          _j\n"))
    print((r"      /_\\.__,\"\".   ,.'  \"`-...________.---\"     .\".   ,.  / \\\n"))
    print((r"             \\_/\"\"\"-'                           `-'--(_,`\"`-` mh\n"))
def day_counter(): #Day Counter
    global day
    day = day + 1
def train(): #Training option
    global day
    global level
    level = level + 1
    day_counter()
def rest(): #Resting option
    global day
    day_counter()
def info_screen(): #Information screen
    evolve()
    if mood >= 75:
        print("Mood: Happy")
    elif mood <= 25:
        print("Mood: Sad")
    else:
        print("Mood: Neutral")
    print(f"Day {day}")
def evolve(): #Evolution function
        if level < 16:
            bulbasaur()
            print("Pokemon: Bulbasaur")
            name == "Bulbasaur"
        elif level < 32:
            ivysaur()
            print("Pokemon: Ivysaur")
            name == "Ivysaur"
        else:
            venusaur()
            print("Pokemon: Venusaur")
            name == "Venusaur"
def gym(): #Win/Loss function for gym battles
    global level
    global day
    global mood
    if mood >= 75:
        chance = int(random.randint(5,10 + level))
    elif mood <= 25:
        chance = int(random.randint(1,10 + level))
    else:
        chance = int(random.randint(3,10 + level))
    if chance >= 7:
        level = level + 2
        day = day + 1
        print("You Win")
    else:
        day = day + 1
        print("You Lose")
def final(): #Win/Loss function for final battle
    global level
    global day
    global mood
    if mood >= 75:
        player = random.randint(16, level + 16)
        boss = random.randint(32,64)
    elif mood <= 25:
        player = random.randint(1,level)
        boss = random.randint(32,64)
    else:
        player = random.randint(8, level + 8)
        boss = random.randint(32,64)
    if player >= boss:
        print("Good Ending: Pokemon is Saved!")
        print("You Win!")
        print("Thank you for playing my game!")
    elif player < boss:
        print("Bad Ending: You Die")
        print("You Lose!")
        print("Thank you for playing my game!")
def mood_effect():
    global mood
    if play == "train":
        tiredness = random.randint(1,2)
        if tiredness == 1:
            mood = mood - 1
        else:
            mood = mood
    elif play == "rest":
        mood = mood + 1

#Main
mood = 50 #Player mood
day = 1 #Day
level = 1 #Level
while True:
    play = input("Do you want to train, rest, gym battle, boss battle, see info, save game, or quit? ")
    if play == "train":
        train()
        mood_effect()
    elif play == "rest":
        mood_effect()
    elif play == "gym battle":
        gym()
    elif play == "boss battle":
        final()
        break
    elif play == "quit":
        break
    elif play == "see info":
        info_screen()
    elif play == "save game":
        save_game()
    else:
        continue
