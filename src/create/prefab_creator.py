import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def crear_cuadrado(ecs_world: esper.World, 
                   size: pygame.Vector2,  
                   pos: pygame.Vector2, 
                   vel: pygame.Vector2, 
                   col: pygame.Color)->None:
    
    cuad_entity = ecs_world.create_entity()
    ecs_world.add_component(entity = cuad_entity, component_instance=CSurface(size = size, color= col))
    ecs_world.add_component(entity=cuad_entity, component_instance=CTransform(pos=pos))
    ecs_world.add_component(entity=cuad_entity, component_instance=CVelocity(vel = vel))