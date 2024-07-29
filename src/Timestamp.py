from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')

def getTimeStamp():
    now = datetime.now(JST)
    return now.strftime("%Y%m%d%H%M%S")