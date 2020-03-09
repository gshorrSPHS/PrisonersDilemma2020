import random 

team_name = 'bird-tray'
strategy_name = 'Play nice, or else...'
strategy_description =  'oh boy i sure do love not being betrayed hey what are you doing bro stop BRO STOP AAAAAAAAAAAAAAAAAAAA' 

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history) == 0:
      return 'c'
    if their_history.count('b') <= 4 and len(my_history) >= 1:
      return their_history[-1]
    elif random.random() < 0.01:
      return 'c'
    else:
      return 'b'
