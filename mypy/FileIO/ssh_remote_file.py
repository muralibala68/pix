import paramiko
# from contextlib import contextmanager


host = 'localhost'
user = 'user'
pwd = 'pwd'


def create_ssh(hostname=host, username=user, password=pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("connecting...")
        ssh.connect(hostname, username=username, password=password)
        print("connected")
        yield ssh
    finally:
        print("closing...")
        ssh.close()
        print("closed")


def main():
#    create_ssh(host, user, pwd)
    create_ssh()


# to be completed # ...


if __name__ == "__main__":
    main()
