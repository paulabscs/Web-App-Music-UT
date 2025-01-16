**paulabscs**

# Prototype Distributed End-To-End Web App

This project represents an evolving Python web application comprising a distributed end-to-end structure. Flask, SQLAlchemy, and Pydantic are key features and packages implemented in this application. Flask provides an efficient routing system, essential for any web application. The project employs a database for persistent data storage, enhanced by a repository pattern to streamline content delivery to end users and ensure efficient data management.


## Architectural Overview

The repository pattern orchestrates database operations, such as populating the database with data from structured data sources and retrieving track records. It ensures the systematic conversion of database entities into Data Transfer Objects (DTOs) and JSON-compatible dictionaries, facilitating seamless data serialization and internal logic operations. This pattern supports various transformations between different forms of track representations, ensuring flexibility and consistency in data handling while adhering to object-oriented principles.

### Structure

- Database Layer: /Data/DBContext
- Repository Layer: /RepoContext
- ORM Layer: /Dtos
- Model Layer: /Models
- Controller Layer: /Controllers
- View Layer: /static


## Specifics

### Surface-Level Backend

- APIController.py: Manages API endpoints and handles client requests.
- TrackRepo.py: Defines the repository pattern for accessing and manipulating track data.
- track_dto.py: Represents data transfer objects for tracks.
- track_orm.py: Converts between TrackDTO and ORM models.
- repo_context.py: Encapsulates the repository pattern for data access operations.

### Core Backend

- Program.py: Initializes and configures the Flask app.
- session_manager.py: Manages the creation and lifecycle of database sessions.
- context_manager.py: Provides utility functions for managing database connections and context-specific operations.
- Controller.py: Sets up the database and other controllers.


## Usage Information

### Conda Virtual Environment setup

- Install Conda (miniconda3 Version 24.9.2)
- Create the Environment
- Open your terminal or command prompt, then navigate to the directory where the `yml` file is located. Use the following commands to create and run a new environment from environment.yml:

### Setup Virtual Environment using conda

- conda create --name UT_Music --file environment.yml
- conda activate UT_Music

### Setup VSCode Python Interpreter

- Enter the VSCode command palette type '>select interpreter' 
- Choose 'Python 3.10.6 ('UT_Music') ~\miniconda3\envs\UT_Music\python.exe

### Running the app

- Check your conda environment is activated/the terminal has the prefix (UT_Music)
- 'python Program.py'






