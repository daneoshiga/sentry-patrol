import click
from prettyconf import config

APP_NAME = 'patrol'

config.starting_path = (click.get_app_dir(APP_NAME))

SENTRY_API_TOKEN = config('SENTRY_API_TOKEN')

ISSUE_STATUSES = ('resolved', 'unresolved', 'resolvedInNextRelease', 'ignored')
