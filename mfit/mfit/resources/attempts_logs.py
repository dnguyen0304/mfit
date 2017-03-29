# -*- coding: utf-8 -*-

import mfit
from . import Base
from mfit import models
from mfit import views


class AttemptsLogs(Base):

    _model = models.AttemptsLogs
    _view = views.AttemptsLogs

    def get(self, id, attempts_id):
        return super().get(id=id)

    def put(self, id, attempts_id):
        return super().get(id=id)

    def delete(self, id, attempts_id):
        return super().get(id=id)

    @classmethod
    def get_self_url(cls, entity):
        return mfit.api.url_for(cls._resource,
                                attempts_id=entity.attempts_id,
                                id=entity.id,
                                _external=True)


AttemptsLogs._resource = AttemptsLogs

