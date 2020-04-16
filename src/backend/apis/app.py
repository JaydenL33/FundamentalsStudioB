# Version 3.1
# Created by Aaron Su 16 Dec 2019
# Modified by Jayden Lee 15/04/2020

from src import create_app

app = create_app()

Local = False

import sys

if Local == False:
# if __name__ == "__main__":
    app.run(debug=True, host='134.122.104.123')
else:
    app.run(debug=True, host='localhost')
