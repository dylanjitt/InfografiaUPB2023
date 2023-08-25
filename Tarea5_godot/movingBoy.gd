extends Node2D



@export var speed = 2
@export var anglespeed=3

var velocity = Vector2(0,0)
var angle=0
func _process(delta):
	velocity=velocity*speed
	position+=velocity*delta
	
	rotation+=angle*anglespeed*delta
	
	
func update_velocity():
	velocity = Vector2(0, 0)

func _on_button_button_up():
	update_velocity()
	velocity.y-=1

func _on_button_button_down():
	update_velocity()
	velocity.y+=1

func _on_button_button_left():
	update_velocity()
	velocity.x-=1

func _on_button_button_right():
	update_velocity()
	velocity.x+=1

func _stop_x():
	update_velocity()
	velocity.x+=0
	
func _stop_y():
	update_velocity()
	velocity.y+=0
	
func _turn_left():
	angle-=1
	
func _turn_right():
	angle+=1
	
func _stop_turn():
	angle=0
