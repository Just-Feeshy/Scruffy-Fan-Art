import turtle;

# God please help me - Feeshy 2021

def longHair():
    scruffyPen.left(22.5);
    scruffyPen.forward(30);
    scruffyPen.left(67.5 * 2);
    scruffyPen.forward(30);
    scruffyPen.left(225 - 22.5);

scruffyPen = turtle.Turtle();
scruffyPen.speed(10);
scruffyPen.penup();
scruffyPen.right(90);
scruffyPen.color('brown');
scruffyPen.pensize(5);
scruffyPen.setx(-65);
scruffyPen.pendown();
scruffyPen.circle(65, 180);
scruffyPen.penup();
scruffyPen.setx(80);
scruffyPen.pendown();
scruffyPen.circle(80, 180);

longHair();

for i in range(2):
    scruffyPen.left(45);
    scruffyPen.forward(15);
    scruffyPen.left(90);
    scruffyPen.forward(15);
    scruffyPen.left(225);

for i in range(4):
    longHair();

scruffyPen.penup();
scruffyPen.setx(7);
scruffyPen.sety(80);
scruffyPen.left(125);
scruffyPen.pendown();
scruffyPen.forward(75);
scruffyPen.right(130);
scruffyPen.forward(75);

scruffyPen.penup();
scruffyPen.setx(-7);
scruffyPen.sety(80);
scruffyPen.left(10);

scruffyPen.right(125);
scruffyPen.pendown();
scruffyPen.forward(75);
scruffyPen.left(130);
scruffyPen.forward(69);

scruffyPen.penup();
scruffyPen.setx(0);
scruffyPen.sety(-45);
scruffyPen.left(-180);
scruffyPen.pendown();
scruffyPen.circle(5, 170);

scruffyPen.hideturtle();
scruffyPen = None;