#from pubsub import PubSub


class PubSub:
    def __init__(self):
        #self.subscribers = {}
        from collections import defaultdict
        self.subscribers = defaultdict(list)

    def subscribe(self, event):
        def decorator(fn):
            
            #if event not in self.subscribers:
            #    self.subscribers[event] = []
            #self.subscribers[event].append(fn)
            
            #self.subscribers.setdefault(event, []).append(fn)
            self.subscribers[event].append(fn)

        return decorator

    def publish(self, event, *args, **kwargs):
        for subscriber in self.subscribers.get(event, []):
            subscriber(*args, **kwargs)


ps = PubSub()

@ps.subscribe("connect")
def on_connect(host):
    print("Handling connection to", host)

@ps.subscribe("connect")
def validate(host):
    print("Validating connection on", host)

@ps.subscribe("connect")
def log_connection(host):
    print("Logging connection on", host)

@ps.subscribe("exit")
def on_exit(host):
    print("Cleaning up resources for", host)


def run():
    print("Running the server...")
    ps.publish("connect", "localhost")
    print("working...")
    ps.publish("exit", "localhost")

if __name__ == '__main__':
    run()



