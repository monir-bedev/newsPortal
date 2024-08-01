# NewsPortal

> The project basically consists of news portal.

If you want to install the news portal project in your local development server. Please follow the instructions.

### Dependencies
- Python3.12
- PostgreSQL

###### Instructions:

```bash
git clone https://github.com/monir-bedev/newsPortal
cd newsPortal
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> If finally successfully installed then you should run the following command.

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

### Other Resources
> If you want to create a new requirement.txt file you should follow the command below.

```bash
pip freeze > requirements.txt 
```
