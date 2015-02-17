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

def dict_to_html(data, indent = ' ' * 4, pad = ''):
    html = '{0}<dl>\n'.format(pad)
    for key, val in data.items():
        pad2 = pad + indent
        if isinstance(val, list):
            html += '{0}<dt>{1}</dt>\n{2}<dd>\n{3}\n{4}</dd>\n'.format(pad2, key, pad2, list_to_html(val, indent, pad2 + indent), pad2)
        elif isinstance(val, dict):
            html += '{0}<dt>{1}</dt>\n{2}<dd>\n{3}\n{4}</dd>\n'.format(pad2, key, pad2, dict_to_html(val, indent, pad2 + indent), pad2)
        else:
            html += '{0}<dt>{1}</dt>\n{2}<dd>{3}</dd>\n'.format(pad2, key, pad2, val)
    html += '{0}</dl>'.format(pad)
    return html

def list_to_html(data, indent = ' ' * 4, pad = ''):
    html = '{0}<ul>\n'.format(pad)
    for val in data:
        pad2 = pad + indent
        if isinstance(val, list):
            html += '{0}<li>\n{1}\n{2}</li>\n'.format(pad2, list_to_html(val, indent, pad2 + indent), pad2)
        elif isinstance(val, dict):
            html += '{0}<li>\n{1}\n{2}</li>\n'.format(pad2, dict_to_html(val, indent, pad2 + indent), pad2)
        else:
            html += '{0}<li>{1}</li>\n'.format(pad2, val)
    html += '{0}</ul>'.format(pad)
    return html

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

render_html = lambda **args: '<html>\n{0}<body>\n{1}\n{2}</body>\n</html>\n'.format(' ' * 4, dict_to_html(args, ' ' * 4, ' ' * 8), ' ' * 4)
render_json = lambda **args: json.dumps(args, indent = 4)
render_yaml = lambda **args: yaml.safe_dump(args)

@app.route('/info', methods=["GET"])
@mimerender(
    default = 'html',
    html = render_html,
    yaml  = render_yaml,
    json = render_json
)
def get_info():
    return get_data('plugins/info/')

@app.route('/status', methods=["GET"])
@mimerender(
    default = 'html',
    html = render_html,
    yaml  = render_yaml,
    json = render_json
)
def get_status():
    return get_data('plugins/status/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
