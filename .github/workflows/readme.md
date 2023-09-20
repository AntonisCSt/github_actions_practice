
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
