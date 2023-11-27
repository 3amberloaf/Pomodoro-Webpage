FROM python:3.8-buster
# FROM pulls python 

COPY requirements.txt .
# copies files from local directory to dockerfile

ENV FLASK_APP=app
ENV PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV PATH="/home/myuser/.local/bin:${PATH}"
# ENV is stored at the OS level so people cant change the code, i.e user/password

RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    /usr/local/bin/python3 -m pip install -r requirements.txt &&\
    adduser myuser
### 3 different ways (run, command, entry point)
# run is a commit, does all the installation for running the program
# entry point - system can only have one entry point and cannot be overriden, starts a program at the end of committing
# CMD - can be overriden but only can have one, starts a program
# dont let anyone run as root user, important to adduser myuser
WORKDIR /home/myuser
# changes the working directory to the new user

COPY --chown=myuser:myuser . .
# copy from my local directory to the user of the image, sets the permissions
CMD gunicorn -w 4 --bind 0.0.0.0:$PORT "app:create_app()"
# gunicorn errors will just be '500' but docker compose shows detailed errors in flask development server
# CMD line in compose overrides the gunicorn 