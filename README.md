
# Notepad App (Django & Reactjs)

A Notepad App that seamlessly integrates the power of Django and React.js frameworks. With this app, you can jot down your thoughts, ideas, and reminders effortlessly. Whether you're creating new notes, editing existing ones, or organizing your thoughts.

## Preview
![Preview](./img.png)

## Demo

link to demo
![](notpad.gif)
(https://screenrec.com/share/ePnAoVgUtK)
## Installation

Install my-project with npm

```bash
  npm create-react-app
```
```bash
list of npm package installed:

├── @testing-library/jest-dom@5.17.0
├── @testing-library/react@13.4.0
├── @testing-library/user-event@13.5.0
├── react-dom@18.2.0
├── react-router-dom@6.22.3
├── react-scripts@5.0.1
├── react@18.2.0
└── web-vitals@2.1.4
```
Install requirment python package:
```bash

    asgiref==3.7.2
    backports.zoneinfo==0.2.1
    Django==4.2.11
    django-cors-headers==4.3.1
    djangorestframework==3.14.0
    psycopg2==2.9.9
    pytz==2024.1
    sqlparse==0.4.4
    typing-extensions==4.10.0
    tzdata==2024.1
```
## From Setup to Deployment

First is to setup Backend and Frontend below is steps:

```bash
  create a folder
```
```bash
  create one folder name BE in that.
```
```bash
  setup venv for BE using cmd:

  python -m venv {name_env}
```
```bash
  install requirment package:
    asgiref==3.7.2
    backports.zoneinfo==0.2.1
    Django==4.2.11
    django-cors-headers==4.3.1
    djangorestframework==3.14.0
    psycopg2==2.9.9
    pytz==2024.1
    sqlparse==0.4.4
    typing-extensions==4.10.0
    tzdata==2024.1
```
```bash
  now in the main folder create FE folder by cmd:
  npx create-react-app {name_of_folder_for_forntend}
```
```bash
  So now you will have two folder in the main folder
```
```bash
  after completing setup now we need BE (Django) url to give allow the permission to use when integrating with FE (Reactjs):

  install in python env -- django-cors-headers

  in settings.py of your project name:
  add in INSTALL_APPS --- " 'corsheaders', " 
  add in MIDDELEWARE --- "'corsheaders.middleware.CorsMiddleware',"
  and at end of file add " CORS_ALLOW_ALL_ORIGINS = True"
```

To deploy this project to run in same local host.

```bash
  After complete of Frontend integrated with Backend we will run this cmd in frontend directory.

  --- npm run build
```
```bash
    then after build is complete now copy the frontend folder and paste in backend folder 
```
```bash
  now go to setting.py in django go to 'TEMPLATES' wirte:

  'DIRS': [BASE_DIR / '{name_of_FE_folder}/build'],
```
```bash
  scroll down in setting.py and create name "STATICFILES_DIRS" below "STATIC_URL" like this:

  STATICFILES_DIRS = [
    BASE_DIR / 'frontend/build/static'
]
```
```bash
  after mapped build and static go urls.py of main django folder and us template view :

  from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('',TemplateView.as_view(template_name='index.html')) ---> write your html of FE in here 
]

```
```bash
so now when you run your django server both react ad Django will work in same localhost.
```

## Authors

- [@divanov11](https://github.com/divanov11/Django-React-NotesApp) (For Referance)

- https://www.youtube.com/watch?v=tYKRAXIio28&list=PLzk5YvP9F0plJD_AAiZTAcMt82dmXIH9l&index=2&t=10262s (also check his youtube channel)


## Acknowledgements

- [Follow for more like this on youtube ](https://www.youtube.com/watch?v=tYKRAXIio28&list=PLzk5YvP9F0plJD_AAiZTAcMt82dmXIH9l&index=2&t=10262s)


## Best of tools to go throught for Ract UI

MeterialUI: it is best tool for ui and get codes for react.

React hook form: it is another tool which we can use less code and more stablity.

Recharts: for varity charts

material react table: for varity of tables

Nivo: for varity charts



