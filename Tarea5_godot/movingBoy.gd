extends Node2D



@export var speed = 5
@export var anglespeed=0.1

var velocity = Vector2(0,0)
var angle=0
func _process(delta):
	position.x+=velocity.x
	position.y+=velocity.y
	rotation+=anglespeed*angle
	if Input.is_anything_pressed():
		if Input.is_key_pressed(KEY_UP):
			_on_button_button_up()
		if Input.is_key_pressed(KEY_DOWN):
			_on_button_button_down()
		if Input.is_key_pressed(KEY_LEFT):
			_on_button_button_left()
		if Input.is_key_pressed(KEY_RIGHT):
			_on_button_button_right()
		if Input.is_key_pressed(KEY_A):
			_turn_left()
		if Input.is_key_pressed(KEY_D):
			_turn_right()
	else:
		_stop_x()
		_stop_y()
		_stop_turn()
	#if Input.is_key_pressed()
	


func _on_button_button_up():
	
	velocity.y=-speed

func _on_button_button_down():
	
	velocity.y=speed

func _on_button_button_left():
	
	velocity.x=-speed

func _on_button_button_right():
	
	velocity.x=speed

func _stop_x():
	
	velocity.x=0
	
func _stop_y():
	
	velocity.y=0
	
func _turn_left():
	angle-=1
	
func _turn_right():
	angle+=1
	
func _stop_turn():
	angle=0

#if Input.is_key
