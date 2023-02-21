from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional, Union
from crossref.models.org.w3.pkg_1998.math.math_ml.abs import Abs
from crossref.models.org.w3.pkg_1998.math.math_ml.and_mod import And
from crossref.models.org.w3.pkg_1998.math.math_ml.annotation import Annotation
from crossref.models.org.w3.pkg_1998.math.math_ml.annotation_xml import AnnotationXml
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
from crossref.models.org.w3.pkg_1998.math.math_ml.cartesianproduct import Cartesianproduct
from crossref.models.org.w3.pkg_1998.math.math_ml.cbytes import Cbytes
from crossref.models.org.w3.pkg_1998.math.math_ml.ceiling import Ceiling
from crossref.models.org.w3.pkg_1998.math.math_ml.codomain import Codomain
from crossref.models.org.w3.pkg_1998.math.math_ml.columnalignstyle import Columnalignstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.common_pres_att_value import CommonPresAttValue
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
from crossref.models.org.w3.pkg_1998.math.math_ml.determinant import Determinant
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
from crossref.models.org.w3.pkg_1998.math.math_ml.exponentiale import Exponentiale
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
from crossref.models.org.w3.pkg_1998.math.math_ml.lowlimit import (
    Apply,
    Bind,
    Cerror,
    Ci,
    Cn,
    Csymbol,
    Declare,
    Fn,
    ListType,
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
from crossref.models.org.w3.pkg_1998.math.math_ml.lt import Lt
from crossref.models.org.w3.pkg_1998.math.math_ml.maligngroup import Maligngroup
from crossref.models.org.w3.pkg_1998.math.math_ml.malignmark import Malignmark
from crossref.models.org.w3.pkg_1998.math.math_ml.math_attributes_display import MathAttributesDisplay
from crossref.models.org.w3.pkg_1998.math.math_ml.math_attributes_overflow import MathAttributesOverflow
from crossref.models.org.w3.pkg_1998.math.math_ml.math_attributes_value import MathAttributesValue
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
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_accent import MstyleGeneralattributesAccent
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_accentunder import MstyleGeneralattributesAccentunder
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_align import MstyleGeneralattributesAlign
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_bevelled import MstyleGeneralattributesBevelled
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_charalign import MstyleGeneralattributesCharalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_denomalign import MstyleGeneralattributesDenomalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_dir import MstyleGeneralattributesDir
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_edge import MstyleGeneralattributesEdge
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_equalcolumns import MstyleGeneralattributesEqualcolumns
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_equalrows import MstyleGeneralattributesEqualrows
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_fence import MstyleGeneralattributesFence
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_form import MstyleGeneralattributesForm
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_indentalign import MstyleGeneralattributesIndentalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_indentalignfirst import MstyleGeneralattributesIndentalignfirst
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_indentalignlast import MstyleGeneralattributesIndentalignlast
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_largeop import MstyleGeneralattributesLargeop
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_linebreak import MstyleGeneralattributesLinebreak
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_linebreakstyle import MstyleGeneralattributesLinebreakstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_location import MstyleGeneralattributesLocation
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_longdivstyle import MstyleGeneralattributesLongdivstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_mathvariant import MstyleGeneralattributesMathvariant
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_movablelimits import MstyleGeneralattributesMovablelimits
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_numalign import MstyleGeneralattributesNumalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_separator import MstyleGeneralattributesSeparator
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_side import MstyleGeneralattributesSide
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_stackalign import MstyleGeneralattributesStackalign
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_stretchy import MstyleGeneralattributesStretchy
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_symmetric import MstyleGeneralattributesSymmetric
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_generalattributes_value import MstyleGeneralattributesValue
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_specificattributes_displaystyle import MstyleSpecificattributesDisplaystyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mstyle_specificattributes_infixlinebreakstyle import MstyleSpecificattributesInfixlinebreakstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable import Mtable
from crossref.models.org.w3.pkg_1998.math.math_ml.mtext import Mtext
from crossref.models.org.w3.pkg_1998.math.math_ml.naturalnumbers import Naturalnumbers
from crossref.models.org.w3.pkg_1998.math.math_ml.neq import Neq
from crossref.models.org.w3.pkg_1998.math.math_ml.not_mod import Not
from crossref.models.org.w3.pkg_1998.math.math_ml.notanumber import Notanumber
from crossref.models.org.w3.pkg_1998.math.math_ml.notin import Notin
from crossref.models.org.w3.pkg_1998.math.math_ml.notprsubset import Notprsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.notsubset import Notsubset
from crossref.models.org.w3.pkg_1998.math.math_ml.or_mod import Or
from crossref.models.org.w3.pkg_1998.math.math_ml.outerproduct import Outerproduct
from crossref.models.org.w3.pkg_1998.math.math_ml.partialdiff import Partialdiff
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
from crossref.models.org.w3.pkg_1998.math.math_ml.scalarproduct import Scalarproduct
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
from crossref.models.org.w3.pkg_1998.math.math_ml.vectorproduct import Vectorproduct
from crossref.models.org.w3.pkg_1998.math.math_ml.verticalalign import Verticalalign
from crossref.models.org.w3.pkg_1998.math.math_ml.xor import Xor

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Math:
    class Meta:
        name = "math"
        namespace = "http://www.w3.org/1998/Math/MathML"

    apply: List[Apply] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    bind: List[Bind] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ci: List[Ci] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cn: List[Cn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    csymbol: List[Csymbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cbytes: List[Cbytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cerror: List[Cerror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cs: List[Cs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    share: List[Share] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    piecewise: List[Piecewise] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    declare: List[Declare] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fn: List[Fn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reln: List[Reln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    interval: List[Interval] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    moment: List[Moment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    log: List[Log] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ln: List[Ln] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    codomain: List[Codomain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    domain: List[Domain] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ident: List[Ident] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    inverse: List[Inverse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lambda_value: List[Lambda] = field(
        default_factory=list,
        metadata={
            "name": "lambda",
            "type": "Element",
        }
    )
    compose: List[Compose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    quotient: List[Quotient] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    divide: List[Divide] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    minus: List[Minus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    power: List[Power] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rem: List[Rem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    root: List[Root] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    factorial: List[Factorial] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    abs: List[Abs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    conjugate: List[Conjugate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arg: List[Arg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    real: List[Real] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    imaginary: List[Imaginary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    floor: List[Floor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ceiling: List[Ceiling] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    exp: List[Exp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    min: List[Min] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    max: List[Max] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lcm: List[Lcm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    gcd: List[Gcd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    times: List[Times] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    plus: List[Plus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    xor: List[Xor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    or_value: List[Or] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
        }
    )
    and_value: List[And] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
        }
    )
    not_value: List[Not] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
        }
    )
    equivalent: List[Equivalent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    implies: List[Implies] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    exists: List[Exists] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    forall: List[Forall] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    leq: List[Leq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    geq: List[Geq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lt: List[Lt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    gt: List[Gt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    eq: List[Eq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    tendsto: List[Tendsto] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    factorof: List[Factorof] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    approx: List[Approx] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    neq: List[Neq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    int_value: List[Int] = field(
        default_factory=list,
        metadata={
            "name": "int",
            "type": "Element",
        }
    )
    diff: List[Diff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    partialdiff: List[Partialdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    laplacian: List[Laplacian] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    curl: List[Curl] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    grad: List[Grad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    divergence: List[Divergence] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        }
    )
    set: List[Set] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cartesianproduct: List[Cartesianproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    intersect: List[Intersect] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    union: List[UnionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    setdiff: List[Setdiff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notprsubset: List[Notprsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notsubset: List[Notsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notin: List[Notin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    in_value: List[In] = field(
        default_factory=list,
        metadata={
            "name": "in",
            "type": "Element",
        }
    )
    prsubset: List[Prsubset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    subset: List[Subset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    card: List[Card] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sum: List[Sum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    product: List[Product] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    limit: List[Limit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arctanh: List[Arctanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arcsinh: List[Arcsinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arcsech: List[Arcsech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arcsec: List[Arcsec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arccsch: List[Arccsch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arccsc: List[Arccsc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arccoth: List[Arccoth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arccot: List[Arccot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arccosh: List[Arccosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arctan: List[Arctan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arccos: List[Arccos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    arcsin: List[Arcsin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    coth: List[Coth] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    csch: List[Csch] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sech: List[Sech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    tanh: List[Tanh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cosh: List[Cosh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sinh: List[Sinh] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cot: List[Cot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    csc: List[Csc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sec: List[Sec] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    tan: List[Tan] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cos: List[Cos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sin: List[Sin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mode: List[Mode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    median: List[Median] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    variance: List[Variance] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sdev: List[Sdev] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mean: List[Mean] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    matrixrow: List[Matrixrow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    matrix: List[Matrix] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    vector: List[Vector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    transpose: List[Transpose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    determinant: List[Determinant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    selector: List[Selector] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    outerproduct: List[Outerproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    scalarproduct: List[Scalarproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    vectorproduct: List[Vectorproduct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    emptyset: List[Emptyset] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    primes: List[Primes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    complexes: List[Complexes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    naturalnumbers: List[Naturalnumbers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rationals: List[Rationals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    reals: List[Reals] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    integers: List[Integers] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    infinity: List[Infinity] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    eulergamma: List[Eulergamma] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    pi: List[Pi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    false: List[FalseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    true: List[TrueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    notanumber: List[Notanumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    imaginaryi: List[Imaginaryi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    exponentiale: List[Exponentiale] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    maction: List[Maction] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mlongdiv: List[Mlongdiv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mstack: List[Mstack] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mtable: List[Mtable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mmultiscripts: List[Mmultiscripts] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    munderover: List[Munderover] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mover: List[Mover] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    munder: List[Munder] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    msubsup: List[Msubsup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    msup: List[Msup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    msub: List[Msub] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    menclose: List[Menclose] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mfenced: List[Mfenced] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mphantom: List[Mphantom] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mpadded: List[Mpadded] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    merror: List[Merror] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mstyle: List[Mstyle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mroot: List[Mroot] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    msqrt: List[Msqrt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mfrac: List[Mfrac] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mrow: List[Mrow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    maligngroup: List[Maligngroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    malignmark: List[Malignmark] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ms: List[Ms] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mspace: List[Mspace] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mtext: List[Mtext] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mo: List[Mo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mn: List[Mn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mi: List[Mi] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    semantics: List["Math.Semantics"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mathcolor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathbackground: Optional[Union[str, CommonPresAttValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    scriptlevel: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    displaystyle: Optional[MstyleSpecificattributesDisplaystyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    scriptsizemultiplier: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    scriptminsize: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    infixlinebreakstyle: Optional[MstyleSpecificattributesInfixlinebreakstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    decimalpoint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*\S\s*",
        }
    )
    accent: Optional[MstyleGeneralattributesAccent] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    accentunder: Optional[MstyleGeneralattributesAccentunder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    align: Optional[MstyleGeneralattributesAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    alignmentscope: List[MstyleGeneralattributesValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    bevelled: Optional[MstyleGeneralattributesBevelled] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charalign: Optional[MstyleGeneralattributesCharalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charspacing: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    close: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    columnalign: List[Columnalignstyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    columnlines: List[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    columnspacing: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        }
    )
    columnspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    columnwidth: List[MstyleGeneralattributesValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    crossout: List[MstyleGeneralattributesValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    denomalign: Optional[MstyleGeneralattributesDenomalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    depth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    dir: Optional[MstyleGeneralattributesDir] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    edge: Optional[MstyleGeneralattributesEdge] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    equalcolumns: Optional[MstyleGeneralattributesEqualcolumns] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    equalrows: Optional[MstyleGeneralattributesEqualrows] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fence: Optional[MstyleGeneralattributesFence] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    form: Optional[MstyleGeneralattributesForm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    frame: Optional[Linestyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    framespacing: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "length": 2,
            "tokens": True,
        }
    )
    groupalign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\s*\{\s*(left|center|right|decimalpoint)(\s+(left|center|right|decimalpoint))*\})*\s*",
        }
    )
    height: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indentalign: Optional[MstyleGeneralattributesIndentalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentalignfirst: Optional[MstyleGeneralattributesIndentalignfirst] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentalignlast: Optional[MstyleGeneralattributesIndentalignlast] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    indentshift: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indentshiftfirst: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indentshiftlast: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    indenttarget: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    largeop: Optional[MstyleGeneralattributesLargeop] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    leftoverhang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreak: Optional[MstyleGeneralattributesLinebreak] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreakmultchar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    linebreakstyle: Optional[MstyleGeneralattributesLinebreakstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lineleading: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    linethickness: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    location: Optional[MstyleGeneralattributesLocation] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    longdivstyle: Optional[MstyleGeneralattributesLongdivstyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lquote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lspace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    mathsize: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    mathvariant: Optional[MstyleGeneralattributesMathvariant] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maxsize: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    minlabelspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    minsize: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    movablelimits: Optional[MstyleGeneralattributesMovablelimits] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mslinethickness: Optional[Union[str, MstyleGeneralattributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    notation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    numalign: Optional[MstyleGeneralattributesNumalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    open: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rightoverhang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    rowalign: List[Verticalalign] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    rowlines: List[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    rowspacing: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        }
    )
    rowspan: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rquote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    rspace: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    selection: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    separator: Optional[MstyleGeneralattributesSeparator] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    separators: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    shift: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    side: Optional[MstyleGeneralattributesSide] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stackalign: Optional[MstyleGeneralattributesStackalign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stretchy: Optional[MstyleGeneralattributesStretchy] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    subscriptshift: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    superscriptshift: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    symmetric: Optional[MstyleGeneralattributesSymmetric] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    valign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    width: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    xref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    display: Optional[MathAttributesDisplay] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    maxwidth: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    overflow: Optional[MathAttributesOverflow] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    altimg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    altimg_width: Optional[str] = field(
        default=None,
        metadata={
            "name": "altimg-width",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    altimg_height: Optional[str] = field(
        default=None,
        metadata={
            "name": "altimg-height",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    altimg_valign: Optional[Union[str, MathAttributesValue]] = field(
        default=None,
        metadata={
            "name": "altimg-valign",
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    alttext: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cdgroup: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mode_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "mode",
            "type": "Attribute",
        }
    )
    macros: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Semantics:
        apply: Optional[Apply] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        bind: Optional[Bind] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        ci: Optional[Ci] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cn: Optional[Cn] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        csymbol: Optional[Csymbol] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cbytes: Optional[Cbytes] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cerror: Optional[Cerror] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cs: Optional[Cs] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        share: Optional[Share] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        piecewise: Optional[Piecewise] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        declare: Optional[Declare] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        fn: Optional[Fn] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        reln: Optional[Reln] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        interval: Optional[Interval] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        moment: Optional[Moment] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        log: Optional[Log] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        ln: Optional[Ln] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        image: Optional[Image] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        codomain: Optional[Codomain] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        domain: Optional[Domain] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        ident: Optional[Ident] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        inverse: Optional[Inverse] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        lambda_value: Optional[Lambda] = field(
            default=None,
            metadata={
                "name": "lambda",
                "type": "Element",
            }
        )
        compose: Optional[Compose] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        quotient: Optional[Quotient] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        divide: Optional[Divide] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        minus: Optional[Minus] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        power: Optional[Power] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        rem: Optional[Rem] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        root: Optional[Root] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        factorial: Optional[Factorial] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        abs: Optional[Abs] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        conjugate: Optional[Conjugate] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arg: Optional[Arg] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        real: Optional[Real] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        imaginary: Optional[Imaginary] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        floor: Optional[Floor] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        ceiling: Optional[Ceiling] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        exp: Optional[Exp] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        min: Optional[Min] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        max: Optional[Max] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        lcm: Optional[Lcm] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        gcd: Optional[Gcd] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        times: Optional[Times] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        plus: Optional[Plus] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        xor: Optional[Xor] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        or_value: Optional[Or] = field(
            default=None,
            metadata={
                "name": "or",
                "type": "Element",
            }
        )
        and_value: Optional[And] = field(
            default=None,
            metadata={
                "name": "and",
                "type": "Element",
            }
        )
        not_value: Optional[Not] = field(
            default=None,
            metadata={
                "name": "not",
                "type": "Element",
            }
        )
        equivalent: Optional[Equivalent] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        implies: Optional[Implies] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        exists: Optional[Exists] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        forall: Optional[Forall] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        leq: Optional[Leq] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        geq: Optional[Geq] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        lt: Optional[Lt] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        gt: Optional[Gt] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        eq: Optional[Eq] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        tendsto: Optional[Tendsto] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        factorof: Optional[Factorof] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        approx: Optional[Approx] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        neq: Optional[Neq] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        int_value: Optional[Int] = field(
            default=None,
            metadata={
                "name": "int",
                "type": "Element",
            }
        )
        diff: Optional[Diff] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        partialdiff: Optional[Partialdiff] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        laplacian: Optional[Laplacian] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        curl: Optional[Curl] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        grad: Optional[Grad] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        divergence: Optional[Divergence] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        list_value: Optional[ListType] = field(
            default=None,
            metadata={
                "name": "list",
                "type": "Element",
            }
        )
        set: Optional[Set] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cartesianproduct: Optional[Cartesianproduct] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        intersect: Optional[Intersect] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        union: Optional[UnionType] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        setdiff: Optional[Setdiff] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        notprsubset: Optional[Notprsubset] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        notsubset: Optional[Notsubset] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        notin: Optional[Notin] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        in_value: Optional[In] = field(
            default=None,
            metadata={
                "name": "in",
                "type": "Element",
            }
        )
        prsubset: Optional[Prsubset] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        subset: Optional[Subset] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        card: Optional[Card] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        sum: Optional[Sum] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        product: Optional[Product] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        limit: Optional[Limit] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arctanh: Optional[Arctanh] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arcsinh: Optional[Arcsinh] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arcsech: Optional[Arcsech] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arcsec: Optional[Arcsec] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arccsch: Optional[Arccsch] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arccsc: Optional[Arccsc] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arccoth: Optional[Arccoth] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arccot: Optional[Arccot] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arccosh: Optional[Arccosh] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arctan: Optional[Arctan] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arccos: Optional[Arccos] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        arcsin: Optional[Arcsin] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        coth: Optional[Coth] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        csch: Optional[Csch] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        sech: Optional[Sech] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        tanh: Optional[Tanh] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cosh: Optional[Cosh] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        sinh: Optional[Sinh] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cot: Optional[Cot] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        csc: Optional[Csc] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        sec: Optional[Sec] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        tan: Optional[Tan] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        cos: Optional[Cos] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        sin: Optional[Sin] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mode: Optional[Mode] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        median: Optional[Median] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        variance: Optional[Variance] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        sdev: Optional[Sdev] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mean: Optional[Mean] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        matrixrow: Optional[Matrixrow] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        matrix: Optional[Matrix] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        vector: Optional[Vector] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        transpose: Optional[Transpose] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        determinant: Optional[Determinant] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        selector: Optional[Selector] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        outerproduct: Optional[Outerproduct] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        scalarproduct: Optional[Scalarproduct] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        vectorproduct: Optional[Vectorproduct] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        emptyset: Optional[Emptyset] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        primes: Optional[Primes] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        complexes: Optional[Complexes] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        naturalnumbers: Optional[Naturalnumbers] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        rationals: Optional[Rationals] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        reals: Optional[Reals] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        integers: Optional[Integers] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        infinity: Optional[Infinity] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        eulergamma: Optional[Eulergamma] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        pi: Optional[Pi] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        false: Optional[FalseType] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        true: Optional[TrueType] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        notanumber: Optional[Notanumber] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        imaginaryi: Optional[Imaginaryi] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        exponentiale: Optional[Exponentiale] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        maction: Optional[Maction] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mlongdiv: Optional[Mlongdiv] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mstack: Optional[Mstack] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mtable: Optional[Mtable] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mmultiscripts: Optional[Mmultiscripts] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        munderover: Optional[Munderover] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mover: Optional[Mover] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        munder: Optional[Munder] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        msubsup: Optional[Msubsup] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        msup: Optional[Msup] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        msub: Optional[Msub] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        menclose: Optional[Menclose] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mfenced: Optional[Mfenced] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mphantom: Optional[Mphantom] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mpadded: Optional[Mpadded] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        merror: Optional[Merror] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mstyle: Optional[Mstyle] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mroot: Optional[Mroot] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        msqrt: Optional[Msqrt] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mfrac: Optional[Mfrac] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mrow: Optional[Mrow] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        maligngroup: Optional[Maligngroup] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        malignmark: Optional[Malignmark] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        ms: Optional[Ms] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mspace: Optional[Mspace] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mtext: Optional[Mtext] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mo: Optional[Mo] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mn: Optional[Mn] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        mi: Optional[Mi] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        semantics: Optional["Math.Semantics"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "sequence": 53,
            }
        )
        annotation_xml: List[AnnotationXml] = field(
            default_factory=list,
            metadata={
                "name": "annotation-xml",
                "type": "Element",
                "sequence": 53,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        xref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        class_value: List[str] = field(
            default_factory=list,
            metadata={
                "name": "class",
                "type": "Attribute",
                "tokens": True,
            }
        )
        style: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        other: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        other_attributes: Dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##other",
            }
        )
        encoding: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        definition_url: Optional[str] = field(
            default=None,
            metadata={
                "name": "definitionURL",
                "type": "Attribute",
            }
        )
        cd: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
