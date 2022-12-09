create database ETL01;
use ETL01;

update streaming 
set duration_num = 0
where duration_num = 'sin';


# Máxima duración según tipo de film (película/serie), por plataforma y por año
select duration_num, title
from streaming
where plataforma = "hulu" and release_year = 2018 and duration_type = 'min'
order by duration_num desc limit 1;


# Cantidad de películas y secories (separado) por plataforma (averiguar si van separados)
select COUNT(*) as 'Cantidad de Peliculas' , type as 'Type'
from streaming
where plataforma = 'netflix'
group by type;


# Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo
select plataforma, COUNT(genero) as frecuencia_genero
from streaming
inner join genero_t
on streaming.index = genero_t.index
where genero = 'comedy'
group by plataforma
order by frecuencia_genero desc limit 1;


# Actor que más se repite según plataforma y año.
select cast, COUNT(cast) as frecuencia_actor , plataforma
from actors
inner join streaming
on actors.index = streaming.index
where plataforma = 'netflix' and release_year = 2018 and cast != 'sin dato'
group by cast
order by frecuencia_actor desc limit 1;
