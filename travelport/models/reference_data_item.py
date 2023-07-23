from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class ReferenceDataItem:
    """
    Parameters
    ----------
    additional_info
        Any additional information specific to a type of value being
        returned.
    code
        The code of the reference data item.
    name
        The name of the reference data item.
    description
        The description of the reference data item.
    deprecated
        Indicates if the reference data item is deprecated.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    additional_info: list[ReferenceDataItem.AdditionalInfo] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    deprecated: None | bool = field(
        default=None,
        metadata={
            "name": "Deprecated",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class AdditionalInfo:
        """
        Parameters
        ----------
        value
        type_value
            This will identify different additionalInfo.
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "min_length": 1,
                "max_length": 255,
            }
        )
        type_value: None | str = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
            }
        )
