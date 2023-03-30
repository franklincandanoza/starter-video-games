import pygame
import esper
from threading import Timer
import copy

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.create.prefab_creator import crear_cuadrado
    

def system_enemy_spawner(ecs_world: esper.World)->None:
    components = ecs_world.get_components(CEnemySpawner)
    
    c_e:CEnemySpawner
    
    for entity, (c_e) in components:
        for c in c_e:
            if not c.processed:
                for event in c.events:
                    
                    #if event.enemy_type == "TypeA" and event.time == 3:
                    timer = Timer(event.time,crear_cuadrado, kwargs={"ecs_world" : ecs_world,"size" : copy.copy(c.enemies[event.enemy_type].size),"pos" : copy.copy(event.position),"vel": copy.copy(c.enemies[event.enemy_type].velocity), "col" : c.enemies[event.enemy_type].color})
                    timer.start()
                
                c.processed = True  
            