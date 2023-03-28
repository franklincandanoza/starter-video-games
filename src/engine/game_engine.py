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
        pass

    def _calculate_time(self):
        pass

    def _process_events(self):
        for event in pygame.event.get():
            
            # Evento cuando se cierra con la X el navegador o cuando se presiona ALT+F4
            if event.type == pygame.QUIT:
                print("Cerrando la ventana")
                self.is_running = False
        
    def _update(self):
        pass

    def _draw(self):
        # Limpiamos la pantalla
        self.screen.fill(color=(0,200,128))
        
        # Presentamos ahora la imagen (desplegarla)
        pygame.display.flip()
        

    def _clean(self):
        pygame.quit()
