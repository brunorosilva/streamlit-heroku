"""
Usage:
    get_requirements.py [options] [<appname>] [<path>] [<email>] 

Arguments:
    <appname>             The app filename.
    <path>                The path to the directory containing the application
                          files for which a requirements file should be
                          generated (defaults to the current working
                          directory).
    <email>               The email associated with your Heroku account.

Options:
    --no-reqs             Don`t make a requirements file
    --no-setup            Don`t make a setup.sh file
    --no-proc             Don`t make a Procfile
    --force               Substitute the current requirements.txt.
"""
from docopt import docopt
import os
import sys

def make_requirements(args, force=False):
    print("Getting requirements for \n")

    input_path = args['<path>']
    
    if input_path is None:
        input_path = os.path.abspath(os.curdir)
    
    for f in os.listdir(input_path):
        if f.endswith('.py'):
            print(f)

    print("\nPlease wait for the requirements file to be done!")   
    if force:
        os.system('pipreqs --force '+input_path)
    else:
        os.system('pipreqs '+input_path)

def make_setup(args):
    input_path = args['<path>']
    
    if input_path is None:
        input_path = os.path.abspath(os.curdir)


    f = open(input_path + "\\setup.sh", "w")

    email = args['<email>']
    if email is None:
        email = input("Looks like you forgot to put your Heroku email, please type it here\n")
    f.writelines(
    ['mkdir -p ~/.streamlit/\n',
    'echo "[general]\n',
    'email = \\\"' + str(email) + '\\\"\n',
    '" > ~/.streamlit/credentials.toml\n',
    'echo "[server]\n',
    'headless = true\n',
    'port = $PORT\n',
    'enableCORS = false\n',
    '" > ~/.streamlit/config.toml\n']
    )
    f.close()

def make_procfile(args):

    input_path = args['<path>']
    
    if input_path is None:
        input_path = os.path.abspath(os.curdir)


    f = open(input_path + "\\Procfile", "w")

    appname = args['<appname>']
    if appname is None:
        appname = input("Looks like you forgot to put your appname, please type it here \n")

    if not appname.endswith(".py"):
        appname = appname + ".py"
    
    f.write("web: sh setup.sh && streamlit run " + appname)
    f.close()


def main():
    args = docopt(__doc__, version="0.0.1")

    # there's a better way to do this, but I'm stupid (maybe using dicts, be my guest)
    if args['--no-reqs']:
        pass
    else:
        make_requirements(args)
    if args['--force'] and (not args['--no-reqs']):
        make_requirements(args, True)
    else:
        pass
    if args['--no-setup']:
        pass
    else:
        make_setup(args)
    if args['--no-proc']:
        pass
    else:
        make_procfile(args)
    
if __name__ == '__main__':
    main()
