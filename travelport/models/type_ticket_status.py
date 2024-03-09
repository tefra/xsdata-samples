from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeTicketStatus(Enum):
    """
    Status for the ticket (Ticketed, Voided, etc)

    Properties
    ----------
    U
        Code="U" Description="Unticketed"
    T
        Code="T" Description="Ticketed"
    V
        Code="V" Description="Voided"
    R
        Code="R" Description="Refunded"
    X
        Code="X" Description="eXchanged"
    Z
        Code="Z" Description="Unknown/Archived/Carrier Modified"
    N
        Code="N" Description="Unused"
    S
        Code="S" Description="Used"
    """

    U = "U"
    T = "T"
    V = "V"
    R = "R"
    X = "X"
    Z = "Z"
    N = "N"
    S = "S"
