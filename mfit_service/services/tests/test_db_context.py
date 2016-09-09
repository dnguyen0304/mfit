# -*- coding: utf-8 -*-

import uuid

import sqlalchemy
from nose.tools import assert_raises, assert_true

import mfit_service
from mfit_service import models
from mfit_service import services


class TestDBContext:

    def __init__(self):
        db_context_factory = services.DBContextFactory(
            connection_string=mfit_service.configuration['repositories']['PostgreSQL']['connection_string'])
        self.db_context = db_context_factory.create()

        self.user = models.Users(
            email_address='bruiser.cornelius@{}.com'.format(uuid.uuid4()),
            first_name='Bruiser',
            last_name='Nguyen')

        self.requires_teardown = False

    def test_create_new_entity(self):
        self.db_context.add(self.user, created_by=1)
        self.db_context.commit()

        assert_true(sqlalchemy.inspect(self.user).persistent)

        self.requires_teardown = True

    def test_create_new_entity_without_created_by_argument(self):
        assert_raises(TypeError, self.db_context.add, self.user)

    def test_update_entity(self):
        self.db_context.add(self.user, created_by=-1)
        self.db_context.commit()

        self.user.first_name = 'foo'
        self.db_context.add(self.user, updated_by=-1)
        self.db_context.commit()

        assert_true(sqlalchemy.inspect(self.user).persistent)

        self.requires_teardown = True

    def test_update_entity_without_updated_by_argument(self):
        self.db_context.add(self.user, created_by=-1)
        self.db_context.commit()

        self.user.first_name = 'foo'
        assert_raises(TypeError, self.db_context.add, self.user)

        self.requires_teardown = True

    def teardown(self):
        if self.requires_teardown:
            self.db_context.delete(self.user)
            self.db_context.commit()
        self.db_context.close()

