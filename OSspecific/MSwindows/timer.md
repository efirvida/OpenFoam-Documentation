# timer 
## Class
timer

## Description
Implements a timeout mechanism. Usage is as following:

    timer myTimer(5);     // 5 sec
..
if (timedOut(myTimer))
{
        // timed out
}
else
{
        // do something possible blocking
}

Constructor set signal handler on sigalarm and alarm(). Destructor
clears these.

timedOut is macro because setjmp can't be in member function of timer.
?something to do with stack frames.

WARNING: setjmp restores complete register state so including local vars
held in regs. So if in blocking part something gets calced in a stack
based variable make sure it is declared 'volatile'.

## SourceFiles
timer.C

