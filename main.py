#uvicorn
import uvicorn

#fastapi
from fastapi import FastAPI
from fastapi import status

#python
from typing import List

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

## Users

@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(): 
    pass

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login(): 
    pass

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users(): 
    pass

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user(): 
    pass

@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user(): 
    pass

@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user(): 
    pass

if __name__ == "__main__":uvicorn.run(
        "__main__:app",
        host="localhost",
        port=8000,
        reload=True,
        workers=2
    )