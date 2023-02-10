# Installation Setup
* go to nfvpap folder
* `docker compose build`
* setup `.env` from `.env.example`
* `docker compose up -d`
* Run migrate for an init database(之後會用到，目前沒有)
`docker-compose -f docker-compose.yml exec web python manage.py migrate`

# develop
* create the new app
  * `docker-compose -f docker-compose.yml exec web python manage.py startapp [new app name]`
  * create the urls.py in [new app name] folder
  * create new path in urls.py of nfvpap folder 
    ```
    urlpatterns = [
            ...
            path('[new app name]/', include('[new app name].urls')),
            ...
        ]
    ```
  * create new app in setting.py
    ```
    INSTALLED_APPS = [
        ...
        # 自帶模組
        '[new app name]',
        ...
    ]
    ```
  * create new templates folder in [new app name] folder
  * create new [new app name] folder in templates folder
    