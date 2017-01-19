# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative

__all__ = ['Base']


@as_declarative()
class Base:

    # When the primary key is named "id", not specifying the data type
    # causes SQLAlchemy to raise warnings, FlushErrors, and
    # CompileErrors.
    id = Column(Integer, primary_key=True)

    created_at = Column()
    created_by = Column()
    updated_at = Column()
    updated_by = Column()

