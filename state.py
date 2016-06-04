from telebot import types

class State:
    def message(self):
        return self.message

    def markup(self):
        markup = types.ReplyKeyboardMarkup()
        for option in self.options.keys():
            markup.row(option)
        return markup

    def next(self, answer):
        next_state = self.options.get(answer, None)
        if not next_state:
            next_state = State(message="Ooops, something went wrong :(")
       else:
            next_state = next_state()
        return next_state