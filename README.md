static-api
==========

A tool for generating HTTP APIs off of static files.


License
-------
Free software: GNU General Public License v3


Installing
----------

  ```
  $ pip install static-api
  ```


Usage
-----

  ```
  $ static_api <dir> --port=<port_number>
  ```

  This runs a Flask app. The URLs map to the .json files inside `<dir>`. You can also specify a port with `--port`. If unset, it will use port 5000.

  Example:

  ```
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
  ```

  Let's display the contents of 1.json::

  ```
  $ cat dummy_api/users/1.json
  ```

  It's a simple multi-line JSON file.
  ```
  {
    "username": "jdoe",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```

  Now let's run static_api and serve responses based on  files inside dummy_api

  ```
  $ static_api dummy_api
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

  If you visit http://127.0.0.1:5000/users/1/, it will return this response:

  ```
  {
    "username": "jdoe",
    "first_name": "John",
    "last_name": "Doe"
  }
  ```


  If you want to make a "list" endpoint like http://127.0.0.1:5000/users/, make sure you have a file named `users.json`.

  ```
  {
    "error": false,
    "data": ["john", "paul", "george", "ringo"]
  }
  ```

Credits
-------

This package was created with Audrey Roy Greenfeld's `cookiecutter` project and the `audreyr/cookiecutter-pypackage` project template.
* https://github.com/audreyr/cookiecutter
* https://github.com/audreyr/cookiecutter-pypackage
