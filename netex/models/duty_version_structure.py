from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .duty_parts_rel_structure import DutyPartsRelStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .timetable_frame_ref import TimetableFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DutyVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Duty_VersionStructure"

    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    finishing_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preparation_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timetable_frame_ref: TimetableFrameRef | None = field(
        default=None,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duty_parts: DutyPartsRelStructure | None = field(
        default=None,
        metadata={
            "name": "dutyParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
