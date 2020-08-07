from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.travelport.com/soa/common/security/SessionContext_v1"


@dataclass
class SessionContext:
    """A XML payload that contains either the Session Context Token or the Session
    Properties.

    :ivar sess_tok: A Session Token provided by Travelport
    :ivar sess_prop: A session property combination
    """
    class Meta:
        namespace = "http://www.travelport.com/soa/common/security/SessionContext_v1"

    sess_tok: Optional["SessionContext.SessTok"] = field(
        default=None,
        metadata=dict(
            name="SessTok",
            type="Element"
        )
    )
    sess_prop: List["SessionContext.SessProp"] = field(
        default_factory=list,
        metadata=dict(
            name="SessProp",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class SessTok:
        """
        :ivar id: ID of the Session Token
        """
        id: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class SessProp:
        """
        :ivar nm: Name of the Session Property
        :ivar val: Value of the Session Property
        """
        nm: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )
        val: Optional[str] = field(
            default=None,
            metadata=dict(
                type="Attribute",
                required=True
            )
        )
