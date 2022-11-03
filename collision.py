
def collide(obsticles, player):
    for obs in obsticles:
        x1 = obs.points[0].left
        y1 = obs.points[0].top
        x2 = obs.points[1].left
        y2 = obs.points[1].top
        x3 = obs.points[2].left
        y3 = obs.points[2].top
        x4 = obs.points[3].left
        y4 = obs.points[3].top

        clipped_line = player.hit_rect.clipline((x1, y1, x2, y2))

        if clipped_line:
            print("COLLISION")
    # cx = player[0]
    # cy = player[1]

    # for obs in obsticles:
    #     x1 = obs.points[0].left
    #     y1 = obs.points[0].top
    #     x2 = obs.points[1].left
    #     y2 = obs.points[1].top
    #     x3 = obs.points[2].left
    #     y3 = obs.points[2].top
    #     x4 = obs.points[3].left
    #     y4 = obs.points[3].top

        

    #     m = (y2-y1)/(x2-x1)

    #     if (m * (cx-x1) + y1) == cy:
    #         print("COLLISION")
    #     if (m * (cx-x2) + y2) == cy:
    #         print("COLLISION")
    #     if (m * (cx-x3) + y3) == cy:
    #         print("COLLISION")
    #     if (m * (cx-x4) + y4) == cy:
    #         print("COLLISION")

        # print(x1, y1)
        # print(x2, y2)
        # print(x3, y3)
        # print(x4, y4)



        
    # the two points that define the line
    # p1 = [1, 6]
    # p2 = [3, 2]

    # extract x's and y's, just for an easy code reading
    # x1, y1 = p1
    # x2, y2 = p2

    # m = (y2-y1)/(x2-x1)

    # your centroid
    # centroid = [2,4]
    # x3, y3 = centroid

    # check if centroid belongs to the line
    # if (m * (x3-x1) + y1) == y3:
    #     print("Centroid belongs to line")