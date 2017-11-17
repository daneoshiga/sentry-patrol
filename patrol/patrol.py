import requests

from .sentry_api_client.api import get_api_instance


class Patrol:

    def __init__(self, sentry_api_token, timeout=None):
        self.headers = {
            'Authorization': 'Bearer {}'.format(sentry_api_token)
        }
        self.timeout = timeout
        self.api = get_api_instance(sentry_api_token, timeout)

    def _fetch_resources(self, endpoint, organization, project):
        endpoint = getattr(self.api, endpoint)
        method = getattr(endpoint, 'list')

        resources = method(organization, project)
        yield from resources.body

        next_link = resources.client_response.links['next']
        while next_link['results'] == 'true':
            response = requests.get(next_link['url'], timeout=self.timeout, headers=self.headers)
            yield from response.json()
            next_link = response.links['next']

    def events(self, organization, project):
        return self._fetch_resources('project_events', organization, project)

    def event(self, organization, project, event_id):
        return self.api.project_events.fetch(organization, project, event_id).body

    def issues(self, organization, project):
        return self._fetch_resources('project_issues', organization, project)

    def issue(self, issue_id):
        return self.api.issues.fetch(issue_id).body

    def update_issue(self, issue_id, data):
        return self.api.issues.update(issue_id, body=data).body

    def projects(self, organization):
        return self.api.projects.list(organization).body
