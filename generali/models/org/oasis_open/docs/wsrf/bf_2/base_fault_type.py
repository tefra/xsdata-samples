from dataclasses import dataclass, field
from typing import Dict, List, Optional
from xsdata.models.datatype import XmlDateTime
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
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Timestamp",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
            "required": True,
        },
    )
    originator: Optional[EndpointReferenceType] = field(
        default=None,
        metadata={
            "name": "Originator",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    error_code: Optional[BaseFaultTypeErrorCode] = field(
        default=None,
        metadata={
            "name": "ErrorCode",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    description: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    fault_cause: Optional[BaseFaultTypeFaultCause] = field(
        default=None,
        metadata={
            "name": "FaultCause",
            "type": "Element",
            "namespace": "http://docs.oasis-open.org/wsrf/bf-2",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
