import multiprocessing
bind = "0.0.0.0:8080"
workers = 2
errorlog = '/home/shawn/blog_project/gunicorn.error.log'

#accesslog = './gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'gunicorn_blog_project'