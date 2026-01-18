from __future__ import annotations

from dataclasses import dataclass, field

from ...hl7_v3.ne2008.core.datatypes_base import Ii
from ...hl7_v3.ne2008.multi_cache.mcci_in000002_uv01 import McciIn000002Uv01
from ...hl7_v3.ne2008.multi_cache.prpa_in201304_uv02 import PrpaIn201304Uv02
from ...hl7_v3.ne2008.multi_cache.prpa_in201309_uv02 import PrpaIn201309Uv02
from ...hl7_v3.ne2008.multi_cache.prpa_in201310_uv02 import PrpaIn201310Uv02
from ...hl7_v3.ne2008.multi_cache.prpa_mt201301_uv02 import (
    PrpaMt201301Uv02Patient,
)
from ...hl7_v3.ne2008.multi_cache.prpa_mt201307_uv02 import (
    PrpaMt201307Uv02QueryByParameter,
)
from ...hl7_v3.ne2008.multi_cache.prpa_mt201310_uv02 import (
    PrpaMt201310Uv02Patient,
)
from ..common.nhinc_common import (
    AssertionType,
    NhinTargetCommunitiesType,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CreateFault201310RequestType:
    sender_oid: None | str = field(
        default=None,
        metadata={
            "name": "senderOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    receiver_oid: None | str = field(
        default=None,
        metadata={
            "name": "receiverOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class Create201302RequestType:
    prpa201310_patient: None | PrpaMt201310Uv02Patient = field(
        default=None,
        metadata={
            "name": "PRPA201310Patient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    prpa201301_patient: None | PrpaMt201301Uv02Patient = field(
        default=None,
        metadata={
            "name": "PRPA201301Patient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    remote_patient_id: None | str = field(
        default=None,
        metadata={
            "name": "remotePatientId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    remote_device_id: None | str = field(
        default=None,
        metadata={
            "name": "remoteDeviceId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    sender_oid: None | str = field(
        default=None,
        metadata={
            "name": "senderOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    receiver_oid: None | str = field(
        default=None,
        metadata={
            "name": "receiverOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class Create201305RequestType:
    prpa201301_patient: None | PrpaMt201301Uv02Patient = field(
        default=None,
        metadata={
            "name": "PRPA201301Patient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    local_device_id: None | str = field(
        default=None,
        metadata={
            "name": "localDeviceId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    sender_oid: None | str = field(
        default=None,
        metadata={
            "name": "senderOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    receiver_oid: None | str = field(
        default=None,
        metadata={
            "name": "receiverOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class Create201310RequestType:
    pseudo_patient_id: None | str = field(
        default=None,
        metadata={
            "name": "pseudoPatientId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    pseudo_assigning_authority_id: None | str = field(
        default=None,
        metadata={
            "name": "pseudoAssigningAuthorityId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    local_device_id: None | str = field(
        default=None,
        metadata={
            "name": "localDeviceId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    sender_oid: None | str = field(
        default=None,
        metadata={
            "name": "senderOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    receiver_oid: None | str = field(
        default=None,
        metadata={
            "name": "receiverOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    prpa201307_query_by_parameter: None | PrpaMt201307Uv02QueryByParameter = (
        field(
            default=None,
            metadata={
                "name": "PRPA201307QueryByParameter",
                "type": "Element",
                "namespace": "urn:hl7-org:v3",
                "required": True,
            },
        )
    )


@dataclass
class CreateAckMsgRequestType:
    local_device_id: None | str = field(
        default=None,
        metadata={
            "name": "localDeviceId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    orig_msg_id: None | Ii = field(
        default=None,
        metadata={
            "name": "origMsgId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    msg_text: None | str = field(
        default=None,
        metadata={
            "name": "msgText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    sender_oid: None | str = field(
        default=None,
        metadata={
            "name": "senderOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    receiver_oid: None | str = field(
        default=None,
        metadata={
            "name": "receiverOID",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class CreateFault201310Request(CreateFault201310RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerMcciIn000002Uv01RequestType:
    class Meta:
        name = "PIXConsumer_MCCI_IN000002UV01RequestType"

    mcci_in000002_uv01: None | McciIn000002Uv01 = field(
        default=None,
        metadata={
            "name": "MCCI_IN000002UV01",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    assertion: None | AssertionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class PixconsumerPrpaIn201304UvrequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVRequestType"

    prpa_in201304_uv02: None | PrpaIn201304Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201304UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    assertion: None | AssertionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class PixconsumerPrpaIn201304UvsecuredRequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVSecuredRequestType"

    prpa_in201304_uv02: None | PrpaIn201304Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201304UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class PixconsumerPrpaIn201309UvrequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVRequestType"

    prpa_in201309_uv02: None | PrpaIn201309Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201309UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    assertion: None | AssertionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class PixconsumerPrpaIn201309UvresponseType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVResponseType"

    prpa_in201310_uv02: None | PrpaIn201310Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201310UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class PixconsumerPrpaIn201309UvsecuredRequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVSecuredRequestType"

    prpa_in201309_uv02: None | PrpaIn201309Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201309UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    nhin_target_communities: None | NhinTargetCommunitiesType = field(
        default=None,
        metadata={
            "name": "NhinTargetCommunities",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class PixconsumerPrpaIn201310UvrequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVRequestType"

    prpa_in201310_uv02: None | PrpaIn201310Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201310UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    assertion: None | AssertionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class PixconsumerPrpaIn201310UvsecuredRequestType:
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVSecuredRequestType"

    prpa_in201310_uv02: None | PrpaIn201310Uv02 = field(
        default=None,
        metadata={
            "name": "PRPA_IN201310UV02",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class Create201302Request(Create201302RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class Create201305Request(Create201305RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class Create201310Request(Create201310RequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class CreateAckMsgRequest(CreateAckMsgRequestType):
    class Meta:
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerMcciIn000002Uv01Request(
    PixconsumerMcciIn000002Uv01RequestType
):
    class Meta:
        name = "PIXConsumer_MCCI_IN000002UV01Request"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201304Uvrequest(PixconsumerPrpaIn201304UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201304UvsecuredRequest(
    PixconsumerPrpaIn201304UvsecuredRequestType
):
    class Meta:
        name = "PIXConsumer_PRPA_IN201304UVSecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309Uvrequest(PixconsumerPrpaIn201309UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309Uvresponse(PixconsumerPrpaIn201309UvresponseType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVResponse"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201309UvsecuredRequest(
    PixconsumerPrpaIn201309UvsecuredRequestType
):
    class Meta:
        name = "PIXConsumer_PRPA_IN201309UVSecuredRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201310Uvrequest(PixconsumerPrpaIn201310UvrequestType):
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVRequest"
        namespace = "urn:hl7-org:v3"


@dataclass
class PixconsumerPrpaIn201310UvsecuredRequest(
    PixconsumerPrpaIn201310UvsecuredRequestType
):
    class Meta:
        name = "PIXConsumer_PRPA_IN201310UVSecuredRequest"
        namespace = "urn:hl7-org:v3"
