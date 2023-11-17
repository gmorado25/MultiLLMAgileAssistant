import argparse, os, sys
from pathlib import Path

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

__base_dir = Path(__file__).resolve()

def multillm(args: argparse.Namespace) -> None:
    server_address = args.command
    print(server_address)

def main() -> int:

    parser = argparse.ArgumentParser(
        prog='Multi-LLM Agile Assistant',
        description=__description
    )
    subparsers = parser.add_subparsers(dest='command')

    server_parser = subparsers.add_parser(name='server', description='Arguments for starting the web server.')
    server_parser.add_argument('-a', '--address', dest='address', help='Set the host address for the web server.', default='127.0.0.1')
    server_parser.add_argument('-p', '--port', dest='port', help='Set the port number for the web server.', default='8000')
    server_parser.add_argument('-d', '--debug', action='store_true', help='Run the web server in debug mode.')

    client_parser = subparsers.add_parser(name='client', description='Arguments for starting the UI service.')
    client_parser.add_argument('-a', '--address', dest='address', help='Set the host address for the internal UI service.', default='127.0.0.1')
    client_parser.add_argument('-p', '--port', dest='port', help='Set the port number for the internal UI service.', default='127.0.0.1')
    client_parser.add_argument('-d', '--debug', action='store_true', help='Run the client service in debug mode.')

    config_parser = subparsers.add_parser(name='config', description='Arguments for specifying config files.')
    config_parser.add_argument('-k', '--keys', dest='key_path', help='Set the path to the auth key config file.', default=(__base_dir / 'server/config/keys-dev.json'))
    config_parser.add_argument('-m', '--models', dest='model_path', help='Set the path to the models config file.', default=(__base_dir / '/server/config/models.json'))
    config_parser.add_argument('-r', '--relative', action='store_true', help='Indicate the file paths are relative to the project root.')

    try:
        args = parser.parse_args()
        multillm(args)
    except Exception as e:
        print("An error occurred: ", e)

    return os.EX_OK

if (__name__ == '__main__'):
    sys.exit(main())