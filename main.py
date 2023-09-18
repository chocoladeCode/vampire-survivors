@namespace
class SpriteKind:
    Immune = SpriteKind.create()
    trough = SpriteKind.create()
    DungeonKey = SpriteKind.create()
    SuperEnemy = SpriteKind.create()
    Scatterani = SpriteKind.create()
    coin = SpriteKind.create()
    SuperShield = SpriteKind.create()

def on_on_overlap(sprite2, otherSprite2):
    info.change_countdown_by(-10)
    sprites.destroy(otherSprite2)
sprites.on_overlap(SpriteKind.Immune, SpriteKind.SuperEnemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    global Truefalse, TextCheck
    sprites.destroy(otherSprite)
    Truefalse = 1
    TextCheck = 1
sprites.on_overlap(SpriteKind.player, SpriteKind.trough, on_on_overlap2)

def on_on_overlap3(sprite6, otherSprite6):
    global coinsnumber
    sprites.destroy(otherSprite6, effects.confetti, 500)
    coinsnumber += 1
sprites.on_overlap(SpriteKind.player, SpriteKind.coin, on_on_overlap3)

def on_on_overlap4(sprite5, otherSprite5):
    info.change_score_by(1)
    sprites.destroy(otherSprite5)
    if info.score() < 40:
        sprites.destroy(sprite5)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

def on_on_overlap5(sprite9, otherSprite9):
    global coinsnumber
    sprites.destroy(otherSprite9, effects.confetti, 500)
    coinsnumber += 1
sprites.on_overlap(SpriteKind.Immune, SpriteKind.coin, on_on_overlap5)

def Key():
    global KeyDungeon
    for value in tiles.get_tiles_by_type(sprites.swamp.swamp_tile16):
        KeyDungeon = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 5 5 5 . . . . . . . . . . 
                            . . . 5 . 5 5 5 5 5 5 5 . . . . 
                            . . . 5 5 5 . . 5 . 5 . . . . . 
                            . . . . . . . . e . e . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.DungeonKey)
        tiles.place_on_tile(KeyDungeon, value)
        tiles.set_tile_at(value, sprites.dungeon.dark_ground_center)

def on_on_overlap6(sprite3, otherSprite3):
    sprites.destroy(otherSprite3)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.SuperEnemy, on_on_overlap6)

def on_on_score():
    game.show_long_text("Level hard", DialogLayout.CENTER)
    Character.set_position(450, 450)
info.on_score(60, on_on_score)

def on_on_score2():
    game.show_long_text("Level medium", DialogLayout.CENTER)
    Character.set_position(450, 450)
info.on_score(30, on_on_score2)

def on_on_overlap7(sprite22, otherSprite22):
    sprites.destroy(otherSprite22, effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.SuperShield, SpriteKind.enemy, on_on_overlap7)

def on_on_overlap8(sprite24, otherSprite24):
    sprites.destroy(otherSprite24, effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.SuperShield,
    SpriteKind.SuperEnemy,
    on_on_overlap8)

