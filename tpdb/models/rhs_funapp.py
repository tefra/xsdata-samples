from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.name import Name
from tpdb.models.type_mod import Type
from tpdb.models.var import Var


@dataclass(kw_only=True)
class RhsFunapp:
    class Meta:
        global_type = False

    name: Name = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    arg: list[RhsFunappArg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RhsLambda:
    """
    :ivar var:
    :ivar type_value:
    :ivar funapp:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    var: list[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    type_value: Type = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    funapp: None | RhsFunapp = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: None | RhsLambda = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: None | RhsApplication = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RhsApplication:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: list[RhsFunapp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    var: list[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    lambda_value: list[RhsLambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    application: list[RhsApplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class RhsFunappArg:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: None | RhsFunapp = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    var: None | Var = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: None | RhsLambda = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: None | RhsApplication = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
