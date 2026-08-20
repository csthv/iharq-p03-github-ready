from __future__ import annotations
from contextlib import contextmanager
import signal,threading,time

@contextmanager
def wallclock_limit(seconds,label='OPERATION'):
    """POSIX main-thread hard wall-clock guard used in Kaggle/Linux scientific stages.
    Falls back to post-hoc elapsed verification outside the main thread while still failing visibly.
    """
    seconds=float(seconds)
    if seconds<=0: raise ValueError('WALLCLOCK_LIMIT_MUST_BE_POSITIVE')
    start=time.monotonic(); armed=False; old_handler=None
    def _timeout(signum,frame): raise TimeoutError(f'FAILED_TIMEOUT:{label}:{seconds}s')
    if threading.current_thread() is threading.main_thread() and hasattr(signal,'SIGALRM'):
        old_handler=signal.getsignal(signal.SIGALRM); signal.signal(signal.SIGALRM,_timeout); signal.setitimer(signal.ITIMER_REAL,seconds); armed=True
    try:
        yield
    finally:
        if armed:
            signal.setitimer(signal.ITIMER_REAL,0); signal.signal(signal.SIGALRM,old_handler)
        elapsed=time.monotonic()-start
        if elapsed>seconds and not armed: raise TimeoutError(f'FAILED_TIMEOUT:{label}:{elapsed:.3f}>{seconds}s')
