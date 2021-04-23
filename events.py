handlers = {}

def add_handler(type, handler):
  if type not in handlers:
    handlers[type] = []
  handlers[type].append(handler)

def handle(event):
  if event.type in handlers:
    for handler in handlers[event.type]:
      handler(event)