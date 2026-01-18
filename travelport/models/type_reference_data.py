from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class TypeReferenceData:
    """
    Parameters
    ----------
    code
        The code of the reference data item.
    name
        The name of the reference data item.
    description
        The description of the reference data item.
    deprecated_date
        Used to set deprecated date
    """

    class Meta:
        name = "typeReferenceData"

    code: str = field(
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
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    deprecated_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DeprecatedDate",
            "type": "Attribute",
        },
    )
