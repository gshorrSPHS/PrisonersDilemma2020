import random 
team_name = 'The Roman Catholic Church'
strategy_name =  'Las Vegas'
strategy_description = 'Randomly chooses unless a threatening pattern is detected.'
def move(my_history, their_history, my_score, their_score):
    bees = 0
    seas = 0
    recentbees = 0
    recentseas = 0
    choices = ['b', 'c']
    for letter in their_history: 
      if letter == 'b':
        bees += 1
      elif letter == 'c':
        seas += 1
    for letter in their_history[-3:]: 
      if letter == 'b':
        recentbees += 1
      elif letter == 'c':
        recentseas += 1
    pattern = ''
    recentpattern = ''
    if bees > seas: pattern = 'b'
    elif seas > bees: pattern = 'c'
    if recentbees > recentseas: recentpattern = 'b'
    elif recentseas > recentbees: recentpattern = 'c'
    if pattern == 'b':
      if recentpattern == 'b':
        return 'b'
      if recentpattern == 'c':
        return 'c'
    elif pattern == 'c':
      return random.choice(choices)
    else: return random.choice(choices)
