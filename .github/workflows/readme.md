
ls -a we see that we have:

`./    ../   .git/`

there is no `.github`. We can see only `.git`.

Lets create `.github/workflows/learning_github_actions.yml`

```yml
name: learn-github-actions
run-name: ${{ github.actor }} is learning GitHub Actions
on: [push]
jobs:
  check-bats-version:
    runs-on: ubuntu-latest
    steps:
      - run: echo 'Hello World'
```

Now lets run a Python related worflow:
# reference: https://github.com/actions/setup-python

```yml
name: Python Script Workflow
run-name: ${{ github.actor }} is learning GitHub Actions with a Python example
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.10
    
    - name: Install dependencies
      run: pip install -r requirements/requirements.txt
    
    - name: Run Python script
      run: python main.py
```
`Error: The version '3.1' with architecture 'x64' was not found for Ubuntu 22.04.`

FIX: convert 3.10 to '3.10' it regnognizes it as a string

# Protecting our project
## adding linting, formating and testing

```txt
pandas==1.3.3
flake8==3.9.2
black==21.7b0
pytest==6.2.5
```

lets now add some linting and formating:

we added a `test/test_df.py`

```python
def create_dataframe():
    data = {'Name': ['George', 'Giannis', 'Charlie'],
            'Age': [25, 30, 35]}
    return pd.DataFrame(data)

def test_dataframe_column_names():
    df = create_dataframe()
    expected_columns = ['Name', 'Age']
    assert df.columns.tolist() == expected_columns, "Column names are not as expected"
```
As you see so far it is like creating a new enviroment (ubuntu) and loading our scripts and running them.
We dont care about the hardware or the server. We just choose an OS and test our scripts. We will see a similar concept with Docker.

See the following different approaches:


```yml
name: Python Script Workflow
run-name: ${{ github.actor }} is learning GitHub Actions with a Python example
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"
    
    - name: Install dependencies
      run: pip install -r requirements/requirements.txt
    
    - name: Lint with Flake8
      run: flake8 .
    
    - name: Format code with Black
      run: black .
    
    - name: Run Pytest
      run: pytest
    
    - name: Run Python script
      run: python main.py

    - name: Lint, Format, and Test (run together )
      run: flake8 . && black . && pytest . && python main.py

```
In this example, if any of the commands (flake8, black, pytest, or python main.py) fails (returns a non-zero exit status), the subsequent commands won't execute, and the workflow run will be marked as failed.
