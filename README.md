# Custom Twitter API

It is an API that emulate the twitter data model

## Structure

### Tweets
- GET /tweets/ -> Shows all tweets
- GET /tweets/{id} -> Shows a specific tweet
- POST /tweets/ -> Creates a new tweet
- PUT /tweets/{id} -> Updates a specific tweet
- DELETE /tweets/{id} -> Deletes a specific tweet
### Authentication
- POST /auth/signup -> Registers a new user
- POST /auth/login -> Login a user
### Users
- GET /users/ -> Shows all users
- GET /users/{id} -> Gets a specific user
- PUT /users/{id} -> Updates a specific user
- DELETE /users/{id} -> Deletes a specific use

#### Other Resources
- [REST Resource Naming Guide](https://restfulapi.net/resource-naming/)