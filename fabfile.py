from __future__ import with_statement
from fabric.api import sudo, env, run, get, local, cd, prefix, put
from fabric.context_managers import shell_env
from contextlib import contextmanager as _contextmanager
from fabric.decorators import hosts


env.use_ssh_config = True
env.hosts = ['icm_django']
env.shell = 'bash -c'
env.directory = '/home/black_line_studio/black_line_studio'
env.activate = 'source /home/black_line_studio/env/bin/activate'
dbname = dbuser = 'black_line_studio'
hostuser = hostgroup = 'black_line_studio'
wsgifilename = 'black_line_studio'
DJANGO_SETTINGS_MODULE = "black_line_studio.settings.production"

@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            with shell_env(DJANGO_SETTINGS_MODULE=DJANGO_SETTINGS_MODULE):
                yield


def pull():
    with virtualenv():
        sudo('git pull origin master')
        sudo('chown -R %s:%s .' % (hostuser, hostgroup))


def initdb(islocal=False):
    if not islocal:
        run('/usr/pgsql-10/bin/createuser -U postgres -d %s' % dbuser)
        run('/usr/pgsql-10/bin/createdb -U %s %s' % (dbuser, dbname))
    local('createuser -U postgres -d %s' % dbuser)
    local('createdb -U %s %s' % (dbuser, dbname))


def servmigrate():
    with virtualenv():
        sudo('python manage.py migrate')


def getdb():
    run('pg_dump -h 10.11.29.106 -U %s %s > /tmp/%s.sql' % (dbuser, dbname, dbname))
    get('/tmp/%s.sql' % dbname, '/tmp/%s.sql' % dbname)
    run('rm /tmp/%s.sql' % dbname)


def updatedb():
    local('dropdb -U %s %s' % (dbuser, dbname))
    local('createdb -U %s %s' % (dbuser, dbname))
    local('psql -U %s %s < /tmp/%s.sql' % (dbuser, dbname, dbname))
    local('rm /tmp/%s.sql' % dbname)


def syncdb():
    getdb()
    updatedb()


def pushdb():
    local('pg_dump -U %s %s > /tmp/%s.sql' % (dbuser, dbname, dbname))
    local("sed -i -e 's/as integer//gI' /tmp/%s.sql" % (dbuser,))
    local("sed -i -e 's/SET row_security = off;//gI' /tmp/%s.sql" % (dbuser,))
    local("sed -i -e 's/SET idle_in_transaction_session_timeout = 0;//gI' /tmp/%s.sql" % (dbuser,))
    local("sed -i -e 's/CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;//gI' /tmp/%s.sql" % (dbuser,))
    # local("sed -i -e 's/COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';//gI' /tmp/%s.sql" % (dbuser,))
    put('/tmp/%s.sql' % dbname, '/tmp/%s.sql' % dbname)
    local('rm /tmp/%s.sql' % dbname)
    sudo('/usr/pgsql-10/bin/dropdb -U %s %s' % (dbuser, dbname))
    sudo('/usr/pgsql-10/bin/createdb -U %s %s' % (dbuser, dbname))
    sudo('/usr/pgsql-10/bin/psql -U %s %s < /tmp/%s.sql' % (dbuser, dbname, dbname))
    sudo('rm /tmp/%s.sql' % dbname)


def syncmedia():
    local('rsync -avzP -e ssh %s:%s/media/ ./media/' % (env.hosts, env.directory))


def pushmedia():
    local('rsync -avzP --rsync-path="sudo rsync" -e ssh ./media/ %s:%s/media/' % (env.host, env.directory))


def deploy():
    pull()
    with virtualenv():
       sudo('python manage.py collectstatic --noinput')
       sudo('touch %s.wsgi' % wsgifilename)


def updateenv():
    pull()
    with virtualenv():
        sudo('pip install -r requirements.txt')
