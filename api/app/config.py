from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:CMcrpb.12@host.docker.internal:3306/ETL01')

meta = MetaData()
