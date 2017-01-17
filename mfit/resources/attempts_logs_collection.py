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

        data = [self._resource.get_self_link(entity=attempts_log)
                for attempts_log
                in attempts_logs]

        links = {
            'self': app.api.url_for(AttemptsLogsCollection,
                                    attempts_id=attempts_id,
                                    _external=True)
        }

        return collections.OrderedDict([('data', data), ('links', links)])

    def post(self, attempts_id):
        return super().post()


AttemptsLogsCollection._resource_collection = AttemptsLogsCollection

