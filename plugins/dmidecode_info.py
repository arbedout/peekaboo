#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

def dmidecode_info():
    data = {}

    # Serial number
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'system-serial-number'], stdout=PIPE).communicate()[0]
        data['serial_number'] = output.strip()
    except:
        pass

    # Manufacturer
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'system-manufacturer'], stdout=PIPE).communicate()[0]
        data['manufacturer'] = output.strip()
    except:
        pass

    # Version
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'system-version'], stdout=PIPE).communicate()[0]
        data['product_version'] = output.strip()
    except:
        pass

    # Product name
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'system-product-name'], stdout=PIPE).communicate()[0]
        data['product'] = output.strip()
    except:
        pass

    # BIOS release date
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'bios-release-date'], stdout=PIPE).communicate()[0]
        data['bios_rel_date'] = output.strip()
    except:
        pass

    # BIOS vendor
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'bios-vendor'], stdout=PIPE).communicate()[0]
        data['bios_vendor'] = output.strip()
    except:
        pass

    # BIOS version
    try:
        output = Popen(['sudo', 'dmidecode', '-s', 'bios-version'], stdout=PIPE).communicate()[0]
        data['bios_version'] = output.strip()
    except:
        pass

    return data

if __name__ == "__main__":
    print dmidecode_info()
