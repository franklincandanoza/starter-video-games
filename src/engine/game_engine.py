import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.create.prefab_creator import crear_cuadrado

from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_render
from src.ecs.systems.s_screen_bounce import system_screen_bounce

class GameEngine:
    def __init__(self) -> None:
        # 1. Inicializa todo lo que necesitamos para iniciar
        pygame.init() 
        
        # 2. Creamos una ventana y con SCALED es para se ajuste al tamño con una escala mejor
        self.screen = pygame.display.set_mode((640,360),pygame.SCALED) 
        
        # 3. Necesitamos un relos
        self.clock = pygame.time.Clock()
        
        # 4. Variable para saber si el juego está corriendo
        self.is_running = False
    
        # 5. Velocidad de los frames
        self.framerate = 60
        
        # 6. Valor para usar para cálculo del reloj
        self.delta_time = 0    
        
        self.ecs_world = esper.World()
        
    

    # Aquí vemos la implementación del game loop
    def run(self) -> None: 
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        # Creamos la entidad
        crear_cuadrado(ecs_world=self.ecs_world, 
                       size=pygame.Vector2(50,50),
                       pos=pygame.Vector2(150,300), 
                       vel=pygame.Vector2(-200,300), 
                       col = pygame.Color(255,100,100))

    def _calculate_time(self):
        #Mueva el reloj (En caso de ser cero, irá lo más rápido que pueda)
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time()/1000 # Pasamos a segundos

    def _process_events(self):
        for event in pygame.event.get():
            
            # Evento cuando se cierra con la X el navegador o cuando se presiona ALT+F4
            if event.type == pygame.QUIT:
                self.is_running = False
        
    def _update(self):
        system_movement(world=self.ecs_world, delta_time=self.delta_time)
        system_screen_bounce(world=self.ecs_world, screen=self.screen)
        

    def _draw(self):
        # Limpiamos la pantalla
        self.screen.fill(color=(0,200,128))
        
        system_render(world=self.ecs_world, screen = self.screen)
        
        # Presentamos ahora la imagen (desplegarla)
        pygame.display.flip()
        

    def _clean(self):
        pygame.quit()
