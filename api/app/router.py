from fastapi import APIRouter
from config import engine
from model import actors,streaming,genero_t
from sqlalchemy import func, select

one = APIRouter()

@one.get("/")
def read_root():
    return {"Hello": "World"}

@one.get('/maxduration')
def maxduration(plataforma:str,year:int,tipo_duracion:str):
    with engine.connect() as conn:
        respuesta = conn.execute(select(streaming.c.duration_num,streaming.c.title)
                                    .where(streaming.c.plataforma==plataforma)
                                    .where(streaming.c.release_year==year)
                                    .where(streaming.c.duration_type==tipo_duracion)
                                     .order_by(streaming.c.duration_num.desc()))
        return respuesta.first()

@one.get('/cantidad_serie_pelicula')
def cantidad_serie_pelicula(plataforma:str):
    with engine.connect() as conn:
            respuesta = conn.execute(select(func.count(streaming.c.type),streaming.c.type)
                                        .where(streaming.c.plataforma==plataforma)
                                        .group_by(streaming.c.type))
            return respuesta.fetchall()

@one.get('/cantidad_genero_plataforma')
def cantidad_genero_plataforma(genero:str):
    with engine.connect() as conn:
        respuesta = conn.execute(select(func.count(streaming.c.plataforma),streaming.c.plataforma)
                                    .join(genero_t,genero_t.c.index == streaming.c.index)
                                    .where(genero_t.c.genero==genero)
                                    .group_by(streaming.c.plataforma)
                                    .order_by(func.count(streaming.c.plataforma).desc()))
        return respuesta.first()

@one.get('/frecuencia_actor')
def frecuencia_actor(plataforma:str,year:int):
    with engine.connect() as conn:
        respuesta = conn.execute(select(func.count(actors.c.cast),actors.c.cast)
                                    .join(streaming,streaming.c.index == actors.c.index)
                                    .where(streaming.c.plataforma==plataforma)
                                    .where(streaming.c.release_year==year)
                                    .where(actors.c.cast!='sin dato')
                                    .group_by(actors.c.cast)
                                    .order_by(func.count(actors.c.cast).desc()))
        return respuesta.first()
