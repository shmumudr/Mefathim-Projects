import pygame
import settings as st

class Entity(pygame.sprite.Sprite):
    """
    Base class for game entities.
    """
    def __init__(self, img, position, life):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.life = life
        self.rect = self.image.get_rect()
        self.rect.center = position
    def shoot(self, direction):
        """
        Create a Bullet instance to represent a shot fired by the entity.
        - direction: The direction of the shot (1 for up, -1 for down).
        Returns:
        - bullet: The Bullet instance representing the shot.
        """
        bullet = Bullet(st.BULLET_IMAGE, (self.rect.center), direction)
        return bullet


class Player(Entity):
    """
    Class representing the player entity.
    """
    def __init__(self, img, position, life):
        super().__init__(img, position, life)

    def move(self, key):
        """
        Move the player entity based on the input key.
        """
        if key == "left":
            self.rect.centerx -= st.PLAYER_SPEED
        if key == "right":
            self.rect.centerx += st.PLAYER_SPEED
        self.rect.clamp_ip(st.SCREEN_RECT)



class Invader(Entity):
    """
    Class representing an invader entity (enemy).
    """
    def __init__(self, img, position, life, score):
        super().__init__(img, position, life)
        self.direction = 1
        self.score = score

    # Update the position of the invader based on its direction.
    def update(self, flip=False):
        factor = 0
        if flip:
            self.direction *= -1
            factor = 1

        self.rect.move_ip(st.ENEMY_SPEED * self.direction, st.ENEMY_SPEED * factor)


class Bullet(Entity):
    """
    Class representing a bullet entity.
    """
    def __init__(self, img,  position, direction):
        super().__init__(img, position, direction)
        self.direction = direction
        self.image.fill('red',special_flags=pygame.BLEND_RGBA_MIN)

    # Update the position of the bullet based on its direction.
    def update(self):
        self.rect.move_ip(0, self.direction * st.BULLET_SPEED)
        if self.rect.bottom < 0 or self.rect.bottom > st.HEIGHT_SCREEN:
            self.kill()

    # Render the bullet on the screen.
    def render(self, screen):
       screen.blit(self.image, self.rect)


class Button:
    """
    Class representing a clickable button.
    """

    def __init__(self, x, y, image, scale):

        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image.fill('red', special_flags=pygame.BLEND_RGBA_MIN)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.hovered = False

    def hover(self):
        """
        Check if the button is hovered by the mouse cursor and update appearance accordingly.
        """
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.hovered = True
            # Change button appearance to indicate hovering
            self.image.fill((0, 80, 80), special_flags=pygame.BLEND_RGBA_MAX)
        else:
            self.hovered = False
            # Change button appearance back to normal
            self.image.fill('red', special_flags=pygame.BLEND_RGBA_MIN)

    def draw(self, surface):
        """
        Draw the button on the specified surface.
        """
        action = False
        pos = pygame.mouse.get_pos()

        # Check for hovering and update appearance
        self.hover()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action


class Star(object):
    def __init__(self, x, y, yspeed):
        self.colour = st.WHITE
        self.radius = 1
        self.x = st.x
        self.y = st.y
        self.yspeed = st.yspeed

    def draw(self):
        pygame.draw.circle(st.SCREEN, self.colour, (self.x, self.y), self.radius)

    def fall(self):
        self.y += self.yspeed
        self.check_if_i_should_reappear_on_top()

    def check_if_i_should_reappear_on_top(self):
        if self.y >= st.HEIGHT_SCREEN:
            self.y = 0