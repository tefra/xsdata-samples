from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class OtaAirLowFareSearchRqTransactionStatusCode(Enum):
    """
    Attributes:
        START: This is the first message within a transaction.
        END: This is the last message within a transaction.
        ROLLBACK: This indicates that all messages within the current
            transaction must be ignored.
        IN_SERIES: This is any message that is not the first or last
            message within a transaction.
    """

    START = "Start"
    END = "End"
    ROLLBACK = "Rollback"
    IN_SERIES = "InSeries"
