from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.rhs_funapp import (
    RhsApplication,
    RhsFunapp,
    RhsLambda,
)
from tpdb.models.var import Var


@dataclass
class Rhs:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        name = "rhs"

    funapp: Optional[RhsFunapp] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    var: Optional[Var] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: Optional[RhsLambda] = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: Optional[RhsApplication] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
