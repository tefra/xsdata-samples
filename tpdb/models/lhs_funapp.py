from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.name import Name
from tpdb.models.type_mod import Type
from tpdb.models.var import Var


@dataclass
class LhsFunapp:
    class Meta:
        global_type = False

    name: None | Name = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    arg: list[LhsFunappArg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class LhsLambda:
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
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    type_value: None | Type = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        },
    )
    funapp: None | LhsFunapp = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: None | LhsLambda = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: None | LhsApplication = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class LhsApplication:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: list[LhsFunapp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    var: list[Var] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    lambda_value: list[LhsLambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    application: list[LhsApplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )


@dataclass
class LhsFunappArg:
    """
    :ivar funapp:
    :ivar var:
    :ivar lambda_value: the type is the type of the bound variable
    :ivar application: an application of a function (first term) on an
        argument (second term): (first second)
    """

    class Meta:
        global_type = False

    funapp: None | LhsFunapp = field(
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
    lambda_value: None | LhsLambda = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    application: None | LhsApplication = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
