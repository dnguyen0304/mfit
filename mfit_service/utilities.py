# -*- coding: utf-8 -*-

import enum
import json
import os


class AutomaticEnum(enum.Enum):

    def __new__(cls):
        value = len(cls.__members__) + 1
        object_ = object.__new__(cls)
        object_._value_ = value

        return object_


class Environment(AutomaticEnum):
    Production = ()
    Test = ()
    Development = ()


# TODO (duyn): make this a singleton
def get_configuration(project_name, depth):

    """
    Returns Dictionary

    x
    The project name is normalized. The convention is to use uppercase
    without delimiters.

    Parameters
    ----------
    project_name : String
        Project name.
    depth : Integer

    environment : mfit_service.environment.Environment, default None
        Environment type.
    """

    # TODO (duyn): How do you make this more flexible?
    environment_variable = project_name.replace('_', '').upper() + '_ENVIRONMENT'

    try:
        environment = getattr(Environment, os.environ['MFITSERVICE_ENVIRONMENT'])
    except KeyError:
        message = 'An environment variable is missing. '
        suggestion = ("""Try checking the environment variables. """
                      """{} should be set to "Production", """
                      """"Staging", etc.""")
        raise EnvironmentError(message + suggestion.format(environment_variable))

    project_directory = os.path.dirname(os.path.realpath(__file__)) + '/' + '../' * depth

    with open(project_directory + 'project.config', 'r') as file:
        configuration = json.loads(file.read())[environment.name]

    return configuration


configuration = get_configuration(project_name='mfit_service', depth=1)

