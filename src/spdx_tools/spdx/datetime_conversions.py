# SPDX-FileCopyrightText: 2022 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from datetime import datetime


def datetime_from_str(date_str: str) -> datetime:
    if not isinstance(date_str, str):
        raise TypeError(f"Could not convert str to datetime, invalid type: {type(date_str).__name__}")

    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")  # raises ValueError if format does not match
    return date


def datetime_to_iso_string(date: datetime) -> str:
    """
    Return an ISO-8601 representation of a datetime object.
    """
    return date.isoformat() + "Z"
