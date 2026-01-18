from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .output_detail_enumeration import OutputDetailEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkFrameRequestPolicyStructure:
    maximum_number_of_elements: None | int = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    include_deleted: None | bool = field(
        default=None,
        metadata={
            "name": "IncludeDeleted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    urgency: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "Urgency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    must_have_by: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "MustHaveBy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_detail: Iterable[OutputDetailEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RequestDetail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
