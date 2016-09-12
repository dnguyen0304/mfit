# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields


class Base(marshmallow.Schema):

    created_on = fields.DateTime()
    created_by = fields.Integer()
    updated_on = fields.DateTime()
    updated_by = fields.Integer()

    class Meta:
        ordered = True

