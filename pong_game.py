# Jake Wolfe, ENGR 1050, Spring 2023, Final Project
# Collaborators: none
# creating the classic arcade game 'Pong' using the turtle library

# PONG GAME
# USER ENTERS PREFERRED DIFFICULTY, THEN CLICKS PLAY TO BEGIN
# FIRST TO FIVE POINTS WINS!






# insert turtle library
import turtle as t

difficulty = input("Select Difficulty Level (easy, medium, hard):")
# create main screen for game
screen = t.Screen()

# set background color, title, and screen size
screen.bgcolor('black')
screen.title = ('PONG')
screen.setup(width=1000, height = 600)

# create title screen
title_screen = t.Turtle()
title_screen.speed(0)
title_screen.color('white')
title_screen.penup()
title_screen.hideturtle()
title_screen.goto(0, 100)
title_screen.write('Welcome to Pong!', align='center', font=('Calibri', 36, 'normal'))
title_screen.goto(0, 50)
title_screen.write('Use the W and S keys to move Player 1 up and down', align='center', font=('Calibri', 24, 'normal'))
title_screen.goto(0, 0)
title_screen.write('Use the Up and Down arrows to move Player 2 up and down', align='center', font=('Calibri', 24, 'normal'))
title_screen.goto(0, -50)
title_screen.write('First to 5 points wins; Click the Play button to start', align='center', font=('Calibri', 24, 'normal'))

# create "Play" button that starts the game
play_button = t.Turtle()
play_button.speed(0)
play_button.color('white')
play_button.penup()
play_button.shapesize(stretch_wid=2, stretch_len=8)
play_button.goto(0, -150)
play_button.write('PLAY', align='center', font=('Calibri', 35, 'normal'))

# function to start the game
def start_game(x, y):
	"""Starts Pong game
	Inputs: x and y
	Outputs: updated ball positions
	Usage:
	Returns: animated ball movements and collisions
	"""
