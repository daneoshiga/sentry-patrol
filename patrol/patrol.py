from requests.utils import parse_header_links

from .sentry_api_client.api import get_api_instance


class Patrol:

    def __init__(self, sentry_api_token, timeout=None):
        self.api = get_api_instance(sentry_api_token, timeout)

    def events(self, organization, project):
        events = self.api.project_events.list(organization, project)
        yield from events.body

        links = parse_header_links(events.headers.get('Link'))
        while links[1]['results'] == 'true':
            events = self.api.project_events.list(organization, project)
            yield from events.body

    def issues(self, organization, project):
        issues = self.api.project_issues.list(organization, project)
        yield from issues.body

        links = parse_header_links(issues.headers.get('Link'))
        while links[1]['results'] == 'true':
            issues = self.api.project_issues.list(organization, project)
            yield from issues.body
