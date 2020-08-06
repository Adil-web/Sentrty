import os
import sentry_sdk

from bottle import route, run, request, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration
from http import HTTPStatus

SENTRY_DSN = os.environ.get("SENTRY_DSN")
sentry_sdk.init(dsn=SENTRY_DSN, integrations=[BottleIntegration()])

@route("/")
def index():
    return "Запросы можно отправлять на /success и /fail"


@route('/success')  
def index():  
    return "success"

@route('/fail')  
def index():  
    raise RuntimeError("There is an error!")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
