from turtle import Turtle, Screen

# Setup screen
screen = Screen()
screen.title("Click to Get Coordinates")
screen.setup(width=540, height=600)
screen.bgpic("india.gif")  # Make sure india.gif is in the same folder

# Click handler
def get_mouse_click_coor(x, y):
    print(f"{x}, {y}")

# Listen for mouse clicks
screen.onscreenclick(get_mouse_click_coor)

# Keep window open
screen.mainloop()
