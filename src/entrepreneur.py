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
from abm_template.src.baseagent import BaseAgent

# ============================================================================
#
# class Entrepreneur
#
# ============================================================================


class Entrepreneur(BaseAgent):

    identifier = ""
    parameters = {}
    state_variables = {}
    accounts = []

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Entrepreneur, self).set_identifier(_value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, _value):
        super(Entrepreneur, self).set_parameters(_value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _value):
        super(Entrepreneur, self).set_state_variables(_value)

    def __str__(self):
        super(Entrepreneur, self).__str__()

    def __init__(self, _identifier, _params, _variables):
        super(Entrepreneur, self).__init__(_identifier, _params, _variables)
