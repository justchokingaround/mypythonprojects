#!/usr/bin/env python3
import sys
import subprocess, os
from time import sleep, time

__author__ = "Prahlad Yeri"
__version__ = "1.0.7"


def execute_shell(command, error=''):
    return execute(command, wait=True, shellexec=True, errorstring=error)


def execute(command='', errorstring='', wait=True, shellexec=False, ags=None):
    try:
        if (shellexec):
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            p = subprocess.Popen(args=ags)
        # test
        if wait:
            p.wait()
            result = get_stdout(p)
            return result
        else:
            return p
    except subprocess.CalledProcessError as e:
        print('error occured:' + errorstring)
        return errorstring
    except Exception as ea:
        print('Exception occured:' + str(ea))
        return errorstring
        # show_message("Error occured: " + ea.message)


def get_stdout(pi):
    result = pi.communicate()
    if len(result[0]) > 0:
        return result[0]
    else:
        return result[1]  # some error has occured


def killall(process):
    cnt = 0
    pid = is_process_running(process)
    while pid != 0:
        execute_shell('kill ' + str(pid))
        pid = is_process_running(process)
        cnt += 1
    return cnt


def batt_per():
    cmd = "upower -i /org/freedesktop/UPower/devices/battery_BAT0"
    r = execute_shell(cmd)
    for line in r.splitlines():
        if line.strip().startswith(b'percentage:'):
            per = line.strip().split(b'percentage:')[1].strip().replace(b'%', b'')
            return float(per)


if __name__ == "__main__":
    print("Batteryboy v" + __version__);
    print("Waiting for battery data to change.\n");
    last_checked = 0
    last_per, per = 0, 0
    last_changed = 0
    total, tottime, average = 0, 0, 0
    start = time()
    is_first_time = True
    while (True):
        if (time() - last_checked) > 2:  # check again
            tottime = time() - start
            per = batt_per()
            if last_per > 0 and per != last_per:
                consumed = last_per - per
                if consumed < 0:
                    print("Negative consumption found. Is battery plugged in?")
                    break
                seconds = time() - last_changed
                if consumed > 1: seconds = seconds / consumed
                if not is_first_time:
                    total += consumed
                    average = (total / (tottime / 60 / 60))
                    print(
                        "Used ~1%% in %d secs. Remaining: %d%%, Total consumed: %d%%, Average consumed: %0.2f%% per hour." % (
                        seconds, per, total, average))
                is_first_time = False
                last_changed = time()
            elif last_per == 0:
                pass
            last_per = per
            last_checked = time()
            if last_changed == 0: last_changed = last_checked