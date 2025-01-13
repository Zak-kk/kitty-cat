@namespace
class SpriteKind:
    coin = SpriteKind.create()
    flower = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.set_game_over_effect(False, effects.melt)
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_a_pressed():
    if meow_meow.vy == 0:
        meow_meow.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile2)

def on_on_overlap(sprite3, otherSprite):
    info.change_score_by(1)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite2):
    global bee
    bee = sprites.create(img("""
            . . f f f . . . . . . . . . . . 
                    f f f c c . . . . . . . . f f f 
                    f f c c c . c c . . . f c b b c 
                    f f c 3 c c 3 c c f f b b b c . 
                    f f c 3 b c 3 b c f b b c c c . 
                    f c b b b b b b c f b c b c c . 
                    c c 1 b b b 1 b c b b c b b c . 
                    c b b b b b b b b b c c c b c . 
                    c b 1 f f 1 c b b c c c c c . . 
                    c f 1 f f 1 f b b b b f c . . . 
                    f f f f f f f b b b b f c . . . 
                    f f 2 2 2 2 f b b b b f c c . . 
                    . f 2 2 2 2 2 b b b c f . . . . 
                    . . f 2 2 2 b b b c f . . . . . 
                    . . . f f f f f f f . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    animation.run_image_animation(bee,
        [img("""
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
        """)],
        500,
        False)
sprites.on_overlap(SpriteKind.player, SpriteKind.flower, on_on_overlap2)

bee: Sprite = None
flower2: Sprite = None
coins: Sprite = None
meow_meow: Sprite = None
scene.set_background_color(9)
meow_meow = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . f . . . 
            . . . . . . . . . . . . f f . . 
            f f f f f f f f f f f f f f f . 
            . . . . f f f f f f f f f 5 f f 
            . . . . f f f f f f f f f f f f 
            . . . . . f . f . . f . f . . . 
            . . . . . f . f . . f . f . . . 
            . . . . . f . f . . f . f . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(meow_meow, 100, 0)
meow_meow.ay = 345
scene.camera_follow_sprite(meow_meow)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile4
""")):
    coins = sprites.create(img("""
            . . b b b b . . 
                    . b 5 5 5 5 b . 
                    b 5 d 3 3 d 5 b 
                    b 5 3 5 5 1 5 b 
                    c 5 3 5 5 1 d c 
                    c d d 1 1 d d c 
                    . f d d d d f . 
                    . . f f f f . .
        """),
        SpriteKind.coin)
    animation.run_image_animation(coins,
        [img("""
                . . b b b b . . 
                        . b 5 5 5 5 b . 
                        b 5 d 3 3 d 5 b 
                        b 5 3 5 5 1 5 b 
                        c 5 3 5 5 1 d c 
                        c d d 1 1 d d c 
                        . f d d d d f . 
                        . . f f f f . .
            """),
            img("""
                . . b b b . . . 
                        . b 5 5 5 b . . 
                        b 5 d 3 d 5 b . 
                        b 5 3 5 1 5 b . 
                        c 5 3 5 1 d c . 
                        c 5 d 1 d d c . 
                        . f d d d f . . 
                        . . f f f . . .
            """),
            img("""
                . . . b b . . . 
                        . . b 5 5 b . . 
                        . b 5 d 1 5 b . 
                        . b 5 3 1 5 b . 
                        . c 5 3 1 d c . 
                        . c 5 1 d d c . 
                        . . f d d f . . 
                        . . . f f . . .
            """),
            img("""
                . . . b b . . . 
                        . . b 5 5 b . . 
                        . . b 1 1 b . . 
                        . . b 5 5 b . . 
                        . . b d d b . . 
                        . . c d d c . . 
                        . . c 3 3 c . . 
                        . . . f f . . .
            """),
            img("""
                . . . b b . . . 
                        . . b 5 5 b . . 
                        . b 5 1 d 5 b . 
                        . b 5 1 3 5 b . 
                        . c d 1 3 5 c . 
                        . c d d 1 5 c . 
                        . . f d d f . . 
                        . . . f f . . .
            """),
            img("""
                . . . b b b . . 
                        . . b 5 5 5 b . 
                        . b 5 d 3 d 5 b 
                        . b 5 1 5 3 5 b 
                        . c d 1 5 3 5 c 
                        . c d d 1 d 5 c 
                        . . f d d d f . 
                        . . . f f f . .
            """)],
        350,
        True)
    tiles.place_on_tile(coins, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile5
""")):
    flower2 = sprites.create(img("""
            . . 2 2 b b b b b . . . . . . . 
                    . 2 b 4 4 4 4 4 4 b . . . . . . 
                    2 2 4 4 4 4 d d 4 4 b . . . . . 
                    2 b 4 4 4 4 4 4 d 4 b . . . . . 
                    2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                    2 2 b 4 4 4 4 4 4 4 b e . . . . 
                    . 2 b b b 4 4 4 b b b e . . . . 
                    . . e b b b b b b b e e . . . . 
                    . . . e e b 4 4 b e e e b . . . 
                    . . . . . e e e e e e b d b b . 
                    . . . . . . . . . . . b 1 1 1 b 
                    . . . . . . . . . . . c 1 d d b 
                    . . . . . . . . . . . c 1 b c . 
                    . . . . . . . . . . . . c c . .
        """),
        SpriteKind.flower)
    tiles.place_on_tile(flower2, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))