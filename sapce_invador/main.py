import pygame
import settings as st
from main_menu import Manage

# Initialize pygame
pygame.init()
pygame.font.init()

# Create a game instance
game = Manage()
game.start_game()

# Main game loop
run = st.RUN
while run:
    st.SCREEN.fill(st.BLACK)


    # Display the start button if it's the start of the game
    if st.DISPLAY_START:
        st.SCREEN.blit(st.START_BUTTON.image, (st.START_BUTTON.rect.x, st.START_BUTTON.rect.y))

    # Handle events
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game.player_shoot()

    # Draw and animate stars in the background
    game.draw_stars()

    # Check if the start button is clicked
    if game.start_clicked():
        game.run_game()

    # Update the display שמג
    pygame.display.flip()
    st.CLOCK.tick(st.FPS)

pygame.quit()