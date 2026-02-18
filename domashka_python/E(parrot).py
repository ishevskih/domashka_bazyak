import random

class Parrot:
    def __init__(self, phrase):
        self.phrases = [phrase] 
    def say(self, repeats=1):
        for _ in range(repeats):
            random_phrase = random.choice(self.phrases)
            print(random_phrase)
    def learn(self, new_phrase):
        self.phrases.append(new_phrase)
    def show_phrases(self):
        print("Я знаю такие фразы:")
        for i, phrase in enumerate(self.phrases, 1):
            print(f"{i}. {phrase}")
p = Parrot("Гав!")
p.say() 
p.learn("Мяу!")
p.say()                  
              

