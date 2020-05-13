# The application will run until the task kill is executed. This can be used for many purpose, like listening to a RabbitMQ queue for example.
#!/usr/bin/env python
import signal
import sys
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
