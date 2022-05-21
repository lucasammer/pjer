import pjer
import handydandy
x=pjer.sprite([
  0,0,0,0,
  0,0,0,0,
  0,0,0,1,
  1,1,1,1
],0.100,10, True)
g=pjer.sprite([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,],100,10,False)
g.draw(0,-50)
g.draw(-40,-50)
g.draw(-80,-50)
g.draw(40,-50)
g.draw(80,-50)
x.draw(-30,100)
while True:
  x.move(x.x,x.y-10)
  g.draw(0,-50)
handydandy.userinput.quitpause('end')