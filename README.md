# a-light-bike-game-demo-2d



libraries used: pygame


demo.py:
image.load -> transform.scale -> screen.blit
(slow)
or

set_mode(dims, pygame.SCALED)
(optimized)
or

image.load->intermediate.blit->transform.scale->screen.blit
(control/handleing)
