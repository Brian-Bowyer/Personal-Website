from collections import namedtuple

# namedtuple defaults apply to the last slice
Project = namedtuple('Project', 
                    ['filename', 'title', 'description', 'github_link', 'live_link'],
                    defaults=[None, None])
PROJECTS = [
    #Project('bagofnouns.jpg', 
    #        "Bag of Nouns", 
    #        "Web app to play the game Bag of Nouns (also sometimes called Monikers)"),
    #Project('bta.jpg', 
    #        "Bubble Turtle Adventure", 
    #        "Sidescrolling video game"),
    Project('blorb.png', 
            "Blorb", 
            "Procedurally generated resource-collecting video game with infinite map",
            github_link='https://github.com/benthemonkey/Blorb',
            live_link=''),
    #Project('story_scraper.jpg', 
    #        "Story Scraper", 
    #        "Computational linguistics class project which scraped large amounts of fanfiction to produce linguistic corpus"),
    Project('self.jpg', 
            "This Very Website", 
            "This website! The one that you are reading right now.",
            github_link='https://github.com/Brian-Bowyer/Personal-Website')
]