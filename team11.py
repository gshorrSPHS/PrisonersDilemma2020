import random 
team_name = 'Sibo & Shane'
strategy_name = 'Follow unless patterns appear'
strategy_description = "collude if they colluded last time and betray if they betrayed last time. If last few responses were the same, do the opposite (e.g. 'bbbb' ---> 'c')"
                                                                                                                                  
def move(my_history, their_history, my_score, their_score):
    choices = ['c','b']
    if len(my_history) == 0:
      return 'c'
    elif their_history [-4:] == 'bbbb':
      return 'c'
    elif their_history [-4:] == 'cccc':
      return 'b'
    elif their_history [-3:] == 'bbb':
      return 'c'
    elif their_history [-3:] == 'ccc':
      return 'b'
    elif their_history [-1] == 'c':
      return 'c'
    elif their_history [-1] == 'b':
      return 'b'
    elif their_score < my_score:
      return 'b'
    elif their_score > my_score:
      return 'c'
    else:
      return 'c'                                                                                                                                   
