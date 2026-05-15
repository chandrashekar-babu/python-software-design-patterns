class NoSubscriber(Exception): pass

class PubSub:
    def __init__(self):
        from collections import defaultdict
        self.events = defaultdict(list)
        #self.events = {}

    def subscribe(self, event):
        def decorator(fn):
            self.events[event].append(fn)
            #self.events.setdefault(event, []).append(fn)
        return decorator

    def publish(self, event, *args, **kwargs):
        if event not in self.events:
            raise NoSubscriber(f"No subscribers registered for {event}")
        for subscriber in self.events[event]:
            subscriber(*args, **kwargs)
