namespace SpriteKind {
    export const Immune = SpriteKind.create()
    export const trough = SpriteKind.create()
    export const DungeonKey = SpriteKind.create()
    export const SuperEnemy = SpriteKind.create()
    export const Scatterani = SpriteKind.create()
    export const coin = SpriteKind.create()
    export const SuperShield = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Immune, SpriteKind.SuperEnemy, function (sprite2, otherSprite2) {
    info.changeCountdownBy(-10)
    sprites.destroy(otherSprite2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.trough, function (sprite, otherSprite) {
    sprites.destroy(otherSprite)
    Truefalse = 1
    TextCheck = 1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.coin, function (sprite6, otherSprite6) {
    sprites.destroy(otherSprite6, effects.confetti, 500)
    coinsnumber += 1
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite5, otherSprite5) {
    info.changeScoreBy(1)
    sprites.destroy(otherSprite5)
    if (info.score() < 40) {
        sprites.destroy(sprite5)
    }
})
sprites.onOverlap(SpriteKind.Immune, SpriteKind.coin, function (sprite9, otherSprite9) {
    sprites.destroy(otherSprite9, effects.confetti, 500)
    coinsnumber += 1
})
function Key () {
    for (let value of tiles.getTilesByType(sprites.swamp.swampTile16)) {
        KeyDungeon = sprites.create(img`
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
            `, SpriteKind.DungeonKey)
        tiles.placeOnTile(KeyDungeon, value)
        tiles.setTileAt(value, sprites.dungeon.darkGroundCenter)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.SuperEnemy, function (sprite3, otherSprite3) {
    sprites.destroy(otherSprite3)
    info.changeScoreBy(1)
})
info.onScore(60, function () {
    game.showLongText("Level hard", DialogLayout.Center)
    Character.setPosition(450, 450)
})
info.onScore(30, function () {
    game.showLongText("Level medium", DialogLayout.Center)
    Character.setPosition(450, 450)
})
sprites.onOverlap(SpriteKind.SuperShield, SpriteKind.Enemy, function (sprite22, otherSprite22) {
    sprites.destroy(otherSprite22, effects.disintegrate, 500)
})
sprites.onOverlap(SpriteKind.SuperShield, SpriteKind.SuperEnemy, function (sprite24, otherSprite24) {
    sprites.destroy(otherSprite24, effects.disintegrate, 500)
})
info.onCountdownEnd(function () {
    sprites.destroyAllSpritesOfKind(SpriteKind.SuperShield)
    sprites.destroyAllSpritesOfKind(SpriteKind.Immune)
    sprites.destroyAllSpritesOfKind(SpriteKind.SuperEnemy)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    Character = sprites.create(img`
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
        `, SpriteKind.Player)
    Character.setPosition(450, 450)
    SuperCheck = 0
    scene.cameraFollowSprite(Character)
    animation.runImageAnimation(
    Character,
    assets.animation`myAnim1`,
    200,
    true
    )
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.DungeonKey, function (sprite4, otherSprite4) {
    sprites.destroy(otherSprite4)
    for (let value2 of tiles.getTilesByType(sprites.dungeon.doorLockedNorth)) {
        tiles.setWallAt(value2, false)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Scatterani, function (sprite8, otherSprite8) {
    sprites.destroy(otherSprite8)
    ScatterCheck = 1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SuperEnemy, function (sprite7, otherSprite7) {
    info.changeLifeBy(-1)
    pause(500)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite32, otherSprite32) {
    info.changeLifeBy(-1)
    music.play(music.stringPlayable("C5 C5 - - - - - - ", 1000), music.PlaybackMode.UntilDone)
})
info.onScore(50, function () {
    game.splash("Whip Unlocked")
})
info.onScore(200, function () {
    game.showLongText("Level Insane!", DialogLayout.Center)
    Character.setPosition(450, 450)
})
sprites.onOverlap(SpriteKind.Immune, SpriteKind.Enemy, function (sprite23, otherSprite23) {
    sprites.destroy(otherSprite23)
})
info.onScore(40, function () {
    game.splash("Bullet Phase Unlocked")
    pause(5000)
})
function Variables () {
    Truefalse = 0
    Tid = 0
    TextCheck = 0
    ScatterCheck = 0
    coinsnumber = 0
    SuperCheck = 0
}
let Whip: Sprite = null
let myEnemy: Sprite = null
let shooty: Sprite = null
let Time = 0
let Tid = 0
let ScatterCheck = 0
let SuperCheck = 0
let KeyDungeon: Sprite = null
let coinsnumber = 0
let TextCheck = 0
let Truefalse = 0
let coins: Sprite = null
let Character: Sprite = null
tiles.setCurrentTilemap(tilemap`Map`)
game.showLongText("The year is 345 bc, Monsters have taken over the world.", DialogLayout.Top)
game.showLongText("you are tasked with destorying as many monsters before they inevitable get to you", DialogLayout.Bottom)
Character = sprites.create(img`
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
    `, SpriteKind.Player)
let phase = sprites.create(img`
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
    `, SpriteKind.trough)
let Scatter = sprites.create(assets.image`Scatter`, SpriteKind.Scatterani)
Scatter.setPosition(760, 23)
animation.runImageAnimation(
Scatter,
assets.animation`Scatterani`,
200,
true
)
animation.runImageAnimation(
phase,
assets.animation`PhaseTrough`,
200,
true
)
animation.runImageAnimation(
Character,
assets.animation`myAnim1`,
200,
true
)
phase.setPosition(31, 270)
scene.cameraFollowSprite(Character)
Character.setPosition(randint(0, 600), randint(0, 600))
Key()
Variables()
info.setLife(10)
game.setGameOverMessage(false, "You snooze you loose")
for (let index = 0; index < 5; index++) {
    coins = sprites.create(assets.image`coin`, SpriteKind.coin)
    coins.setPosition(randint(0, 600), randint(0, 600))
}
game.onUpdate(function () {
    controller.moveSprite(Character)
})
game.onUpdate(function () {
    if (Truefalse == 1 && Time < 0) {
        if (SuperCheck == 0) {
            sprites.destroyAllSpritesOfKind(SpriteKind.Player)
            sprites.destroyAllSpritesOfKind(SpriteKind.SuperShield)
            sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
            Character = sprites.create(assets.image`Shield Character`, SpriteKind.Immune)
            Time = 80
            if (TextCheck == 1) {
                game.splash("Shield Unlocked")
                TextCheck = 0
            }
            animation.runImageAnimation(
            Character,
            assets.animation`ShieldChar`,
            200,
            true
            )
            Character.setPosition(450, 450)
            scene.cameraFollowSprite(Character)
            info.startCountdown(20)
        }
    }
})
game.onUpdateInterval(1000, function () {
    shooty = sprites.createProjectileFromSprite(assets.image`throwing knife 2`, Character, 90, 0)
})
forever(function () {
    if (info.score() > 30) {
        pause(1000)
        shooty = sprites.createProjectileFromSprite(assets.image`trowing knife 1`, Character, -90, 0)
    }
})
forever(function () {
    pause(1000)
    Time += -1
    Tid = Math.constrain(Tid, 0, 999)
})
forever(function () {
    if (info.score() < 30) {
        pause(5000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Ghostani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.castle.tileGrass2)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 30) {
        pause(2000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Ghostani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.castle.tileGrass2)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() < 30) {
        pause(5000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Batani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.dungeon.darkGroundCenter)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() < 30) {
        pause(5000)
        myEnemy = sprites.create(assets.image`Dragen`, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Dragenani`,
        200,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 30) {
        pause(2000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Batani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.dungeon.darkGroundCenter)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 30) {
        pause(2000)
        myEnemy = sprites.create(assets.image`Dragen`, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Dragenani`,
        200,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (ScatterCheck == 1) {
        pause(2000)
        shooty = sprites.createProjectileFromSprite(assets.image`Scatter2`, Character, -50, -300)
        shooty = sprites.createProjectileFromSprite(assets.image`Scatter2`, Character, 0, -300)
        shooty = sprites.createProjectileFromSprite(assets.image`Scatter2`, Character, 50, -300)
    }
})
forever(function () {
    if (coinsnumber == 5) {
        sprites.destroyAllSpritesOfKind(SpriteKind.Immune)
        sprites.destroyAllSpritesOfKind(SpriteKind.Player)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        Character = sprites.create(img`
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
            `, SpriteKind.SuperShield)
        SuperCheck = 1
        scene.cameraFollowSprite(Character)
        animation.runImageAnimation(
        Character,
        assets.animation`SuperShieldani`,
        500,
        true
        )
        coinsnumber = 0
        info.startCountdown(40)
    }
})
forever(function () {
    if (info.score() > 50) {
        pause(1000)
        Whip = sprites.createProjectileFromSprite(assets.image`ShootDash`, Character, 0, 100)
        pause(500)
        sprites.destroy(Whip, effects.disintegrate, 500)
    }
})
forever(function () {
    if (info.score() > 60) {
        pause(2000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Ghostani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.castle.tileGrass2)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 60) {
        pause(2000)
        myEnemy = sprites.create(assets.image`shark`, SpriteKind.SuperEnemy)
        tiles.placeOnRandomTile(myEnemy, sprites.castle.tileGrass2)
        myEnemy.follow(Character, 35)
        animation.runImageAnimation(
        myEnemy,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        true
        )
    }
})
forever(function () {
    if (info.score() > 200 && ScatterCheck == 1) {
        pause(2000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Ghostani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.castle.tileGrass2)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 60) {
        pause(2000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Batani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.dungeon.darkGroundCenter)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 60) {
        pause(2000)
        myEnemy = sprites.create(assets.image`Dragen`, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Dragenani`,
        200,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 200 && ScatterCheck == 1) {
        pause(2000)
        myEnemy = sprites.create(img`
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
            `, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Batani`,
        100,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.dungeon.darkGroundCenter)
        myEnemy.follow(Character, 35)
    }
})
forever(function () {
    if (info.score() > 200 && ScatterCheck == 1) {
        pause(2000)
        myEnemy = sprites.create(assets.image`Dragen`, SpriteKind.Enemy)
        animation.runImageAnimation(
        myEnemy,
        assets.animation`Dragenani`,
        200,
        true
        )
        tiles.placeOnRandomTile(myEnemy, sprites.builtin.brick)
        myEnemy.follow(Character, 35)
    }
})
