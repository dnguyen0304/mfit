# -*- coding: utf-8 -*-

import uuid

from nose.tools import assert_equals, assert_raises, raises

import mfit_service
from mfit_service import models
from mfit_service import services


class TestDBContext:

    def __init__(self):
        db_context_factory = services.DBContextFactory(
            connection_string=mfit_service.configuration['repositories']['PostgreSQL']['connection_string'])
        self.db_context = db_context_factory.create()

        self.data = {
            'email_address': 'bruiser.cornelius@{}.com'.format(uuid.uuid4()),
            'first_name': 'Bruiser',
            'last_name': 'Nguyen'}

        self.dummy_users = []

    def test_create_new_entity(self):
        self.db_context.add(models.Users(**self.data), created_by=-1)
        self.db_context.commit()

        user = self.db_context.query(models.Users) \
                              .filter_by(email_address=self.data['email_address']) \
                              .one()
        self.dummy_users.append(user)

    @raises(TypeError)
    def test_create_new_entity_without_created_by_argument(self):
        self.db_context.add(models.Users(**self.data))

    def test_update_entity(self):
        self.db_context.add(models.Users(**self.data), created_by=-1)
        self.db_context.commit()
        user = self.db_context.query(models.Users) \
                              .filter_by(email_address=self.data['email_address']) \
                              .one()
        user.first_name = 'foo'
        self.db_context.add(user, updated_by=-1)
        self.db_context.commit()

        user = self.db_context.query(models.Users) \
            .filter_by(email_address=self.data['email_address']) \
            .one()
        assert_equals(user.first_name, 'foo')
        self.dummy_users.append(user)

    def test_update_entity_without_updated_by_argument(self):
        user = models.Users(**self.data)
        self.db_context.add(user, created_by=-1)
        self.db_context.commit()

        user.first_name = 'foo'
        assert_raises(TypeError, self.db_context.add, user)

        self.dummy_users.append(user)

    def teardown(self):
        for dummy_user in self.dummy_users:
            self.db_context.delete(dummy_user)
            self.db_context.commit()

