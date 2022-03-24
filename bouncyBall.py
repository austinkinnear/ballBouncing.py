def bouncyBall():
  x = 400 #starting xPosition of the ball
  y = 400 #starting yPosition of the ball
  width = 50 #width of ball
  height = 50 #height of ball
  vx = 6 #velocity X
  vy = 9 #velocity Y
  i = 0  #variable 
  while i < 200: #amount of frames to the video
    i += 1 
    canvas = makeEmptyPicture(500,500)
    addOvalFilled(canvas, x, y , width, height, green)
    x+= vx
    y+= vy
    if x > 500: #width of canvas =500
      vx = -6 #when x reaches far right it changes to negative to go left 
    if y > 500: # height of 500
      vy = -9 #when y reaches top it changes to negative to go down
    if x < 0:
      vx = 6
    if y < 0:
      vy = 9
    explore(canvas)
