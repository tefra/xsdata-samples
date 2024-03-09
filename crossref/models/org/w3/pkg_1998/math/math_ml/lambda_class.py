from dataclasses import dataclass, field
from typing import Dict, List, Optional

from crossref.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from crossref.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from crossref.models.org.w3.pkg_1998.math.math_ml.approx import Approx
from crossref.models.org.w3.pkg_1998.math.math_ml.arccos import Arccos
from crossref.models.org.w3.pkg_1998.math.math_ml.arccosh import Arccosh
from crossref.models.org.w3.pkg_1998.math.math_ml.arccot import Arccot
from crossref.models.org.w3.pkg_1998.math.math_ml.arccoth import Arccoth
from crossref.models.org.w3.pkg_1998.math.math_ml.arccsc import Arccsc
from crossref.models.org.w3.pkg_1998.math.math_ml.arccsch import Arccsch
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsec import Arcsec
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsech import Arcsech
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsin import Arcsin
from crossref.models.org.w3.pkg_1998.math.math_ml.arcsinh import Arcsinh
from crossref.models.org.w3.pkg_1998.math.math_ml.arctan import Arctan
from crossref.models.org.w3.pkg_1998.math.math_ml.arctanh import Arctanh
from crossref.models.org.w3.pkg_1998.math.math_ml.arg import Arg
from crossref.models.org.w3.pkg_1998.math.math_ml.card import Card
from crossref.models.org.w3.pkg_1998.math.math_ml.cartesianproduct import (
    Cartesianproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.cbytes import Cbytes
from crossref.models.org.w3.pkg_1998.math.math_ml.ceiling import Ceiling
from crossref.models.org.w3.pkg_1998.math.math_ml.cerror import (
    Apply,
    Bind,
    Bvar,
    Cerror,
    Ci,
    Cn,
    Condition,
    Csymbol,
    Declare,
    Domainofapplication,
    Fn,
    ListType,
    Lowlimit,
    Piecewise,
    Reln,
    Set,
    Uplimit,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from crossref.models.org.w3.pkg_1998.math.math_ml.complexes import Complexes
from crossref.models.org.w3.pkg_1998.math.math_ml.compose import Compose
from crossref.models.org.w3.pkg_1998.math.math_ml.conjugate import Conjugate
from crossref.models.org.w3.pkg_1998.math.math_ml.cos import Cos
from crossref.models.org.w3.pkg_1998.math.math_ml.cosh import Cosh
from crossref.models.org.w3.pkg_1998.math.math_ml.cot import Cot
from crossref.models.org.w3.pkg_1998.math.math_ml.coth import Coth
from crossref.models.org.w3.pkg_1998.math.math_ml.cs import Cs
from crossref.models.org.w3.pkg_1998.math.math_ml.csc import Csc
from crossref.models.org.w3.pkg_1998.math.math_ml.csch import Csch
from crossref.models.org.w3.pkg_1998.math.math_ml.curl import Curl
from crossref.models.org.w3.pkg_1998.math.math_ml.determinant import (
    Determinant,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.diff import Diff
from crossref.models.org.w3.pkg_1998.math.math_ml.divergence import Divergence
from crossref.models.org.w3.pkg_1998.math.math_ml.divide import Divide
from crossref.models.org.w3.pkg_1998.math.math_ml.domain import Domain
from crossref.models.org.w3.pkg_1998.math.math_ml.emptyset import Emptyset
from crossref.models.org.w3.pkg_1998.math.math_ml.eq import Eq
from crossref.models.org.w3.pkg_1998.math.math_ml.equivalent import Equivalent
from crossref.models.org.w3.pkg_1998.math.math_ml.eulergamma import Eulergamma
from crossref.models.org.w3.pkg_1998.math.math_ml.exists import Exists
from crossref.models.org.w3.pkg_1998.math.math_ml.exp import Exp
from crossref.models.org.w3.pkg_1998.math.math_ml.exponentiale import (
    Exponentiale,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.factorial import Factorial
from crossref.models.org.w3.pkg_1998.math.math_ml.factorof import Factorof
from crossref.models.org.w3.pkg_1998.math.math_ml.false import FalseType
from crossref.models.org.w3.pkg_1998.math.math_ml.floor import Floor
from crossref.models.org.w3.pkg_1998.math.math_ml.forall import Forall
from crossref.models.org.w3.pkg_1998.math.math_ml.gcd import Gcd
from crossref.models.org.w3.pkg_1998.math.math_ml.geq import Geq
from crossref.models.org.w3.pkg_1998.math.math_ml.grad import Grad
from crossref.models.org.w3.pkg_1998.math.math_ml.gt import Gt
from crossref.models.org.w3.pkg_1998.math.math_ml.ident import Ident
from crossref.models.org.w3.pkg_1998.math.math_ml.image import Image
from crossref.models.org.w3.pkg_1998.math.math_ml.imaginary import Imaginary
from crossref.models.org.w3.pkg_1998.math.math_ml.imaginaryi import Imaginaryi
from crossref.models.org.w3.pkg_1998.math.math_ml.implies import Implies
from crossref.models.org.w3.pkg_1998.math.math_ml.in_mod import In
from crossref.models.org.w3.pkg_1998.math.math_ml.infinity import Infinity
from crossref.models.org.w3.pkg_1998.math.math_ml.int_mod import Int
from crossref.models.org.w3.pkg_1998.math.math_ml.integers import Integers
from crossref.models.org.w3.pkg_1998.math.math_ml.intersect import Intersect
from crossref.models.org.w3.pkg_1998.math.math_ml.interval import Interval
from crossref.models.org.w3.pkg_1998.math.math_ml.inverse import Inverse
from crossref.models.org.w3.pkg_1998.math.math_ml.lambda_mod import Lambda
from crossref.models.org.w3.pkg_1998.math.math_ml.laplacian import Laplacian
from crossref.models.org.w3.pkg_1998.math.math_ml.lcm import Lcm
from crossref.models.org.w3.pkg_1998.math.math_ml.leq import Leq
from crossref.models.org.w3.pkg_1998.math.math_ml.limit import Limit
from crossref.models.org.w3.pkg_1998.math.math_ml.ln import Ln
from crossref.models.org.w3.pkg_1998.math.math_ml.log import Log
from crossref.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from crossref.models.org.w3.pkg_1998.math.math_ml.matrix import Matrix
from crossref.models.org.w3.pkg_1998.math.math_ml.matrixrow import Matrixrow
from crossref.models.org.w3.pkg_1998.math.math_ml.max import Max
from crossref.models.org.w3.pkg_1998.math.math_ml.mean import Mean
from crossref.models.org.w3.pkg_1998.math.math_ml.median import Median
from crossref.models.org.w3.pkg_1998.math.math_ml.min import Min
from crossref.models.org.w3.pkg_1998.math.math_ml.minus import Minus
from crossref.models.org.w3.pkg_1998.math.math_ml.mode import Mode
from crossref.models.org.w3.pkg_1998.math.math_ml.moment import Moment
from crossref.models.org.w3.pkg_1998.math.math_ml.naturalnumbers import (
    Naturalnumbers,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.neq import Neq
from crossref.models.org.w3.pkg_1998.math.math_ml.not_mod import Not
from crossref.models.org.w3.pkg_1998.math.math_ml.notanumber import Notanumber
from crossref.models.org.w3.pkg_1998.math.math_ml.notin import Notin
from crossref.models.org.w3.pkg_1998.math.math_ml.notprsubset import (
    Notprsubset,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.notsubset import Notsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.or_mod import Or
from crossref.models.org.w3.pkg_1998.math.math_ml.outerproduct import (
    Outerproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.partialdiff import (
    Partialdiff,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.pi import Pi
from crossref.models.org.w3.pkg_1998.math.math_ml.plus import Plus
from crossref.models.org.w3.pkg_1998.math.math_ml.power import Power
from crossref.models.org.w3.pkg_1998.math.math_ml.primes import Primes
from crossref.models.org.w3.pkg_1998.math.math_ml.product import Product
from crossref.models.org.w3.pkg_1998.math.math_ml.prsubset import Prsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.quotient import Quotient
from crossref.models.org.w3.pkg_1998.math.math_ml.rationals import Rationals
from crossref.models.org.w3.pkg_1998.math.math_ml.real import Real
from crossref.models.org.w3.pkg_1998.math.math_ml.reals import Reals
from crossref.models.org.w3.pkg_1998.math.math_ml.rem import Rem
from crossref.models.org.w3.pkg_1998.math.math_ml.root import Root
from crossref.models.org.w3.pkg_1998.math.math_ml.scalarproduct import (
    Scalarproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.sdev import Sdev
from crossref.models.org.w3.pkg_1998.math.math_ml.sec import Sec
from crossref.models.org.w3.pkg_1998.math.math_ml.sech import Sech
from crossref.models.org.w3.pkg_1998.math.math_ml.selector import Selector
from crossref.models.org.w3.pkg_1998.math.math_ml.setdiff import Setdiff
from crossref.models.org.w3.pkg_1998.math.math_ml.share import Share
from crossref.models.org.w3.pkg_1998.math.math_ml.sin import Sin
from crossref.models.org.w3.pkg_1998.math.math_ml.sinh import Sinh
from crossref.models.org.w3.pkg_1998.math.math_ml.subset import Subset
from crossref.models.org.w3.pkg_1998.math.math_ml.sum import Sum
from crossref.models.org.w3.pkg_1998.math.math_ml.tan import Tan
from crossref.models.org.w3.pkg_1998.math.math_ml.tanh import Tanh
from crossref.models.org.w3.pkg_1998.math.math_ml.tendsto import Tendsto
from crossref.models.org.w3.pkg_1998.math.math_ml.times import Times
from crossref.models.org.w3.pkg_1998.math.math_ml.transpose import Transpose
from crossref.models.org.w3.pkg_1998.math.math_ml.true import TrueType
from crossref.models.org.w3.pkg_1998.math.math_ml.union import UnionType
from crossref.models.org.w3.pkg_1998.math.math_ml.variance import Variance
from crossref.models.org.w3.pkg_1998.math.math_ml.vector import Vector
from crossref.models.org.w3.pkg_1998.math.math_ml.vectorproduct import (
    Vectorproduct,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class LambdaType:
    class Meta:
        name = "lambda.class"
        namespace = "http://www.w3.org/1998/Math/MathML"

    bvar: List[Bvar] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domainofapplication: List[Domainofapplication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lowlimit: List[Lowlimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uplimit: List[Uplimit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    apply: Optional[Apply] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bind: Optional[Bind] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ci: Optional[Ci] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cn: Optional[Cn] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csymbol: Optional[Csymbol] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cbytes: Optional[Cbytes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cerror: Optional[Cerror] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cs: Optional[Cs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    share: Optional[Share] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    piecewise: Optional[Piecewise] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    declare: Optional[Declare] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fn: Optional[Fn] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reln: Optional[Reln] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    interval: Optional[Interval] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    moment: Optional[Moment] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    log: Optional[Log] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ln: Optional[Ln] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    image: Optional[Image] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    codomain: Optional[Codomain] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ident: Optional[Ident] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    inverse: Optional[Inverse] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: Optional[Lambda] = field(
        default=None,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    compose: Optional[Compose] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    quotient: Optional[Quotient] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    divide: Optional[Divide] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    minus: Optional[Minus] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    power: Optional[Power] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rem: Optional[Rem] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    root: Optional[Root] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    factorial: Optional[Factorial] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abs: Optional[Abs] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conjugate: Optional[Conjugate] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arg: Optional[Arg] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    real: Optional[Real] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imaginary: Optional[Imaginary] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floor: Optional[Floor] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ceiling: Optional[Ceiling] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exp: Optional[Exp] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    min: Optional[Min] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    max: Optional[Max] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lcm: Optional[Lcm] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gcd: Optional[Gcd] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    times: Optional[Times] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    plus: Optional[Plus] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    xor: Optional[Xor] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        },
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    equivalent: Optional[Equivalent] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    implies: Optional[Implies] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exists: Optional[Exists] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    forall: Optional[Forall] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    leq: Optional[Leq] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geq: Optional[Geq] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    lt: Optional[Lt] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gt: Optional[Gt] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    eq: Optional[Eq] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tendsto: Optional[Tendsto] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    factorof: Optional[Factorof] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    approx: Optional[Approx] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    neq: Optional[Neq] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    int_value: Optional[Int] = field(
        default=None,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )
    diff: Optional[Diff] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    partialdiff: Optional[Partialdiff] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    laplacian: Optional[Laplacian] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    curl: Optional[Curl] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    grad: Optional[Grad] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    divergence: Optional[Divergence] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    list_value: Optional[ListType] = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    set: Optional[Set] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cartesianproduct: Optional[Cartesianproduct] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    intersect: Optional[Intersect] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    union: Optional[UnionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    setdiff: Optional[Setdiff] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notprsubset: Optional[Notprsubset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notsubset: Optional[Notsubset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notin: Optional[Notin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    in_value: Optional[In] = field(
        default=None,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    prsubset: Optional[Prsubset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subset: Optional[Subset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    card: Optional[Card] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sum: Optional[Sum] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    product: Optional[Product] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    limit: Optional[Limit] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arctanh: Optional[Arctanh] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsinh: Optional[Arcsinh] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsech: Optional[Arcsech] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsec: Optional[Arcsec] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccsch: Optional[Arccsch] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccsc: Optional[Arccsc] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccoth: Optional[Arccoth] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccot: Optional[Arccot] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccosh: Optional[Arccosh] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arctan: Optional[Arctan] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arccos: Optional[Arccos] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    arcsin: Optional[Arcsin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    coth: Optional[Coth] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csch: Optional[Csch] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sech: Optional[Sech] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tanh: Optional[Tanh] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cosh: Optional[Cosh] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sinh: Optional[Sinh] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cot: Optional[Cot] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    csc: Optional[Csc] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sec: Optional[Sec] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tan: Optional[Tan] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    cos: Optional[Cos] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sin: Optional[Sin] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mode: Optional[Mode] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    median: Optional[Median] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    variance: Optional[Variance] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sdev: Optional[Sdev] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mean: Optional[Mean] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    matrixrow: Optional[Matrixrow] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    matrix: Optional[Matrix] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vector: Optional[Vector] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    transpose: Optional[Transpose] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    determinant: Optional[Determinant] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    selector: Optional[Selector] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    outerproduct: Optional[Outerproduct] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    scalarproduct: Optional[Scalarproduct] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vectorproduct: Optional[Vectorproduct] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    emptyset: Optional[Emptyset] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    primes: Optional[Primes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    complexes: Optional[Complexes] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    naturalnumbers: Optional[Naturalnumbers] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rationals: Optional[Rationals] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reals: Optional[Reals] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    integers: Optional[Integers] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    infinity: Optional[Infinity] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    eulergamma: Optional[Eulergamma] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    pi: Optional[Pi] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    false: Optional[FalseType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    true: Optional[TrueType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notanumber: Optional[Notanumber] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    imaginaryi: Optional[Imaginaryi] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    exponentiale: Optional[Exponentiale] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    encoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "definitionURL",
            "type": "Attribute",
        },
    )