# hide title screen and play button
	title_screen.clear()
	play_button.clear()
	title_screen.hideturtle()
	play_button.hideturtle()

	# player 1 paddle
	play1_pad = t.Turtle()
	play1_pad.speed(0)
	play1_pad.color('green')
	play1_pad.shape('square')

	# set shape of paddle to be rectangle: wid = 6, len =2
	play1_pad.shapesize(stretch_wid=6,stretch_len=2)

	# set initial position of player 1 paddle
	play1_pad.penup()
	play1_pad.goto(-400,0)


	# player 2 paddle
	play2_pad = t.Turtle()
	play2_pad.speed(0)
	play2_pad.color('blue')
	play2_pad.shape('square')

	# set shape of paddle to be rectangle: wid = 6, len =2
	play2_pad.shapesize(stretch_wid=6,stretch_len=2)

	# set initial position of player 2 paddle
	play2_pad.penup()
	play2_pad.goto(400,0)


	# create game ball
	ball = t.Turtle()
	ball.speed(40)
	ball.shape('circle')
	ball.color('pink')
	ball.penup()
	ball.goto(0,0)
	
	# altering ball speed and paddle size for different difficulties
	if difficulty == 'hard':
		ball.dx = 8.5
		ball.dy = -8.5
		play1_pad.shapesize(stretch_wid=4,stretch_len=2)
		play2_pad.shapesize(stretch_wid=4,stretch_len=2)

	elif difficulty == 'medium':
		ball.dx = 6
		ball.dy = -6
		play1_pad.shapesize(stretch_wid=7,stretch_len=2)
		play2_pad.shapesize(stretch_wid=7,stretch_len=2)

	elif difficulty == 'easy':
		ball.dx = 4
		ball.dy = -4
		play1_pad.shapesize(stretch_wid=10,stretch_len=3)
		play2_pad.shapesize(stretch_wid=10,stretch_len=3)
	else:
		print('Invalid difficulty level, defaulting to easy')
		ball.dx = 4
		ball.dy = -4
		play1_pad.shapesize(stretch_wid=10,stretch_len=3)
		play2_pad.shapesize(stretch_wid=10,stretch_len=3)
		

	# set initial score
	player1 = 0
	player2 = 0

	# displaying the score
	score = t.Turtle()
	score.speed(0)
	score.color('white')
	score.penup()
	score.hideturtle()
	score.goto(0,250)
	score.write("Player 1: 0    	Player 2: 0",align='center', font = ("Calibri", 24, "normal"))

	
	# functions to move paddles up and down

	def play1_up():
		"""
		Controls player 1 ability to go up
		"""
		y = play1_pad.ycor()
		y+= 20
		play1_pad.sety(y)

	def play1_down():
		"""
		Controls player 1 ability to go down
		"""
		y = play1_pad.ycor()
		y -= 20
		play1_pad.sety(y)

	def play2_up():
		"""
		Controls player 2 ability to go up
		"""
		y = play2_pad.ycor()
		y+= 20
		play2_pad.sety(y)

	def play2_down():
		"""		
		Controls player 2 ability to go down
		"""
		y = play2_pad.ycor()
		y -= 20
		play2_pad.sety(y)


	# allow players to use keys to control paddles
	screen.listen()
	screen.onkeypress(play1_up, 'w')
	screen.onkeypress(play1_down, 's')
	screen.onkeypress(play2_up, "Up")
	screen.onkeypress(play2_down, "Down")

	while True:
		screen.update()
		# update ball positions by adding movement speed
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		
		# check to see collisions with sides

		if ball.ycor() > 280:
			ball.sety(280)
			ball.dy *= -1
		
		if ball.ycor() < -280:
			ball.sety(-280)
			ball.dy *= -1

		if ball.xcor() > 500:
			ball.goto(0,0)
			ball.dy *= -1
			#updates score if goal is scored
			player1 += 1
			score.clear()
			score.write("Player 1: {}    	Player 2: {}".format(player1,player2), align = 'center', font = ("Calibri", 24, "normal"))

		if ball.xcor() < -500:
			ball.goto(0,0)
			ball.dy *= -1
			#updates score if goal is scored
			player2 += 1
			score.clear()
			score.write("Player 1: {}    	Player 2: {}".format(player1,player2), align = 'center', font = ("Calibri", 24, "normal"))


		# collision between paddle and balls on right side

		if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < play2_pad.ycor() + 50 and ball.ycor() > play2_pad.ycor() - 50):			
			ball.setx(360)
			ball.dx*=-1

		# collision between paddle and balls on left side
		if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < play1_pad.ycor() + 50 and ball.ycor() > play1_pad.ycor() - 50):
			ball.setx(-360)
			ball.dx *= -1


			# game ends when one player scores 5

		if player1 == 5:
			# hide gameplay screen
			play1_pad.hideturtle()
			play2_pad.hideturtle()
			ball.hideturtle()
			# create exit screen displaying message that player 1 wins
			exit_screen = t.Turtle()
			exit_screen.speed(0)
			exit_screen.color('white')
			exit_screen.penup()
			exit_screen.hideturtle()
			exit_screen.goto(0, 75)
			exit_screen.write('Player 1 Wins!', align='center', font=('Calibri', 48, 'normal'))

		if player2 == 5:
			# hide gameplay screen
			play1_pad.hideturtle()
			play2_pad.hideturtle()
			ball.hideturtle()
			# create exit screen displaying message that player 1 wins
			exit_screen = t.Turtle()
			exit_screen.speed(0)
			exit_screen.color('white')
			exit_screen.penup()
			exit_screen.hideturtle()
			exit_screen.goto(0, 75)
			exit_screen.write('Player 2 Wins!', align='center', font=('Calibri', 48, 'normal'))
						

# listen for clicks on "Play" button
play_button.onclick(start_game)

# start game loop
screen.mainloop()