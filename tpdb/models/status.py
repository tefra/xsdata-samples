from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.maybe import Maybe
from tpdb.models.no import No
from tpdb.models.yes import Yes


@dataclass(kw_only=True)
class Status:
    """
    This tag shows the termination status of this problem, if known.

    The reason for using sub-elements is that &lt;yes/&gt; can optionally
    be extended by complexity bound information.
    """

    class Meta:
        name = "status"

    no: None | No = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    maybe: None | Maybe = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    yes: None | Yes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
