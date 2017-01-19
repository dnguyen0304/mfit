# -*- coding: utf-8 -*-

import collections

from mfit import app
from mfit import models
from mfit import resources


class AttemptsLogsCollection(resources.BaseCollection):

    _model = models.AttemptsLogs
    _resource = resources.AttemptsLogs

    def get(self, attempts_id):
        attempts_logs = self._db_context.query(self._model) \
                                        .filter_by(attempts_id=attempts_id) \
                                        .all()

        data = [self._resource.get_self_url(entity=attempts_log)
                for attempts_log
                in attempts_logs]

        urls = {
            'self': self.get_self_url(entity=attempts_logs[0].attempt)
        }

        return collections.OrderedDict([('data', data), ('urls', urls)])

    def post(self, attempts_id):
        return super().post()

    @classmethod
    def get_self_url(cls, entity):
        return app.api.url_for(cls._resource_collection,
                               attempts_id=entity.id,
                               _external=True)


AttemptsLogsCollection._resource_collection = AttemptsLogsCollection

