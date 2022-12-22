# simple-reminders

This little console application was built to provide simple reminders of
anniversaries, tasks, and other things.

## Requirements

`windows-curses` is required if using windows.
Otherwise `curses` is packaged by default.

## Setup

Create a config file in any location based on `simple-reminders-config.json.example` file.
Create a `config.json` in the repo based on the `config.json.example` file,
and include the path to the config file you made earlier.

## Tests

Execute the line below to run all the tests and ensure everything is working

> python -m unittest discover tests
