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
# class Worker
#
# ============================================================================


class Worker(BaseAgent):

    identifier = ""
    parameters = {}
    state_variables = {}
    accounts = []

    state_variables['wage_belief'] = 0  # belief about price of labour

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Worker, self).set_identifier(_value)

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, _value):
        super(Worker, self).set_parameters(_value)

    def get_state_variables(self):
        return self.state_variables

    def set_state_variables(self, _value):
        super(Worker, self).set_state_variables(_value)

    def __str__(self):
        super(Worker, self).__str__()

    def __init__(self, _identifier, _params, _variables):
        super(Worker, self).__init__(_identifier, _params, _variables)

    def post_labour_offers(self, enviromnent):  # tries to sell optimally given wage beliefs
        optimal_labour_amount = self.find_optimal_labour_amount()
        enviromnent.postings.append([self.state_variables['wage_belief'], optimal_labour_amount, self])

    def update_wage_belief(self):  # Update belief about labour price
        pass

    def find_optimal_labour_amount(self):  # Find optimal amount of labour to sell given wage beliefs
        pass

    def consume(self):  # Workers consume everything they earn
        pass
