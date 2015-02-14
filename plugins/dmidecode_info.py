#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import isfile
from subprocess import CalledProcessError, check_output

def _get_dmi_info(name, fname):
    val = ''
    try:
        val = check_output(['sudo', 'dmidecode', '-s', 'system-serial-number'])
    except CalledProcessError as e:
        if isfile(fname):
            f = open(fname, 'r')
            val = f.readline()
            f.close
    return val.strip()

def dmidecode_info():
    data = {}
    data['serial_number'] = _get_dmi_info('system-serial-number', '/sys/devices/virtual/dmi/id/product_serial')
    data['manufacturer'] = _get_dmi_info('system-manufacturer', '/sys/devices/virtual/dmi/id/chassis_vendor')
    data['product_version'] = _get_dmi_info('product_version', '/sys/devices/virtual/dmi/id/product_version')
    data['product'] = _get_dmi_info('system-product-name', '/sys/devices/virtual/dmi/id/product_name')
    data['bios_date'] = _get_dmi_info('bios-release-date', '/sys/devices/virtual/dmi/id/bios_date')
    data['bios_vendor'] = _get_dmi_info('bios-vendor', '/sys/devices/virtual/dmi/id/bios_vendor')
    data['bios_version'] = _get_dmi_info('bios-version', '/sys/devices/virtual/dmi/id/bios_version')
    return data

if __name__ == "__main__":
    print dmidecode_info()
