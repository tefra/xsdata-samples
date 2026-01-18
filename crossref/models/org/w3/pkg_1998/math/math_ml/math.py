from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from crossref.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from crossref.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from crossref.models.org.w3.pkg_1998.math.math_ml.annotation import Annotation
from crossref.models.org.w3.pkg_1998.math.math_ml.annotation_xml import (
    AnnotationXml,
)
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
    Cerror,
    Ci,
    Cn,
    Csymbol,
    Declare,
    Fn,
    List,
    Maction,
    Menclose,
    Merror,
    Mfenced,
    Mfrac,
    Mlongdiv,
    Mmultiscripts,
    Mover,
    Mpadded,
    Mphantom,
    Mroot,
    Mrow,
    Msqrt,
    Mstack,
    Mstyle,
    Msub,
    Msubsup,
    Msup,
    Munder,
    Munderover,
    Piecewise,
    Reln,
    Set,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from crossref.models.org.w3.pkg_1998.math.math_ml.columnalignstyle import (
    Columnalignstyle,
)
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
from crossref.models.org.w3.pkg_1998.math.math_ml.linestyle import Linestyle
from crossref.models.org.w3.pkg_1998.math.math_ml.ln import Ln
from crossref.models.org.w3.pkg_1998.math.math_ml.log import Log
from crossref.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from crossref.models.org.w3.pkg_1998.math.math_ml.maligngroup import (
    Maligngroup,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.malignmark import Malignmark
from crossref.models.org.w3.pkg_1998.math.math_ml.math_accent import MathAccent
from crossref.models.org.w3.pkg_1998.math.math_ml.math_accentunder import (
    MathAccentunder,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_align import MathAlign
from crossref.models.org.w3.pkg_1998.math.math_ml.math_bevelled import (
    MathBevelled,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_charalign import (
    MathCharalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_denomalign import (
    MathDenomalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_dir import MathDir
from crossref.models.org.w3.pkg_1998.math.math_ml.math_display import (
    MathDisplay,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_displaystyle import (
    MathDisplaystyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_edge import MathEdge
from crossref.models.org.w3.pkg_1998.math.math_ml.math_equalcolumns import (
    MathEqualcolumns,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_equalrows import (
    MathEqualrows,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_fence import MathFence
from crossref.models.org.w3.pkg_1998.math.math_ml.math_form import MathForm
from crossref.models.org.w3.pkg_1998.math.math_ml.math_indentalign import (
    MathIndentalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_indentalignfirst import (
    MathIndentalignfirst,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_indentalignlast import (
    MathIndentalignlast,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_infixlinebreakstyle import (
    MathInfixlinebreakstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_largeop import (
    MathLargeop,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_linebreak import (
    MathLinebreak,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_linebreakstyle import (
    MathLinebreakstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_location import (
    MathLocation,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_longdivstyle import (
    MathLongdivstyle,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_mathvariant import (
    MathMathvariant,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_movablelimits import (
    MathMovablelimits,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_numalign import (
    MathNumalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_overflow import (
    MathOverflow,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_separator import (
    MathSeparator,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_side import MathSide
from crossref.models.org.w3.pkg_1998.math.math_ml.math_stackalign import (
    MathStackalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_stretchy import (
    MathStretchy,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_symmetric import (
    MathSymmetric,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math_value import MathValue
from crossref.models.org.w3.pkg_1998.math.math_ml.matrix import Matrix
from crossref.models.org.w3.pkg_1998.math.math_ml.matrixrow import Matrixrow
from crossref.models.org.w3.pkg_1998.math.math_ml.max import Max
from crossref.models.org.w3.pkg_1998.math.math_ml.mean import Mean
from crossref.models.org.w3.pkg_1998.math.math_ml.median import Median
from crossref.models.org.w3.pkg_1998.math.math_ml.mi import Mi
from crossref.models.org.w3.pkg_1998.math.math_ml.min import Min
from crossref.models.org.w3.pkg_1998.math.math_ml.minus import Minus
from crossref.models.org.w3.pkg_1998.math.math_ml.mn import Mn
from crossref.models.org.w3.pkg_1998.math.math_ml.mo import Mo
from crossref.models.org.w3.pkg_1998.math.math_ml.mode import Mode
from crossref.models.org.w3.pkg_1998.math.math_ml.moment import Moment
from crossref.models.org.w3.pkg_1998.math.math_ml.ms import Ms
from crossref.models.org.w3.pkg_1998.math.math_ml.mspace import Mspace
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable import Mtable
from crossref.models.org.w3.pkg_1998.math.math_ml.mtext import Mtext
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
from crossref.models.org.w3.pkg_1998.math.math_ml.verticalalign import (
    Verticalalign,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Math:
    class Meta:
        name = "math"
        namespace = "http://www.w3.org/1998/Math/MathML"

    apply: list[Apply] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    bind: list[Bind] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ci: list[Ci] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cn: list[Cn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csymbol: list[Csymbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cbytes: list[Cbytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cerror: list[Cerror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cs: list[Cs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    share: list[Share] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    piecewise: list[Piecewise] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    declare: list[Declare] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fn: list[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reln: list[Reln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    interval: list[Interval] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    moment: list[Moment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    log: list[Log] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ln: list[Ln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    image: list[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    codomain: list[Codomain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    domain: list[Domain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ident: list[Ident] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    inverse: list[Inverse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lambda_value: list[Lambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
        },
    )
    compose: list[Compose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    quotient: list[Quotient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    divide: list[Divide] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    minus: list[Minus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    power: list[Power] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rem: list[Rem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    root: list[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    factorial: list[Factorial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    abs: list[Abs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    conjugate: list[Conjugate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arg: list[Arg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    real: list[Real] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    imaginary: list[Imaginary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    floor: list[Floor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ceiling: list[Ceiling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exp: list[Exp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    min: list[Min] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    max: list[Max] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lcm: list[Lcm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gcd: list[Gcd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    times: list[Times] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    plus: list[Plus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    xor: list[Xor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    or_value: list[Or] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
        },
    )
    and_value: list[And] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
        },
    )
    not_value: list[Not] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
        },
    )
    equivalent: list[Equivalent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    implies: list[Implies] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exists: list[Exists] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    forall: list[Forall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    leq: list[Leq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    geq: list[Geq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lt: list[Lt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gt: list[Gt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    eq: list[Eq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tendsto: list[Tendsto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    factorof: list[Factorof] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    approx: list[Approx] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    neq: list[Neq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    int_value: list[Int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
        },
    )
    diff: list[Diff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    partialdiff: list[Partialdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    laplacian: list[Laplacian] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    curl: list[Curl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    grad: list[Grad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    divergence: list[Divergence] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    set: list[Set] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cartesianproduct: list[Cartesianproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    intersect: list[Intersect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    union: list[UnionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    setdiff: list[Setdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notprsubset: list[Notprsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notsubset: list[Notsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notin: list[Notin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    in_value: list[In] = field(
        default_factory=list,
        metadata={
            "name": "in",
            "type": "Element",
        },
    )
    prsubset: list[Prsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    subset: list[Subset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    card: list[Card] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sum: list[Sum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    product: list[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    limit: list[Limit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arctanh: list[Arctanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsinh: list[Arcsinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsech: list[Arcsech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsec: list[Arcsec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccsch: list[Arccsch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccsc: list[Arccsc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccoth: list[Arccoth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccot: list[Arccot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccosh: list[Arccosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arctan: list[Arctan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arccos: list[Arccos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    arcsin: list[Arcsin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    coth: list[Coth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csch: list[Csch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sech: list[Sech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tanh: list[Tanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cosh: list[Cosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sinh: list[Sinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cot: list[Cot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    csc: list[Csc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sec: list[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tan: list[Tan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    cos: list[Cos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sin: list[Sin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mode: list[Mode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    median: list[Median] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    variance: list[Variance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    sdev: list[Sdev] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mean: list[Mean] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    matrixrow: list[Matrixrow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    matrix: list[Matrix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    vector: list[Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    transpose: list[Transpose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    determinant: list[Determinant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    selector: list[Selector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    outerproduct: list[Outerproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    scalarproduct: list[Scalarproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    vectorproduct: list[Vectorproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    emptyset: list[Emptyset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    primes: list[Primes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    complexes: list[Complexes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    naturalnumbers: list[Naturalnumbers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rationals: list[Rationals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    reals: list[Reals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    integers: list[Integers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    infinity: list[Infinity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    eulergamma: list[Eulergamma] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    pi: list[Pi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    false: list[FalseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    true: list[TrueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    notanumber: list[Notanumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    imaginaryi: list[Imaginaryi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    exponentiale: list[Exponentiale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    maction: list[Maction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mlongdiv: list[Mlongdiv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mstack: list[Mstack] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mtable: list[Mtable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mmultiscripts: list[Mmultiscripts] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    munderover: list[Munderover] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mover: list[Mover] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    munder: list[Munder] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    msubsup: list[Msubsup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    msup: list[Msup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    msub: list[Msub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    menclose: list[Menclose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mfenced: list[Mfenced] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mphantom: list[Mphantom] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mpadded: list[Mpadded] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    merror: list[Merror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mstyle: list[Mstyle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mroot: list[Mroot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    msqrt: list[Msqrt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mfrac: list[Mfrac] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mrow: list[Mrow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    maligngroup: list[Maligngroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    malignmark: list[Malignmark] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ms: list[Ms] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mspace: list[Mspace] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mtext: list[Mtext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mo: list[Mo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mn: list[Mn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mi: list[Mi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    semantics: list[Math.Semantics] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mathcolor: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    mathbackground: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        },
    )
    scriptlevel: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    displaystyle: MathDisplaystyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    scriptsizemultiplier: Decimal | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    scriptminsize: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    infixlinebreakstyle: MathInfixlinebreakstyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    decimalpoint: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*\S\s*",
        },
    )
    accent: MathAccent | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    accentunder: MathAccentunder | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    align: MathAlign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    alignmentscope: list[MathValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    bevelled: MathBevelled | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charalign: MathCharalign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charspacing: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    close: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    columnalign: list[Columnalignstyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnlines: list[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    columnspacing: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        },
    )
    columnspan: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    columnwidth: list[MathValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    crossout: list[MathValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    denomalign: MathDenomalign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    depth: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    dir: MathDir | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    edge: MathEdge | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    equalcolumns: MathEqualcolumns | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    equalrows: MathEqualrows | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fence: MathFence | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: MathForm | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    frame: Linestyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    framespacing: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "length": 2,
            "tokens": True,
        },
    )
    groupalign: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\s*\{\s*(left|center|right|decimalpoint)(\s+(left|center|right|decimalpoint))*\})*\s*",
        },
    )
    height: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentalign: MathIndentalign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalignfirst: MathIndentalignfirst | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentalignlast: MathIndentalignlast | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    indentshift: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentshiftfirst: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indentshiftlast: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    indenttarget: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    largeop: MathLargeop | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    leftoverhang: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    length: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreak: MathLinebreak | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreakmultchar: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    linebreakstyle: MathLinebreakstyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lineleading: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    linethickness: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    location: MathLocation | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    longdivstyle: MathLongdivstyle | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lquote: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lspace: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    mathsize: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    mathvariant: MathMathvariant | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxsize: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    minlabelspacing: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    minsize: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    movablelimits: MathMovablelimits | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mslinethickness: str | MathValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    notation: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    numalign: MathNumalign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    open: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    position: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rightoverhang: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    rowalign: list[Verticalalign] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    rowlines: list[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    rowspacing: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        },
    )
    rowspan: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rquote: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    rspace: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    selection: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    separator: MathSeparator | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    separators: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    shift: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    side: MathSide | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stackalign: MathStackalign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stretchy: MathStretchy | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subscriptshift: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    superscriptshift: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    symmetric: MathSymmetric | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    width: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    xref: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    class_value: list[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        },
    )
    style: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    display: MathDisplay | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    maxwidth: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    overflow: MathOverflow | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    altimg: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    altimg_width: str | None = field(
        default=None,
        metadata={
            "name": "altimg-width",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    altimg_height: str | None = field(
        default=None,
        metadata={
            "name": "altimg-height",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    altimg_valign: str | MathValue | None = field(
        default=None,
        metadata={
            "name": "altimg-valign",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        },
    )
    alttext: object | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cdgroup: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mode_attribute: str | None = field(
        default=None,
        metadata={
            "name": "mode",
            "type": "Attribute",
        },
    )
    macros: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Semantics:
        apply: Apply | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        bind: Bind | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ci: Ci | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cn: Cn | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        csymbol: Csymbol | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cbytes: Cbytes | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cerror: Cerror | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cs: Cs | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        share: Share | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        piecewise: Piecewise | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        declare: Declare | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        fn: Fn | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        reln: Reln | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        interval: Interval | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        moment: Moment | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        log: Log | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ln: Ln | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        image: Image | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        codomain: Codomain | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        domain: Domain | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ident: Ident | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        inverse: Inverse | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        lambda_value: Lambda | None = field(
            default=None,
            metadata={
                "name": "lambda",
                "type": "Element",
            },
        )
        compose: Compose | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        quotient: Quotient | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        divide: Divide | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        minus: Minus | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        power: Power | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        rem: Rem | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        root: Root | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        factorial: Factorial | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        abs: Abs | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        conjugate: Conjugate | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arg: Arg | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        real: Real | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        imaginary: Imaginary | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        floor: Floor | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ceiling: Ceiling | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        exp: Exp | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        min: Min | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        max: Max | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        lcm: Lcm | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        gcd: Gcd | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        times: Times | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        plus: Plus | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        xor: Xor | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        or_value: Or | None = field(
            default=None,
            metadata={
                "name": "or",
                "type": "Element",
            },
        )
        and_value: And | None = field(
            default=None,
            metadata={
                "name": "and",
                "type": "Element",
            },
        )
        not_value: Not | None = field(
            default=None,
            metadata={
                "name": "not",
                "type": "Element",
            },
        )
        equivalent: Equivalent | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        implies: Implies | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        exists: Exists | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        forall: Forall | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        leq: Leq | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        geq: Geq | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        lt: Lt | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        gt: Gt | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        eq: Eq | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        tendsto: Tendsto | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        factorof: Factorof | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        approx: Approx | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        neq: Neq | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        int_value: Int | None = field(
            default=None,
            metadata={
                "name": "int",
                "type": "Element",
            },
        )
        diff: Diff | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        partialdiff: Partialdiff | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        laplacian: Laplacian | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        curl: Curl | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        grad: Grad | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        divergence: Divergence | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        list_value: List | None = field(
            default=None,
            metadata={
                "name": "list",
                "type": "Element",
            },
        )
        set: Set | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cartesianproduct: Cartesianproduct | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        intersect: Intersect | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        union: UnionType | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        setdiff: Setdiff | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        notprsubset: Notprsubset | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        notsubset: Notsubset | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        notin: Notin | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        in_value: In | None = field(
            default=None,
            metadata={
                "name": "in",
                "type": "Element",
            },
        )
        prsubset: Prsubset | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        subset: Subset | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        card: Card | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sum: Sum | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        product: Product | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        limit: Limit | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arctanh: Arctanh | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arcsinh: Arcsinh | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arcsech: Arcsech | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arcsec: Arcsec | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arccsch: Arccsch | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arccsc: Arccsc | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arccoth: Arccoth | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arccot: Arccot | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arccosh: Arccosh | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arctan: Arctan | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arccos: Arccos | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        arcsin: Arcsin | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        coth: Coth | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        csch: Csch | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sech: Sech | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        tanh: Tanh | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cosh: Cosh | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sinh: Sinh | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cot: Cot | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        csc: Csc | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sec: Sec | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        tan: Tan | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        cos: Cos | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sin: Sin | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mode: Mode | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        median: Median | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        variance: Variance | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        sdev: Sdev | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mean: Mean | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        matrixrow: Matrixrow | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        matrix: Matrix | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        vector: Vector | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        transpose: Transpose | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        determinant: Determinant | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        selector: Selector | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        outerproduct: Outerproduct | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        scalarproduct: Scalarproduct | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        vectorproduct: Vectorproduct | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        emptyset: Emptyset | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        primes: Primes | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        complexes: Complexes | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        naturalnumbers: Naturalnumbers | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        rationals: Rationals | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        reals: Reals | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        integers: Integers | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        infinity: Infinity | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        eulergamma: Eulergamma | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        pi: Pi | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        false: FalseType | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        true: TrueType | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        notanumber: Notanumber | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        imaginaryi: Imaginaryi | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        exponentiale: Exponentiale | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        maction: Maction | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mlongdiv: Mlongdiv | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mstack: Mstack | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mtable: Mtable | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mmultiscripts: Mmultiscripts | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        munderover: Munderover | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mover: Mover | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        munder: Munder | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        msubsup: Msubsup | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        msup: Msup | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        msub: Msub | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        menclose: Menclose | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mfenced: Mfenced | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mphantom: Mphantom | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mpadded: Mpadded | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        merror: Merror | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mstyle: Mstyle | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mroot: Mroot | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        msqrt: Msqrt | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mfrac: Mfrac | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mrow: Mrow | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        maligngroup: Maligngroup | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        malignmark: Malignmark | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ms: Ms | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mspace: Mspace | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mtext: Mtext | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mo: Mo | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mn: Mn | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        mi: Mi | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        semantics: Math.Semantics | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        annotation_xml: list[AnnotationXml] = field(
            default_factory=list,
            metadata={
                "name": "annotation-xml",
                "type": "Element",
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        xref: object | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        class_value: list[str] = field(
            default_factory=list,
            metadata={
                "name": "class",
                "type": "Attribute",
                "tokens": True,
            },
        )
        style: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        href: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        other: object | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        other_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            },
        )
        encoding: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        definition_url: str | None = field(
            default=None,
            metadata={
                "name": "definitionURL",
                "type": "Attribute",
            },
        )
        cd: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        name: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
