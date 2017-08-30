#!/usr/bin/env python
# -*- coding: utf-8 -*-
############
# Standard #
############
import logging
import time
from collections import OrderedDict
import pytest

###############
# Third Party #
###############
import numpy as np
from ophyd.device import Device

########
# SLAC #
########

##########
# Module #
##########
from .conftest import (using_fake_epics_pv, get_classes_in_module)
from pcdsdevices.epics import aerotech

logger = logging.getLogger(__name__)

@using_fake_epics_pv
@pytest.mark.parametrize("dev", get_classes_in_module(aerotech, Device))
def test_aerotech_devices_instantiate_and_run_ophyd_functions(dev):
    device = dev("TEST")
    assert(isinstance(device.read(), OrderedDict))
    assert(isinstance(device.describe(), OrderedDict))
    assert(isinstance(device.describe_configuration(), OrderedDict))
    assert(isinstance(device.read_configuration(), OrderedDict))
    
