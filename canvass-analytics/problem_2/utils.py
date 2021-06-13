from collections import namedtuple
import datetime
from enum import Enum
from os import environ
import typing as t

import dateparser


DEFAULT_NUM_OF_CHUNKS = 10
NUM_OF_CHUNKS = int(environ.get("NUM_OF_CHUNKS", DEFAULT_NUM_OF_CHUNKS))


def _date_factory(s: str) -> t.Optional[datetime.date]:
    try:
        date_formats = [
            "%Y-%M-%d",
            "%-m/%-d/-%y",
        ]
        date_time: datetime.datetime = dateparser.parse(s, date_formats=date_formats)
        date: datetime.date = date_time.date() if date_time is not None else None
    except Exception as e:
        print(e, f"s={s}")
        return None
    return date


def _int_factory(s: str) -> t.Optional[int]:
    try:
        return int(s)
    except ValueError:
        return None


class ColumnNames(Enum):
    DEVICE_ID = "Device_ID"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    DATE = "Date"


COLUMN_FACTORIES: t.Dict[str, t.Callable[[str], t.Any]] = {
    ColumnNames.DEVICE_ID.value: _int_factory,
    ColumnNames.A.value: _int_factory,
    ColumnNames.B.value: _int_factory,
    ColumnNames.C.value: _int_factory,
    ColumnNames.D.value: _int_factory,
    ColumnNames.DATE.value: _date_factory,
}
COLUMN_DEFAULTS: t.Dict[str, t.Any] = {
    ColumnNames.DEVICE_ID.value: 0,
    ColumnNames.A.value: 0,
    ColumnNames.B.value: 0,
    ColumnNames.C.value: 0,
    ColumnNames.D.value: 0,
    ColumnNames.DATE.value: datetime.date.min,
}
Row = namedtuple(
    typename="Row",
    field_names=(t.value for t in ColumnNames),
)


def make_chunk_file_name(base_file_name: str, chunk_id: int) -> str:
    return f"{base_file_name}.chunk.{chunk_id}"
