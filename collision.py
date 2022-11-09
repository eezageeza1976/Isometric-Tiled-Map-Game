
def collide(obsticles, player):
    for obs in obsticles:
        for i in range(3):
            clipped_line = player.hit_rect.clipline((obs.points[i].left, obs.points[i].top, obs.points[i+1].left, obs.points[i+1].top))
            if clipped_line:
                start, end = clipped_line
                x1, y1 = start
                x2, y2 = end
                return start
            if i == 2:
                clipped_line = player.hit_rect.clipline((obs.points[i+1].left, obs.points[i+1].top, obs.points[0].left, obs.points[0].top)) 
                if clipped_line:
                    start, end = clipped_line
                    x1, y1 = start
                    x2, y2 = end
                    return start

def collide_with_walls(obsticles, player, dir):
    if dir == 'x':
        hits = collide(obsticles, player)
        if hits:
            if hits[0] > player.rect.centerx:
                player.pos.x = hits[0] - player.hit_rect.width / 2
            if hits[0] < player.rect.centerx:
                player.pos.x = hits[0] + player.hit_rect.width / 2
            player.vel.x = 0
            player.hit_rect.centerx = player.pos.x
    if dir == 'y':
        hits = collide(obsticles, player)
        if hits:
            if hits[1] > player.rect.centery:
                player.pos.y = hits[1] - player.hit_rect.height / 2
            if hits[1] < player.rect.centery:
                player.pos.y = hits[1] + player.hit_rect.height / 2
            player.vel.y = 0
            player.hit_rect.centery = player.pos.y    