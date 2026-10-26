import os


def site_identity(request):
    return {"site_name": os.environ.get("SITE_NAME", "Bitácora Robótica")}