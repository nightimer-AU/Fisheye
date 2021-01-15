

# PYGAME IS REQUIRED
try:
    import pygame
    from pygame import Color, Surface, SRCALPHA, RLEACCEL, BufferProxy
    from pygame.surfarray import pixels3d, array_alpha, pixels_alpha, array3d
    from pygame.image import frombuffer
    import pathlib
    import FishEyeAlgorithm
except ImportError:
    print("\n<Pygame> library is missing on your system."
          "\nTry: \n   C:\\pip install pygame on a window command prompt.")
    raise SystemExit

if __name__ == '__main__':

    w, h = 400, 400
    screen = pygame.display.set_mode((w * 2, h))
    imagepath = pathlib.Path('images/EMARALD.jpg')
    background = pygame.image.load('back.png').convert()
    background.set_alpha(None)

    surface24 = pygame.image.load(imagepath).convert()
    surface32 = pygame.image.load(imagepath).convert_alpha()

    background = pygame.transform.smoothscale(background, (w * 2, h))
    surface24 = pygame.transform.smoothscale(surface24, (w, h))
    surface32 = pygame.transform.smoothscale(surface32, (w, h))

    i = 0
    fisheye_surface = FishEyeAlgorithm.fish_eye(surface32)
    while 1:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                MOUSE_POS = event.pos

        if keys[pygame.K_F8]:
            pygame.image.save(screen, 'Screendump' + str(i) + '.png')
            
        if keys[pygame.K_ESCAPE]:
            break

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(fisheye_surface, (0, 0))
        screen.blit(surface24, (w, 0))
        pygame.display.flip()

        i += 1
    pygame.quit()
