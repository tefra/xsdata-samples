from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from generali.models.org.oasis_open.docs.wsrf.bf_2.base_fault_type_description import (
    BaseFaultTypeDescription,
)
from generali.models.org.oasis_open.docs.wsrf.bf_2.base_fault_type_error_code import (
    BaseFaultTypeErrorCode,
)
from generali.models.org.oasis_open.docs.wsrf.bf_2.base_fault_type_fault_cause import (
    BaseFaultTypeFaultCause,
)
from generali.models.org.w3.pkg_2005.pkg_08.addressing.endpoint_reference_type import (
    EndpointReferenceType,
)

__NAMESPACE__ = "http://docs.oasis-open.org/wsrf/bf-2"


@dataclass
class BaseFaultType:
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    timestamp: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
            "required": True,
        },
    )
    originator: EndpointReferenceType | None = field(
        default=None,
        metadata={
            "name": "Originator",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    error_code: BaseFaultTypeErrorCode | None = field(
        default=None,
        metadata={
            "name": "ErrorCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    description: list[BaseFaultTypeDescription] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    fault_cause: BaseFaultTypeFaultCause | None = field(
        default=None,
        metadata={
            "name": "FaultCause",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
