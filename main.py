def on_up_repeated():
    mySprite.y += -5
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_right_repeated():
    mySprite.x += 5
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_down_repeated():
    mySprite.y += 5
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_left_repeated():
    mySprite.x += -5
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

enemy2_ready = 0
puntos = 0
mySprite: Sprite = None
music.play(music.create_song(assets.song("""
        start music
    """)),
    music.PlaybackMode.UNTIL_DONE)
scene.set_background_image(assets.image("""
    map
"""))
mySprite = sprites.create(assets.image("""
    player
"""), SpriteKind.player)
mySprite2 = sprites.create(assets.image("""
    enemy
"""), SpriteKind.enemy)
mySprite3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
mySprite.set_bounce_on_wall(True)
mySprite2.set_bounce_on_wall(True)
mySprite2.set_position(120, 40)
mySprite3.set_position(120, 40)
mySprite2.follow(mySprite, 25)

def on_forever():
    global puntos
    info.change_score_by(1)
    puntos += 1
    pause(1000)
forever(on_forever)

def on_forever2():
    global mySprite3, enemy2_ready
    while puntos > 4 == True:
        mySprite3 = sprites.create(assets.image("""
            Enemy2
        """), SpriteKind.enemy)
        mySprite3.follow(mySprite, 25)
        enemy2_ready = 1
forever(on_forever2)

def on_forever3():
    while (mySprite.overlaps_with(mySprite2) or mySprite.overlaps_with(mySprite3) and enemy2_ready == 1) == True:
        game.game_over(False)
forever(on_forever3)
