# Version 3.1
# Created by Aaron Su 16 Dec 2019
# Modified by Jayden Lee 15/04/2020

from src import create_app

app = create_app()
app.run(debug=True, host='134.122.104.123')
import sys

if "everywhere" in sys.argv:
# if __name__ == "__main__":
    pass
else:
    pass
