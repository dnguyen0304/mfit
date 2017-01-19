# -*- coding: utf-8 -*-

import enum
import json
import os

__all__ = ['AutomaticEnum', 'Environment', 'get_configuration']


class AutomaticEnum(enum.Enum):

    def __new__(cls):
        value = len(cls.__members__) + 1
        object_ = object.__new__(cls)
        object_._value_ = value
        return object_


class Environment(AutomaticEnum):

    Production = ()
    Staging = ()
    Testing = ()
    Development = ()


# TODO (duyn): Change this into a singleton.
def get_configuration(project_name, depth, _configuration_file=None):

    """
    Get the configuration file based on it's relative location.

    The project name is standardized. The convention is to use uppercase
    without delimiters. The configuration file **must** be named
    "project.config". Its contents **must** be formatted as JSON with the
    top-level objects specifying the environment. For example:

    ```
    {
      "Production": {},
      "Staging": {},
      ...,
    }
    ```

    Parameters
    ----------
    project_name : str
        Project name.
    depth : int
        Number of layers (i.e. sub-directories) between the
        configuration file and this source code file. A depth of 0
        implies both files are in the same directory.
    _configuration_file : File, optional
        Used for testing. Defaults to None.

    Returns
    -------
    dict
        Parsed configuration.

    Raises
    ------
    EnvironmentError
        If the project's environment has not been set.
    KeyError
        If the configuration file does not have a top-level object
        corresponding to the environment.
    """

    environment_variable = project_name.replace('_', '').upper() + '_ENVIRONMENT'

    try:
        environment = getattr(Environment, os.environ[environment_variable])
    except (AttributeError, KeyError):
        message = """
The project's environment could not be found in the shell environment.

To set the project's environment for the current shell session, from the
terminal run

    export {environment_variable}="Production"

To set the project's environment for the current and all future shell
sessions, from the terminal run

    echo 'export {environment_variable}="Production"' >> ~/.bashrc

Below is the list of acceptable values. Note they are case-sensitive.
    - Production
    - Staging
    - Testing
    - Development
"""
        raise EnvironmentError(
            message.format(environment_variable=environment_variable))

    if _configuration_file is None:
        project_directory = (os.path.dirname(os.path.realpath(__file__))
                             + '/'
                             + '../' * depth)
        with open(project_directory + 'project.config', 'r') as file:
            raw_configuration = file.read()
    else:
        raw_configuration = _configuration_file.read()

    try:
        parsed_configuration = json.loads(raw_configuration)[environment.name]
    except KeyError:
        message = (
            """The configuration file does not have a top-level object """
            """corresponding to the environment (i.e. """
            """"{environment_name}").""")
        raise KeyError(message.format(environment_name=environment.name))

    return parsed_configuration

