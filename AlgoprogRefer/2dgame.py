import pygame

pygame.init()
screen=pygame.display.set_mode((1200,720))
clock=pygame.time.Clock()

running=True
dt=0

player_pos=pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        screen.fill('purple')
        pygame.draw.circle(screen,'red',player_pos,40)

        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 200 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 200 * dt
        if keys[pygame.K_s]:
            player_pos.y += 200 * dt
        if keys[pygame.K_d]:
            player_pos.x += 200 * dt
        
        if player_pos.x <= 0:
            player_pos.x = 0
        elif player_pos.x >= 1200:
            player_pos.x = 1200
        
        if player_pos.y <= 0:
            player_pos.y = 0
        elif player_pos.y >= 720:
            player_pos.y = 720
            
        pygame.display.flip()
        dt=clock.tick(60)/1000
pygame.quit()