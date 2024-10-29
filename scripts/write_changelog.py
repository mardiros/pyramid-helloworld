#!/usr/bin/env python3
import datetime
from pyramid_helloworld import __version__


header = (
    f"## {__version__} - " f"Released on {datetime.datetime.now().date().isoformat()}"
)
with open("CHANGELOG.md.new", "w") as changelog:
    changelog.write(header)
    changelog.write("\n\n")
    changelog.write("* please write here\n\n\n")
