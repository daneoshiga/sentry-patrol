Sentry Patrol
=============

Sentry Patrol offers a CLI (Command Line Interface) to the Sentry API.

The project is still in alpha state and in active development

.. contents:: **Table of Contents**

Setup
~~~~~

.. code:: bash

    pipenv install --dev
    python setup.py develop
    export SENTRY_API_TOKEN=<your-token>


How to get your sentry API Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You have to access the Sentry API Page (https://sentry.io/api/). Then you
must log in and get you API Auth Token.


How to use
~~~~~~~~~~

For a list of commands and options, check the help output with:

.. code:: bash

    patrol --help


Events
~~~~~~

This command lists events for a given sentry project. It can be used as follows:

.. code:: bash

    patrol events <org-name> <project-name>

This command fetch an event for a given sentry project. It can be used as follows:

.. code:: bash

    patrol event <org-name> <project-name> <event-id>


Issues
~~~~~~

This command list issues for a sentry a project. It can be used as follows:

.. code:: bash

    patrol issues <org-name> <project-name>

This command fetch an issue for a sentry a project. It can be used as follows:

.. code:: bash

    patrol issue <issue-id>

This command update an issues status. It can be used as follows:

.. code:: bash

    patrol issues <issue-id> <status>
