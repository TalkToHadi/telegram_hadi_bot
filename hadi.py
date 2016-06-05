import telebot
from telebot import types


TOKEN = '228469213:AAEnb6laZGjxnkTQBbEhZuxdEjHFAqhznzc' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)

STATES = {
    'Initial': {
        'message': (
            "Hi there. My name is Hadi, I'm here for you. What's up?"
        ),
        'options': [
            "I'm feeling up! :D",
            "Not feeling great today :(",
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
    "Not feelin great today :(": {
        'message': ('Ooops'),
        'options': []
    },
    "I'm stressed with paperwork": {
        'message': (
            "Sorry, I can't help you with this but I know who can!"
            "You should check Burocrazy, those guys are cool"
        ),
        'options': [

        ]
    },
    "I need help with my paperwork": {
        'message': (
            "Sorry, I can't help you with this but I know who can!"
            "You should check Burocrazy, those guys are cool"
        ),
        'options': [

        ]
    },
    "None of that": {
        'message': (
            "Sorry, I can't help you with this"
        ),
        'options': [

        ]
    },
    "Maybe on another time": {
        'message': (
            "Oops, I'm sorry to hear that"
            "Talk to me later if you want"
        ),
        'options': [

        ]
    },
    "Yeah, I would like talk with someone": {
        'message': (
            "Let me introduce you to my friend Hans!"
        ),
        'options': [

        ]
    },
    "HotLine": {
        'message': (
            "You need inmediate help!"
            "Call the emergency hotline"
            "http://www.suicide.org/hotlines/international/germany-suicide-hotlines.html"
            "http://www.frauenhauskoordinierung.de/english-summary.html"
        ),
        'options': [

        ]
    },
    "Yes, of course!": {
        'message': (
            "Check this web page!"
            "https://www.youtube.com/results?search_query=funny"
        ),
        'options': [

        ]
    },
    "I'm mentally exhausted": {
        'message': (
            "Try an app like HeadSpace to learn how to meditate"
            "https://www.headspace.com/"
        ),
        'options': [

        ]
    },
    "Yeah, I'd love to!": {
        'message': (
            "Here you can find cinemas around you!"
            "https://www.google.com/maps?q=cinema"
        ),
        'options': [

        ]
    },
    "Not right now": {
        'message': (
            "Here you can find sports events (and more)!"
            "https://www.sportsworld.co.uk/events"
        ),
        'options': [

        ]
    },
    "Not really": {
        'message': (
            "Do you prefer to go to cinema?"
        ),
        'options': [
            "Yeah, I'd love to!",
            "Not right now",
        ]
    },
    "Not right now": {
        'message': (
            "What about watching some funny videos?"
        ),
        'options': [
            "Yes, of course!",
            "Not really",
        ]
    },
    "Yeah, sure!": {
        'message': (
            "Check MeetUp! You'll find something you like for sure"
            "http://www.meetup.com/"
        ),
        'options': [

        ]
    },
    "I would like to find cool things to do around": {
        'message': (
            "Check MeetUp! You'll find something you like for sure"
            "http://www.meetup.com/"
        ),
        'options': [

        ]
    },
    "It would be cool to join some activity": {
        'message': (
            "Check MeetUp! You'll find something you like for sure"
            "http://www.meetup.com/"
        ),
        'options': [

        ]
    },
    "I'm bored": {
        'message': (
            "Would you like to meet people with your same interests?"
        ),
        'options': [
            "Yeah, sure!",
            "Not right now",
        ]
    },
    "I'm tired": {
        'message': (
            "Why are you tired?"
        ),
        'options': [
            "I'm mentally exhausted",
        ]
    },
    "I'm feeling ill": {
        'message': (
            "Look this awesome link to german national health system"
            "http://www.howtogermany.com/pages/healthinsurance.html"
        ),
        'options': [

        ]
    },
    "Not right now": {
        'message': (
            "Watch this inpirational talks on how to deal with feeling lonely"
            "http://www.keepinspiring.me/25-creative-and-surprising-things-to-do-when-you-feel-lonely/"
        ),
        'options': [

        ]
    },
    "Some food would be great": {
        'message': (
            "Try searching at GoogleMaps :)"
            "https://www.google.com/maps"
        ),
        'options': [

        ]
    },
    "I want to go somewhere": {
        'message': (
            "Try searching at GoogleMaps :)"
            "https://www.google.com/maps"
        ),
        'options': [

        ]
    },
    "I miss my country": {
        'message': (
            "It's hard to be away from home"
        ),
        'options': [
            "Some food would be great",
            "I would like to find cool things to do around",
        ]
    },
    "Someone to talk to": {
        'message': (
            "Would you like to meet new people?"
        ),
        'options': [
            "Yeah, I would like talk with someone",
            "It would be cool to join some activity",
            "Not right now",
        ]
    },
    "I feel lonely": {
        'message': (
            "Would you like to meet new people?"
        ),
        'options': [
            "Yeah, I would like talk with someone",
            "It would be cool to join some activity",
            "Not right now",
        ]
    },
    "I'm lost": {
        'message': (
            "What are you looking for?"
        ),
        'options': [
            "I want to go somewhere",
            "I need help with my paperwork",
            "Someone to talk to",      
        ]
    },
    "Not feeling great today :(": {
        'message': (
            "So sorry to hear that. "
            "Whats wrong?"
        ),
        'options': [
            "I'm bored",
            "I'm stressed with paperwork",
            "I'm lost",
            "I'm tired",
            "I miss my country",
            "I feel lonely",
            "I'm feeling ill",
            "None of that",
        ]
    },
    "Yeah!": {
        'message': (
            "Let me introduce you to my friend Laila!"
        ),
        'options': [

        ]
    }
}



def generate_markup(state):
    if not state['options']:
        return None
    markup = types.ReplyKeyboardMarkup()
    for option in state['options']:
        markup.row(option)
    return markup


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(answer):
#     initial = STATES['Initial']
#     markup = generate_markup(initial)
#     if markup:
#         bot.send_message(
#             answer.chat.id,
#             initial['message'],
#             reply_markup=markup)
#     else:
#         bot.send_message(
#             answer.chat.id,
#             initial['message'])

@bot.message_handler(func=lambda m: True)
def handle_message(answer):
    chat_id = answer.chat.id
    next_state = STATES.get(answer.text, STATES['Initial'])
    markup = generate_markup(next_state)
    if markup:
        bot.send_message(
            chat_id,
            next_state['message'],
            reply_markup=markup)
    else:
        bot.send_message(
            chat_id,
            next_state['message'])

bot.polling(none_stop=True)
