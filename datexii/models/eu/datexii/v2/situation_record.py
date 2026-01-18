from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.cause import Cause
from datexii.models.eu.datexii.v2.comment import Comment
from datexii.models.eu.datexii.v2.confidentiality_value_enum import (
    ConfidentialityValueEnum,
)
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.impact import Impact
from datexii.models.eu.datexii.v2.management import Management
from datexii.models.eu.datexii.v2.probability_of_occurrence_enum import (
    ProbabilityOfOccurrenceEnum,
)
from datexii.models.eu.datexii.v2.severity_enum import SeverityEnum
from datexii.models.eu.datexii.v2.situation_record_extension_type import (
    SituationRecordExtensionType,
)
from datexii.models.eu.datexii.v2.source import Source
from datexii.models.eu.datexii.v2.url_link import UrlLink
from datexii.models.eu.datexii.v2.validity import Validity

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SituationRecord:
    """
    An identifiable versioned instance of a single record/element within a
    situation.

    :ivar situation_record_creation_reference: A unique alphanumeric
        reference (either an external reference or GUID) of the
        SituationRecord object (the first version of the record) that
        was created by the original supplier.
    :ivar situation_record_creation_time: The date/time that the
        SituationRecord object (the first version of the record) was
        created by the original supplier.
    :ivar situation_record_observation_time: The date/time that the
        information represented by the current version of the
        SituationRecord was observed by the original (potentially
        external) source of the information.
    :ivar situation_record_version_time: The date/time that this current
        version of the SituationRecord within the situation was written
        into the database of the supplier which is involved in the data
        exchange. Identity and version of record are defined by the
        class stereotype implementation.
    :ivar situation_record_first_supplier_version_time: The date/time
        that the current version of the Situation Record was written
        into the database of the original supplier in the supply chain.
    :ivar confidentiality_override: The extent to which the related
        information may be circulated, according to the recipient type.
        Recipients must comply with this confidentiality statement. This
        overrides any confidentiality defined for the situation as a
        whole in the header information.
    :ivar probability_of_occurrence: An assessment of the degree of
        likelihood that the reported event will occur.
    :ivar severity: The assessment of the impact (in terms of severity)
        that this element of the situation is having, or will have, on
        the traffic flow as perceived by the supplier.
    :ivar source:
    :ivar validity:
    :ivar impact:
    :ivar cause:
    :ivar general_public_comment: A comment which may be freely
        distributed to the general public
    :ivar non_general_public_comment: A comment which should not be
        distributed to the general public.
    :ivar url_link:
    :ivar group_of_locations:
    :ivar management:
    :ivar situation_record_extension:
    :ivar id:
    :ivar version:
    """

    situation_record_creation_reference: None | str = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    situation_record_creation_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    situation_record_observation_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    situation_record_version_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    situation_record_first_supplier_version_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "situationRecordFirstSupplierVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    confidentiality_override: None | ConfidentialityValueEnum = field(
        default=None,
        metadata={
            "name": "confidentialityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    probability_of_occurrence: None | ProbabilityOfOccurrenceEnum = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    severity: None | SeverityEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    source: None | Source = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    validity: None | Validity = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    impact: None | Impact = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    cause: None | Cause = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    general_public_comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    non_general_public_comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    url_link: list[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_locations: None | GroupOfLocations = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    management: None | Management = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    situation_record_extension: None | SituationRecordExtensionType = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
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
