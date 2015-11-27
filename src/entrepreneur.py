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

    state_variables['wage_belief'] = 0  # belief about price of labour
    state_variables['equity'] = 0
    state_variables['capital'] = 0
    state_variables['money'] = 0
    state_variables['invetsment_opportunity'] = False  # Whether we can invest in this period

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

    def obtain_optimal_labour(self, environment):  # get labour from posts that will maximise profit given capital equity (wage beliefs on the side of workers)
        pass
        # shuffle the postings and find the ones below wage belief until end of postings or filled the requirements

    def update_wage_belief(self):  # Update belief about labour price
        pass

    def choose_optimal_investment(self):  # Here we chose optimal investment, maybe how much to consume also and call self.consume()
        # maximise productivity*capital^gamma*labour^(1-gamma)-wage_belief*labour | prod/gamma/wage_belief given, max capital, max labour iteration over two dim
        # will it always be max for max capital? if so just find the labour amount with fixed capital (1dim search with certain precision)
        # or do we maximize r as in (productivity*capital^gamma*labour^(1-gamma)-wage_belief*labour) / capital then more interesting but less reasonable
        # 
        pass

    def consume(self, environment):  # Smooth consumption (now|future) - from infinite sum of logs
        comsumption_amount = (1 - environment.static_parameters['beta']) * (state_variables['equity'] + state_variables['money'])  # money+equity, what about production?

    def amortisation(self, environment):
        self.state_variables['capital'] = self.state_variables['capital'] * environment.parameters['lambda']

    def invest(self):
        pass

#MAX PROFITS >> SMOOTH CONSUMPTION
#
