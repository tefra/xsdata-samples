from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "http://www.travelport.com/soa/common/security/SessionContext_v1"
)


@dataclass
class SessionContext:
    """
    A XML payload that contains either the Session Context Token or the Session
    Properties.

    Parameters
    ----------
    sess_tok
        A Session Token provided by Travelport
    sess_prop
        A session property combination
    """

    class Meta:
        namespace = (
            "http://www.travelport.com/soa/common/security/SessionContext_v1"
        )

    sess_tok: None | SessionContext.SessTok = field(
        default=None,
        metadata={
            "name": "SessTok",
            "type": "Element",
        },
    )
    sess_prop: list[SessionContext.SessProp] = field(
        default_factory=list,
        metadata={
            "name": "SessProp",
            "type": "Element",
            "max_occurs": 999,
        },
    )

    @dataclass
    class SessTok:
        """
        Parameters
        ----------
        id
            ID of the Session Token
        """

        id: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SessProp:
        """
        Parameters
        ----------
        nm
            Name of the Session Property
        val
            Value of the Session Property
        """

        nm: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
        val: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )
