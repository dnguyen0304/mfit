# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base():

    # TODO (duyn): Do you need to specify the column name if it is 
    # identical to the attribute?
    created_on = Column()
    created_by = Column()
    updated_on = Column()
    updated_by = Column()

