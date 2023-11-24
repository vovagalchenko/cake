#!/usr/bin/python3 -u

from __future__ import print_function
from builtins import str
import subprocess, sys, os, tempfile

print("Status: 204 No Content")
print("Content-Length: 0")
print()

tmp_dir_name = "/tmp/cooksmart"
if not os.path.exists(tmp_dir_name):
    sys.stderr.write("created tmp dir")
    os.makedirs(tmp_dir_name)
error_log_path = tmp_dir_name + '/error_log_' + str(os.getpid())
error_log = open(error_log_path, 'w')
analytics_body = os.fdopen(tempfile.mkstemp()[0], "w")
analytics_body.write(sys.stdin.read())
analytics_body.seek(0)
processing_script_path = os.path.join(os.path.abspath(sys.path[0]), "process_analytics.py")
p = subprocess.Popen([processing_script_path, error_log_path], stdout=error_log, stderr=error_log, stdin=analytics_body)
