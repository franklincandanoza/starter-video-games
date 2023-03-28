import esper   

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity    
        
def system_movement(world: esper.World, delta_time: float)-> None:
    components = world.get_components(CTransform, CVelocity)
    
    c_t:CTransform
    c_v:CVelocity
    
    for entity, (c_t, c_v) in components:
        c_t.pos.x += c_t.pos.x * delta_time
        c_v.vel.y += c_v.vel.y * delta_time