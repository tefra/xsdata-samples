from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    Sdg,
    VariationPoint,
)
from .any_instance_ref import AnyInstanceRef
from .c_identifier import CIdentifier
from .nmtoken_string import NmtokenString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RptHook:
    """
    This meta class provide the ability to describe a rapid prototyping
    hook.

    This can either be described by an other AUTOSAR system with the
    category RPT_SYSTEM or as a non AUTOSAR software.

    :ivar code_label: This attribute provides a code label which is used
        in the implementation of the hook. For example this can be an C
        function name or the name of data definition.
    :ivar mcd_identifier: This attribute provides an identifier which
        shall be used in a MCD System to display the Rpt Hook.
    :ivar rpt_ar_hook_iref: This describes the hook with the means of
        another AUTOSAR system.
    :ivar sdgs: This property allows to keep special data which is not
        represented by the standard model. It can be utilized to keep
        e.g. tool specific data.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "RPT-HOOK"

    code_label: CIdentifier | None = field(
        default=None,
        metadata={
            "name": "CODE-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mcd_identifier: NmtokenString | None = field(
        default=None,
        metadata={
            "name": "MCD-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rpt_ar_hook_iref: AnyInstanceRef | None = field(
        default=None,
        metadata={
            "name": "RPT-AR-HOOK-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sdgs: RptHook.Sdgs | None = field(
        default=None,
        metadata={
            "name": "SDGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class Sdgs:
        sdg: list[Sdg] = field(
            default_factory=list,
            metadata={
                "name": "SDG",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
