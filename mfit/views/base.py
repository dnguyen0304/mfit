# -*- coding: utf-8 -*-

import marshmallow
from marshmallow import fields


class Base(marshmallow.Schema):

    created_at = fields.DateTime()
    created_by = fields.String()
    updated_at = fields.DateTime()
    updated_by = fields.String()

    class Meta:
        ordered = True

