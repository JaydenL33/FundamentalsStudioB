__doc__="""Run ingest logic for the server's database. This calls cleaner, pusher and dashViewer."""

# core user lib
import cleaner
import pusher
import dashViewer as views

# Python core
import time
import os

cleaner.main()
pusher.main()
views.main()

# TODO: after this call a git commit and push to update GitHub and let anyone see the latest data
