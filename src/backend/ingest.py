__doc__="""Run ingest logic for the server's database. This calls cleaner, pusher and dashViewer."""

# core user lib
from . import cleaner, pusher, dashViewer

# Python core
import time
import os

cleaner.main()
pusher.main()
dashViewer.main()

# TODO: after this call a git commit and push to update GitHub and let anyone see the latest data
