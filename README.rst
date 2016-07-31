===============================
static-api
===============================


.. image:: https://img.shields.io/pypi/v/static_api.svg
        :target: https://pypi.python.org/pypi/static_api

.. image:: https://img.shields.io/travis/darylyu/static_api.svg
        :target: https://travis-ci.org/darylyu/static_api

.. image:: https://readthedocs.org/projects/static-api/badge/?version=latest
        :target: https://static-api.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/darylyu/static_api/shield.svg
     :target: https://pyup.io/repos/github/darylyu/static_api/
     :alt: Updates


A tool for generating HTTP APIs off of static files.


* Free software: GNU General Public License v3
* Documentation: https://static-api.readthedocs.io.


Installing
----------

  .. code-block:: bash
    $ pip install static-api


Usage
-----

  .. code-block:: bash
    $ static_api <dir>

  This runs a Flask app. The URLs map to the .json files inside <dir>

  Example:

  .. code-block:: bash
    # You have a directory named dummy_api and inside it
    # is a directory named users.
    $ ls -l dummy_api
    total 1
    drwxr-xr-x  12 dyu  staff   408 Jul 31 21:08 users

    # Inside users/ are files named 1.json and 2.json
    $ ls -l dummy_api/users
    total 2
    -rw-r--r--@ 1 dyu  staff   102 Jul 31 21:12 1.json
    -rw-r--r--@ 1 dyu  staff   104 Jul 31 21:12 2.json

  Let's display the contents of 1.json::

    $ cat dummy_api/users/1.json

  It's a simple multi-line JSON file.
  .. code-block:: json
    {
      "username": "jdoe",
      "first_name": "John",
      "last_name": "Doe"
    }

  Now let's run static_api and serve responses based on  files inside dummy_api

    .. code-block:: bash
      $ static_api dummy_api
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

  If you visit http://127.0.0.1:5000/users/1/, it will return this response:

    .. code-block:: json
      {
        "username": "jdoe",
        "first_name": "John",
        "last_name": "Doe"
      }


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

