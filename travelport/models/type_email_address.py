from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.email_1 import Email1
from travelport.models.simple_name_1 import SimpleName1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class TypeEmailAddress:
    class Meta:
        name = "typeEmailAddress"

    email: None | Email1 = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    simple_name: None | SimpleName1 = field(
        default=None,
        metadata={
            "name": "SimpleName",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
