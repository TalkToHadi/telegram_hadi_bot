import telebot
from telebot import types

TOKEN = '239519305:AAH-1nJiWwqyigWQvg-qxZKpo6nnKpGh2sU' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)


"""
class Critical(State):
    message = (
        "Please seek help inmediatly"
    )

class NoHelp(State):
    message = (
        "Sorry, I can't help you with this"
    )

class Burocrazy(State):
    message = (
        "Sorry, I can't help you with this but I know who can!"
        "You should check Burocrazy, those guys are cool"
    )

class Oops(State):
    message = (
        "Oops, I'm sorry to hear that"
        "Talk to me later if you want"
    )

class Introduce(State):
    message = (
        "Let me introduce you to my friend Hans!"
    )

class FeelUp(State):
    


class HotLine(State):
    message = (
        "You need inmediate help!"
        "Call the emergency hotline"
        "http://www.suicide.org/hotlines/international/germany-suicide-hotlines.html"
        "http://www.frauenhauskoordinierung.de/english-summary.html"
    )


class FunnyVideos(State):
    message = (
        "Check this web page!"
        "https://www.youtube.com/results?search_query=funny"
    )

class HeadSpace(State):
    message = (
        "Try an app like HeadSpace to learn how to meditate"
    )


class Cinema(State):
    message = (
        "Here you can find cinemas around you!"
        "https://www.google.com/maps?q=cinema"
    )


class Sports(State):
    message = (
        "Here you can find sports events (and more)!"
        "https://www.sportsworld.co.uk/events"
    )


class Bored3(State):
    options = {
        "Yeah, I'd love to!": Cinema,
        "Not right now": Sports,
    }
    message = (
        "Do you prefer to go to cinema?"
    )


class Bored2(State):
    options = {
        "Yes, of course!": FunnyVideos,
        "Not really": Bored3,
    }
    message = (
        "What about watching some funny videos?"
    )

class MeetUp(State):
    message = (
    "Check MeetUp! You'll find something you like for sure"
    "http://www.meetup.com/"
    )


class Bored(State):
    options = {
        "Yeah, sure!": MeetUp,
        "Not right now": Bored2,
    }

    message = (
        "Would you like to meet people with your same interests?"
    )


class Tired(State):
    options = {
        "I'm mentally exhausted": HeadSpace,
        # "I feel my body has no energy": Sleeping,
    }
    message = (
        "Why are you tired?"
    )


class Ill(State):
    message = (
        "Look this awesome link to german national health system"
    )



class TedTalk(State):
    message = (
        "Watch this inpirational talks on how to deal with feeling lonely"
        "http://www.keepinspiring.me/25-creative-and-surprising-things-to-do-when-you-feel-lonely/"
    )


class GoogleMaps(State):
    message = (
        "Try searching at GoogleMaps :)"
        "https://www.google.com/maps"
    )

class HomeSick(State):
    options = {
        "Some food would be great": GoogleMaps,
        "I would like to find cool things to do around": MeetUp,
    }
    message = (
        "It's hard to be away from home"
    )

class Lonely(State):
    options = {
        "Yeah, I would like talk with someone": Introduce,
        "It would be cool to join some activity": MeetUp,
        "Not right now": TedTalk,
    }

    message = (
        "Would you like to meet new people?"
    )

class Lost(State):
    options = {
        "I want to go somewhere": GoogleMaps,
        "I need help with my paperwork": Burocrazy,
        "Someone to talk to": Lonely,
    }

    message = (
        "What are you looking for?"
    )


class FeelDown(State):
    options = {
        "I'm bored": Bored,
        # "I'm sad": Sad,
        "I'm stressed with paperwork": Burocrazy,
        "I'm lost": Lost,
        "I'm tired": Tired,
        "I miss my country": HomeSick,
        "I feel lonely": Lonely,
        # "I'm angry": Angry,
        "I'm feeling ill": Ill,
        "None of that": NoHelp,
    }

    message = (
        "So sorry to hear that"
        "Whats wrong?"
    )
"""

STATES = {
    'Initial': {
        'message': (
            "Hi there. My name is Hadi, I'm here for you. What's up?"
        )
        'options': [
            "I'm feeling up! :D",
            "Not feelin great today :(",
        ]
    },
    "I'm feeling up! :D": {
        'message': (
            "Great!"
            "Would you like to cheer someone up?"
        ),
        'options': [
            "Yeah!",
            "Maybe on another time",
        ]
    },
}

def markup(state):
    markup = types.ReplyKeyboardMarkup()
    for option in state['options']:
        markup.row(option)
    return markup


@bot.message_handler(commands=['start', 'help'])
def send_welcome(answer):
    initial = STATES['Initial']
    bot.send_message(
        answer.chat.id,
        initial['message'],
        reply_markup=markup(initial))

@bot.message_handler(func=lambda m: True)
def handle_message(answer):
    chat_id = answer.chat.id
    next_state = STATES[answer.text]
    bot.send_message(
        chat_id,
        next_state['message'],
        reply_markup=markup(next_state))


bot.polling()
