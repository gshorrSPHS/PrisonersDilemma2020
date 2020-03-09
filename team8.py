team_name = 'Paul Gabor'
strategy_name =  'Victory or Tie'
strategy_description = 'Ensures victory or a tie every time based on score.'
    
def move(my_history, their_history, my_score, their_score):

  
	if len(my_history) < 5:
		return "b"
	elif my_score >= their_score:
		if my_score - 500 > their_score:
			return "c"
		else:
			return "b"
	else:
		return "b"
