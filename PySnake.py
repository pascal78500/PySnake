import pygame

pygame.init()

class Snake(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.head = pygame.image.load("head.png")
        self.head = self.head.convert()
        transColor = self.head.get_at((1,1))
        self.head.set_colorkey(transColor)
        self.body = pygame.image.load("body.png")
        self.body = self.body.convert()
        self.body.set_colorkey(transColor)

    def update(self):
        pass

    def reset(self):
        pass

def main():
    print("Welcome in PySnake")
    width = 300
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PySnake")

    #create background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    # create snake
    snake = Snake((10,10))

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_q:
                    run = False

        screen.blit(background,(0,0))
        screen.blit(snake.head,snake.pos)
        screen.blit(snake.body, (10,0))
        pygame.display.flip()




# state management
main()

#exit properly from the application
pygame.quit()