def on_countdown_end():
    global Character, SuperCheck
    sprites.destroy_all_sprites_of_kind(SpriteKind.SuperShield)
    sprites.destroy_all_sprites_of_kind(SpriteKind.Immune)
    sprites.destroy_all_sprites_of_kind(SpriteKind.SuperEnemy)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    Character = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f f . . . . . 
                    . . . f f e e e e f 2 f . . . . 
                    . . f f e e e e f 2 2 2 f . . . 
                    . . f e e e f f e e e e f . . . 
                    . . f f f f e e 2 2 2 2 e f . . 
                    . . f e 2 2 2 f f f f e 2 f . . 
                    . f f f f f f f e e e f f f . . 
                    . f f e 4 4 e b f 4 4 e e f . . 
                    . f e e 4 d 4 1 f d d e f . . . 
                    . . f e e e e e d d d f . . . . 
                    . . . . f 4 d d e 4 e f . . . . 
                    . . . . f e d d e 2 2 f . . . . 
                    . . . f f f e e f 5 5 f f . . . 
                    . . . f f f f f f f f f f . . . 
                    . . . . f f . . . f f f . . . .
        """),
        SpriteKind.player)
    Character.set_position(450, 450)
    SuperCheck = 0
    scene.camera_follow_sprite(Character)
    animation.run_image_animation(Character, assets.animation("""
        myAnim1
    """), 200, True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap9(sprite4, otherSprite4):
    sprites.destroy(otherSprite4)
    for value2 in tiles.get_tiles_by_type(sprites.dungeon.door_locked_north):
        tiles.set_wall_at(value2, False)
sprites.on_overlap(SpriteKind.player, SpriteKind.DungeonKey, on_on_overlap9)

def on_on_overlap10(sprite8, otherSprite8):
    global ScatterCheck
    sprites.destroy(otherSprite8)
    ScatterCheck = 1
sprites.on_overlap(SpriteKind.player, SpriteKind.Scatterani, on_on_overlap10)

def on_on_overlap11(sprite7, otherSprite7):
    info.change_life_by(-1)
    pause(500)
sprites.on_overlap(SpriteKind.player, SpriteKind.SuperEnemy, on_on_overlap11)

def on_on_overlap12(sprite32, otherSprite32):
    info.change_life_by(-1)
    music.play(music.string_playable("C5 C5 - - - - - - ", 1000),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap12)

def on_on_score3():
    game.splash("Whip Unlocked")
info.on_score(50, on_on_score3)

def on_on_score4():
    game.show_long_text("Level Insane!", DialogLayout.CENTER)
    Character.set_position(450, 450)
info.on_score(200, on_on_score4)

def on_on_overlap13(sprite23, otherSprite23):
    sprites.destroy(otherSprite23)
sprites.on_overlap(SpriteKind.Immune, SpriteKind.enemy, on_on_overlap13)

def on_on_score5():
    game.splash("Bullet Phase Unlocked")
    pause(5000)
info.on_score(40, on_on_score5)

def Variables():
    global Truefalse, Tid, TextCheck, ScatterCheck, coinsnumber, SuperCheck
    Truefalse = 0
    Tid = 0
    TextCheck = 0
    ScatterCheck = 0
    coinsnumber = 0
    SuperCheck = 0
myEnemy: Sprite = None
Whip: Sprite = None
shooty: Sprite = None
Time = 0
Tid = 0
ScatterCheck = 0
SuperCheck = 0
KeyDungeon: Sprite = None
coinsnumber = 0
TextCheck = 0
Truefalse = 0
coins: Sprite = None
Character: Sprite = None
tiles.set_current_tilemap(tilemap("""
    Map
"""))
game.show_long_text("The year is 345 bc, Monsters have taken over the world.",
    DialogLayout.TOP)
game.show_long_text("you are tasked with destorying as many monsters before they inevitable get to you",
    DialogLayout.BOTTOM)
Character = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . f f e e e e f 2 f . . . . 
            . . f f e e e e f 2 2 2 f . . . 
            . . f e e e f f e e e e f . . . 
            . . f f f f e e 2 2 2 2 e f . . 
            . . f e 2 2 2 f f f f e 2 f . . 
            . f f f f f f f e e e f f f . . 
            . f f e 4 4 e b f 4 4 e e f . . 
            . f e e 4 d 4 1 f d d e f . . . 
            . . f e e e e e d d d f . . . . 
            . . . . f 4 d d e 4 e f . . . . 
            . . . . f e d d e 2 2 f . . . . 
            . . . f f f e e f 5 5 f f . . . 
            . . . f f f f f f f f f f . . . 
            . . . . f f . . . f f f . . . .
    """),
    SpriteKind.player)
phase = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . c d 5 d c . . . . . 
            . . . b c c d 5 5 5 d c c b . . 
            . . b d d 5 5 5 5 5 5 5 d d b . 
            . . . b c c d 5 5 5 d c c b . . 
            . . . . . . c d 5 d c . . . . . 
            . . . . . . . c 5 c . . . . . . 
            . . . . . . . c d c . . . . . . 
            . . . . . . . b d b . . . . . . 
            . . . . . . . . b . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.trough)
Scatter = sprites.create(assets.image("""
    Scatter
"""), SpriteKind.Scatterani)
Scatter.set_position(760, 23)
animation.run_image_animation(Scatter, assets.animation("""
    Scatterani
"""), 200, True)
animation.run_image_animation(phase, assets.animation("""
    PhaseTrough
"""), 200, True)
animation.run_image_animation(Character, assets.animation("""
    myAnim1
"""), 200, True)
phase.set_position(31, 270)
scene.camera_follow_sprite(Character)
Character.set_position(randint(0, 600), randint(0, 600))
Key()
Variables()
info.set_life(10)
game.set_game_over_message(False, "You snooze you loose")
for index in range(5):
    coins = sprites.create(assets.image("""
        coin
    """), SpriteKind.coin)
    coins.set_position(randint(0, 600), randint(0, 600))

