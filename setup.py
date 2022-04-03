import os

import pydevd_pycharm

from app import create_app

app = create_app()

debug = os.getenv('DEBUG', 'False')
if debug == 'True':
    pydevd_pycharm.settrace('host.docker.internal', port=4586, stderrToServer=True, stdoutToServer=True, suspend=False)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=4586)
