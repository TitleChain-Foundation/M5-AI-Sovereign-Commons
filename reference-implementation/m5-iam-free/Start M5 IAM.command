#!/bin/sh
# Double-click to open the free M5 IAM app (macOS).
cd "$(dirname "$0")" || exit 1
exec python3 m5_iam_app.py
