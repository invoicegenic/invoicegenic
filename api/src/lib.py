'''
'''
from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(tz=timezone.utc)


def to_utc_iso(dt: datetime) -> str:
    return dt.isoformat() + 'Z'


def to_mysql_datetime_string(dt: datetime) -> str:
    return dt.strftime('%Y-%m-%d %H:%M:%S')
