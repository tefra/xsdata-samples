from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xmlns.generali.com/services/program/FeedbackProgramService/v1"


@dataclass
class LocalPoliciesTypeLocalPolicyPartyIdsPartyId:
    """
    :ivar value:
    :ivar party_type: Party type will be one of the following: INS -
        Insured CED - Cedant REI - Reinsurer BRK - Broker INC - Insurer
    :ivar party_guns:
    """
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    party_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Attribute",
        }
    )
    party_guns: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyGUNS",
            "type": "Attribute",
            "required": True,
        }
    )
