from simple_rest_client.resource import Resource, AsyncResource


class AsyncProjectEvents(AsyncResource):
    actions = {
        'list': {'method': 'GET', 'url': 'projects/{}/{}/events/'}
        'head': {'method': 'HEAD', 'url': 'projects/{}/{}/events/'}
    }


class ProjectEvents(Resource):
    actions = {
        'list': {'method': 'GET', 'url': 'projects/{}/{}/events/'}
    }
