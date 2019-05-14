from simple_rest_client.api import API

from ..sentry_api_client import resource


def get_api_instance(token="", timeout=None):
    headers = {
        "Authorization": "Bearer {}".format(token),
        "Content-Type": "application/json",
    }

    api_root_url = "https://sentry.io/api/0/"

    api = API(
        api_root_url=api_root_url,
        headers=headers,
        json_encode_body=True,
        timeout=timeout,
    )

    api.add_resource(resource_name="issues", resource_class=resource.Issues)
    api.add_resource(
        resource_name="project_events", resource_class=resource.ProjectEvents
    )
    api.add_resource(
        resource_name="project_issues", resource_class=resource.ProjectIssues
    )
    api.add_resource(resource_name="projects", resource_class=resource.Projects)

    return api
