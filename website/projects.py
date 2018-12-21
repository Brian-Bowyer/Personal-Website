from collections import namedtuple

# namedtuple defaults apply to the last slice
Project = namedtuple('Project', 
                    ['filename', 'title', 'description', 'github_link', 'live_link'],
                    defaults=[None, None])
PROJECTS = [
    #Project('bagofnouns.jpg', 
    #        "Bag of Nouns", 
    #        "Web app to play the game Bag of Nouns (also sometimes called Monikers)"),
    Project(filename='discord_bot.jpg', 
            title="Dice Roller Bot", 
            description="Discord bot written in Python to roll dice according to VtR rules.",
            github_link='https://github.com/Brian-Bowyer/Discord-VTR-Dice'),
    Project(filename='dice_chart.png', 
            title="Dice System Tester", 
            description="Python program that used the Numpy/Scipy/Matplotlib stack to calculate the odds of certain things happening in a certain tabletop RPG system.\
             (For the curious: the system was Vampire the Requiem, and the certain things were the odds of getting a given number of successes on a roll I expected my character to make very often.)",
            ),
    Project(filename='bta.png', 
            title="Bubble Turtle Adventure", 
            description="Unity3D game written in C# about a turtle fighting bees in a post-apocalyptic wasteland.",
            github_link='https://github.com/Cammac7/Game-Design-Project'),
    Project('blorb.png', 
            "Blorb", 
            "Procedurally generated resource-collecting video game with infinite map",
            github_link='https://github.com/benthemonkey/Blorb'),
    Project('self.jpg', 
            "This Very Website", 
            "This website! The one that you are reading right now.",
            github_link='https://github.com/Brian-Bowyer/Personal-Website')
]