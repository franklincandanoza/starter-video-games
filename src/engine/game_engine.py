import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.create.prefab_creator import crear_generador_de_enemigos, SpawmLevelEvent
from threading import Timer
import json
import pydantic


from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_render
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner

class Size(pydantic.BaseModel):
    w: int
    h: int
    
class Color(pydantic.BaseModel):
    r: int
    g: int
    b: int
    
class Windows(pydantic.BaseModel):
    title: str
    size : Size
    bg_color : Color
    framerate: int

class GameEngine:
    def __init__(self) -> None:
        # 1. Inicializa todo lo que necesitamos para iniciar
        pygame.init() 
        
        # 2. Creamos una ventana y con SCALED es para se ajuste al tamño con una escala mejor
        # 3. Necesitamos un relos
        self.clock = pygame.time.Clock()
        
        # 4. Variable para saber si el juego está corriendo
        self.is_running = False
    
        # 6. Valor para usar para cálculo del reloj
        self.delta_time = 0    
        
        self.ecs_world = esper.World()
        
    

    # Aquí vemos la implementación del game loop
    def run(self) -> None: 
        #self._create()
        self._load_configuration()
        self._create_spaw()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()
        
    def _load_configuration(self):
        
        with open('assets/cfg/enemies.json') as enemies_json_file, open('assets/cfg/level_01.json') as level_json_file, open('assets/cfg/window.json') as window_json_file :
        
            self.enemies = json.load(enemies_json_file)
            self.level = json.load(level_json_file)
            self.window = Windows(**json.load(window_json_file))
            
        self.screen = pygame.display.set_mode((self.window.size.w,self.window.size.h),pygame.SCALED)
        pygame.display.set_caption(self.window.title)
        
        
        
    def _create_spaw(self):
        crear_generador_de_enemigos(ecs_world=self.ecs_world, level = self.level, enemies=self.enemies)
    
    def _calculate_time(self):
        #Mueva el reloj (En caso de ser cero, irá lo más rápido que pueda)
        self.clock.tick(self.window.framerate)
        self.delta_time = self.clock.get_time()/1000 # Pasamos a segundos

    def _process_events(self):
        for event in pygame.event.get():
            
            # Evento cuando se cierra con la X el navegador o cuando se presiona ALT+F4
            if event.type == pygame.QUIT:
                self.is_running = False
        
    def _update(self):
        system_movement(world=self.ecs_world, delta_time=self.delta_time)
        system_screen_bounce(world=self.ecs_world, screen=self.screen)
        system_enemy_spawner(ecs_world=self.ecs_world)
        

    def _draw(self):
        # Limpiamos la pantalla
        self.screen.fill(color=(self.window.bg_color.r,self.window.bg_color.g, self.window.bg_color.b))
        
        system_render(world=self.ecs_world, screen = self.screen)
        
        # Presentamos ahora la imagen (desplegarla)
        pygame.display.flip()
        

    def _clean(self):
        pygame.quit()
