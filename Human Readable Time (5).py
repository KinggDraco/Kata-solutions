def make_readable(seconds):
    hours = 0
    minutes = 0
    secs = 0
    
    while seconds >= 1:
        if seconds >= 3600:
            hours += 1
            seconds -= 3600
        elif seconds >= 60:
            minutes += 1
            seconds -= 60
        else:
            secs += 1
            seconds -= 1
    return(f"{hours:02}" + ":" + f"{minutes:02}" + ":" + f"{secs:02}")
