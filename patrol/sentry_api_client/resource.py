from simple_rest_client.resource import Resource


class ProjectEvents(Resource):
    actions = {
        'fetch': {'method': 'GET', 'url': 'projects/{}/{}/events/{}'},
        'list': {'method': 'GET', 'url': 'projects/{}/{}/events/'}
    }


class ProjectIssues(Resource):
    actions = {
        'fetch': {'method': 'GET', 'url': 'issues/{}/'},
        'list': {'method': 'GET', 'url': 'projects/{}/{}/issues/'},
        'update': {'method': 'PUT', 'url': 'issues/{}/'},
    }
