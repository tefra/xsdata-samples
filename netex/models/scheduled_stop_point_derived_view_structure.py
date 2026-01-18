from dataclasses import dataclass, field
from typing import Optional, Union

from .derived_view_structure import DerivedViewStructure
from .external_object_ref_structure import ExternalObjectRefStructure
from .fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from .multilingual_string import MultilingualString
from .presentation_structure import PresentationStructure
from .private_code import PrivateCode
from .private_code_structure import PrivateCodeStructure
from .scheduled_stop_point_ref import ScheduledStopPointRef
from .stop_type_enumeration import StopTypeEnumeration
from .type_of_point_ref import TypeOfPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "ScheduledStopPoint_DerivedViewStructure"

    scheduled_stop_point_ref: FareScheduledStopPointRef | ScheduledStopPointRef | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_point_ref: TypeOfPointRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_suffix: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_stop_code: PrivateCodeStructure | None = field(
        default=None,
        metadata={
            "name": "ShortStopCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: PrivateCodeStructure | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: PrivateCode | None = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_stop_point_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: str | None = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stop_type: StopTypeEnumeration | None = field(
        default=None,
        metadata={
            "name": "StopType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    compass_bearing: float | None = field(
        default=None,
        metadata={
            "name": "CompassBearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: PresentationStructure | None = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
