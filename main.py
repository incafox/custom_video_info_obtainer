# from typing import Optional
import uvicorn
from fastapi import FastAPI, APIRouter, Depends
from routers import users
from routers import scraper
# from routers import users
# router = APIRouter(
#     prefix="/items",
#     tags=["items"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
app = FastAPI()
app.include_router(users.router)
app.include_router(scraper.router)

@app.get("/")
async def root():
    return {"message": "ssScraper is running updattte"}

if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
