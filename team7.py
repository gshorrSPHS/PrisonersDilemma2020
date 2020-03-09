team_name = 'Luca Martin Leone'
strategy_name =  'percentage'
strategy_description = 'Its based on whether our code is losing or not, if it is losing it is mpre likely to betray. If it is winning, it is more likly to collude. After 90 matches our chances become more extreme as if we are winning, the colluding chance goes up by a thrid. If we are winning, the chances of betraying become 80%.'


def move(my_history, their_history, my_score, their_score):
  matches = len(my_history)
  if matches >= 90:
    if my_score < their_score:
      return random.choice(['c','b','b','b','b'])
    elif my_score > their_score:
      return random.choice(['c','c','b'])
    else:
      return random.choice(['c','b'])
  else:
    if my_score < their_score:
      return random.choice(['c','b','b'])
    elif my_score > their_score:
      return random.choice(['c', 'c', 'c', 'b', 'b'])
    else:
      return random.choice(['c','b'])
