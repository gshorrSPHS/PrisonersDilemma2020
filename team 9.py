team_name = 'Collusion'
strategy_name =  'Imitate'
strategy_description = 'If you betray, we will too.  If you collude, we will too.'

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0:
      return 'b'
    elif their_history[-2] == 'c' and their_history[-1] == 'c':
      return 'c'
    elif their_history[-1] == 'b':
      return 'b'
    elif my_score <= their_score:
      return 'b'
    elif their_score < my_score:
      return 'b'
    else:
      return 'b'
