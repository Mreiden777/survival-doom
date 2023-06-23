controller.up.onEvent(ControllerButtonEvent.Repeated, function () {
    mySprite.y += -5
})
controller.right.onEvent(ControllerButtonEvent.Repeated, function () {
    mySprite.x += 5
})
controller.down.onEvent(ControllerButtonEvent.Repeated, function () {
    mySprite.y += 5
})
controller.left.onEvent(ControllerButtonEvent.Repeated, function () {
    mySprite.x += -5
})
let enemy2_ready = 0
let puntos = 0
let mySprite: Sprite = null
music.play(music.createSong(assets.song`start music`), music.PlaybackMode.UntilDone)
scene.setBackgroundImage(assets.image`map`)
mySprite = sprites.create(assets.image`player`, SpriteKind.Player)
let mySprite2 = sprites.create(assets.image`enemy`, SpriteKind.Enemy)
let mySprite3 = sprites.create(img`
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
    `, SpriteKind.Enemy)
mySprite.setBounceOnWall(true)
mySprite2.setBounceOnWall(true)
mySprite2.setPosition(120, 40)
mySprite3.setPosition(120, 40)
mySprite2.follow(mySprite, 25)
forever(function () {
    info.changeScoreBy(1)
    puntos += 1
    pause(1000)
})
forever(function () {
    while (puntos > 4 == true) {
        mySprite3 = sprites.create(assets.image`Enemy2`, SpriteKind.Enemy)
        mySprite3.follow(mySprite, 25)
        enemy2_ready = 1
    }
})
forever(function () {
    while ((mySprite.overlapsWith(mySprite2) || mySprite.overlapsWith(mySprite3) && enemy2_ready == 1) == true) {
        game.gameOver(false)
    }
})
