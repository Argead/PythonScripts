#usr/bin/python3
"""
Initialize a bottle application to run a fast web experiment.
"""
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str, help="Name of directory to be created to contain the application.")
parser.add_argument('-v', '--virtualenv', action='store_true', help="Create a virtual environment for this project.")
args = parser.parse_args()

def initialize_directory():
    #Create and navigate to the dir from the directory argument.
    print('Setting up project directory...')
    if os.path.isabs(args.directory):
        if not os.path.exists(args.directory):
            #TODO: This mkdir call will likely fail for an abspath. More logic needed to handle creating the dir iteratively, esp. if more than one nested directory needs to be created.
            os.mkdir(args.directory)
    elif args.directory != os.getcwd():
        if not os.path.exists(args.directory):
            #TODO: This mkdir call will also fail if nested directories need to be created. Needs to split the args.directory provided and iterate over each dir level, validating whether it exists, creating it if not, then stepping into it and repeating the iteration.
            os.mkdir(args.directory)
    os.chdir(args.directory)
    
    #Create directory for static files.
    subprocess.call('mkdir static', shell=True)
    subprocess.call('touch static/index.html', shell=True)
    subprocess.call('touch static/style.css', shell=True)
    
    #Create the app.py file for the project.
    subprocess.call('touch app.py', shell=True)
    
    #Setup a virtualenv for the project if specified.
    if args.virtualenv:
        #TODO: validate that virtualenv is installed first.
        print('Installing virtual environment...')
        subprocess.call('virtualenv venv -p python3', shell=True)
        
    #Install bottle for the project.
    print('Installing bottle framework...')
    if args.virtualenv:
        #TODO: logic to confirm if pip3 is installed and to install it if not.
        pip3_path = os.getcwd() + '/venv/bin/pip3'
        install_cmd = 'install bottle'
        bottle_install_command = '{} {}'.format(pip3_path, install_cmd)
        subprocess.call(bottle_install_command, shell=True)
    else:
        subprocess.call('pip3 install bottle', shell=True)

    #Install bottle-sqlite module.
    print('Installing bottle-sqlite module...')
    if args.virtualenv:
        pip3_path = os.getcwd() + '/venv/bin/pip3'
        install_cmd = 'install bottle-sqlite'
        orm_install_command = '{} {}'.format(pip3_path, install_cmd)
        subprocess.call(orm_install_command, shell=True)
    else:
        subprocess.call('pip3 install bottle-sqlite', shell=True)
        
        
    #Write boilerplate content into app.py. This is temporary, until a better alternative is implemented.    
    app_file = open('app.py', 'w')
    app_file.write('#!/usr/bin/python3' + os.linesep * 2)
    app_file.write('import bottle' + os.linesep)
    app_file.write('import datetime' + os.linesep)
    app_file.write('import re' + os.linesep)
    app_file.write('import sqlite3' + os.linesep)
    app_file.write(os.linesep * 2)
    app_file.write('app = bottle.Bottle()' + os.linesep)
    app_file.write('connection = sqlite3.connect("test.db")' + os.linesep)
    app_file.write('cursor = connection.cursor()' + os.linesep)
    app_file.write('try:' + os.linesep)
    app_file.write('\tcursor.execute("""CREATE TABLE emails (email, time, IP)""")' + os.linesep)
    app_file.write('except sqlite3.Error:' + os.linesep)
    app_file.write('\tpass' + os.linesep)
    app_file.write(os.linesep)
    
    #Index Route logic
    app_file.write('@bottle.route("/", method="GET")' + os.linesep)
    app_file.write('def index():' + os.linesep)
    app_file.write('\treturn bottle.static_file("index.html", root="static")')
    app_file.write(os.linesep)
    
    app_file.write('@bottle.route("/", method="POST")' + os.linesep)
    app_file.write('def register():' + os.linesep)
    app_file.write('\temail=bottle.request.forms.get("email")' + os.linesep)
    app_file.write('\temail_pattern="^[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+$"' + os.linesep)
    app_file.write('\tif re.match(email_pattern, email):' + os.linesep)
    app_file.write('\t\tcurrent_time = str(datetime.datetime.now())' + os.linesep)
    app_file.write('\t\tip = str(bottle.request.get("REMOTE_ADDR"))' + os.linesep)
    app_file.write('\t\tcommand = "INSERT INTO emails VALUES(\'{}\', \'{}\', \'{}\')".format(email, current_time, ip)' + os.linesep)
    app_file.write('\t\tcursor.execute(command)' + os.linesep)
    app_file.write('\t\tconnection.commit()' + os.linesep)
    app_file.write('\treturn "Thank you for registering! Expect updates soon."'+os.linesep)
    
    
    #Index html file content
    index_file = open('static/index.html', 'w')
    index_file.write('<!doctype html>' + os.linesep)
    index_file.write('<html>' + os.linesep)
    index_file.write('<head>' + os.linesep)
    index_file.write('<title>Experiment Page</title>' + os.linesep)
    index_file.write('<link href="style.css" type="text/css" rel="stylesheet">' + os.linesep)
    index_file.write('</head>' + os.linesep)
    index_file.write('<body>' + os.linesep)
    index_file.write('<h1>Prodct Description!</h1>' + os.linesep)
    index_file.write('<span>The description of what you are developing goes here!</span>' + os.linesep)
    index_file.write('</ br>' + os.linesep)
    index_file.write('<h3>Sign up for updates</h3>' + os.linesep)
    index_file.write('<form action="/" method="post">' + os.linesep)
    index_file.write('\tEmail: <input name="email" type="text" />' + os.linesep)
    index_file.write('\t<input value="Register" type="submit" />' + os.linesep)
    index_file.write('</form>' + os.linesep)
    index_file.write('</body>' + os.linesep)
    index_file.write('</html>' + os.linesep)
    index_file.close()
   
    #App launch logic
    app_file.write(os.linesep * 2)
    app_file.write('bottle.run(host="localhost", port=8000, debug=False)')
    app_file.close()


    print('Initialization completed')
    
if __name__ == '__main__':
    initialize_directory()
        
    
