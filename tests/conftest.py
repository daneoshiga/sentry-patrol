from unittest import mock
import pytest
from click.testing import CliRunner

from patrol.patrol import Patrol


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def patrol():
    patrol = Patrol('TOKEN')
    patrol.api = mock.Mock()
    return patrol


@pytest.fixture
def event():
    return {
        'eventID': 'id',
        'message': 'message'
    }


@pytest.fixture
def issue():
    return {
        'id': 'id',
        'title': 'title',
        'status': 'unresolved'
    }
