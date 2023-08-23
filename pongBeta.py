import arcade

# Constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 15
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 5

class PongGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Pong Game")
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.ball_change_x = BALL_SPEED
        self.ball_change_y = BALL_SPEED
        self.left_paddle_y = height // 2
        self.right_paddle_y = height // 2

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, BALL_RADIUS, arcade.color.WHITE)
        arcade.draw_rectangle_filled(PADDLE_WIDTH // 2, self.left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)
        arcade.draw_rectangle_filled(self.width - PADDLE_WIDTH // 2, self.right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.WHITE)

    def on_update(self, delta_time):
        self.ball_x += self.ball_change_x
        self.ball_y += self.ball_change_y

        # Colisiones con los bordes
        if self.ball_x <= BALL_RADIUS or self.ball_x >= self.width - BALL_RADIUS:
            self.ball_change_x *= -1
            print("gol ")
        if self.ball_y <= BALL_RADIUS or self.ball_y >= self.height - BALL_RADIUS:
            self.ball_change_y *= -1
            

        # Colisiones con las paletas
        if (self.ball_x - BALL_RADIUS <= PADDLE_WIDTH and self.left_paddle_y - PADDLE_HEIGHT // 2 <= self.ball_y < self.left_paddle_y + PADDLE_HEIGHT // 2) or (self.ball_x + BALL_RADIUS >= self.width - PADDLE_WIDTH and self.right_paddle_y - PADDLE_HEIGHT // 2 <= self.ball_y <= self.right_paddle_y + PADDLE_HEIGHT // 2):
            self.ball_change_x *= -1
            print("colision")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.left_paddle_y += PADDLE_SPEED
        elif key == arcade.key.S:
            self.left_paddle_y -= PADDLE_SPEED
        elif key == arcade.key.UP:
            self.right_paddle_y += PADDLE_SPEED
        elif key == arcade.key.DOWN:
            self.right_paddle_y -= PADDLE_SPEED
            

def main():
    window = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()