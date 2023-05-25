# Python 3.10 e o jogo da tartaruga
# Pattern Match Estrutural
print(
    """\
    Jogo da Tartaruga

    comandos:
        move x y
        move steps
        turn angle (default 90)
        draw shape size (line|circle)
        write text
        stop
        exit
    """
)

from turtle import Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("black", "green")
turtle.penup()


while True:
    command: list[str] = input("🐢> ").strip().split()
    # move 2 3 - ["move", "2", "3"]

    match command:
        case ["move", *points]:
            match points:
                case [x, y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))

        case ["turn", *options]:
            match options:
                case [angle]:
                    turtle.right(float(angle))
                case _:
                    turtle.right(90)

        case ["draw", shape, size]:
            turtle.pendown()
            if shape == "circle":
                turtle.circle(float(size))
            elif shape == "line":
                turtle.forward(float(size))
            turtle.penup()

        case ["write", text]:
            turtle.write(" ".join(text), None, "center", "16pt 20")
            
        case ["exit" | "stop"]:
            break

        case _:
            print("invalid option")
