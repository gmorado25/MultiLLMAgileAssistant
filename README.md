# Multi-LLM Agile Assistant - SE4485 Software Engineering Project

The Multi-LLM Agile Assistant is a program designed to assist software teams
with the production of draft deliverables during the software development
lifecycle (SDLC). This project runs as a web application that connects to
backend prompt library and LLM server(s). The instructions for setting up the development environment for the project
are listed below. Users looking to install and run the application can
download the web server and client project code from the project Github [here](https://github.com/RyanEubank/Multi-LLM-Agile-Assistant).

Many of the steps outlined here in the ReadMe are automated through a
useful command line tool, 'multillm.py' in the root directory of the project.
It is highly recommended that users use this tool for their needs as it
avoids the hassle of many manual steps. However, as a precaution, all
steps in the project setup and running the code are detailed for both the
command line tool and the manual steps.

## Build Requirements

Building the project requires 2 setups for the individual backend and frontend
applications. The requirements for each are discussed below.

### Backend/Server Requirements

The backend project requires at minimum python version 3.11 and can be verified
with the command:

```
python -V
```

Users must also have a c++ compiler and CMake tools installed
on their machine. Windows users can download Visual Studio C++ build tools
on Microsoft's [website](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
as the easiest option. Linux/MAC users can find the appropriate tools with [VSCode](https://code.visualstudio.com/docs/cpp/config-clang-mac).
Remaining backend dependencies are installed with the setup script discussed
in the Environment Setup [section](#environment-setup).

### Frontend/Client Requirements

Building the frontend code requires NodeJS and Node Package Manager. This can
be verified with the command:

```
node --version
```

Remaining frontend dependencies are installed with the setup script discussed
in the Environment Setup [section](#environment-setup)

## Acquire API Keys

Many LLMs are accessible through web APIs, and this project interacts with
some models using those external systems. 

### OpenAI keys

In order to use OpenAI's models (ChatGPT via GPT 3.5 or GPT4, etc.) users need
an account and an API key. The company has an open source API that can be queried 
over the internet and requires authorization by using this key. Users can sign up for either
a full time paid account or a limited time free trial on OpenAI's [website](https://platform.openai.com/docs/quickstart?context=python).
Follow the documentation there to set up an account and generate your own API key.
Once in hand, follow the [configuration section](#-setup-configuration-files) to
make sure this key authorizes your interactions with OpenAI's models.

### Google keys

In order to use Google's VertexAI models (which powers services like Google Bard, etc.)
users must acquire a Google Cloud project key to authorize their interactions
with google services. Follow this (guide)[https://www.youtube.com/watch?v=Zi-W2pPVmzU] to setup 
your own google cloud account and enable VertexAI and generate an API key. 
Once in hand, follow the [configuration section](#-setup-configuration-files) to make sure 
this key authorizes your interactions with Google's models.

*Note* - There are multiple routes to obtaining an API key for Google's models,
such as MakerSuite, etc. Follow Google's [documentation](https://developers.generativeai.google/) 
on using other services other than Google Cloud for connecting to google's AI models.

### Anthropic Keys

In order to use Anthropic's models (Claude, Claude2), users require an API key from the company.
Signup for access here and follow instructions [here](https://www.anthropic.com/earlyaccess) 
to create an account and obtain access.
*Note* - As of the time of writing, we have been unable to obtain an early access token
from Anthropic, but the infrastructure built in the project should be capable of
supporting querying Anthropic's models via LangChain by including a valid
API key in the auth. keys configuration file.

## Local LLM Setup (Optional)

The Multi-LLM system is capacle of running and querying LLMs locally via
[Llama.cpp](https://github.com/ggerganov/llama.cpp). Users can install
any valid .gguf format model supported by the open source project. Users may also 
optionally setup hardware/GPU support for running local models, see the Llama.cpp 
Github for details.

This section will guide users through the process of downloading a small Llama
model from [HuggingFace](https://huggingface.co/) and running it locally. Users
with capable Nvidia hardware can follow along to install GPU support, and those
without can still install and run in CPU-only mode. Other hardware support
and options for Llama.cpp are listed on the Llama.cpp Github.

### Download local model(s)

First, users must download a valid .gguf format (uses 4-bit quatization) model to 
run with Llama.cpp. There are open source tools available for converting 
.safetensor models, .ggml (old format used by Llama.cpp) and others into .gguf, 
but their use is outside the scope of this guide. The Llama model used to test
was a 7B parameter model from HuggingFace [here](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF#provided-files).

Read through the documentation carefully to select and download a model compatible
with your hardware. Pay close attention to memory requirements. Once downloaded,
move the .gguf file to the 'server/models' directory in the MultiLLM project, or
remember where the model file is located, you will need the full path
when setting up your model [configuration](#-setup-configuration-files) later.

### Install in CPU-only mode

This is the default option, no special actions are required. Follow the
[setup](#environment-setup) as written.

### Install with Nvidia CUDA support

This requires an Nvidia graphics card. Users without proper hardware
should install for CPU-only as described above. To install with Nvidia support, follow along 
with the documentation on the Llama.cpp Github. First be sure Nvidia CUDA is installed on
your machine, via Nvidia's [website](https://developer.nvidia.com/accelerated-computing-toolkit).

**IMPORTANT** Requires Nvidia CUDA version 11 or lower. Nvidia recently released version 12,
but many libraries and platforms have not adopted newer versions yet. This project was
tested before CUDA v12 was widely used, and at the time this guide was written (Nov. 2023) that
version will not function with Llama.cpp to run local LLMs on your GPU.

Verify that Nvidia CUDA is installed on your machine by running the command:
```
$ nvcc -V
```

To install the python-llama-cpp package with CUDA support make sure the following
environment variables are set (and exported!):

<details>
<summary>Windows Powershell</summary>

```
$Env:FORCE_CMAKE=1
$Env:CMAKE_ARGS="-DLLAMA_CUBLAS=on" 
```
</details><details>
<summary>Windows Cmdline</summary>

```
set "FORCE_CMAKE=1"
set "CMAKE_ARGS=-DLLAMA_CUBLAS=on"
```
</details><details>
<summary>Linux/MAC</summary>

```
export FORCE_CMAKE=1
export CMAKE_ARGS="-DLLAMA_CUBLAS=on"
```
</details><br>

and install the package manually with<br>
```
pip install llama-cpp-python
```

To force reinstall if you wish to change the hardware binding or are reinstalling
with GPU support, run
```
pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir
```

See the LangChain [documentation](https://python.langchain.com/docs/integrations/llms/llamacpp)
for further installation support.

## Environment Setup

Development setup is streamlined with the help of several shell scripts and a
project command line tool. Anyone starting with a new clone of the project can
either use the command line tool to automatically setup their project or
follow the manual steps discussed [here](#setup-project-manually)

### Automatic Setup

<details>
<summary>Windows</summary>

```
python multillm.py --setup
```

</details><details>
<summary>Linux/MacOS</summary>

```
python3 multillm.py --setup
```
</details>

<br>
This command will setup a virtual environment for the server and download and
install all of the neccessary python packages, as well as setup the NextJS 
project for the fontend and install its dependencies.
<br>

### Manual Setup

Users who are unable to run the automatic setup script can follow these steps
to manually construct their project environment and install dependencies.
First, to install back-end dependencies it is recommended to use a python
virtual environment for package management, and ensure that modules do not
conflict with any global packages.

To create a virtual environment, run the python command:
<details>
<summary>Windows</summary>

```
python -m venv .project_env
```
</details><details>
<summary>Linux/MacOS</summary>

```
python3 -m venv .project_env
```
</details><br>

This creates a local environment directory named '.project_env' inside the server
folder in the project. Next, to install dependencies to that envirnment, rather 
than globally, users must activate the virtual environment. This is achieved by running
the activation script created when the envirnment was set up:

<details>
<summary>Windows Powershell</summary>

```
.\server\.project_env\Scripts\activate.ps1
```
</details><details>
<summary>Windows Cmdline</summary>

```
.\server\.project_env\Scripts\activate.bat
```
</details><details>
<summary>Linux/MacOS</summary>

```
source ./server/.project_env/bin/activate
```
</details>

Now users can install the neccessary dependencies for the django server with the command:

```
pip install -r server/config/requirements.txt
```

This will take serveral minutes to complete as pip installs all the required libraries.
When done, users will need to navigate to the client sub project.
```
cd client
```
To install front end dependencies, run the command:
```
npm install
```
This will again take a few minutes to complete. Once finished the project is setup,
and there is one last step before users can run the code.

## Setup configuration files

The back end server has several configuration files it needs to run. These
are not provided with the repository as they are either local requirements
specific to each user or must be kept secure/private (API keys).

There are 2 configuration files required, your LLM model configuration,
and API keys. See below for how each should be stored and formatted.

### LLM models config

Create a new file in the server/sonfig directory of the project and name it
'models.json' (This is the default config path for models, users are welcome
to specify their own name and path manually when running the server, but
must remember to explicitly set where the server looks for the models configuration).

The models file specifies what LLMs are registered and set up in the server.
This is done because creating those objects is a time consuming and expensive
process, and setup is done once when the sever loads. The models config file should
contain a json array of objects like:

```
[
    {
        "id": "Llama",
        "class": "multi_llm.models.meta_models.Llama2",
        "args": {
            "model_path": <Path to your Llama .gguf file>,
            // specify creation arguments for Llama...
        }
    },
    // specify other models ...
]
```

Every model in the configuration should have at minimum the following fields:
* 'id': This is the unique name used to identify the object in the system registry. 
The 'id' field is user's choice, and can be any valid string. Note this name will
appear in the list of 'queryable' models on the UI dashboard when the project is run.

* 'class': This is the python module path to the class used to construct the model. All current models
in the system inherit from the AbstractEndpoint class which provides a single query interface for the
system. New models can easily be created that extend or inherit this interface, and can be added
in the system without modifying any other code by simply including their module path in this field.

* 'args': This is a dictionary like json object for python **kwargs, or key-value arugments passed to the 
model constructor at creation. These arguments are model specific. It is best to see LangChain 
[documentation](https://python.langchain.com/docs/get_started/introduction) and [API reference](https://api.python.langchain.com/en/latest/api_reference.html) 
for how best to structure your arguments in the configuration. For example, most models need an argument
"model_name" that specifies what variant of the model you want to use; the query interface
used by the system is a chat-like interface, and will work best with 'chat models' as opposed to text-based models.

A list of model documentation for the currently available models is:
* [Llama](https://api.python.langchain.com/en/latest/llms/langchain.llms.llamacpp.LlamaCpp.html?highlight=llama%20cpp#langchain.llms.llamacpp.LlamaCpp)
* [Google Models](https://api.python.langchain.com/en/latest/llms/langchain.llms.vertexai.VertexAI.html?highlight=vertexai#langchain.llms.vertexai.VertexAI)
* [OpenAI Models](https://api.python.langchain.com/en/latest/llms/langchain.llms.openai.OpenAI.html?highlight=openai#langchain.llms.openai.OpenAI)
* [Anthropic Models](https://api.python.langchain.com/en/latest/llms/langchain.llms.anthropic.Anthropic.html?highlight=anthropic#langchain.llms.anthropic.Anthropic)

All model classes in the system are in the models folder in the multi-llm django [app](/server/src/multi_llm/models/).
A full example config that uses all models currently implemented and uses GPU support for Llama is as follows:
<details>
<Summary>models.json</Summary>

```
[
    {
        "id": "Llama",
        "class": "multi_llm.models.meta_models.Llama2",
        "args": {
            "model_path": "<path to llama file>",
            "n_gpu_layers": 50,     
            "n_ctx": 2048,          
            "n_batch": 512       
        }
    },
    {
        "id": "Bard",
        "class": "multi_llm.models.google_models.ChatBison",
        "args": {
            "model_name": "chat-bison"
        }
    },
    {
        "id": "Claude",
        "class": "multi_llm.models.anthropic_models.Claude2",
        "args": {
            "model_name": "claude-2"
        }
    },
    {
        "id": "GPT3.5",
        "class": "multi_llm.models.open_ai_models.GPT",
        "args": {
            "model_name": "gpt-3.5-turbo"
        }
    },
    {
        "id": "Test",
        "class": "multi_llm.models.test_model.MockInputModel",
        "args": {
            "model_name": "test-model"
        }
    }
]
```
</details><br>

*Note* - It is not neccessary to include every model in your models.json config, 
nor are you limited to using each model only once. For example, users could
specify two models from Google's vertexAI, one with the argument "model_name": "chat-bison",
and the other with "model_name": "code-bison", that will create two different models,
one that has been trained for general purpose chat, aand another specifically for
code generation and processing. The list of models in the configuration can be as
long as needed, though do keep in mind that more models in the system means
a longer startup sequence.

### API key config

The other config file needed (somewhat optionally, as many models support constructing 
by passingthe neccessary API key directly, which in theory could be written directly into the
models config) is a config file for API keys. This file is required regardless if
users use any models that need authentication, as the server will attempt to read
it on startup to get the secret key used for the internal django server.

An example api-key config is included with the project in the file 
[key-dev.json](/server/config/keys-dev.json). The file must be set up as a single
root json object, with sections "llm_auth_keys", and "jira_tokens". At minimum the
'llm_auth_keys" array must have a value MULTI_LLM_SECRET_KEY, or the server
will fail to load.<br>

*Note* - The Jira tokens are currently unused, as Jira integration is a planned
feature for a future release.

## Starting the Server

Running the project code requires 2 steps, starting the back end server, which
hosts the REST API methods and automatically serves files from the front end
project, and starting the NextJS front-end to build and render the UI (NextJS
will run as an internal service, and does not need to be accessible to
any actual users or have a public address).

### Automatic start

The simplest way to start the project is to run the command line tool
without any arguments. Run:
<details>
<Summary>Windows</Summary>

```
python multillm.py
```
</details><details>
<Summary>Linux/MAC</Summary>

```
python3 multillm.py
```
</details>

This will start both the server and the NextJS service with default values
each in a separate terminal. This method is useful for a quickstart and
testing if the projects compile/run, but most of the time users will want
to specify some options. *Note* - By default the project runs with debug=false,
this will cause css styling to break because django does not automatically
server static files when in production mode (deploy on actual application
server would be a nice todo for future work).

The most common options will be running in debug mode. Users can specify either
the server or client projects to start in debug mode, or both at the same time.
Use the command option --debug (or '-d' for short) for the server and/or client in any order:
<details>
<Summary>Windows</Summary>

```
python multillm.py server --debug client --debug
```
</details><details>
<Summary>Linux/MAC</Summary>

```
python3 multillm.py --debug client --debug
```
</details><br>

Another useful option is specifying the path to your configuration files. This
is done through the 'config' command. Use the option '--keys' (or -k) to specify
the path to the api key config, and --models or -m to specify the models config path as follows:

<details>
<Summary>Windows</Summary>

```
python multillm.py config --keys <path to keys> --models <path to models>
```
</details><details>
<Summary>Linux/MAC</Summary>

```
python3 multillm.py config --keys <path to keys> --models <path to models>
```
</details><br>

This will start the server and NextJS service in separate terminals as before,
but the server will load the specified config files.<br>

The recommended way to start the project is with server debug true, and NextJS
debug false (This is because running Django in debug mode will ensure it serves
static files like css styling and NextJS debug false will pre render the 
pages for much faster load times). *Another Note* - NextJS does not seem to 
work well when serving interal SPA routes in debug mode when synced with
Django, and running NextJS in debug mode may not work correctly.

The full list of options and arguments can be easily acquired with the -h or --help
option. Running --help on the base multillm command displays global options, and
further running --help with each of the sub commands (server, client, or config)
will display detailed help messages for each of those and their various options.

### Manual start

To start the server manually, first open a terminal, and set the following
environment variables needed by the system:
```
SERVER_ADDRESS=<address to run django on>
SERVER_PORT=<port number to run django on>
NEXTJS_ADDRESS=<address nextjs is running on>
NEXTJS_PORT=<port number nextjs is running on>
AUTH_KEYS_FILE=<path to api key config>
LLM_MODELS_FILE=<path to models config>
SERVER_DEBUG=<boolean to run django in debug or not>
```

Be sure to use the correct sytax for your terminal and that these
values are exported to running processes. Next, navigate to the django 
project root:
```
cd server/src
```
and run this command to start the back end server:

<details>
<Summary>Windows</Summary>

```
python manage.py runserver %SERVER_ADDRESS%:%SERVER_PORT%
```
</details><details>
<Summary>Linux/MAC</Summary>

```
python3 manage.py runserver $(SERVER_ADDRESS):$(SERVER_PORT)
```
</details>

Finally, start the front end NextJS service by navigating back to the
client project root:
```
cd .. // back to project root
cd client // and on to client project
```

Run the command to start the UI service in debug mode:
<details>
<Summary>Windows</Summary>

```
npx next dev -H %NEXTJS_ADDRESS% -p %NEXTJS_PORT%
```
</details><details>
<Summary>Linux/MAC</Summary>

```
npx next dev -H $(NEXTJS_ADDRESS) -p $(NEXTJS_PORT)
```
</details>

Or run in production mode (recommended) with these commands:
<details>
<Summary>Windows</Summary>

```
npx next build
npx next start -H %NEXTJS_ADDRESS% -p %NEXTJS_PORT%
```
</details><details>
<Summary>Linux/MAC</Summary>

```
npx next build
npx next start -H $(NEXTJS_ADDRESS) -p $(NEXTJS_PORT)
```
</details><br>

__Congratulations! The Multi-LLM Assistant is now up and running!__