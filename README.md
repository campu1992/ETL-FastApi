# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="https://images.prismic.io/northcoders/1d4f4f17-ee87-454c-8db0-6e7f4974a312_Screen+Shot+2022-08-24+at+11.41.11.png?auto=compress%2Cformat&rect=0%2C0%2C1914%2C1072&w=800&fit=max&q=60"  height=300>
</p>



<hr>  

## **Introducción**  

Mi nombre es Carlos Campuzano de DATA05, este es mi primer proyecto de ETL para Henry.
La idea de este proyecto es interiorizar los conocimientos aprendidos en las clases y ser capaz de realizar todo el proceso de ETL para posteriormente hacer la elaboración y ejecución de una API.



## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos que nos proporciona Henry, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para realizar las consultas a través de una API. 


Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)

## **Tecnologias usadas**

+ Python

+ Mysql
  
+ FastApi

+ Docker


## **Pasos del proyecto**  

<p align="center">
<img src="https://learn.microsoft.com/pt-br/azure/architecture/data-guide/images/etl.png"  height=400>
</p>  
  

1. Ingesta y normalización de datos mediante Python y sus librerias como pandas, numpy.

2. Creacion de Base de datos y carga de archivos mediante sqlalchemy.

3. Creacion de Api en en un entorno virtual dockerizado.

4. Realizar consultas solicitadas

6. Video demostrativo: https://drive.google.com/file/d/10Z9xHa494Kj2y5LVDjdgxru_d9u3BV3C/view?usp=sharing


## **Conclusión**  

Fue un trabajo muy desafiante que me llevo al limite. Aprendi cosas que jamas hubiera imaginado como FastApi y Docker.
La verdad me llevo una alegria muy grande al poder terminar este trabajo y quedarme con todos estos conocimientos.
Tambien reforce mis conocimientos en pandas y sql.  
Saludos cordiales!  
Carlos Campuzano  

<p align="center">
<img src="https://clubedosgeeks.com.br/wp-content/uploads/2016/01/dormrm.gif"  height=400>
</p>  
  

