import os

# Load the env file
is_development = os.getenv("DEV")

# Configurations of the Settings for any Mode of the Project
if is_development == "True":
    from .development import *

    if os.environ.get("RUN_MAIN") == "true":
        print("🔧 Project Started in The Developer Mode.")
else:
    from .production import *

    if os.environ.get("RUN_MAIN") == "true":
        print("🏗️ Project Started in The Production Mode.")
