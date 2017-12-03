from datetime import datetime


class Timing(object):
    """
    For measurement execution time of a process.
    """

    def __init__(self, processname=''):
        self._processname = processname
        self._starttime = datetime
        self._endtime = datetime

    def start(self):
        if self._processname:
            print("'%s' started." % self._processname)
        self._starttime = datetime.now()

    def stop(self):
        self._endtime = datetime.now()
        elapsedtime = self._endtime - self._starttime
        if self._processname:
            print("'%s' finished." % self._processname)
            process = "'%s'" % self._processname
        else:
            process = ''
        print("++++++++++++SUMMARY+EXECUTION+TIME+%s+++++++++++++" % process)
        print("Elapsed time %s:" % process + "%d min, %.3f sec" % divmod(elapsedtime.total_seconds(), 60))
