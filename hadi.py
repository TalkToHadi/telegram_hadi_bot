#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from telebot import types


TOKEN = '228469213:AAEnb6laZGjxnkTQBbEhZuxdEjHFAqhznzc' #Ponemos nuestro TOKEN generado con el @BotFather
bot = telebot.TeleBot(TOKEN)

STATES = {
    'Initial': {
        'message': (
            "Hi there. My name is Hadi :) \n"
            "What language do you want to speak with me? \n"
            "مرحبا! \n"
            "اسمي هادي  بأية لغة تود أن نتحدث؟ \n"
        ),
        'options': [
            'English',
            'العربية',
        ],
    },
    'العربية': {
        'message': (
            "أنا هنا من أجلك. ماذا تفعل؟"
        ),
        'options': [
            "أشعر حتى! :D",
            "لا شعور عظيم اليوم :(",
        ],
    },
    'English': {
        'message': (
            "I'm here for you. What's up?"
        ),
        'options': [
            "I'm feeling up! :D",
            "Not feeling great today :(",
        ],
    },
    "I'm feeling up! :D": {
        'message': (
            "Great!"
            "Would you like to cheer someone up?"
        ),
        'options': [
            "Yeah!",
            "Maybe on another time",
        ],
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

        ],
    },
    "I need help with my paperwork": {
        'message': (
            "Sorry, I can't help you with this but I know who can! \n"
            "You should check Burocrazy, those guys are cool \n"
        ),
        'options': [

        ],
    },
    "None of that": {
        'message': (
            "Sorry, I can't help you with this"
        ),
        'options': [

        ],
    },
    "Maybe on another time": {
        'message': (
            "Ooops, I'm sad to hear that! \n"
            "Talk to me later if you want"
        ),
        'options': [

        ],
    },
    "Yeah, I would like talk with someone": {
        'message': (
            "Let me introduce you to my friend Hans!"
        ),
        'options': [

        ],
        'contact': {
            'name': 'Hans',
            'phone_number': '+49 629073543'
        }
    },
    "Yes, of course!": {
        'message': (
            "Check this web page! \n"
            "https://www.youtube.com/results?search_query=funny"
        ),
        'options': [

        ],
    },
    "I'm mentally exhausted": {
        'message': (
            "Try an app like HeadSpace to learn how to meditate \n"
            "https://www.headspace.com/"
        ),
        'options': [

        ],
    },
    "Yeah, I'd love to!": {
        'message': (
            "Here you can find cinemas around you! \n"
            "https://www.google.com/maps?q=cinema"
        ),
        'options': [

        ],
    },
    "No, not right now": {
        'message': (
            "Here you can find sports events (and more)! \n"
            "https://www.sportsworld.co.uk/events"
        ),
        'options': [
            "Ok, not bored anymore",
            "Not interested, I'm still bored"
        ],
    },
    "Ok, not bored anymore": {
        'message': (
            "Great!"
        ),
        'options': [],
    },
    "Not interested, I'm still bored": {
        'message': (
            "Some ideas for you to enjoy: \n"
            "https://www.buzzfeed.com/leonoraepstein/things-to-do-when-you-are-bored-out-of-your-mind?utm_term=.qi5x2v7Gd#.qv6JEANy7"
        ),
        'options': [],
    },
    "Not really": {
        'message': (
            "Do you prefer to go to cinema?"
        ),
        'options': [
            "Yeah, I'd love to!",
            "Rather not",
        ],
    },
    "Rather not": {
        'message': (
            "What about watching some funny videos?"
        ),
        'options': [
            "Yes, of course! \n",
            "Not really",
        ]
    },
    "Yeah, sure!": {
        'message': (
            "Check MeetUp! You'll find something you like for sure \n"
            "http://www.meetup.com/"
        ),
        'options': [

        ]
    },
    "I would like to find cool things to do around": {
        'message': (
            "Check MeetUp! You'll find something you like for sure \n"
            "http://www.meetup.com/"
        ),
        'options': [

        ]
    },
    "It would be cool to join some activity": {
        'message': (
            "Check MeetUp! You'll find something you like for sure \n"
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
            "No, not right now",
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
            "Look this awesome link to german national health system \n"
            "http://www.howtogermany.com/pages/healthinsurance.html"
        ),
        'options': [

        ]
    },
    "Not right now": {
        'message': (
            "Watch this inpirational talks on how to deal with feeling lonely \n"
            "http://www.keepinspiring.me/25-creative-and-surprising-things-to-do-when-you-feel-lonely/"
        ),
        'options': [

        ]
    },
    "Some food would be great": {
        'message': (
            "Try searching at GoogleMaps :) \n"
            "https://www.google.com/mapsq=restaurants"
        ),
        'options': [

        ]
    },
    "I want to go somewhere": {
        'message': (
            "Try searching at GoogleMaps :)  \n"
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
            "I could use some advice about homesickness",
            "Some food would be great",
            "I would like to find cool things to do around",
        ]
    },
    "I could use some advice about homesickness": {
        'message': (
            "Try this one ;)",
            "http://www.gooverseas.com/blog/ways-reduce-homesickness-abroad"
        ),
        'options': []
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
    "I'm sad": {
        'message': (
            "how long have you been sad?"
        ),
        'options': [
            "For less than a month",
            "Actually, longer than a month",
        ]
    },
    "For less than a month": {
        'message': (
            "Try to get some ideas from here\n",
            "https://www.ted.com/talks/dan_gilbert_asks_why_are_we_happy"
        ),
        'options': []
    },
    "Actually, longer than a month": {
        'message': (
            "Just to let you know, here are some helpful advices\n"
            "http://www.suicide.org/hotlines/international/germany-suicide-hotlines.html \n"
            "http://www.frauenhauskoordinierung.de/english-summary.html"
        ),
        'options': []
    },





    "Not feeling great today :(": {
        'message': (
            "So sorry to hear that.  \n"
            "Whats wrong?"
        ),
        'options': [
            "I'm bored",
            "I'm stressed with paperwork",
            "I'm lost",
            "I'm tired",
            "I'm sad",
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

        ],
        'contact': {
            'name': 'Laila',
            'phone_number': '+49 674410279'
        }
    }
}


def generate_markup(state):
    if not state.get('options'):
        return types.ReplyKeyboardHide(selective=False)

    markup = types.ReplyKeyboardMarkup()
    for option in state['options']:
        markup.row(option)
    return markup


@bot.message_handler(func=lambda m: True)
def handle_message(answer):
    chat_id = answer.chat.id
    next_state = STATES.get(answer.text, STATES['Initial'])
    markup = generate_markup(next_state)
    bot.send_message(
        chat_id,
        next_state['message'],
        reply_markup=markup)
    if next_state.get('contact'):
        contact = next_state['contact']
        bot.send_contact(
            chat_id,
            contact['phone_number'],
            contact['name'])

bot.polling(none_stop=True)
