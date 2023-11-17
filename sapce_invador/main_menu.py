import pygame, entitys
import settings as st
import random


class Manage:
    def __init__(self):
        self.bullets_of_player = pygame.sprite.Group()
        self.bullets_of_enemy = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy = None
        self.stars = []
        self.current_life = st.PLAYER_LIFE
        self.player = self.create_player()
        self.flip = False
        self.score = 0
        self.score_increment = 10
        self.font = pygame.font.Font(None, 30)
        self.level_font = pygame.font.Font(None, 50)
        self.game_is_over = False
        self.line = None


    def start_game(self):
        self.create_enemies()
        pygame.display.set_caption("SPASE INVADERS")
    def run_game(self):

        if self.game_is_over:
            self.game_over()
        else:
            self.move_enemy()
            self.enemy_shoot()
            self.line_collide()
            self.check_collision()
            self.pressed_keys()
            self.enemies.update(self.move_enemy())
            self.enemies.draw(st.SCREEN)
            self.bullets_of_player.update()
            self.healthBar()
            self.bullets_of_player.draw(st.SCREEN)
            self.bullets_of_enemy.draw(st.SCREEN)
            self.bullets_of_enemy.update()
            score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            life_text = self.font.render(f'life: {self.current_life}', True, (255, 255, 255))
            self.line = pygame.draw.line(st.SCREEN, 'white', [0, st.LINE_HEIGHT],[st.WIDTH_SCREEN, st.LINE_HEIGHT], 3)

            st.SCREEN.blit(score_text, (10, 10))
            st.SCREEN.blit(life_text, (10, 40))
            st.SCREEN.blit(self.player.image, self.player.rect)
            pygame.display.flip()

    def draw_stars(self):
        for star in st.stars:
            star.draw()
            star.fall()

    def start_clicked(self):
        if st.START_BUTTON.draw(st.SCREEN):
            st.IF_START = True
            st.DISPLAY_START = False

        # If the game has started, run the game
        if st.IF_START:
            return True
    def create_player(self):
        player = entitys.Player(st.PLAYER_IMAGE, st.PLAYER_POS, st.PLAYER_LIFE)
        return player

    def create_enemies(self):
        for x in range(1, st.ROW_OF_ENTMEIS):
            for i in range(1, 9):
                self.enemy = entitys.Invader(st.ENEMY_IMAGE, (i * st.WIDTH, x * st.HEIGHT), st.ENEMY_LIFE, x * 10)
                self.enemies.add(self.enemy)

    def pressed_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move("left")
        if keys[pygame.K_RIGHT]:
            self.player.move("right")

    def enemy_shoot(self):
        if len(self.enemies) != 0:
            enemy_shoot = random.choice(self.enemies.sprites())
            rn = random.random()
            if rn < st.NUM_OF_ENEMY_BULLET:
                bullet = enemy_shoot.shoot(1)
                self.bullets_of_enemy.add(bullet)
        else:
            st.RUN == False
            self.next_level()

    def player_shoot(self):
        if len(self.bullets_of_player) < st.NUM_OF_PLAYER_BULLET:
            shoot = self.player.shoot(-1)
            self.bullets_of_player.add(shoot)

    def move_enemy(self):
        for enemy in self.enemies:
            if enemy.rect.right > st.WIDTH_SCREEN * 39 / 40 \
                    or enemy.rect.left < st.WIDTH_SCREEN / 40:
                return True

    def line_collide(self):
        for bullet in self.bullets_of_enemy:
            if bullet.rect.bottom > st.LINE_HEIGHT:
                bullet.kill()
        for enemy in self.enemies:
            if enemy.rect.bottom > st.LINE_HEIGHT:
                enemy.kill()

    def check_collision(self):
        if pygame.sprite.groupcollide(self.enemies, self.bullets_of_player, True, True):
            self.score += 1
        pygame.sprite.groupcollide(self.bullets_of_enemy, self.bullets_of_player, True, True)

        if pygame.sprite.spritecollide(self.player, self.bullets_of_enemy, True):
            self.current_life -= 1
        if self.current_life == 0 or pygame.sprite.spritecollide(self.player, self.enemies, True) :
            self.game_is_over = True

    def healthBar(self):
        ratio = self.current_life / st.PLAYER_LIFE
        pygame.draw.rect(st.SCREEN, "red", (0, st.HEIGHT_SCREEN - 15, 100, 20))
        pygame.draw.rect(st.SCREEN, "green", (0, st.HEIGHT_SCREEN - 15, 100 * ratio, 20))

    def game_over(self):
        stop_text = self.font.render(f'game over, your score is: {self.score}', True, (255, 255, 255))
        st.SCREEN.blit(stop_text, (200, 200))
        start1_img = pygame.image.load('restart1.png').convert_alpha()
        start_button = entitys.Button(350, 300, start1_img, 0.15)
        st.SCREEN.blit(start_button.image, (start_button.rect.x, start_button.rect.y))
        st.ROW_OF_ENTMEIS = 2
        if start_button.draw(st.SCREEN):
            self.restart()


    def restart(self):

        self.game_is_over = False
        self.enemies.empty()
        self.bullets_of_enemy.empty()
        self.bullets_of_player.empty()
        self.start_game()
        st.PLAYER_SPEED = 5
        st.ENEMY_SPEED = 3
        st.BULLET_SPEED = 5
        st.NUM_OF_PLAYER_BULLET = 4
        st.NUM_OF_ENEMY_BULLET = 0.01
        self.score = 0
        st.PLAYER_LIFE = 3
        st.ENEMY_LIFE = 1
        st.LEVEL = 1
        self.current_life = 3


    def next_level(self):
        st.LEVEL += 1
        st.ROW_OF_ENTMEIS += 1
        st.NUM_OF_ENEMY_BULLET += 0.01
        next_level = self.level_font.render(f'level {st.LEVEL} ', False, (255, 0, 0))
        text_rect = next_level.get_rect()
        text_rect.center = (st.WIDTH_SCREEN // 2, st.HEIGHT_SCREEN // 2)
        pygame.time.delay(1000)
        st.SCREEN.blit(next_level, text_rect )
        pygame.display.update()
        self.bullets_of_enemy.empty()
        self.bullets_of_player.empty()
        pygame.time.delay(2000)
        self.create_enemies()
        st.PLAYER_SPEED += 3
        st.ENEMY_SPEED += 3
        st.BULLET_SPEED += 3
        st.NUM_OF_PLAYER_BULLET += 3






