import random 

team_name = 'The Great Depression'
strategy_name =  'heads collude, tails betray'
strategy_description = 'The world is cruel. And the only morality in a cruel world is chance.'
    


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''


    tc = 0
    tb = 0
    mc = 0
    mb = 0
    for letter in their_history:
      if letter == "c":
        tc += 1
      elif letter == "b":
        tb += 1
    for letter in my_history:
      if letter == "c":
        mc += 1
      elif letter == "b":
        mb += 1
    if their_score > my_score:
      if tc > mc: 
        return "c"  
      else:
        return "b"
        
        # need to have something here in case nothing else works
    elif their_score < my_score:
      if tc < mc:
        return "b"  
      else:
        return "c"
    else:
      if tc == mc:
        return "c"
      else:
        return "b"
