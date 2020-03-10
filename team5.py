team_name = 'TeamFive'
strategy_name =  'Tit for Tat'
strategy_description = 'An eye for an eye, a son for a son, and a crime for a crime. Yeet. Our move is the same as their 5th move back'
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
  # if you are trying to say the first round, you figure out what round
  # you are on by doing len(my_history).  if you haven't gone yet, what number is that?ye
    if len(my_history) == 0:
      return "c"
    elif len(my_history) == 1:
      return "b"
    elif len(my_history) == 2:
      return "c"
    elif len(my_history) == 3:
      return "c"
    elif len(my_history) == 4:
      return "b"
      # more than 3 moves
    elif len(my_history) > 4:
      return their_history[-5]
    else:
      return 'b'
      

    # choices = ['c','b']
