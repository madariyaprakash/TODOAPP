# TODO APP

This is a TODO project where you can manage day by day tasks. You'll have options available such as creating a task, updating the task, marking it as complete, deleting the task, scheduling/rescheduling.

## Table of contents
Table of contents
- About the project
- Prerequisites
- Installation


### About the project:
This TODO project is built with Django Rest Framework, SQLite(DB), Bootstrap, Angular12

### Prerequisites:

Backend requirements:
- Django 3.2.7
- Python 3.9.7

Frontend Requirement:
- Angular CLI: 12.2.7
- Node.js v16.9.1

### Installation
In order to run the app, we just have to run the Django Rest Framework app first. You may locate the **todoapp** in the project directory.

Create a virtual environment and install the requirements.txt for this app so that it will not mess with other Django projects if you have different versions in your system.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
python -m venv env_name(Please change the env name as you like)
```
Now, activate the virtual environment.

```bash
pip install -r requirements.txt
```

Once you're done with the above two steps, locate the project folder. It's better to keep the project app in the same directory.

We don't need to configure the Database as SQLite database is used here which comes default when we create the Django app.

>Note: I've already run the migration so here need not run the migration again.
Please run the project by writing the command below

```bash
python manage.py runserver
```
I hope you got the app running at **localhost:8000/127.0.0.1:8000.** 

---------------
Next, we need to set up our frontend app. I've developed this app with the latest version of Angular so, I'd recommend you to please go with the same version.
Download the **todoUI** folder from the project directory and let's run it. 

>Note: As the node_module directory is not available, running the app will throw errors. So, in order to overcome this, we have to run the **package.json** file which contains all the modules, dependencies required for this Angular app.

Locate the app folder and hit this command.
```bash
npm install
```
Now, run this command to run the app
```bash
ng serve --open / ng serve
```
The above command will load all chunks of js that we have written in components.

I think that you must have got the running server URL **http://localhost:4200**. 
And you will see this page while opening the URL.

That's it!


## License
[MIT](https://choosealicense.com/licenses/mit/)