def on_on_update():
    global Character, Time, TextCheck
    if Truefalse == 1 and Time < 0:
        if SuperCheck == 0:
            sprites.destroy_all_sprites_of_kind(SpriteKind.player)
            sprites.destroy_all_sprites_of_kind(SpriteKind.SuperShield)
            sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
            Character = sprites.create(assets.image("""
                    Shield Character
                """),
                SpriteKind.Immune)
            Time = 80
            if TextCheck == 1:
                game.splash("Shield Unlocked")
                TextCheck = 0
            animation.run_image_animation(Character,
                assets.animation("""
                    ShieldChar
                """),
                200,
                True)
            Character.set_position(450, 450)
            scene.camera_follow_sprite(Character)
            info.start_countdown(20)
game.on_update(on_on_update)

def on_on_update2():
    controller.move_sprite(Character)
game.on_update(on_on_update2)

def on_update_interval():
    global shooty
    shooty = sprites.create_projectile_from_sprite(assets.image("""
        throwing knife 2
    """), Character, 90, 0)
game.on_update_interval(1000, on_update_interval)

def on_forever():
    global Character, SuperCheck, coinsnumber
    if coinsnumber == 5:
        sprites.destroy_all_sprites_of_kind(SpriteKind.Immune)
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        Character = sprites.create(img("""
                . . . . . . f f f f . . . . . . 
                            . . . . f f f 2 2 f f f . . . . 
                            . . . f f f 2 2 2 2 f f f . . . 
                            . . f f f e e e e e e f f f . . 
                            . . f f e 2 2 2 2 2 2 e e f . . 
                            . . f e 2 f f f f f f 2 e f . . 
                            . . f f f f e e e e f f f f . . 
                            . f f e f b f 4 4 f b f e f f . 
                            . f e e 4 1 f d d f 1 4 e e f . 
                            . . f e e d d d d d d e e f . . 
                            . . . f e e 4 4 4 4 e e f . . . 
                            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . f f . . f f . . . . .
            """),
            SpriteKind.SuperShield)
        SuperCheck = 1
        scene.camera_follow_sprite(Character)
        animation.run_image_animation(Character,
            assets.animation("""
                SuperShieldani
            """),
            500,
            True)
        coinsnumber = 0
        info.start_countdown(40)
forever(on_forever)

def on_forever2():
    global Whip
    if info.score() > 50:
        pause(1000)
        Whip = sprites.create_projectile_from_sprite(assets.image("""
            ShootDash
        """), Character, 0, 100)
        pause(500)
        sprites.destroy(Whip, effects.disintegrate, 500)
forever(on_forever2)

def on_forever3():
    global myEnemy
    if info.score() > 60:
        pause(2000)
        myEnemy = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Ghostani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.castle.tile_grass2)
        myEnemy.follow(Character, 35)
forever(on_forever3)

