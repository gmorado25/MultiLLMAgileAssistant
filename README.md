# Multi-LLM Agile Assistant - SE4485 Software Engineering Project

The Multi-LLM Agile Assistant is a program designed to assist software teams
with the production of draft deliverables during the software development
lifecycle (SDLC). This project runs as a web application that connects to
backend prompt library and LLM server(s).

The instructions for setting up the development environment for the project
are listed below. Users looking to install and run the application can
download the web server and client code [here]().

## Build Requirements

Building the project requires 2 setups for the individual backend and frontend
applications. The requirements for each are discussed below.

### Backend/Server Requirements

The backend project requires at minimum python version 3.6 and can be verified
with the command:

```
python -V
```

Remaining backend dependencies are installed with the setup script discussed
in the Environment Setup [section](#environment-setup)

### Frontend/Client Requirements

Building the frontend code requires NodeJS and Node Package Manager. This can
be verified with the command:

```
node --version
```

Remaining frontend dependencies are installed with the setup script discussed
in the Environment Setup [section](#environment-setup)

## Environment Setup

Development setup is streamlined with the help of several shell scripts. Anyone starting
with a new clone of the project should run 'setup.bat' or 'setup.sh' relevant to their
workstation operating system.

<details>
<summary>Windows</summary>

```
.\setup.bat
```

</details>

<details>
<summary>Linux</summary>

```
bash setup.sh
```

Alternative way:

```
 bash setup.sh
```

</details>
<br>
This script will setup a virtual environment for the server and download and
install all of the neccessary python packages, as well as setup the React 
project for the fontend and install its dependencies.
<br>

## Starting the Server

Starting the server is simple once dependencies are in place. Open a terminal, navigate to the django project root (./server/multillm), and run

```
python manage.py runserver
```

Alternative way:

```
bash server.sh
```

Open the project in your web browser at the local address specificed in the command's output to verify it is running.

## Starting the Cleint

```
bash client.sh
```

-- TO BE CONT. --
