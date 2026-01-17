from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


class TypeResidency5(Enum):
    """
    The passenger residency type.Residence Type can be Employee, National
    or Resident.
    """

    EMPLOYEE = "Employee"
    NATIONAL = "National"
    RESIDENT = "Resident"
