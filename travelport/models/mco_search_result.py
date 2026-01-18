from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.name_1 import Name1
from travelport.models.type_mcostatus import TypeMcostatus
from travelport.models.type_mcotype import TypeMcotype

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class McoSearchResult:
    """
    Parameters
    ----------
    name
    create_date
        The date the MCO was issued
    number
        The MCO number
    status
        The status of the MCO
    type_value
        The Type of the MCO
    locator_code
        The locator code that the MCO is linked to
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: None | Name1 = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    create_date: XmlDateTime = field(
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
            "required": True,
        }
    )
    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    status: TypeMcostatus = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: TypeMcotype = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
        },
    )
