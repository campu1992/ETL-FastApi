
from sqlalchemy import Table, Column 
from sqlalchemy.types import Integer, String
from config import engine, meta

actors= Table("actors",meta,
        Column("index",Integer),
        Column("cast",String(150)))

genero_t = Table("genero_t",meta,
         Column("index",Integer),
         Column("genero",String(150)))

streaming = Table("streaming",meta,
            Column("index",Integer),
            Column("type",String(150)),
            Column("title",String(150)),
            Column("release_year",Integer),
            Column("duration_num",Integer),
            Column("duration_type",String(150)),
            Column("plataforma",String(150)))

meta.create_all(engine)