def on_forever4():
    global myEnemy
    if info.score() > 60:
        pause(2000)
        myEnemy = sprites.create(assets.image("""
            shark
        """), SpriteKind.SuperEnemy)
        tiles.place_on_random_tile(myEnemy, sprites.castle.tile_grass2)
        myEnemy.follow(Character, 35)
        animation.run_image_animation(myEnemy,
            [img("""
                    .................ccfff..............
                                ................cddbbf..............
                                ...............cddbbf...............
                                ..............fccbbcf............ccc
                                ........ffffffccccccff.........ccbbc
                                ......ffbbbbbbbbbbbbbcfff.....cdbbc.
                                ....ffbbbbbbbbbcbcbbbbcccff..cddbbf.
                                ....fbcbbbbbffbbcbcbbbcccccfffdbbf..
                                ....fbbb1111ff1bcbcbbbcccccccbbbcf..
                                .....fb11111111bbbbbbcccccccccbccf..
                                ......fccc33cc11bbbbccccccccfffbbcf.
                                .......fc131c111bbbcccccbdbc...fbbf.
                                ........f33c111cbbbfdddddcc.....fbbf
                                .........ff1111fbdbbfddcc........fff
                                ...........cccccfbdbbfc.............
                                .................fffff..............
                """),
                img("""
                    .................ccfff..............
                                ................cddbbf..............
                                ...............cddbbf...............
                                .........ffffffccbbcf...............
                                ......fffbbbbbbbbcccff..............
                                .....fbbbbbbbbbbbbbbbcfff......ccccc
                                .....bcbbbbbffbcbcbbbbcccff...cdbbbc
                                .....bbb1111ffbbcbcbbbcccccffcddbbc.
                                .....fb11111111bcbcbbbcccccccbdbbf..
                                ......fccc33c11bbbbbbcccccccccbbcf..
                                .......fc131cc11bbbbccccccccffbccf..
                                ........f33c1111bbbcccccbdbc..fbbcf.
                                .........ff1111cbbbfdddddcc....fbbf.
                                ...........ccc1fbdbbfddcc.......fbbf
                                ..............ccfbdbbfc..........fff
                                .................fffff..............
                """),
                img("""
                    ..................ccfff.............
                                .................cddbbf.............
                                ........fffffffffddbbf..............
                                .......fbbbbbbbbbfcbcf..............
                                .......fbbc111bffbbccffff...........
                                .......fb111111ffbbbbbcccff....ccccc
                                ........f1cc3311bbcbcbbccccf..cdbbbc
                                ........fcc131c1bbbcbcbcccccfcddbbc.
                                .........f111111bbbcbcbccccccbdbbf..
                                .........f1111111bbbbbccccccccbbcf..
                                ..........f111111bbbbcccccccffbccf..
                                ...........c1111cbbbcccccbdbc.fbbcf.
                                ............cc11cbbbfddddddc...fbbf.
                                ..............cffbdbbfdddcc.....fbbf
                                .................fbdbbfcc........fff
                                ..................fffff.............
                """),
                img("""
                    ....................ccfff...........
                                ..........fffffffffcbbbbf...........
                                .........fbbbbbbbbbfffbf............
                                .........fbb111bffbbbbff............
                                .........fb11111ffbbbbbcff..........
                                .........f1cccc11bbcbcbcccf.........
                                ..........fc1c1c1bbbcbcbcccf...ccccc
                                ............c3331bbbcbcbccccfccddbbc
                                ...........c333c1bbbbbbbcccccbddbcc.
                                ...........c331c11bbbbbcccccccbbcc..
                                ..........cc13c111bbbbccccccffbccf..
                                ..........c111111cbbbcccccbbc.fccf..
                                ...........cc1111cbbbfdddddc..fbbcf.
                                .............cccffbdbbfdddc....fbbf.
                                ..................fbdbbfcc......fbbf
                                ...................fffff.........fff
                """),
                img("""
                    ...........fffffff...ccfff..........
                                ..........fbbbbbbbffcbbbbf..........
                                ..........fbb111bbbbbffbf...........
                                ..........fb11111ffbbbbff...........
                                ..........f1cccc1ffbbbbbcff.........
                                ..........ffc1c1c1bbcbcbcccf........
                                ...........fcc3331bbbcbcbcccf..ccccc
                                ............c333c1bbbcbcbccccfcddbbc
                                ............c333c1bbbbbbbcccccddbcc.
                                ............c333c11bbbbbccccccbbcc..
                                ...........cc331c11bbbbccccccfbccf..
                                ...........cc13c11cbbbcccccbbcfccf..
                                ...........c111111cbbbfdddddc.fbbcf.
                                ............cc1111fbdbbfdddc...fbbf.
                                ..............cccfffbdbbfcc.....fbbf
                                ....................fffff........fff
                """),
                img("""
                    ....................................
                                ....................................
                                ....................................
                                ...............ccffff...............
                                ..............cddbbbf...............
                                .......ffffffcddbbbf................
                                .....ffbbbbbbbbbbbbbcfff.......ccccc
                                ...ffbbbbbbbbcbcbbbbbcccff....cdbbbc
                                ..fbbbbbbbbbbcbbcbbbbcccccfffcddbbc.
                                .fbcbbbbbbbbbbcbcbbbbccccccccbdbbf..
                                .fbbbbbbbfffbbcbbbbbccccccccccbbcf..
                                .ffbb1111fffbbcbbbbcccccccbcffbccf..
                                ..ff111111111bbbbccccccbbbcc..fbbcf.
                                ....ccccccc111bdbbbfddbccc.....ffbbf
                                ........ccccccfbdbbbfcc..........fff
                                ...............ffffff...............
                """)],
            200,
            True)
forever(on_forever4)

def on_forever5():
    global myEnemy
    if info.score() > 200 and ScatterCheck == 1:
        pause(2000)
        myEnemy = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Ghostani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.castle.tile_grass2)
        myEnemy.follow(Character, 35)
forever(on_forever5)

