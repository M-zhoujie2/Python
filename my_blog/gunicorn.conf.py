# coding:utf-8
# !/btn/bash

import multiprocessing

bind = "127.0.0.1:8888"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
proc_name = "mdwiki"
user = "root"
chdir = "/root/api/python/my_blog"
# daemon = False
# group = "root"
loglevel = "info"
errorlog = chdir + "/log/gunicorn/error.log"
accesslog = chdir + "/log/gunicorn/access.log"
# ssl
# keyfile=
# certfile=
# ca_certs=
