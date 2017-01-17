# -*- coding: utf-8 -*-

from mfit import app
from mfit import models
from mfit import resources
from mfit import views


class AttemptsLogs(resources.Base):

    _model = models.AttemptsLogs
    _view = views.AttemptsLogs

    def get(self, id, attempts_id):
        return super().get(id=id)

    def put(self, id, attempts_id):
        return super().get(id=id)

    def delete(self, id, attempts_id):
        return super().get(id=id)

    @classmethod
    def get_self_link(cls, entity):
        return app.api.url_for(cls._resource,
                               attempts_id=entity.attempts_id,
                               id=entity.id,
                               _external=True)


AttemptsLogs._resource = AttemptsLogs