def on_forever6():
    global myEnemy
    if info.score() > 60:
        pause(2000)
        myEnemy = sprites.create(img("""
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
        animation.run_image_animation(myEnemy, assets.animation("""
            Batani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.dungeon.dark_ground_center)
        myEnemy.follow(Character, 35)
forever(on_forever6)

def on_forever7():
    global myEnemy
    if info.score() > 60:
        pause(2000)
        myEnemy = sprites.create(assets.image("""
            Dragen
        """), SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Dragenani
        """), 200, True)
        tiles.place_on_random_tile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
forever(on_forever7)

def on_forever8():
    global myEnemy
    if info.score() > 200 and ScatterCheck == 1:
        pause(2000)
        myEnemy = sprites.create(img("""
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
        animation.run_image_animation(myEnemy, assets.animation("""
            Batani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.dungeon.dark_ground_center)
        myEnemy.follow(Character, 35)
forever(on_forever8)

def on_forever9():
    global myEnemy
    if info.score() > 200 and ScatterCheck == 1:
        pause(2000)
        myEnemy = sprites.create(assets.image("""
            Dragen
        """), SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Dragenani
        """), 200, True)
        tiles.place_on_random_tile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
forever(on_forever9)

def on_forever10():
    global shooty
    if info.score() > 30:
        pause(1000)
        shooty = sprites.create_projectile_from_sprite(assets.image("""
            trowing knife 1
        """), Character, -90, 0)
forever(on_forever10)

def on_forever11():
    global Time, Tid
    pause(1000)
    Time += -1
    Tid = Math.constrain(Tid, 0, 999)
forever(on_forever11)

def on_forever12():
    global myEnemy
    if info.score() < 30:
        pause(5000)
        myEnemy = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Ghostani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.castle.tile_grass2)
        myEnemy.follow(Character, 35)
forever(on_forever12)

def on_forever13():
    global myEnemy
    if info.score() > 30:
        pause(2000)
        myEnemy = sprites.create(img("""
                ........................
                            ........................
                            ........................
                            ........................
                            ..........ffff..........
                            ........ff1111ff........
                            .......fb111111bf.......
                            .......f11111111f.......
                            ......fd11111111df......
                            ......fd11111111df......
                            ......fddd1111dddf......
                            ......fbdbfddfbdbf......
                            ......fcdcf11fcdcf......
                            .......fb111111bf.......
                            ......fffcdb1bdffff.....
                            ....fc111cbfbfc111cf....
                            ....f1b1b1ffff1b1b1f....
                            ....fbfbffffffbfbfbf....
                            .........ffffff.........
                            ...........fff..........
                            ........................
                            ........................
                            ........................
                            ........................
            """),
            SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Ghostani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.castle.tile_grass2)
        myEnemy.follow(Character, 35)
forever(on_forever13)

def on_forever14():
    global myEnemy
    if info.score() < 30:
        pause(5000)
        myEnemy = sprites.create(img("""
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
        animation.run_image_animation(myEnemy, assets.animation("""
            Batani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.dungeon.dark_ground_center)
        myEnemy.follow(Character, 35)
forever(on_forever14)

def on_forever15():
    global myEnemy
    if info.score() < 30:
        pause(5000)
        myEnemy = sprites.create(assets.image("""
            Dragen
        """), SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Dragenani
        """), 200, True)
        tiles.place_on_random_tile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
forever(on_forever15)

def on_forever16():
    global myEnemy
    if info.score() > 30:
        pause(2000)
        myEnemy = sprites.create(img("""
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
        animation.run_image_animation(myEnemy, assets.animation("""
            Batani
        """), 100, True)
        tiles.place_on_random_tile(myEnemy, sprites.dungeon.dark_ground_center)
        myEnemy.follow(Character, 35)
forever(on_forever16)

def on_forever17():
    global myEnemy
    if info.score() > 30:
        pause(2000)
        myEnemy = sprites.create(assets.image("""
            Dragen
        """), SpriteKind.enemy)
        animation.run_image_animation(myEnemy, assets.animation("""
            Dragenani
        """), 200, True)
        tiles.place_on_random_tile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
forever(on_forever17)

def on_forever18():
    global shooty
    if ScatterCheck == 1:
        pause(2000)
        shooty = sprites.create_projectile_from_sprite(assets.image("""
            Scatter2
        """), Character, -50, -300)
        shooty = sprites.create_projectile_from_sprite(assets.image("""
            Scatter2
        """), Character, 0, -300)
        shooty = sprites.create_projectile_from_sprite(assets.image("""
            Scatter2
        """), Character, 50, -300)
forever(on_forever18)
