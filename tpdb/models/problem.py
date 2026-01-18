from dataclasses import dataclass, field

from tpdb.models.metainformation import Metainformation
from tpdb.models.problem_type import ProblemType
from tpdb.models.startterm import Startterm
from tpdb.models.status import Status
from tpdb.models.strategy import Strategy
from tpdb.models.trs import Trs


@dataclass
class Problem:
    """
    This is the root element representing a termination problem.

    Versioning Information: Version 0.4: added higher-order features
    (courtesy Albert Rubio and Rene Thiemann) Version 0.32: removed the
    targetNamespace Version 0.31: adds the capability to have multiple
    originalfilename tags; removed the strategy=NONE. Version 0.3: adds the
    /problem/metainformation/originalfilename tag. Version 0.2: first
    official release.
    """

    class Meta:
        name = "problem"

    trs: Trs | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    strategy: Strategy | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    startterm: Startterm | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    status: Status | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    metainformation: Metainformation | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    type_value: ProblemType | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
