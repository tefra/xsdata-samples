from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.country_enum import CountryEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NamedArea:
    """An area defined by a name and/or in terms of known boundaries, such as
    country or county boundaries or allocated control area of particular authority.

    The attributes do not form a union; instead, the smallest
    intersection forms the resulting area.

    :ivar country: ISO 3166-1 two character country code.
    :ivar nation: Name of a nation (e.g. Wales) which is a sub-division
        of an ISO recognised country.
    :ivar county: Name of a county (administrative sub-division).
    :ivar area_name: Name of an area.
    :ivar police_force_control_area: Name of a police force area.
    :ivar road_operator_control_area: Name of a road operator control
        area.
    :ivar named_area_extension:
    """
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    nation: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    county: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    area_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "areaName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    police_force_control_area: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "policeForceControlArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    road_operator_control_area: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "roadOperatorControlArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    named_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "namedAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
