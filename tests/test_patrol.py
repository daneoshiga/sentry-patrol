from unittest import mock

from patrol import cli


@mock.patch('patrol.patrol.Patrol.events')
def test_events(mock_events, cli_runner):
    mock_events.return_value = []
    result = cli_runner.invoke(cli.events, ['organization', 'project'])

    assert result.exit_code == 0
    assert mock_events.called


@mock.patch('patrol.patrol.Patrol.event')
def test_event(mock_event, cli_runner, event):
    mock_event.return_value = event
    result = cli_runner.invoke(cli.event, ['organization', 'project', 'event_id'])

    assert result.exit_code == 0
    assert mock_event.called


@mock.patch('patrol.patrol.Patrol.issues')
def test_issues(mock_issues, cli_runner):
    mock_issues.return_value = []
    result = cli_runner.invoke(cli.issues, ['organization', 'project'])

    assert result.exit_code == 0
    assert mock_issues.called


@mock.patch('patrol.patrol.Patrol.issue')
def test_issue(mock_issue, cli_runner, issue):
    mock_issue.return_value = issue
    result = cli_runner.invoke(cli.issue, ['issue_id'])

    assert result.exit_code == 0
    assert mock_issue.called


@mock.patch('patrol.patrol.Patrol.update_issue')
def test_update_issue(mock_issue, cli_runner, issue):
    mock_issue.return_value = issue
    result = cli_runner.invoke(cli.update_issue_status, ['issue_id', '--status', 'unresolved'])

    assert result.exit_code == 0
    assert mock_issue.called


@mock.patch('patrol.patrol.Patrol.projects')
def test_projects(mock_projects, cli_runner):
    mock_projects.return_value = []
    result = cli_runner.invoke(cli.projects, ['organization'])

    assert result.exit_code == 0
    assert mock_projects.called
