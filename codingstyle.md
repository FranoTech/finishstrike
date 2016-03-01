## Introduction ##

This page have been created to alert everybody about coding style.


## Details ##

Here is some coding style that must be acquired by this project:
-assignment "equal" signs must be surrounded by spaces:
> Bad:
> > a=b

> Good:
> > a = b

-named parameters "equal" signs must not be surrounded by spaces:

> Bad:
> > foo(a = b)

> Good:
> > foo(a=b)

-dictionnaries "colon" separator must be followed by a space, and must be preceeded by no space:

> Bad:
> > {a:b}
> > {a : b}
> > {a :b}

> Good:
> > {a: b}

-block-begining python keywords' "colon" must be preceeded by no space:

> Bad:
> > if a :
> > else :

> Good:
> > if a:
> > else:

-comas must be followed by a space, and must be preceeded by no space:

> Bad:
> > a,b
> > a ,b
> > a , b

> Good:
> > a, b

-file should always end with an empty line (to make diff happy)

API missuse/suboptimal use:
-"get" python methods support a default value:
-iter- variants should be used preferently when iterating:

> Bad:
> > a.items()
> > a.keys()
> > a.values()

> Good:
> > a.iteritems()
> > a.iterkeys()
> > a.itervalues()
-dict.in should be used instead of list.in:

> Bad:
> > a in b.keys()

> Good:
> > a in b

Minor problems (minor because fixing them conflicts with others good practices):
-lines are 79 char long, no more, no less. Avoid unneeded line folding (too-short lines) and wrap long lines after 79th char (or below, if more appropriate).

-indentation levels are 2-spaces large (even at class level)

-strings should use single quotes where it does not imply extra escaping

-avoid defining extra variables (it can improve code readability in some cases)

> a = b
> return a

-abbreviation use is strongly discouraged. I'm not sure if "regex" falls in this category, though.