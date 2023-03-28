import pygame

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
        self.vel_cuad = pygame.Vector2(100,100)
        self.pos_cuad = pygame.Vector2(150,100)
        size_cuad = pygame.Vector2(50,50)
        col_cuad = pygame.Color(255,255,100)
        
        # Creamos la superficio
        self.surf_cuad = pygame.Surface(size_cuad)
        # Coloreamos la superficie
        self.surf_cuad.fill(col_cuad)

    def _calculate_time(self):
        #Mueva el reloj (En caso de ser cero, irá lo más rápido que pueda)
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time()/1000 # Pasamos a segundos

    def _process_events(self):
        for event in pygame.event.get():
            
            # Evento cuando se cierra con la X el navegador o cuando se presiona ALT+F4
            if event.type == pygame.QUIT:
                print("Cerrando la ventana")
                self.is_running = False
        
    def _update(self):
        # Avanzamos en X a 100 pixeles por segundo (Delta time)
        self.pos_cuad.x += self.vel_cuad.x * self.delta_time
        self.pos_cuad.y += self.vel_cuad.y * self.delta_time

    def _draw(self):
        # Limpiamos la pantalla
        self.screen.fill(color=(0,200,128))
        
        # Pintamos el cuadrado
        self.screen.blit(source = self.surf_cuad, dest = self.pos_cuad)
        
        # Presentamos ahora la imagen (desplegarla)
        pygame.display.flip()
        

    def _clean(self):
        pygame.quit()
