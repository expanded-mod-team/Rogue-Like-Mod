init:
    $ circlewipe = ImageDissolve("wipes/circlewipe-cw.jpg", 1.0, 8)
    $ ccirclewipe = ImageDissolve("wipes/circlewipe-ccw.jpg", 1.0, 8)
    $ bites = ImageDissolve("wipes/bites.jpg", 1.0, 8)
    $ bowtie = ImageDissolve("wipes/bowtie.png", 1.0, 8)
    $ cmet = ImageDissolve("wipes/cmet.jpg", 1.0, 8)
    $ cwside = ImageDissolve("wipes/cw-side.jpg", 1.0, 8)
    $ cwtop = ImageDissolve("wipes/cw-top.jpg", 1.0, 8)
    $ dots = ImageDissolve("wipes/dots.png", 1.0, 8)
    $ edges = ImageDissolve("wipes/edges.png", 1.0, 8)
    $ flips = ImageDissolve("wipes/flips.png", 1.0, 8)
    $ fur = ImageDissolve("wipes/fur.jpg", 1.0, 8)
    $ fur2 = ImageDissolve("wipes/fur.jpg", 0.1, 8)
    $ fur2 = ImageDissolve("wipes/fur.jpg", 0.1, 8)
    $ goslow = ImageDissolve("wipes/goslow.png", 5.0, 8)
    $ letter = ImageDissolve("wipes/letter.png", 1.0, 8)
    $ maze = ImageDissolve("wipes/maze.png", 1.0, 8)
    $ radio = ImageDissolve("wipes/radio.jpg", 1.0, 8)
    $ snake = ImageDissolve("wipes/snake.png", 1.0, 8)
    $ snake2 = ImageDissolve("wipes/snake2.png", 1.0, 8)
    $ snakes = ImageDissolve("wipes/snakes.png", 1.0, 8)
    $ sunshine = ImageDissolve("wipes/sunshine.jpg", 1.0, 8)
    $ glasswool = ImageDissolve("wipes/glasswool.jpg", 1.0, 8)
    $ wet = ImageDissolve("wipes/wet.jpg", 1.0, 8)

    $ w1 = ImageDissolve("wipes/1.jpg", 1.0, 8)
    $ w2 = ImageDissolve("wipes/2.png", 1.0, 8)
    $ w3 = ImageDissolve("wipes/3.jpg", 1.0, 8)
    $ w4 = ImageDissolve("wipes/4.jpg", 1.0, 8)
    $ w5 = ImageDissolve("wipes/5.jpg", 1.0, 8)
    $ w6 = ImageDissolve("wipes/6.jpg", 1.0, 8)
    $ w7 = ImageDissolve("wipes/7.png", 1.0, 8)
    $ w8 = ImageDissolve("wipes/8.jpg", 1.0, 8)
    $ w9 = ImageDissolve("wipes/9.jpg", 1.0, 8)
    $ w10 = ImageDissolve("wipes/10.jpg", 1.0, 8)
    $ w11 = ImageDissolve("wipes/11.jpg", 1.0, 8)
    $ w12 = ImageDissolve("wipes/12.jpg", 1.0, 8)
    $ w13 = ImageDissolve("wipes/13.jpg", 1.0, 8)
    $ w14 = ImageDissolve("wipes/14.png", 1.0, 8)
    $ w15 = ImageDissolve("wipes/15.png", 1.0, 8)
    $ w16 = ImageDissolve("wipes/16.png", 1.0, 8)
    $ w17 = ImageDissolve("wipes/17.png", 1.0, 8)
    $ w18 = ImageDissolve("wipes/18.png", 1.0, 8)
    $ w19 = ImageDissolve("wipes/19.jpg", 1.0, 8)
    $ w20 = ImageDissolve("wipes/20.jpg", 1.0, 8)
    $ w21 = ImageDissolve("wipes/21.jpg", 1.0, 8)
    $ w22 = ImageDissolve("wipes/22.png", 1.0, 8)
    $ w23 = ImageDissolve("wipes/23.png", 1.0, 8)
    $ w24 = ImageDissolve("wipes/24.png", 1.0, 8)
    $ w25 = ImageDissolve("wipes/25.png", 1.0, 8)
    $ w26 = ImageDissolve("wipes/26.png", 1.0, 8)
    $ w27 = ImageDissolve("wipes/27.png", 1.0, 8)
    $ w28 = ImageDissolve("wipes/28.png", 1.0, 8)


    transform blur(child, Loc = StageRight, LocY = 50):  
        #This puts the sprite at a location relative to the sent variable
        contains:
            child
            alpha 1.0
            pos (Loc,LocY)
        contains:
            child
            alpha 0.2
            pos (Loc,LocY)
        contains:
            child
            alpha 0.2
            pos (Loc,LocY)
        contains:
            child
            alpha 0.2
            pos (Loc,LocY)
        contains:
            child
            alpha 0.2
            pos (Loc,LocY)

    transform zoom_blur(child):
        contains:
            child
            alpha 1.0
        contains:
            child
            alpha 0.2 zoom 1.015
        contains:
            child
            alpha 0.2 zoom 1.010
        contains:
            child
            alpha 0.2 zoom 0.995
        contains:
            child
            alpha 0.2 zoom 0.990