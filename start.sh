#!/bin/sh
# NOTE: ここで createuser や migrate を実行すると、runserver_plus と競合して失敗する
uv run manage.py runserver_plus --cert-file certs/cert.pem --key-file certs/key.pem 0.0.0.0:8000
