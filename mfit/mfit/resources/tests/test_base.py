# -*- coding: utf-8 -*-

import uuid

import sqlalchemy
import sqlalchemy.exc
from nose.tools import assert_true, raises

import mfit
from mfit import models
from mfit.resources import base

__all__ = ['TestDBContext']


class TestDBContext:

    def __init__(self):
        db_context_factory = base.DBContextFactory(
            connection_string=mfit.configuration['repositories']
                                                ['PostgreSQL']
                                                ['connection_string'])
        self.db_context = db_context_factory.create()

        self.user = models.Users(
            email_address='bruiser.cornelius@{}.com'.format(uuid.uuid4()),
            first_name='Bruiser',
            last_name='Nguyen')

    def test_create_new_entity(self):
        self.db_context.add(self.user, created_by=-1)
        self.db_context.commit()

        assert_true(sqlalchemy.inspect(self.user).persistent)

    @raises(TypeError)
    def test_create_new_entity_without_specifying_created_by(self):
        self.db_context.add(self.user)

    def test_update_entity(self):
        self.db_context.add(self.user, created_by=-1)
        self.db_context.commit()

        self.user.first_name = 'foo'
        self.db_context.add(self.user, updated_by=-1)
        self.db_context.commit()

        assert_true(sqlalchemy.inspect(self.user).persistent)

    @raises(TypeError)
    def test_update_entity_without_updated_by_argument(self):
        self.db_context.add(self.user, created_by=-1)
        self.db_context.commit()

        self.user.first_name = 'foo'
        self.db_context.add(self.user)

    def teardown(self):
        try:
            self.db_context.delete(self.user)
            self.db_context.commit()
        except sqlalchemy.exc.InvalidRequestError:
            pass
        finally:
            self.db_context.close()

