import random 
team_name = 'team 4'
strategy_name =  'betray when needed, collude when needed, and random choice when'
strategy_description = 'be mean + try to take advantage of people and their kindness'


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    ''' 

    c = 0
    b = 0
    for letter in their_history:
      if letter == "c":
        c = c + 1
      elif letter == "b":
        b = b + 1
    for letter in my_history:
      if letter == "c":
        c = c + 1
      elif letter == "b":
        b = b + 1
    if c > b:
      return "c"
    elif b > c:
      return "b"
    else:
      return random.choice(['b','c'])
