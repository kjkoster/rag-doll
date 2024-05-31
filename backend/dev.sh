#!/usr/bin/env bash
set -eu
pip -q install --upgrade pip
pip -q install --cache-dir=.pip -r requirements.txt

uvicorn main:app --reload --port 5000 --host 0.0.0.0