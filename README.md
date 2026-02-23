# CS50 Intro to AI with Python

My solutions to Harvard's introduction to AI programming. If you want to check the solutions or build on them, see the installation guide below.

## Installation 

1. Install [Pyenv](https://github.com/pyenv/pyenv).

2. Install Python 3.12 with Pyenv.
    ```
    pyenv install 3.12
    ```

3. Clone or fork this repo.

4. cd into this repo, and set the local Python version to 3.12, before checking if correct.
    ```
    cd path/to/your/version/of/this/repo
    pyenv local 3.12.
    python --version # should show some version of Python 3.12
    ``` 
5. Install dependencies within virtual environment.

    ```
    python -m venv .venv
    source .venv/bin/activate 
    pip install -r requirements.txt
    ```