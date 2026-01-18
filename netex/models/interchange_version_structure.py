from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .access_mode_enumeration import AccessModeEnumeration
from .connection_certainty_enumeration import ConnectionCertaintyEnumeration
from .connection_ref_structure import ConnectionRefStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .external_object_ref_structure import ExternalObjectRefStructure
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class InterchangeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Interchange_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_interchange_ref: None | ExternalObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ExternalInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connection_ref: None | ConnectionRefStructure = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    priority: None | int = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stay_seated: None | bool = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_border: None | bool = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    planned: None | bool = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    guaranteed: None | bool = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    advertised: None | bool = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controlled: None | bool = field(
        default=None,
        metadata={
            "name": "Controlled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    connection_certainty: None | ConnectionCertaintyEnumeration = field(
        default=None,
        metadata={
            "name": "ConnectionCertainty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standard_wait_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_wait_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_automatic_wait_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standard_transfer_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_transfer_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_transfer_time: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    control_centre_notify_threshold: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "ControlCentreNotifyThreshold",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_modes: Iterable[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "transferModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    notice_assignments: None | NoticeAssignmentsRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
