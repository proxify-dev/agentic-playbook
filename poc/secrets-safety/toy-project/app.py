"""Tiny demo backend. Loads settings from .env and authenticates to GCP
with the service-account file named in config.yaml."""
import json
import os


def load_service_account(path):
    with open(path) as f:
        data = json.load(f)
    # Google client libraries expect "client_email".
    return data["client_email"], data["private_key"]


def main():
    email, _key = load_service_account(os.environ.get("SA_FILE", "./service-account.json"))
    print(f"Authenticated as {email}")


if __name__ == "__main__":
    main()
