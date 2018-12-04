# Application constants
ALMATY = 'ALA'
ASTANA = 'TSE'
MOSCOW = 'MOW'
ST_PETERSBURG = 'LED'
SHYMKENT = 'CIT'

# for creating the query to `search` endpoint
# example query request
# {
#   "query": "ALA-CIT201901121000E"
# }
DIRECTIONS = (
    f'{ALMATY}-{ASTANA}',
    f'{ASTANA}-{ALMATY}',
    f'{ALMATY}-{MOSCOW}',
    f'{MOSCOW}-{ALMATY}',
    f'{ALMATY}-{SHYMKENT}',
    f'{SHYMKENT}-{ALMATY}',
    f'{ASTANA}-{MOSCOW}',
    f'{MOSCOW}-{ASTANA}',
    f'{ASTANA}-{ST_PETERSBURG}',
    f'{ST_PETERSBURG}-{ASTANA}',
)
# For prepare the request of tickets
URL_SEARCH = 'https://api.platform.staging.aviata.team/airflow/search'
# with {"query":"ALA-CIT201812161000E"}

# For constructing the url for get `amount` information with requested before.
RESPONSE_URL = \
    'https://api.platform.staging.aviata.team/airflow/search/results'

# Authorization header
AUTHORIZATION = {
    'Authorization': (
        'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMWM1Z'
        'DZmNy03NGJhLTRmZGUtOGYyMS1kN2JhNDE4YTI3MWMiLCJpc3MiOiJ2RjJmMU'
        'NtSHlzYmRGdmJkR1ZVdE5BNkd3WGplOWhKeiIsImlhdCI6MTU0Mjg4MzA0NSw'
        'iZXhwIjoyODY3Mzk1MDQ1LCJjb25zdW1lciI6eyJpZCI6ImQ5YjNlNzlmLTQ4'
        'YTYtNDM3ZC05MDViLTk3NzQ4ZWVmMDVlZCIsIm5hbWUiOiJjaG9jby1rei5ob'
        '3N0In19.oAcPmer0vsnSZeKUmMvPj0emnQopIQKWcaPg7-_cQgA'
    ),
    'Content-Type': 'application/json'
}

START_RELOAD = '0000'
