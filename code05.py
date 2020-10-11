def make_readable(seconds):
    hr = 0
    m = 0
    sec = 0
    hr = seconds//3600
    seconds = seconds % 3600
    m = seconds//60
    seconds = seconds % 60
    sec = seconds
    return '{:02d}'.format(hr) + ':' + '{:02d}'.format(m) + ':' + '{:02d}'.format(sec)