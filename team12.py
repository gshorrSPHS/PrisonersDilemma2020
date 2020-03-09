team_name = 'Team_Epic'
strategy_name =  '66%'
strategy_description = 'we used % of have often we played c or b to determen our move'


def move(my_history, their_history, my_score, their_score):
  tc = 0
  tb = 0
  mc = 0
  mb = 0
  for letter in their_history:
    if letter == "c":
     tc += 1
    if letter == "b":
     tb += 1
  for letter in my_history:
    if letter == "c":
     mc += 1
    if letter == "b":
     mb += 1
  if their_score < my_score:
    if float(mb)/(mb + mc) > 0.66:
     return 'c'
    else:
     return 'b'
  elif my_score > their_score:
    if float(mc)/(mb + mc) < 0.66:
     return 'b'
    else:
     return 'c'
  elif my_score == their_score:
   return random.choice(['c','b'])
      
