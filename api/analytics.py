#!/usr/bin/python -u

import subprocess, sys, os

print "Status: 204 No Content"
print "Content-Length: 0"
print

tmp_dir_name = "/tmp/cooksmart"
if not os.path.exists(tmp_dir_name):
    sys.stderr.write("created tmp dir")
    os.makedirs(tmp_dir_name)
error_log_path = tmp_dir_name + '/error_log_' + str(os.getpid())
error_log = open(error_log_path, 'w')
analytics_body = os.tmpfile()
analytics_body.write(sys.stdin.read())
analytics_body.seek(0)
p = subprocess.Popen(['/var/asswaffle/www/api/process_analytics.py', error_log_path], stdout=error_log, stderr=error_log, stdin=analytics_body)
