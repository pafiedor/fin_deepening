#!/usr/bin/env python
# [SublimeLinter pep8-max-line-length:300]
# -*- coding: utf-8 -*-

"""
fin_deepening is a multi-agent computational model extending
the Kitoyaki/Moore financial deeepening theta-phi model.
Copyright (C) 2015 Paweł Fiedor (Pawel.F.Fiedor@IEEE.org)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

# import logging
# import math
from abm_template.src.baserunner import BaseRunner

# ============================================================================
#
# class Runner
#
# ============================================================================


class Runner(BaseModel):

    identifier = ""
    num_simulations = 0

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Runner, self).set_identifier(_value)

    def get_num_simulations(self):
        return self.model_parameters

    def set_num_simulations(self, _value):
        super(Runner, self).set_num_simulations(_value)

    def __init__(self, model_config):
        super(Model, self).__init__(model_config)

    def do_run(self):
        super(Model, self).do_run()
