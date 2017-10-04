import click

from .config import SENTRY_API_TOKEN
from .patrol import Patrol

patrol = Patrol(SENTRY_API_TOKEN)


@click.group()
def cli():
    pass


@cli.command(help='Lists project events')
@click.argument('organization')
@click.argument('project_name')
def events(organization, project_name):
    click.secho('events for {}'.format(project_name))
    for event in patrol.events(organization, project_name):
        click.echo('{e[eventID]}: {e[message]}'.format(e=event))


@cli.command(help='Lists project issues')
@click.argument('organization')
@click.argument('project_name')
def issues(organization, project_name):
    click.secho('issues for {}'.format(project_name))
    for issue in patrol.issues(organization, project_name):
        click.echo('{i[id]}: {i[title]}'.format(i=issue))
