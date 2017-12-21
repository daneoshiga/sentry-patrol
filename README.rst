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
