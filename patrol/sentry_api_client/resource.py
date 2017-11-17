from simple_rest_client.resource import Resource


class ProjectEvents(Resource):
    actions = {
        'fetch': {'method': 'GET', 'url': 'projects/{}/{}/events/{}/'},
        'list': {'method': 'GET', 'url': 'projects/{}/{}/events/'}
    }


class ProjectIssues(Resource):
    actions = {
        'list': {'method': 'GET', 'url': 'projects/{}/{}/issues/'}
    }


class Issues(Resource):
    actions = {
        'fetch': {'method': 'GET', 'url': 'issues/{}/'},
        'update': {'method': 'PUT', 'url': 'issues/{}/'},
    }
