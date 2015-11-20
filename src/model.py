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
from abm_template.src.basemodel import BaseModel

# ============================================================================
#
# class Model
#
# ============================================================================


class Entrepreneur(BaseModel):

    identifier = ""
    model_parameters = {}
    agents = []
    interactions = None

    def get_identifier(self):
        return self.identifier

    def set_identifier(self, _value):
        super(Model, self).set_identifier(_value)

    def get_model_parameters(self):
        return self.model_parameters

    def set_model_parameters(self, _value):
        super(Model, self).set_model_parameters(_value)

    def get_agents(self):
        return self.agents

    def set_agents(self, _value):
        super(Model, self).set_agents(_value)

    def get_interactions(self):
        return self.interactions

    def set_interactions(self, _value):
        super(Model, self).set_interactions(_value)

    def __str__(self):
        super(Model, self).__str__()

    def __init__(self, model_config):
        super(Model, self).__init__(model_config)

    def initialize_agents(self):
        super(Model, self).initialize_agents()

    def do_update(self):
        super(Model, self).do_update()

    def get_agent_by_id(self):
        super(Model, self).get_agent_by_id()

    def check_agent_homogeneity(self):
        super(Model, self).check_agent_homogeneity()
