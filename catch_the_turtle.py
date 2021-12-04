
#------IMPORT STATEMENTS----------
import turtle as t
import random
import time

#----functions classses etc-------
class Game:
    def run(self):
        self.init_vars()
        self.init_turtles()
        self.count_down()
        self.spot.onclick(self.spot_clicked)
        self.write_score()
        self.window.mainloop()

    def init_vars(self):
        self.window = t.Screen()
        self.window.screensize(600, 600)
        self.objective_clicks    = 5
        self.times_clicked       = 0
        self.timer               = 30
        self.spot_attrs = {
            'size': 1,
            'color': "pink",
            'shape': "turtle"
        }

        self.score = 0
        self.score_font = ("Comic Sans MS", 20, "normal")
        self.game_over_font = ("Impact", 50, "")

    def init_turtles(self):
        self.spot = t.Turtle()
        self.spot.shapesize(self.spot_attrs['size'])
        self.spot.fillcolor(self.spot_attrs['color'])
        self.spot.shape(self.spot_attrs['shape'])

        self.score_writer = t.Turtle()
        self.score_writer.hideturtle()
        self.score_writer.pu()
        self.score_writer.goto(250, 300)

        self.counter = t.Turtle()
        self.counter.hideturtle()
        self.counter.pu()
        self.counter.goto(-350,300)

    # moves turtle to random location
    def change_location(self):
        self.spot.pu()
        self.spot.hideturtle()
        self.spot.goto(random.randint(-300, 300),
                       random.randint(-300, 300))
        self.spot.showturtle()
        self.spot.pd()

    def game_over(self):
        self.spot.hideturtle()
        self.score_writer.pu()
        self.score_writer.goto(-150, 0)
        self.score_writer.write(f"      Game over\nyour score was: {self.score}", \
                                font=self.game_over_font)

    def count_down(self):
        self.timer -= 1
        if self.timer >= 0:
            self.counter.getscreen().ontimer(self.count_down, 1000)
            self.counter.clear()
            self.counter.write(f"Time left: {self.timer}", font=self.score_font)
        else:
            self.game_over()


    def write_score(self):
        self.score_writer.clear()
        self.score_writer.pu()
        self.score_writer.pd()
        self.score_writer.write(f"Score: {self.score}", font=self.score_font)

    def update_score(self):
        self.score += 1
        self.write_score()

    # responding to spot being clicked
    def spot_clicked(self, x, y):
        colors = ["blue", "pink", "red", "yellow", "green", "purple"]
        if self.timer <= 0: # in case of edge cases
            self.spot.hideturtle()
            self.game_over()
            return
        self.update_score()
        self.change_location()
        self.spot.fillcolor(random.choice(colors))
        self.times_clicked += 1

#-----------events----------------
if __name__ == "__main__":
    game = Game()
    game.run()
