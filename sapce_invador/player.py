import pygame
import settings as st
from main_menu import Manage
import entitys

def initialize_game():
    pygame.init()
    pygame.font.init()

def main():
    initialize_game()

    game = Manage()
    game.start_game()

    st.SCREEN.fill(st.BLACK)
    if_start = False
    display_start = True
    start_img = pygame.image.load('start.png').convert_alpha()
    start_button = entitys.Button(350, 300, start_img, 0.8)

    run = st.RUN
    while run:
        st.SCREEN.fill(st.BLACK)
        if display_start:
            st.SCREEN.blit(start_button.image, (start_button.rect.x, start_button.rect.y))

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            handle_event(event, game)

        for star in st.stars:
            star.draw()
            star.fall()

        if start_button.draw(st.SCREEN):
            if_start = True
            display_start = False

        if if_start:
            game.run_game()

        pygame.display.flip()
        st.CLOCK.tick(st.FPS)

    pygame.quit()

def handle_event(event, game):
    if event.type == pygame.QUIT:
        run = False
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game.player_shoot()

if __name__ == "__main__":
    main()

