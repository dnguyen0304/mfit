# -*- coding: utf-8 -*-

import collections

from sqlalchemy import Column
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:

    created_on = Column()
    created_by = Column()
    updated_on = Column()
    updated_by = Column()

    def to_json(self):

        """
        Return Dictionary

        Convert the object into a JSON representation.
        """

        # TODO (duyn): ME-201
        metadata = collections.OrderedDict([
            ('created_on', str(self.created_on)),
            ('created_by', str(self.created_by)),
            ('updated_on', str(self.updated_on)),
            ('updated_by', str(self.updated_by))])

        document = self._to_json_helper()
        document.update(metadata)

        return document

    def _to_json_helper(self):
        pass

