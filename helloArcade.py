import arcade

SCREEN_WIDTH=800
SCREEN_HEIGHT=600
SCREEN_TITLE="Hola Arcade"

if __name__=="__main__":    
    #crear nueva ventana
    arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

    #cambiar el color de fondo
    arcade.set_background_color(arcade.color.WHITE_SMOKE)

    #iniciar render
    arcade.start_render()

    #funciones para dibujar
    arcade.draw_circle_filled(400,300,100,arcade.color.UFO_GREEN)
    arcade.draw_arc_filled(400,300,200,60,arcade.color.BLACK,0,200)
    #go green

    #finalizar render
    arcade.finish_render()

    #correr el programa
    arcade.run()