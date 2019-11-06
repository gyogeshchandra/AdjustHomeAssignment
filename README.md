# Adjust Home Assignment
#### API Endpoint Documentation:
This api exposes the sample dataset through a single generic HTTP API endpoint using Django Framework

#### Installation Steps:

1. Create and activate virtual environment
    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```

2. Install application requirements and change working directory
    ```
    cd AdjustHomeAssignment
    pip install -r requirements.txt
    ```

3. This API requires Postgres, so
    vi settings.py
    replace necessary information mentioned in this directory:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': "adjust",
                'USER': "usr",
                'PASSWORD': "pass",
                'HOST': "localhost",
                'PORT': "5432",
            }
        }

4. Run migrations. This will insert sample dataset into database. 
    ```
    python manage.py migrate
    ```
5. Start the development server to test API
    ```
    python manage.py runserver
    ```

#### API Usage
The client can do the following operations:

sort_by=column1,...,columnN
order=asc|desc
group_by=column1,...,columnN
columns=column1,...,columnN (columns that the client API requires only)
Filters
country=country1,...,countryN
date_after=YYYY-MM-DD
date_before=YYYY-MM-DD
channel=channel 1,...,channelN
os=os1,...,osN
Data and migrations
The API uses Django's default database, SQLite. The used dataset is stored as "dataset.csv", and is processed and stored on the db using a migrate operation.

Examples
Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order
http://localhost:8000/api/metrics/?columns=impressions,clicks&date_before=2017-06-01&group_by=channel,country&sort_by=clicks&order=desc

Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
http://localhost:8000/api/metrics/?columns=installs&os=ios&date_after=2017-05-01&date_before=2017-05-31&group_by=date&sort_by=date

Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order. 
http://localhost:8000/api/metrics/?columns=revenue&date_after=2017-06-01&date_before=2017-06-01&group_by=os&sort_by=revenue&order=desc

Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.
http://localhost:8000/api/metrics/?country=CA&group_by=channel&sort_by=cpi&order=desc&columns=cpi,spend,installs
