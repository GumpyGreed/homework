def availability(w):
      if w in user_word:
            return True
      else:
            return False
def word_order(w):
      index = user_word.index(w, 0, (len(user_word)+1))
      return index
def user_gap(w):
      quantity = len(w)
      user_answer = []
      for i in range(quantity):
             user_answer.append('_')
      return user_answer
def appender (w, i):
      delited = user_answer.pop(i)
      user_answer.insert(i, w)
      return user_answer

        
user_word = str(input())
user_word = list(user_word)
counter = 0
misstake = 3
user_answer = user_gap(user_word)
while counter < misstake:
      user_input = str(input())
      if availability(user_input):
           index = word_order(user_input)
           user_answer = appender(user_input, index)
           print (str(user_answer))
           if user_answer == user_word:
                 print('Win! :)')
                 break
      else:
            print('Misstake!')
            counter += 1

if counter == misstake:
  print('Lose! :(')