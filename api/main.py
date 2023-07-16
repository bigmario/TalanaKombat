from fastapi import FastAPI, status, Body
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from .fight_schema import FightSchema
from .core.fight_core import narrar_pelea


app = FastAPI()


def __custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Talana Challenge - TalanaKombat",
        version="0.0.1",
        description="Reto Python",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = __custom_openapi

origins = [
    "*",
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Welcome Endpoint
@app.get(
    path="/api/welcome", 
    status_code=status.HTTP_200_OK, 
    summary="Welcome", 
    tags=["Welcome"]
)
async def index():
    return JSONResponse(
        {
            "Framework": "FastAPI",
            "Message": "Hello Human, welcome to Talana Challenge",
        }
    )


# Fight Endpoint
@app.post(
    path="/api/fight",
    status_code=status.HTTP_200_OK,
    summary="Narrate a fight",
    tags=["Fight"]
)
async def fight(
    body: FightSchema = Body(...),    
):
    """
    Narrate fight:
    Provides a narrative of the fight and determines the winner based on established actions and rules. 
    """
    fight = narrar_pelea(body)
    return HTMLResponse(fight)
