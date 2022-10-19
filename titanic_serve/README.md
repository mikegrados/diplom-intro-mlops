**Step 1: Create a virtual environment in your local machine**
> python -m venv my_env

**Step 2: Activate the virtual environment**
> my_env\Scripts\activate.bat

**Step 3: Install requirements**
> pip install -r requirements.txt

**Step 4: In the terminal change to the src folder and run**
> uvicorn inference:app --reload

**Step 5: In a browser copy and paste the following url**
> http://127.0.0.1:8000/docs

**Step 6: Send a POST request with the following data**
```
{
    "pclass": 1,
    "name": "Allen, Miss. Elisabeth Walton",
    "sex": "female",
    "age": "29",
    "sibsp": 0,
    "parch": 0,
    "ticket": "24160",
    "fare": "211.3375",
    "cabin": "B5",
    "embarked": "S",
    "boat": "2",
    "body": "?",
    "home_dest": "St Louis, MO"
}
```