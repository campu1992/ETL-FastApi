from fastapi import FastAPI
from router import one

app = FastAPI()





app.include_router(one)