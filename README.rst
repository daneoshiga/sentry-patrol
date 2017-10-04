Sentry Patrol
=============

This is still in alpha state and in active development


Setup
~~~~~

.. code:: bash

    pipenv install --dev
    python setup.py develop
    export SENTRY_API_TOKEN=<your-token>


Example
~~~~~~~

This will list all events of a specific project

.. code:: bash

    patrol events <organization> <project>
