import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from typing import List, Dict
import pydantic
import copy


class SpawmLevelEvent:
    time: int
    enemy_type: str
    position: pygame.Vector2

class SpawnEnemiesData:
    type: str
    size: pygame.Vector2
    color: pygame.Color
    velocity : pygame.Vector2

class SpawnEventData:
    events : List[SpawmLevelEvent]
    enemies : Dict[str, SpawnEnemiesData] 

def crear_cuadrado(ecs_world: esper.World, 
                   size: pygame.Vector2,  
                   pos: pygame.Vector2, 
                   vel: pygame.Vector2, 
                   col: pygame.Color)->None:
    
    
    
    cuad_entity = ecs_world.create_entity()
    ecs_world.add_component(entity = cuad_entity, component_instance=CSurface(size = copy.copy(size), color= col))
    ecs_world.add_component(entity = cuad_entity, component_instance=CTransform(pos=pos))
    ecs_world.add_component(entity = cuad_entity, component_instance=CVelocity(vel = vel))
    
def crear_generador_de_enemigos(ecs_world: esper.World, level : List[Dict[str, str]], enemies : Dict[str,str])->None:
    
    cuad_entity = ecs_world.create_entity()
    ecs_world.add_component(entity = cuad_entity, component_instance=CEnemySpawner(level=level, enemies=enemies))