# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields

__all__ = ['Base']


class Base(marshmallow.Schema):

    id = fields.String()

    created_at = fields.DateTime()
    created_by = fields.String()
    updated_at = fields.DateTime()
    updated_by = fields.String()

    class Meta:
        ordered = True

