#!/usr/bin/env bash

./manage.py sqlmigrate polls 0001

./manage.py check