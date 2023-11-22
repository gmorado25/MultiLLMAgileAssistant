import ipaddress, os, platform, subprocess, sys
from argparse import ArgumentParser, ArgumentTypeError, Namespace, _SubParsersAction
from pathlib import Path

__base_dir = Path(__file__).parent.resolve()

if (platform.system() == "Windows"):
    __shell = ''
    __script_extension = '.bat'
    __scripts_dir = (__base_dir / 'scripts/windows/').resolve().__str__() + '\\'
else:
    __shell = 'bash'
    __script_extension = '.sh'
    __scripts_dir = (__base_dir / 'scripts/linux_mac/').resolve().__str__() + '/'

def port_number(arg: str) -> int:
    MAX_PORT = 65535

    try:
        port = int(arg)
    except ValueError:
        raise ArgumentTypeError(f'Expected valid port number, got {arg}')
    
    if (port <= 0 or port >= MAX_PORT):
        raise ArgumentTypeError(
            f'Expected valid port number between 0 - {MAX_PORT}, got {arg}')
    
    return port

def validateFile(arg: str, isRelativePath: bool) -> str:
    if (isRelativePath):
        file = (__base_dir / arg).resolve().__str__()
    else:
        file = arg

    if not os.path.isfile(file):
        raise ArgumentTypeError("The file %s does not exist!" % file)
    else:
        return file
    
def setupServerCommands(subparser: _SubParsersAction) -> None:
    server_parser: ArgumentParser = subparser.add_parser(
        name='server', 
        description='Arguments for starting the web server.', 
        help='Command to set options for the web server.'
    )

    server_parser.add_argument(
        '-a', '--address', 
        dest='address', 
        help='Set the host address for the web server. Default is 127.0.0.1', 
        default='127.0.0.1',
        type=ipaddress.ip_address
    )

    server_parser.add_argument(
        '-p', '--port', 
        dest='port', 
        help='Set the port number for the web server. Default is port 8000.', 
        default='8000',
        type=port_number
    )

    server_parser.add_argument(
        '-d', '--debug', 
        action='store_true', 
        help='Run the web server in debug mode. Off by default'
    )

    server_parser.add_argument(
        '-t', '--test',
        action='store_true',
        help='Run tests for the Django server.'
    )

def setupClientCommands(subparser: _SubParsersAction) -> None:

    client_parser: ArgumentParser = subparser.add_parser(
        name='client', 
        description='Arguments for starting the UI service.', 
        help='Command to set options for the internal UI server.'
    )

    client_parser.add_argument(
        '-a', '--address', 
        dest='address', 
        help='Set the host address for the internal UI service. Default is 127.0.0.1', 
        default='127.0.0.1',
        type=ipaddress.ip_address
    )

    client_parser.add_argument(
        '-p', '--port', 
        dest='port', 
        help='Set the port number for the internal UI service. Default is 3000.', 
        default='3000',
        type=port_number
    )

    client_parser.add_argument(
        '-d', '--debug', 
        action='store_true', 
        help='Run the client service in debug mode.'
    )

    client_parser.add_argument(
        '-t', '--test',
        action='store_true',
        help='Run tests for the NextJS Project.'
    )

def setupConfigCommands(subparser: _SubParsersAction) -> None:

    config_parser: ArgumentParser = subparser.add_parser(
        name='config', 
        description='Arguments for specifying config files.',
        help='Command to specify location of config files.'
    )

    config_parser.add_argument(
        '-k', '--keys', 
        dest='keys_path', 
        help='Set the path to the auth key config file.', 
        default=(__base_dir / 'server/config/keys-dev.json').resolve().__str__(),
    )

    config_parser.add_argument(
        '-m', '--models', 
        dest='model_path', 
        help='Set the path to the models config file.', 
        default=(__base_dir / 'server/config/models.json').resolve().__str__(),
    )

    config_parser.add_argument(
        '-r', '--relative', 
        action='store_true', 
        help='Indicate the file paths are relative to the project root.'
    )

def splitSubCommandsFromCmdline(argv: list[str]) -> dict[str, list[str]]:
    argsDict = {'server': ['server'], 'client': ['client'], 'config': ['config'], 'other': []}
    
    if (len(argv) > 1):
        def isValidCommand(argument: str) -> bool:
            return argument == 'server' \
                or argument == 'client' \
                or argument == 'config'
        
        command = argv[1] if isValidCommand(argv[1]) else 'other'
        for argument in argv[1:]:
            if (isValidCommand(argument)):
                command = argument
            else:
                argsDict[command].append(argument)

    return argsDict

