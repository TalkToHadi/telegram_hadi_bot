import string
from state import State

class Critical(State):
    message = (
        "Please seek help inmediatly",
    )

class NoHelp(State):
    message = (
        "Sorry, I can't help you with this",
    )
        
class Burocrazy(State):
    message = (
        "Sorry, I can't help you with this but I know who can!",
        "You should check Burocrazy, those guys are cool",
    )

class Initial(State):
    options = [
        "I'm feeling up! :D": FeelUp,
        "Not feelin great today :(": FeelDown,
    ]
    message = (
        "Hi there. My name is Hadi",
        "I'm here for you. What's up",
    )

class FeelUp(State):
    options = [
        "Yeah!": Introduce(),
        "Maybe on another time": Oops(),
    ]
    message = (
        "Great!",
        "Would you like to cheer someone up?",
    )

class FeelDown(State):
    options = [
        "I'm bored": Bored,
        "I'm sad": Sad,
        "I'm stressed with paperwork": Burocrazy,
        "I'm lost": Lost,
        "I'm tired": Tired,
        "I miss my country": HomeSick,
        "I feel lonely": Lonely,
        "I'm angry": Angry,
        "I'm feeling ill": Ill,
        "None of that": NoHelp,
    ]
    
    message = (
        "So sorry to hear that",
        "Whats wrong?",
    )

class HotLine(State):
    message = (
        "You need inmediate help!",
        "Call the emergency hotline",
        "http://www.suicide.org/hotlines/international/germany-suicide-hotlines.html",
        "http://www.frauenhauskoordinierung.de/english-summary.html",
    )

class Bored(State):
    options = [
        "Yeah, sure!": MeetUp,
        "Not right now": Bored2,
    ]

    message = (
        "Would you like to meet people with your same interests?",
    )

class Bored2(State):
    options = [
        "Yes, of course!": FunnyVideos,
        "Not really": Bored3,
    ]
    message = (
        "What about watching some funny videos?",
    )

class Bored3(State):
    options = [
        "Yeah, I'd love to!": Cinema,
        "Not right now": Sports,
    ]
    message = (
        "Do you prefer to go to cinema?",
    )


class FunnyVideos(State):
    message = (
        "Check this web page!",
        "https://www.youtube.com/results?search_query=funny",
    )


class HeadSpace(State):
    message = (
        "Try an app like HeadSpace to learn how to meditate",
    )


class Cinema(State):
    message = (
        "Here you can find cinemas around you!",
        "https://www.google.com/maps?q=cinema",
    )


class Tired(State):
    options = [
        "I'm mentally exhausted": HeadSpace,
        "I feel my body has no energy": Sleeping,
    ]
    message = (
        "Why are you tired?",
    )

class Sports(State):
    message = (
        "Here you can find sports events (and more)!",
        "https://www.sportsworld.co.uk/events",
    )


class Lost(State):
    options = [
        "I want to go somewhere": GoogleMaps,
        "I need help with my paperwork": Burocrazy,
        "Someone to talk to": Lonely,
    ]

    message = (
        "What are you looking for?",
    )


class Ill(State):
    message = (
        "Look this awesome link to german national health system",
    )

class Lonely(State):
    options = [
        "Yeah, I would like talk with someone": Introduce,
        "It would be cool to join some activity": MeetUp,
        "Not right now": TedTalk,
    ]

    message = (
        "Would you like to meet new people?",
    )

class MeetUp(State):
    message = (
        "Check MeetUp! You'll find something you like for sure",
        "http://www.meetup.com/",
    )
        
class TedTalk(State):
    message = (
        "Watch this inpirational talks on how to deal with feeling lonely",
        "http://www.keepinspiring.me/25-creative-and-surprising-things-to-do-when-you-feel-lonely/",
    )


class Introduce(State):
    message = (
        "Let me introduce you to my friend Hans!",
    )

class GoogleMaps(State):
    message = (
        "Try searching at GoogleMaps :)",
        "https://www.google.com/maps",
    )

class HomeSick(State):
    options = [
        "Some food would be great": GoogleMaps,
        "I would like to find cool things to do around": MeetUp,
    ]
    message = (
        "It's hard to be away from home",
    )

class Oops(State):
    message = (
        "Oops, I'm sorry to hear that",
        "Talk to me later if you want",
    )


