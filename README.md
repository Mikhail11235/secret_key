# One-time secret service

This project provides a one-time secret service where users can securely share secrets that are deleted after being viewed.

## Setup Instructions

To run this application, follow these steps:

1. Create an `.env` file in the `./app/` directory and add the following configuration:

    ```dotenv
    # MongoDB Configuration
    MONGO_INITDB_ROOT_USERNAME=YOUR_MONGO_USERNAME
    MONGO_INITDB_ROOT_PASSWORD=YOUR_MONGO_PASSWORD
    MONGO_INITDB_DATABASE=YOUR_MONGO_DB
    MONGO_PORT=YOUR_MONGO_PORT
    
    # Application Configuration
    APP_PORT=YOUR_APP_PORT
    ```


2. Build and run the application using Docker Compose:

    ```bash
    # Build and run with Docker Compose
    $ docker-compose build
    $ docker-compose up
    ```

    **or:**

    ```bash
    # Run MongoDB container with Docker
    $ docker run --name mongodb -d -p ${YOUR_MONGO_PORT}:${YOUR_MONGO_PORT} \
    -e MONGO_INITDB_ROOT_USERNAME=${YOUR_MONGO_USERNAME} \
    -e MONGO_INITDB_ROOT_PASSWORD=${YOUR_MONGO_PASSWORD} \
    -e MONGO_INITDB_DATABASE=${MONGO_INITDB_DATABASE} \
    mongo:latest
    
    # Navigate to the app directory
    $ cd app
    
    # Run the application
    $ uvicorn main:app --reload
    ```


 3. Once the application is running, you can access the API documentation at:

    ```
    http://127.0.0.1:YOUR_APP_PORT/docs
    ```

## Inspiration

This project is inspired by [avito.tech](https://github.com/avito-tech/mi-trainee-task).
