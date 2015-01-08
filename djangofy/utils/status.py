import sys
import utils

class Status():

    def __init__(self, process=''):
        self.process = process

    def _join(s):
        if isinstance(s, list) or isinstance(s, tuple):
            s = ' '.join(s)
        return s

   # Shortcut to print status along with the name of the process
    def log(s):
        s = self._join(s)
        S = "[{process}]".format(process=self.process) + ' ' + s
        lib.log(S)

#         with open('publish.log', 'a') as f:
#             f.write(S+"\n")
#         return

    # Print important message to screen and log
    def important(s):
        s = self._join(s)
        S = (
            "[{process}] ** IMPORTANT!\n\n{s}\n**\n"
        ).format(process=self.process, s=s)
        print S
        lib.log(S)

    # Stop execution
    def stop():
        self.important("Stopping execution here!")
        sys.exit(0) 
