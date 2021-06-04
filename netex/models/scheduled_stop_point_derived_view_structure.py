from dataclasses import dataclass, field
from typing import Optional
from netex.models.derived_view_structure import DerivedViewStructure
from netex.models.external_object_ref_structure import ExternalObjectRefStructure
from netex.models.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.models.multilingual_string import MultilingualString
from netex.models.presentation_structure import PresentationStructure
from netex.models.private_code import PrivateCode
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.scheduled_stop_point_ref import ScheduledStopPointRef
from netex.models.stop_type_enumeration import StopTypeEnumeration
from netex.models.type_of_point_ref import TypeOfPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScheduledStopPointDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "ScheduledStopPoint_DerivedViewStructure"

    fare_scheduled_stop_point_ref: Optional[FareScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRef] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_point_ref: Optional[TypeOfPointRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_suffix: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_stop_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "ShortStopCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_stop_point_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stop_type: Optional[StopTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compass_bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "CompassBearing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
