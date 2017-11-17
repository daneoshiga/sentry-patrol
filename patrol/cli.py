import click

from patrol.config import SENTRY_API_TOKEN, ISSUE_STATUSES
from patrol.patrol import Patrol
from patrol.utils import print_json

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
        click.echo('{eventID}: {message}'.format(**event))


@cli.command(help='Lists project events')
@click.argument('organization')
@click.argument('project_name')
@click.argument('event_id')
def event(organization, project_name, event_id):
    click.secho('event {} for {}'.format(event_id, project_name))
    event = patrol.event(organization, project_name, event_id)
    print_json(event)


@cli.command(help='Lists project issues')
@click.argument('organization')
@click.argument('project_name')
def issues(organization, project_name):
    click.secho('issues for {}'.format(project_name))
    for issue in patrol.issues(organization, project_name):
        click.echo('{id}: {title}'.format(**issue))


@cli.command(help='Retrive issue')
@click.argument('issue_id')
def issue(issue_id):
    issue = patrol.issue(issue_id)
    print_json(issue)


@cli.command(help='Update issue')
@click.argument('issue_id')
@click.option('--status', type=click.Choice(ISSUE_STATUSES))
def update_issue_status(issue_id, status):
    data = {'status': status}
    issue = patrol.update_issue(issue_id, data)
    click.echo('{id}: {title} - {status}'.format(**issue))
