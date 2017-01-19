===========
Flask Etude
===========

.. image:: https://travis-ci.org/dmi-try/flask-etude.svg?branch=master
    :target: https://travis-ci.org/dmi-try/flask-etude

Flask app I'm experimenting with.

Run
===

Install python 3.5 and virtualenv

```bash
$ virtualenv env
...
$ env/bin/pip install -r requirements.txt
...
```

Run server


```bash
$ env/bin/python app/__init__.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Working handlers are http://127.0.0.1:5000/ping and http://127.0.0.1:5000/ping_json

Test the code
=============

Install python 3.5 and tox

```bash
$ tox
...
```

Author
======

Dmitry Pyzhov, http://www.pyzhov.ru/
