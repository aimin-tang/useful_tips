# https://docs.fabfile.org/en/2.6/
# pip install fabric

import fabric

host = 'host_ipv6'
user = 'user'
port = 22
pwd = 'pwd'
key_filename = 'key_file'

def fabric_run():
    c = fabric.Connection(
        host=host, user=user, port=port,
        connect_kwargs={"key_filename": key_filename},
    )

    r = c.run('ls', hide=True)
    print('stdout: {}'.format(r.stdout.strip()))
    print('stderr: {}'.format(r.stderr.strip()))
    print('ok: {}'.format(r.ok))
    print('===================')

def fabric_sudo():
    config = fabric.Config(overrides={'sudo': {'password': pwd}})
    c = fabric.Connection(
        host=host, user=user, port=port,
        config=config, connect_kwargs={"key_filename": key_filename},
    )
    r = c.sudo('ls', hide=True)
    print('stdout: {}'.format(r.stdout))
    print('stderr: {}'.format(r.stderr))
    print('ok: {}'.format(r.ok))
    print('===================')

def fabric_get():
    c = fabric.Connection(
        host=host, user=user, port=port,
        connect_kwargs={"key_filename": key_filename},
    )
    r = c.get('f_name')
    # r = c.put('myfiles.tgz', remote='/opt/mydata/')
    print(r.local, r.remote)

if __name__ == '__main__':
    fabric_run()
    fabric_sudo()
    fabric_get()
