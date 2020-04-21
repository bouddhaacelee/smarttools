import sys


def progress(count, total, status=''):
    from time import time, gmtime, strftime
    global start
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
   
    if count == 0:
        start = time()
    if percents != 0:
        remaining_time = ((100-percents)*(time()-start))/percents
        remaining_time = gmtime(remaining_time)
    else:
        remaining_time = gmtime()
    
    sys.stdout.write('%s : [%s] %s%s ...%s\r' % (strftime("%H:%M:%S", remaining_time), bar, percents, '%', status))
    sys.stdout.flush()

if __name__ == "__main__":
    import time
    for i in range(20):
        progress(i, 20)
        time.sleep(1)

