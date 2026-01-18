from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.severity_enum import SeverityEnum
from datexii.models.eu.datexii.v2.situation_record import SituationRecord
from datexii.models.eu.datexii.v2.situation_versioned_reference import (
    SituationVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Situation:
    """
    An identifiable instance of a traffic/travel situation comprising one
    or more traffic/travel circumstances which are linked by one or more
    causal relationships.

    Each traffic/travel circumstance is represented by a Situation Record.

    :ivar overall_severity: The overall assessment of the impact (in
        terms of severity) that the situation as a whole is having, or
        will have, on the traffic flow as perceived by the supplier.
    :ivar related_situation: A reference to a related situation via its
        unique identifier.
    :ivar situation_version_time: The date/time that this current
        version of the Situation was written into the database of the
        supplier which is involved in the data exchange. Identity and
        version of the situation are defined by the class stereotype
        implementation.
    :ivar header_information:
    :ivar situation_record:
    :ivar situation_extension:
    :ivar id:
    :ivar version:
    """

    overall_severity: None | SeverityEnum = field(
        default=None,
        metadata={
            "name": "overallSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    related_situation: list[SituationVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    situation_version_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "situationVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    header_information: None | HeaderInformation = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    situation_record: list[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    situation_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "situationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
