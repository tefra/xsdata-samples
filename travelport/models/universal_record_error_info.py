from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_error_info_1 import TypeErrorInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecordErrorInfo(TypeErrorInfo1):
    """
    Parameters
    ----------
    locator_code
        Universal Record Locator Code.
    version
        Version of Universal Record.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "required": True,
        },
    )
