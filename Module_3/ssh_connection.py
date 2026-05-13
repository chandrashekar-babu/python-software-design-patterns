from threading import Thread

class SSHConnection:
    attrs = "open", "get", "put", "chmod", "exec_command", "mkdir", "rmdir"

    def __init__(self, hostname, username, password, queue):
        self.hostname, self.username, self.password = hostname, username, password
        self.queue = queue

        from paramiko import SSHClient, AutoAddPolicy
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())

    def __enter__(self):
        self.client.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.password)

        self.channel = self.client.invoke_shell()
        self.stdin = self.channel.makefile("w")
        self.stdout = self.channel.makefile("r")
        self.stderr = self.channel.makefile_stderr("r")
        self.output_thread = Thread(target=self.output)
        self.error_thread = Thread(target=self.error)
        self.output_thread.start()
        self.error_thread.start()
        self.sftp_client = self.client.open_sftp()

        return self

    def __getattr__(self, attr):
        if attr not in self.attrs:
            raise AttributeError(
                f"'{self.__class__}' object has no attribute '{attr}'")

        elif hasattr(self.sftp_client, attr):
            return getattr(self.sftp_client, attr)
        elif hasattr(self.client, attr):
            return getattr(self.client, attr)

    def __exit__(self, et, ev, tb):
        self.sftp_client.close()
        self.stdout.close()
        self.stderr.close()
        self.stdin.close()
        self.channel.close()
        self.client.close()

    def exec(self, command):
         self.stdin.write(command + "\n")

    def output(self):
        for line in self.stdout:
            self.queue.put(self.hostname, "stdout", line)

    def error(self):
        for line in self.stderr:
            self.queue.put(self.hostname, "stderr", line)
