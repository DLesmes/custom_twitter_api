#uvicorn
import uvicorn

#fastapi
from fastapi import FastAPI
from fastapi import status

#models
from models import (
    UserLogin,
    User,
    Tweet
)

app = FastAPI()

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Pages"]
) # Called Path operation decorator
def home(): # Called path operation function
    """
    Home page of the API
    This path returns the home page of the API.
    No parameters are required.
    """
    return {
        "Twitter API'": "Working"
    }

if __name__ == "__main__":uvicorn.run(
        "__main__:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=2
    )