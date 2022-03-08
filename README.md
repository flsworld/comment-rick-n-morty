<div id="top">

<!-- PROJECT SHIELDS -->

  <h1 align="center">Commenting Rick and Morty</h1>

</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project holds a REST API that allow a user to post a comment on characters
and episodes in the universe of Rick&Morty.


### Built With

* [Docker Compose](https://docs.docker.com/compose/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.


### Prerequisites

Follow the instructions on [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
and make sure you have docker-compose properly installed on your machine.
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/flsworld/comment-rick-n-morty.git && cd comment-rick-n-morty
   ```
2. For security reason the environment file is not committed to the repository. 
    Create an env dotfile inside backend folder
    ```sh
   touch backend/.env
   ```
    Define .env file as following
    ```
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_SERVER=postgres
    POSTGRES_PORT=5432
    POSTGRES_DB=dbname
    
    PYTHONPATH=/backend
   
    ``` 

3. Now build the app container and its linked Postgres database container. In your 
terminal, enter the following command
   ```sh
   docker-compose up --build -d
   ```
4. Documentation with all details about available routes should now be accessible at
   ```
   0.0.0.0:8000/docs
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Populate tables in the database
1. Open an interactive prompt in the web container 
```sh
    docker-compose exec web bash
```

2. Run migrations in order to create tables
```sh
    alembic upgrade head
```

3. Execute the python script that will feed the dedicated tables
```sh
    python app/initial_data.py
```

4. You can make sure everything worked properly by opening a psql prompt and 
making some SQL queries. 

_Close current shell on the web container or open a new tab/window in your shell_
```sh
    docker-compose exec postgres bash
    psql -h localhost -U user --dbname=dbname
```
    
Some useful postgres command
* \l - list all databases
* \d+ - list all tables (relations) in the current database
* \d character - describe the character table and the associated columns

See if everything's fine (non-empty table) with a raw SQL query

```sql
    SELECT * FROM character_episode;
```


<p align="right">(<a href="#top">back to top</a>)</p>

### Launch tests suite
Open a shell in the web container and run all tests with 
```sh
    scripts/run_tests.sh
```
After having launched the tests, it is possible to see the coverage. To do so, open the following file `backend/htmlcov/index.html`
with your browser

### Install pre-commit
In order to remain focus on logic during development while not wasting time with trivial style nitpicks, 
pre-commit - a useful tool upon which it is able to install hooks - has been used. In this project 
* black was used to format the code 
* flake8 was used to check compliance with PEP8

Install pre-commit with
```sh
    pre-commit install
```
Run pre-commit on all files
```sh
    pre-commit run --all-files
```
Uninstall pre-commit
```sh
    pre-commit uninstall
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog
- [x] Add back to top links

<!-- CONTACT -->
## Contact

Frédéric Sautot - [@fsautot](https://twitter.com/fsautot) - frederic.sautot@gmail.com

Project Link: [https://github.com/flsworld/comment-rick-n-morty](https://github.com/flsworld/comment-rick-n-morty)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Credit to Tiangolo ! Awesome documentation

* [The whole fastapi website](https://fastapi.tiangolo.com/)

<sub><sup>A Mako reactor is still standing in this project. I hope the new team from the test setup will handle that Fast so everyone will be api #hihi<sub><sup>
<p align="right">(<a href="#top">back to top</a>)</p>
