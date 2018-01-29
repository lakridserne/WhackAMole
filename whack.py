import sys, pygame, random
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0
red = 128, 0, 0

screen = pygame.display.set_mode(size)

ur = pygame.time.Clock()

spiller = pygame.image.load("player_martin.png")
spiller_ramt = pygame.image.load("player_hit_martin.png")
hånd = pygame.image.load("hand.png")

frame = 0
framerate = 30

har_ramt = False

klasker = False
klask_pos = (0, 0)

def tegn_bane():
    screen.fill(red)

    boxe = []

    for kolonne in range(3):
        for række in range(2):
            box_bredde = 150
            box_højde = 200
            margin = 60
            offset_bredde = ((width - (3 * box_bredde) - (margin * 2)) / 2) + box_bredde
            offset_højde = (height - (2 * box_højde) - (margin * 2)) + box_højde
            box = pygame.draw.rect(screen, black, ((margin + kolonne * offset_bredde), (margin + række * offset_højde),
                                                    box_bredde, box_højde))
            boxe.append(box)

    # Returner positionerne af alle boxene
    return boxe

while 1:
    for event in pygame.event.get():
        # Check om spillet er afsluttet
        if event.type == pygame.QUIT: sys.exit()
        
        # Check om der er klasket med musen
        if event.type == pygame.MOUSEBUTTONDOWN:
            klasker = True
            klask_pos = event.pos
            
    # Tegn en tom bane
    boxe = tegn_bane()
    
    # Hvert sekundt findes en ny tilfældig box og klask nulstilles
    if(frame % (framerate * 1) == 0):
         spiller_box = random.choice(boxe)
         klasker = False
    
    # Tegn ansigt i boxen
    pygame.Surface.blit(screen, spiller, spiller_box)
    
    # Tegn hånden hvis der ikke er klasket.
    if not klasker:
        mus_x, mus_y = pygame.mouse.get_pos()
        pygame.Surface.blit(screen, hånd, (mus_x-120, mus_y-130))
    else:
        # Hvis der er klasket, så se om der er ramt og tegn ramt ansigt
        if spiller_box.collidepoint(klask_pos):
            pygame.Surface.blit(screen, spiller_ramt, spiller_box)

    # Tegn skærm og updater frame tæller
    pygame.display.flip()
    ur.tick(framerate)
    frame = frame + 1
    
    