from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .coupling_port_subtypes_enum import CouplingPortSubtypesEnum
from .ref import Ref
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthGlobalTimeManagedCouplingPort:
    """
    Specifies a CouplingPort which is managed by an Ethernet Global Time Domain.

    :ivar coupling_port_ref: Defines which CouplingPort is managed by
        this EthGlobalTimeManagedCouplingPort.
    :ivar pdelay_latency_threshold: Threshold for calculated Pdelay. If
        a measured Pdelay exceeds pdelayLatencyThreshold, the measured
        Pdelay value is discarded.
    :ivar pdelay_request_period: Defines the period for the pdelay
        request messages.
    :ivar pdelay_resp_and_resp_follow_up_timeout: Timeout value for
        Pdelay_Resp and Pdelay_Resp_Follow_Up after a Pdelay_Req has
        been transmitted resp. a Pdelay_Resp has been received. A value
        of 0 or not defining this attribute deactivates this timeout
        observation.
    :ivar pdelay_response_enabled: Defines whether PDELAY RESPONSE and
        PDELAY RESPONSE FOLLOW UP shall be sent on this CouplingPort.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "ETH-GLOBAL-TIME-MANAGED-COUPLING-PORT"

    coupling_port_ref: Optional[
        "EthGlobalTimeManagedCouplingPort.CouplingPortRef"
    ] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdelay_latency_threshold: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PDELAY-LATENCY-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdelay_request_period: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PDELAY-REQUEST-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdelay_resp_and_resp_follow_up_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "PDELAY-RESP-AND-RESP-FOLLOW-UP-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdelay_response_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PDELAY-RESPONSE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class CouplingPortRef(Ref):
        dest: Optional[CouplingPortSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