def multillm(args: dict[str: list[str]], parser: ArgumentParser) -> None:

    # parse separate arguments for every command
    serverArgs = parser.parse_args(args['server'])
    clientArgs = parser.parse_args(args['client'])
    configArgs = parser.parse_args(args['config'])

    # catch-all for error or help messages
    other = parser.parse_args(args['other'])

    if (other.setup == True):
        runSetup()
    elif (serverArgs.test == True):
        runServerTest()
    elif (clientArgs.test == True):
        runUITest()
    else:
        setEnvironmentVariables(serverArgs, clientArgs, configArgs)
        startServer()
        startUI()

def setEnvironmentVariables(
    serverArgs: Namespace, 
    clientArgs: Namespace, 
    configArgs: Namespace
) -> None:
    
    os.environ['AUTH_KEYS_FILE'] = validateFile(configArgs.keys_path, configArgs.relative)
    os.environ['MODELS_CONFIG'] = validateFile(configArgs.model_path, configArgs.relative)
    os.environ['SERVER_DEBUG'] = str(serverArgs.debug)
    os.environ['SERVER_ADDRESS'] = str(serverArgs.address)
    os.environ['SERVER_PORT'] = str(serverArgs.port)
    os.environ['NEXTJS_DEBUG'] = str(clientArgs.debug)
    os.environ['NEXTJS_ADDRESS'] = str(clientArgs.address)
    os.environ['NEXTJS_PORT'] = str(clientArgs.port)

def runSetup() -> None:
    setup = __shell + ' ' + __scripts_dir + 'setup' + __script_extension
    subprocess.Popen(
        [setup.strip(), __base_dir],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

def runServerTest() -> None:
    test_server = __shell + ' ' + __scripts_dir + 'test_server' + __script_extension
    subprocess.Popen(
        [test_server.strip(), __base_dir],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

def runUITest() -> None:
    test_ui = __shell + ' ' + __scripts_dir + 'test_ui' + __script_extension
    subprocess.Popen(
        [test_ui.strip(), __base_dir],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

def startServer() -> None:

    print('[*] Starting Django server.')
    print(f'   \__ Address: {os.getenv("SERVER_ADDRESS")}')
    print(f'   \__ Port number: {os.getenv("SERVER_PORT")}')
    print(f'   \__ Debug = {os.getenv("SERVER_DEBUG")}')
    print(f'   \__ LLM config: "{os.getenv("MODELS_CONFIG")}"')
    print(f'   \__ Authentication Keys: "{os.getenv("AUTH_KEYS_FILE")}"\n')

    server = __shell + ' ' + __scripts_dir + 'server' + __script_extension
    subprocess.Popen(
        [server.strip(), __base_dir],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

def startUI() -> None:
    print('[*] Starting NextJS.')
    print(f'   \__ Address: {os.getenv("NEXTJS_ADDRESS")}')
    print(f'   \__ Port number: {os.getenv("NEXTJS_PORT")}')
    print(f'   \__ Debug = {os.getenv("NEXTJS_DEBUG")}')

    nextjs = __shell + ' ' + __scripts_dir + 'nextjs' + __script_extension
    subprocess.Popen(
        [nextjs.strip(), __base_dir],
        creationflags=subprocess.CREATE_NEW_CONSOLE,
    )

def main(argv: list[str]) -> int:

    __description = \
    '''
    The Multi-LLM Agile Assistant in a web application
    designed to assist users in querying multiple large
    language models (LLMs) to process user data concurrently
    and produce output such as draft documentation, summaries,
    etc.

    Features include a prompt library to manage prompts, and
    sub-prompts like output modifiers, and a configurable
    web server with options for configuring LLM models,
    authentication/API keys, and more.
    '''

    parser = ArgumentParser(
        prog='Multi-LLM Agile Assistant',
        description=__description
    )

    parser.add_argument(
        '-s', '--setup', 
        action='store_true', 
        help='Run the setup script to create environment and build the project.'
    )

    commandParser = parser.add_subparsers(dest='command')
    setupServerCommands(commandParser)
    setupClientCommands(commandParser)
    setupConfigCommands(commandParser)

    try:
        arguments = splitSubCommandsFromCmdline(argv)
        multillm(arguments, parser)

    except Exception as e:
        print("An error occurred: ", e)

    return os.EX_OK

if (__name__ == '__main__'):
    sys.exit(main(sys.argv))