from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


class TypeResidency3(StrEnum):
    """
    The passenger residency type.Residence Type can be Employee, National
    or Resident.
    """

    EMPLOYEE = "Employee"
    NATIONAL = "National"
    RESIDENT = "Resident"
