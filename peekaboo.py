#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import types
from flask import Flask, request, jsonify
from flaskmimerender import mimerender
import yaml
import json


def get_data(path):
    sys.path.insert(0, path)

    modules = {}
    for fn in glob.glob(path + '*.py'):
        fpath, fname = os.path.split(fn)
        mname, ext = os.path.splitext(fname)
        print >> sys.stderr, 'Load module: {0}'.format(mname)
        modules[mname] = __import__(mname)

    data = {}
    for module in modules:
        for name in dir(modules[module]):
            if isinstance(modules[module].__dict__.get(name), types.FunctionType) and not name.startswith('_'):
                print >> sys.stderr, 'Call function: {0}.{1}'.format(module, name)
                try:
                    data.update(modules[module].__dict__.get(name)())
                except:
                    print >> sys.stderr, 'Function call failed'
                    pass
    return data

app = Flask(__name__)

render_json = lambda **args: json.dumps(args, indent = 4)
render_yaml = lambda **args: yaml.safe_dump(args)

@app.route('/info', methods=["GET"])
@mimerender(
    default = 'yaml',
    yaml  = render_yaml,
    json = render_json
)
def get_info():
    return get_data('plugins/info/')

@app.route('/status', methods=["GET"])
@mimerender(
    default = 'yaml',
    yaml  = render_yaml,
    json = render_json
)
def get_status():
    return get_data('plugins/status/')

@app.route('/services', methods=["GET"])
@mimerender(
    default = 'yaml',
    yaml  = render_yaml,
    json = render_json
)
def get_services():
    return get_data('plugins/services/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
