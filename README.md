# Enterprise Connection BeduTech

## Setup

Create a `.env` file:
```
SECRET_KEY=secret_key
GOOGLE_API_KEY=google_api_key # uses Places API
```

## Run

```sh
python -m venv venv # optional
.\venv\Scripts\Activate.ps1 # optional

python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```