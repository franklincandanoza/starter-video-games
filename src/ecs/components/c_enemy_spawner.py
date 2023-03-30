
import pygame
from typing import Dict, List, Any
import pydantic
import dataclasses
import copy

###############################################
#                     Enemy                   #
###############################################

class Size(pydantic.BaseModel):
    x: int
    y : int
    
class Color(pydantic.BaseModel):
    r: int
    g: int
    b: int
    
class JsonEnemy(pydantic.BaseModel):
    size: Size
    color : Color
    velocity_min: int
    velocity_max: int
    
###############################################
#                     Event                   #
###############################################
class JsonPosition(pydantic.BaseModel):
    x: int
    y: int
    
class JsonEvent(pydantic.BaseModel):
    time: int
    enemy_type: str
    position: JsonPosition
    
class JsonLevel(pydantic.BaseModel):
    enemy_spawn_events: List[JsonEvent]
    
###############################################
#                     Game Data               #
###############################################

@dataclasses.dataclass
class SpawmLevelEvent:
    time: int
    enemy_type: str
    position: pygame.Vector2

@dataclasses.dataclass
class SpawnEnemiesData:
    type: str
    size: pygame.Vector2
    color: pygame.Color
    velocity : pygame.Vector2

class CEnemySpawner:
    
    def __init__(self, level : List[Dict[str, str]], enemies : Dict[str,Any]) -> None:
        """
        Recibe información de los diferentes archivos y construye un SpawnLevelEvent basado a esta data
        """  
        self.enemies = self._build_enemies_data(enemies = enemies)
        self.events = self._build_events_data(levels = level)
        self.processed = False
        
    
    def _build_enemies_data(self,enemies : Dict[str,str])->Dict[str, SpawnEnemiesData] :
        
        info = {}
        
        for enemy in enemies.keys():
            enemy_type = enemy
            json_enemy = JsonEnemy(**enemies[enemy_type])
            
            spawn_enemies_data = SpawnEnemiesData(
                type = enemy_type,
                size = pygame.Vector2(json_enemy.size.x, json_enemy.size.y),
                color = pygame.Color(json_enemy.color.r, json_enemy.color.g, json_enemy.color.b),
                velocity = pygame.Vector2(json_enemy.velocity_min, json_enemy.velocity_max)
            )
            info[enemy_type] = spawn_enemies_data 
            
        return info
            
            
    
    def _build_events_data(self,levels : Dict[str, str])->List[SpawmLevelEvent]:
        
        return list(
            map(lambda event: SpawmLevelEvent(time=event.time, 
                                              enemy_type=event.enemy_type, 
                                              position=pygame.Vector2(event.position.x, 
                                                                      event.position.y)
                                              ),
                JsonLevel.parse_obj(levels).enemy_spawn_events )
            )
        
        
        