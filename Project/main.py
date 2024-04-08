from fastapi import FastAPI, Request
from db import engine,Base
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import categorys as category_routes
from routes import user as user_routes
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/login", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("reg.html", {"request": request})
@app.get("/base", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
@app.get("/second", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("second.html", {"request": request})
origins = [
    "localhost:3000"  # Assuming your frontend runs on localhost:3000
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that are allowed to make requests.
    allow_credentials=True,  # Whether to support cookies in the requests.
    allow_methods=["*"],  # Specify which method are allowed.
    allow_headers=["*"],  # Specify which headers are allowed.
)
app.include_router(category_routes.router,prefix="/api")
app.include_router(user_routes.router,prefix="/api")
