from simple_rest_client.resource import Resource, AsyncResource


class ProjectEvents(Resource):
    actions = {
        'list': {'method': 'GET', 'url': 'projects/{}/{}/events/'}
    }


class ProjectIssues(Resource):
    actions = {
        'list': {'method': 'GET', 'url': 'projects/{}/{}/issues/'}
    }
