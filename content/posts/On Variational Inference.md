---
date: 2022-07-06
lastmod: '2022-07-06T13:52:09-07:00'
tags:
- machine-learning
- variational-ml
title: On Variational Inference
---

This is a primer on so-called variational inference in machine learning, based on sections of [Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf) (*An Introduction to Variational Methods for Graphical Models*; 1999). I go over the mathematical forms of variational inference, and I include a discussion on what it means for something to be "variational." I hope this conveys a bit of the generating ideas that give rise to the various forms of variational inference. <!--more-->




$$
\\newcommand{\\0}{\\mathrm{false}}
\\newcommand{\\1}{\\mathrm{true}}
\\newcommand{\\mb}{\\mathbb}
\\newcommand{\\mc}{\\mathcal}
\\newcommand{\\mf}{\\mathfrak}
\\newcommand{\\and}{\\wedge}
\\newcommand{\\or}{\\vee}
\\newcommand{\\es}{\\emptyset}
\\newcommand{\\a}{\\alpha}
\\newcommand{\\t}{\\tau}
\\newcommand{\\T}{\\Theta}
\\newcommand{\\o}{\\omega}
\\newcommand{\\O}{\\Omega}
\\newcommand{\\x}{\\xi}
\\newcommand{\\z}{\\zeta}
\\newcommand{\\fa}{\\forall}
\\newcommand{\\ex}{\\exists}
\\newcommand{\\X}{\\mc{X}}
\\newcommand{\\Y}{\\mc{Y}}
\\newcommand{\\Z}{\\mc{Z}}
\\newcommand{\\P}{\\Phi}
\\newcommand{\\y}{\\psi}
\\newcommand{\\p}{\\phi}
\\newcommand{\\l}{\\lambda}
\\newcommand{\\pr}{\\times}
\\newcommand{\\B}{\\mb{B}}
\\newcommand{\\N}{\\mb{N}}
\\newcommand{\\R}{\\mb{R}}
\\newcommand{\\E}{\\mb{E}}
\\newcommand{\\e}{\\varepsilon}
\\newcommand{\\set}\[1\]{\\left\\{#1\\right\\}}
\\newcommand{\\par}\[1\]{\\left(#1\\right)}
\\newcommand{\\tup}{\\par}
\\newcommand{\\brak}\[1\]{\\left\[#1\\right\]}
\\newcommand{\\vtup}\[1\]{\\left\\langle#1\\right\\rangle}
\\newcommand{\\abs}\[1\]{\\left\\lvert#1\\right\\rvert}
\\newcommand{\\inv}\[1\]{{#1}^{-1}}
\\newcommand{\\ceil}\[1\]{\\left\\lceil#1\\right\\rceil}
\\newcommand{\\df}{\\overset{\\mathrm{def}}{=}}
\\newcommand{\\t}{\\theta}
\\newcommand{\\kl}\[2\]{D\_{\\text{KL}}\\left(#1\\ \\| \\ #2\\right)}
\\newcommand{\\argmin}\[1\]{\\underset{#1}{\\mathrm{argmin}}\\ }
\\newcommand{\\argmax}\[1\]{\\underset{#1}{\\mathrm{argmax}}\\ }
\\newcommand{\\d}{\\mathrm{d}}
\\newcommand{\\L}{\\mc{L}}
\\newcommand{\\M}{\\mc{M}}
\\newcommand{\\Er}{\\mc{E}}
\\newcommand{\\ht}{\\hat{\\t}}
\\newcommand{\\hp}{\\hat{\\p}}
\\newcommand{\\D}{\\mc{D}}
\\newcommand{\\H}{\\mc{H}}
\\newcommand{\\softmax}{\\text{softmax}}
\\newcommand{\\up}\[1\]{^{(#1)}}
$$

# Setup

Let $x = (x\_1,x\_2,x\_3,\\dots) \\in \\X = \\X\_1\\pr\\X\_2\\pr\\X\_3\\pr\\dots$ and $z = (z\_1,z\_2,z\_3,\\dots) \\in \\Z = \\Z\_1\\pr\\Z\_2\\pr\\Z\_3\\pr\\dots$ be finite or infinite length tuples, where $x$ is the *data variable* and $\\X$ is the *data space*, and $z$ is the *hidden* or *latent variable* and $\\Z$ is the *latent space*.

When we visualize $(x,z)$ as a graph, we call each $x\_i$ or $z\_j$ a *node* (in the context of the graphical model literature). However, in this post I will call them *dimensions*. Each $\\X\_i$ and $\\Z\_j$ can be a finite or countable set, or an uncountable set with a metric space (typically the Euclidean metric on $\\R$).

Suppose we have a family of joint distributions $\\set{p\_\\t\\mid\\t\\in\\T}$, i.e. $p\_\\t(x,z)$ is the joint probability of $x$ and $z$ for some choice of $\\t\\in\\T$. We say that $p\_\\t$ is *parametrized* by $\\t$, where $\\T$ is a finite dimensional metric space, e.g. $\\T\\subseteq\\R^r$ with $r\\in\\N$.

We assume that $p\_\\t(x,z)$ and $p\_\\t(z)$ are tractable (i.e. fast) quantities to calculate with a computer (to sufficient precision) for all $(x,z)\\in\\X\\pr\\Z$, but that $p\_\\t(x)$ and $p\_\\t(z\\mid x)$ are intractable (too slow to be useful) while also being quantities of interest.

Variational inference is a method for tractably approximating $p\_\\t(x)$ and $p\_\\t(z\\mid x)$ for all $(x,z)\\in\\X\\pr\\Z$.

## Note about probability notation

When I write $p\_\\t(x,z)$, I am treating $p\_\\t$ as a function of $x$ and $z$ that outputs a probability mass or density.

However, I will overload $p\_\\t$, by argument name, to represent a number of related functions. For instance, the marginal probabilities $p\_\\t(x) = \\int\_\\Z p\_\\t(x,z)\\ \\d z$ and $p\_\\t(z) = \\int\_\\X p\_\\t(x,z)\\ \\d x$ (replacing integrals with sums when variables are discrete) are different quantities depending on whether the argument to $p\_\\t$ is $x$ or $z$. Additionally I might consider marginal probabilities of specific dimensions, e.g. $p\_\\t(x\_{i\_1},x\_{i\_2},\\dots,z\_{j\_1},z\_{j\_2},\\dots)$ is the integral of $p\_\\t(x,z)$ over all dimensions not included as arguments.

Furthermore, we have conditional probabilities, e.g. $p\_\\t(x\\mid z)=p\_\\t(x,z)/p\_\\t(z)$ or $p\_\\t(x\_{i\_1},z\_{j\_1}\\mid x\_{i\_2},z\_{j\_2})=p\_\\t(x\_{i\_1},x\_{i\_2},z\_{j\_1},z\_{j\_2})/p\_\\t(x\_{i\_2},z\_{j\_2})$.

This covers the various functions that $p\_\\t$ can represent, and you can see how the form of the arguments to $p\_\\t$ determines which function we are considering.

# Terminology

My experience with other sources that explain variational inference is that they leave me confused about what the word "variational" is pointing at. E.g. [Murphy 2012](https://probml.github.io/pml-book/book0.html) (*Machine Learning: a Probabilistic Perspective*), [Bishop 2006](https://link.springer.com/book/9780387310732) (*Pattern Recognition and Machine Learning*), [Blei 2016](https://arxiv.org/abs/1601.00670) (*Variational Inference: A Review for Statisticians*), and even Wikipedia: [Variational Bayesian methods](https://en.wikipedia.org/wiki/Variational_Bayesian_methods).

Aside from being irksome, I find the lack of clarity around this word inhibits by ability to grok what authors are thinking when they write about variational inference. Specifically, I want to understand the underlying generating idea for this class of methodologies. As an ML practitioner and researcher, aim to build off of existing ideas. To do that I need to know how previous authors thought about their ideas. Having the generator of an idea, I can play with it and potentially generate something not previously considered.

To that end, this section is a detour to explore the meaning of the word "variational" in the context of variational inference. If this does not interest you, feel free to skip to the next section, [#Variational Inference](#variational-inference).

## What is Variational ?
In the context of variational inference, the word "variational" refers to the [calculus of variations](https://en.wikipedia.org/wiki/Calculus_of_variations) (CoV). Some variational inference texts mention the CoV connection explicitly, e.g. [Bishop 2006](https://link.springer.com/book/9780387310732), section 10.1.

According to Wikipedia,
> The **calculus of variations** is a field of [mathematical analysis](https://en.wikipedia.org/wiki/Mathematical_analysis "Mathematical analysis") that uses variations, which are small changes in [functions](https://en.wikipedia.org/wiki/Function_(mathematics) "Function (mathematics)") and [functionals](https://en.wikipedia.org/wiki/Functional_(mathematics) "Functional (mathematics)"), to find maxima and minima of functionals: [mappings](https://en.wikipedia.org/wiki/Map_(mathematics) "Map (mathematics)") from a set of [functions](https://en.wikipedia.org/wiki/Function_(mathematics) "Function (mathematics)") to the [real numbers](https://en.wikipedia.org/wiki/Real_number "Real number").



[wolfram.com](https://mathworld.wolfram.com/CalculusofVariations.html) gives a slightly different description for the CoV,

> A branch of mathematics that is a sort of generalization of [calculus](https://mathworld.wolfram.com/Calculus.html). Calculus of variations seeks to find the path, curve, surface, etc., for which a given [function](https://mathworld.wolfram.com/Function.html) has a [stationary value](https://mathworld.wolfram.com/StationaryValue.html) (which, in physical problems, is usually a [minimum](https://mathworld.wolfram.com/Minimum.html) or [maximum](https://mathworld.wolfram.com/Maximum.html)).

The "stationary value" here refers to the min or max of a functional, and a functional is a mapping from functions to real numbers. Both accounts of the CoV make reference optimizing a functional.






If we want to use "variational" as an adjective, e.g. in "variational method" ([examples](https://en.wikipedia.org/wiki/History_of_variational_principles_in_physics)), how could we reasonably extrapolate from the above description of the CoV?

Here's my proposal: something is "variational" if it involves an optimization problem with uncountably many degrees of freedom. Equivalently, we are searching over a function space to find an optimal function (according to our optimization criteria). Then a "variation" is some "perturbation" to a candidate function that moves us infinitesimally in some direction in function space.


So with this notion, regular calculus is not variational, despite involving searching over function spaces, because a given function is either the solution or not, and is not scored. I suppose that if we recast integration and differentiation as functionals whose optima are the derivatives and integrals of the desired function, we would be reposing calculus as a variational problem (similar to the kind of problem-reposing we will see in the next section).



## Variational methods in ML
[Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf), section 4, *Basics of variational methodology*, gives us a primer on variational methods.



> Let us begin by considering a simple example. In particular, let us express the logarithm function variationally:
> $$\\ln(x) = \\min\_\\l\\set{\\l x-\\ln\\l-1}\\,.$$
> In this expression $\\l$ is the variational parameter, and we are required to perform the minimization for each value of $x$.

[Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf) is implicitly defining what "variational" means here. We are given an optimization criteria, namely $\\fa x,\\ \\min\_{\\l\_x}\\set{\\l\_x x-\\ln\\l\_x-1}$, which has infinitely many optimization parameters, $\\l\_x$ for every $x$. We could view this optimization as being over the space of (continuous) functions, $\\R\\to\\R$, and searching for some $\\l:\\R\\to\\R$ s.t. $\\l(x) x-\\ln\\l(x)-1$ is minimal for every $x\\in(0,\\infty)$. In this case, $\\l(x)=1/x$ is the solution.

Note that in this problem we don't have a functional. Nevertheless  [Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf) is taking this to be a variational method. If we are to broaden our notion of variational from the previous section, [#What is Variational](#what-is-variational), to accommodate this usage, we could say that a variational problem is an optimization problem over an infinite dimensional function space, or equivalently with infinitely many optimization parameters. In most cases the optimization problem can be specified with a functional, but in this case it is not.

**Question**: Is $\\min\_{\\l:\\R\\to\\R}\\set{\\int\_\\X\\l(x) x-\\ln\\l(x)-1\\ \\d x}$ an equivalent problem? Then $\\mc{F}\[\\l\]=\\int\_\\X\\l(x) x-\\ln\\l(x)-1\\ \\d x$ is our functional.



To generalize this variational method, suppose we have a function $f(x)$ which is intractable to calculate directly, but that we know of some other tractable function, $g(x,\\l)$, s.t. $g(x,\\l) \\geq f(x)$ for all $\\l\\in\\R$ and $x\\in\\X$, and $g(x,\\l) = f(x)$ for some $\\l\\in\\R$, for all $x\\in\\X$ ($g$ is a tight upper bound of $f$). Let $\\l(x) = \\argmin{\\l}g(x,\\l)$. Then $f(x) = g(x,\\l(x))$ for all $x\\in\\X$.

If we are not able to perform the exact minimization $\\argmin{\\l}g(x,\\l)$ symbolically, but we instead find an approximate minimum $\\hat{\\l}\_x$ numerically (e.g. with gradient descent). Then $g(x,\\hat{\\l}\_x)$ is an approximation of $f(x)$, and $g(x,\\hat{\\l}\_x) \\geq f(x)$ is guaranteed. This is now useful as a way to numerically approximate $f(x)$ by converting it into an optimization problem which we know how to numerically approximate.

# Variational Inference
See [Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf), section 6, *The block approach*.

Continuing from the [#Setup](#setup) above, $p\_\\t(z\\mid x)$ is an intractable quantity (for most $z$ and $x$). So instead we introduce the family of tractable distributions $q\_\\p$ on $z$ parametrized by $\\p\\in\\P$, where $q\_\\p(z)$ is intended to be our approximation of $p\_\\t(z\\mid x)$, and $\\p$ will be our variational parameter(s) w.r.t. $x$ (i.e. the optimization solution will be a function from $\\X$ to $\\P$).

Define the following quantities,

$$\\begin{aligned}
\\M(\\t;\\ x) &\\df \\log\\par{1/p\_\\t(x)}\\,, \\\\
\\Er(\\t,\\p;\\ x) &\\df \\kl{q\_\\p(z)}{p\_\\t(z\\mid x)} \\\\&= \\int\_\\Z q\_\\p(z)\\log\\par{\\frac{q\_\\p(z)}{p\_\\t(z\\mid x)}}\\ \\d z\\,, \\\\
\\L(\\t,\\p;\\ x) &\\df \\M(\\t;\\ x) + \\Er(\\t,\\p;\\ x)\\,.
\\end{aligned}$$

All three quantities are non-negative for all $\\t,\\p,x$. Then we have 

$$
\\L(\\t,\\p;\\ x) \\geq \\M(\\t;\\ x)\\,,
$$

with equality when $\\Er(\\t,\\p;\\ x)=0$, i.e. when $q\_\\p(z)=p\_\\t(z\\mid x)$ for all $z$.

Let $\\t$ be constant. When $p\_\\t(\\cdot \\mid x) \\in\\set{q\_\\p(\\cdot)\\mid \\p\\in\\P}$ for all $x$, then we can write $\\M(\\t;\\ x) = \\min\_\\p\\L(\\t,\\p;\\ x)$, with the solution being some function $\\p^\*:\\X\\to\\P$. Hence we have a variational optimization problem whose solution is a function.

Otherwise if $p\_\\t(\\cdot \\mid x) \\notin\\set{q\_\\p(\\cdot)\\mid \\p\\in\\P}$, then $\\L(\\t,\\p;\\ x)$ is forever an upper bound of $\\M(\\t;\\ x)$, but its minimum may still be close enough to $\\M(\\t;\\ x)$ for it to be a reasonable substitute. So the variational minimization problem, $\\fa x,\\ \\min\_{\\p\_x}\\L(\\t,\\p\_x;\\ x)$, is of interest in either case.

A nice property of this particular setup is that the minimization objective, $\\fa x,\\ \\min\_{\\p\_x}\\L(\\t,\\p\_x;\\ x)$, will also achieve $\\fa x,\\ \\min\_{\\p\_x}\\Er(\\t,\\p\_x;\\ x)$ because $\\M(\\t;\\ x)$ remains constant w.r.t. $\\p\_x$ (i.e. the gap $\\Er(\\t,\\p\_x;\\ x)=\\L(\\t,\\p;\\ x) - \\M(\\t;\\ x)$ is minimized). Minimal $\\Er(\\t,\\p\_x;\\ x)$ in turn implies that $q\_\\p(z)$ is the best approximation of $p\_\\t(z\\mid x)$ for all $z,x$. So from our single variational optimization, we get two approximations of intractable quantities: for $\\M(\\t;\\ x)$ and for $p\_\\t(z\\mid x)$. 

---

Note that $\\M(\\t;\\ x)$ is intractable iff $p\_\\t(z\\mid x)$ is intractable, assuming $p\_\\t(x,z)$ is tractable, since $p\_\\t(z\\mid x)=p\_\\t(x,z)\\exp(\\M(\\t;\\ x))$ and $\\M(\\t;\\ x)=\\log\\par{p\_\\t(z\\mid x)/p\_\\t(x,z)}$.

## Tractability

Suppose $\\M(\\t;\\ x)$ is intractable. Then we can subsitute it for our variational approximation, $\\L(\\t,\\p;\\ x)$. Now the question is whether we can tractably calculate $\\L(\\t,\\p;\\ x)$ for all $\\t,\\p,x$. 

We have

$$\\begin{aligned}
\\L(\\t,\\p;\\ x)=\\kl{q\_\\p(z)}{p\_\\t(z)} + \\E\_{z\\sim q\_\\p(z)}\\left\[\\log\\par{1/p\_\\t(x \\mid z)}\\right\]\\,,
\\end{aligned}$$

where $\\kl{q\_\\p(z)}{p\_\\t(z)}=\\int\_\\Z q\_\\p(z)\\log\\par{\\frac{q\_\\p(z)}{p\_\\t(z)}}\\ \\d z$ 
and $\\E\_{z\\sim q\_\\p(z)}\\left\[\\log\\par{1/p\_\\t(x \\mid z)}\\right\]=\\int\_\\Z q\_\\p(z)\\log\\par{1/p\_\\t(x \\mid z)}\\ \\d z$.

See [#Appendix](#appendix) for derivation.

This form is promising because it involves only quantities that we know are tractable, $q\_\\p(z)$, $p\_\\t(z)$ and $p\_\\t(x \\mid z)$. However, calculating expectations w.r.t. $q\_\\p(z)$, and optimizing $\\p$ through those expectations (e.g. with gradient descent) may still be tricky to perform tractably, and further approximations are likely needed. E.g. [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) discusses this problem and ways to get around it. 

## Maximum Likelihood Estimation

See [Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf), section 6.2, *Parameter estimation via variational methods*.

Often, we are interested in solving

$$
\\t^\* = \\argmin{\\t} \\M(\\t;\\ x)\\,.
$$

This is maximum likelihood estimation, which is one way to *fit* a *model* (i.e. the family of distributions $p\_\\t$ for $\\t\\in\\T$) to a dataset. Here, $\\M(\\t;\\ x)$ is called a loss function. Often, we cannot solve this optimization exactly, so we use numerical optimization, such as gradient descent w.r.t. $\\t$.

When the loss $\\M(\\t;\\ x)$ is intractable to calculate, we can replace it with the upper bound $\\L(\\t,\\p;\\ x)$ and then perform the joint minimization

$$
(\\t^\*,\\p^\*)=\\argmin{\\t,\\p} \\L(\\t,\\p;\\ x)\\,,
$$

which also gives us the approximation $q\_{\\p^\*}(z)\\approx p\_{\\t^\*}(z\\mid x)$.

### i.i.d. datasets

Usually, we are performing maximum likelihood estimation on a dataset that we are modeling as i.i.d. Specifically, our dataset is a list, $X=(x\\up{1},\\dots,x\\up{n})$, of $n$ instances of the visible dimensions, where each $x\\up{k} \\in \\X$. As before we have the parametrized distribution $p\_\\t(x,z)$ on $\\X\\pr\\Z$. Since we assume the dataset is i.i.d., then we have 

$$p\_\\t(X) = p\_\\t(x\\up{1},\\dots,x\\up{n}) = \\prod\_{k=1}^n p\_\\t(x\\up{k})\\,,$$

and when $Z \\in \\Z^n$, 

$$p\_\\t(X,Z) = \\prod\_{k=1}^n p\_\\t(x\\up{k},z\\up{k})\\,.$$

Then we have

$$\\begin{aligned}\\M(\\t;\\ X) &= \\log\\par{1/p\_\\t(X)} \\\\&= \\sum\_{k=1}^n \\log\\par{1/p\_\\t(x\\up{k})} \\\\&= \\sum\_{k=1}^n\\M(\\t;\\ x\\up{k})\\,.\\end{aligned}$$

We want to approximate $p\_\\t(z\\mid x)$ like before, but unlike before $x$ is not held fixed. In addition to having $n$ instances of $x$ in our dataset, we also want to efficiently calculate $p\_\\t(z\\mid x)$ on any arbitrary $x\\in\\X$ outside our dataset.

Following the example of [#Variational methods in ML](#variational-methods-in-ml), let's perform a separate minimization for every $x\\in\\X$. That is to say, let $q\_\\p(z)$ be a distribution over $\\Z$ like before, with $\\Er(\\t,\\p;\\ x)=\\kl{q\_\\p(z)}{p\_\\t(z\\mid x)}$ and $\\L(\\t,\\p;\\ x) = \\M(\\t;\\ x) + \\Er(\\t,\\p;\\ x)$.

Then for each $x\\up{k} \\in X$ we have separate parameters $\\p\_{x\\up{k}}$ so that $q\_{\\p\_{x\\up{k}}}(z)$ is our working approximation for $p\_\\t(z\\mid x\\up{k})$. Then our approximation of $p\_\\t(Z\\mid X)$ is $q\_{\\p\_{x\\up{1}},\\dots,\\p\_{x\\up{n}}}(Z)=\\prod\_{k=1}q\_{\\p\_{x\\up{k}}}(z\\up{k})$, and so

$$\\begin{aligned}
\\Er(\\t,\\p;\\ X) &= \\int\_{\\Z^n} q\_{\\p\_{x\\up{1}},\\dots,\\p\_{x\\up{n}}}(Z)\\log\\par{\\frac{q\_{\\p\_{x\\up{1}},\\dots,\\p\_{x\\up{n}}}(Z)}{p\_\\t(Z\\mid X)}}\\ \\d Z \\\\
&= \\int\_{\\Z^n} \\brak{\\prod\_{k=1}^n q\_{\\p\_{x\\up{k}}}(z\\up{k})}\\brak{\\sum\_{k=1}^n\\log\\par{\\frac{q\_{\\p\_{x\\up{k}}}(z\\up{k})}{p\_\\t(z\\up{k}\\mid x\\up{k})}}}\\ \\d z\\up{1}\\dots\\d z\\up{n} \\\\
&= \\sum\_{k=1}^n \\int\_{\\Z} q\_{\\p\_{x\\up{k}}}(z)\\log\\par{\\frac{q\_{\\p\_{x\\up{k}}}(z)}{p\_\\t(z\\mid x\\up{k})}}\\ \\d z \\\\
&= \\sum\_{i=1}^n \\Er(\\t,\\p\_{x\\up{k}};\\ x\\up{k})
\\end{aligned}$$

Then our dataset loss is $\\sum\_{k=1}^n\\L(\\t,\\p\_{x\\up{k}};\\ x\\up{k})$ with $\\L(\\t,\\p\_{x\\up{k}};\\ x\\up{k}) = \\M(\\t;\\ x\\up{k}) + \\Er(\\t,\\p\_{x\\up{k}};\\ x\\up{k})$.


To fit the model to $X=(x\\up{1},\\dots,x\\up{n})$ w.r.t. $\\t$, we perform the joint minimization,

$$
(\\ht,\\hp\_{x\\up{1}},\\dots,\\hp\_{x\\up{n}}) = \\argmin{\\t,\\p\_{x\\up{1}},\\dots,\\p\_{x\\up{n}}} \\sum\_{k=1}^n\\L(\\t,\\p\_{x\\up{k}};\\ x\\up{k})\\,,
$$
to obtain $\\ht$ (we can discard the $\\set{\\hp\_{x\\up{k}}}$).

Then for any $x\\in\\X$ of interest, we perform the minimization

$$
\\hp\_x = \\argmin{\\p} \\L(\\ht,\\p;\\ x)\\,,
$$

giving us $q\_{\\hp\_x}(z) \\approx p\_\\ht(z\\mid x)$.

#### Another Approach

An alternative way to approximate $p\_\\t(z\\mid x)$ for arbitrary $x\\in\\X$ is to have our approximate distribution $q\_\\p$ be a function of both $z$ and $x$ (for a single choice of parameters $\\p$). This is typically notated as $q\_\\p(z\\mid x)$, though this is technically an abuse of notation since we do not define the joint $q\_\\p(x,z)$. We could instead write $q\_{\\p,x}(z)$ or $q\_{\\p}(z;\\ x)$, both of which make it clear that the probability distribution is only over $\\Z$-space. However, I will continue with $q\_\\p(z\\mid x)$ since it visually mimics $p\_\\t(z\\mid x)$ and I find that easier to think about.




Then we have $q\_\\p(Z\\mid X)=\\prod\_{k=1}q\_\\p(z\\up{k}\\mid x\\up{k})$, and so

$$\\begin{aligned}
\\Er(\\t,\\p;\\ X) &= \\int\_{\\Z^n} q\_\\p(Z\\mid X)\\log\\par{\\frac{q\_\\p(Z\\mid X)}{p\_\\t(Z\\mid X)}}\\ \\d Z \\\\
&= \\int\_{\\Z^n} \\brak{\\prod\_{k=1}^n q\_\\p(z\\up{k}\\mid x\\up{k})}\\brak{\\sum\_{k=1}^n\\log\\par{\\frac{q\_\\p(z\\up{k}\\mid x\\up{k})}{p\_\\t(z\\up{k}\\mid x\\up{k})}}}\\ \\d z\\up{1}\\dots\\d z\\up{n} \\\\
&= \\sum\_{k=1}^n \\int\_{\\Z} q\_\\p(z\\mid x\\up{k})\\log\\par{\\frac{q\_\\p(z\\mid x\\up{k})}{p\_\\t(z\\mid x\\up{k})}}\\ \\d z \\\\
&= \\sum\_{i=1}^n \\Er(\\t,\\p;\\ x\\up{k})
\\end{aligned}$$

Then our dataset loss is $\\L(\\t,\\p;\\ X) = \\sum\_{k=1}^n\\L(\\t,\\p;\\ x\\up{k})$ with $\\L(\\t,\\p;\\ x\\up{k}) = \\M(\\t;\\ x\\up{k}) + \\Er(\\t,\\p;\\ x\\up{k})$. 

Our optimization problem becomes

$$
(\\ht,\\hp) = \\argmin{\\t,\\p} \\sum\_{k=1}^n\\L(\\t,\\p;\\ x\\up{k})\\,.
$$

Then $q\_\\hp(z\\mid x) \\approx p\_\\ht(z\\mid x)$ for any $x\\in\\X$ of interest.

This approach may let us approximate $p\_\\t(z\\mid x)$ faster since we don't rerun our optimization process for every $x$. 

**Question**: What other reasons are there to prefer one of these two approaches to i.i.d. MLE. What are the pros and cons of each?




 
# Variational Bayes

See [Jordan et al.](https://link.springer.com/content/pdf/10.1023%2FA%3A1007665907178.pdf), section 7.1.3, *Bayesian methods*.

Variational inference (VI) applied to Bayesian inference is sometimes called "variational Bayes" (VB) (short for "variational Bayesian inference"). Mathematically VI and VB are the same. Whether we are doing Bayesian inference or just inference is a difference about the meaning we ascribe to that math, which determines how we apply it.

Bayesian inference operates in a paradigm which I would call "Bayesian epistemology." Informally, in this paradigm we observe pieces of data over a period of time, we have a set of hypotheses which remain unobserved, and each hypothesis gives us a prediction about what we will observe in the future given the present. To each hypothesis we assign a weight representing our belief about the plausibility of that hypothesis. Then we take the weighted average of all the hypotheses' predictions to get our final prediction which we use, e.g. for decision making. See {{< locallink "Deconstructing Bayesian Inference" "defining-bayesian-inference" >}} for a more in-depth account of Bayesian epistemology.



Formally, suppose we have a joint distribution $P(x,z)$ as before, except that $P$ is not parametrized. We take $\\Z$ to be our hypothesis space and $\\X$ to be the data space. We also suppose that we have partial data, e.g. we observe $x\_{\\leq n} = (x\_1,\\dots,x\_n) \\in \\X\_1\\pr\\dots\\pr\\X\_n$, which is a subset of all the dimensions of the data space $\\X$. I didn't specify that we observe each dimension in the order of its indexing, but for convenience let's re-index so that that is the case. 

Let $P(z)$ be the belief weight we assign for each $z\\in\\Z$. Call $P(z)$ our prior about $z$. Upon observing $x\_{\\leq n}$, our beliefs change, where $P(z\\mid x\_{\\leq n})$ is now the weight we assign to $z$, called the posterior. We are interested in our average prediction distribution over the unobserved data, $x\_{>n} = (x\_{n+1},x\_{n+2},\\dots) \\in \\X\_{n+1}\\pr\\X\_{n+2}\\pr\\dots$, given the observed data $x\_{\\leq n}$,

$$\\begin{aligned}
P(x\_{>n}\\mid x\_{\\leq n}) &= \\int\_{\\Z}P(x\_{>n}\\mid x\_{\\leq n},z)P(z\\mid x\_{\\leq n})\\ \\d z \\\\
\\end{aligned}$$



for all $x\_{>n}\\in\\X\_{>n}$. We can see that the posterior $P(z\\mid x\_{\\leq n})$ is involved in this calculation.

When the posterior is intractable, we can perform VI (now restyled as VB), by defining an approximate posterior $q\_\\p(z)$ parametrized by $\\p$. Like before, let

$$\\M(x\_{\\leq n}) = \\log\\par{1/P(x\_{\\leq n})}$$

$$\\Er(\\p;\\ x\_{\\leq n}) = \\kl{q\_\\p(z)}{P(z\\mid x\_{\\leq n})}$$

and 

$$\\L(\\p;\\ x\_{\\leq n}) = \\M(x\_{\\leq n}) + \\Er(\\p;\\ x\_{\\leq n})$$

Then we want to find $\\p^\*:\\X\_{\\leq n} \\to \\P$ which solves the minimization problem, $\\fa x\_{\\leq n},\\ \\min\_{\\p\_{x\_{\\leq n}}}\\L(\\p\_{x\_{\\leq n}};\\ x\_{\\leq n})$.

**Question**: Supposing our prediction distribution $P(x\_{>n}\\mid x\_{\\leq n})$ is intractable, can we obtain a variational approximation of this probability?

---

In machine learning, model parameters are hypotheses. Bayesian machine learning often seeks to convert a parametrized model like $p\_\\t(x,z)$ into a Bayesian model by putting a prior on $\\T$.

Let $P(x,z,\\t) = p\_\\t(x,z)P(\\t)$ where $P(\\t)$ is the prior probability of $\\t$. Instead of finding a single $\\t^\*$ which maximizes $p\_\\t(x)$, we are interested in the posterior $P(\\t \\mid x)$ and our average prediction of the latent variable, $P(z\\mid x)$.

This is the same as what I outlined above, replacing $x\_{\\leq n} \\mapsto x$, $z\\mapsto\\t$ and $x\_{>n}\\mapsto z$.






# Appendix 


$$\\begin{aligned}
& \\L(\\t,\\p;\\ x) \\\\
=\\ & \\Er(\\t,\\p;\\ x) + \\M(\\t;\\ x) \\\\
=\\ & \\kl{q\_\\p(z)}{p\_\\t(z\\mid x)} + \\log \\par{1/p\_\\t(x)} \\\\
=\\ & \\int\_\\Z q\_\\p(z) \\log\\par{\\frac{q\_\\p(z)}{p\_\\t(z\\mid x)}}\\ \\d z + \\int\_\\Z q\_\\p(z)\\log \\par{\\frac{1}{p\_\\t(x)}}\\ \\d z  \\\\
=\\ & \\int\_\\Z q\_\\p(z) \\log\\par{\\frac{q\_\\p(z)}{p\_\\t(x\\mid z)p\_\\t(z)/p\_\\t(x)}\\cdot\\frac{1}{p\_\\t(x)}}\\ \\d z \\\\
=\\ & \\int\_\\Z q\_\\p(z) \\log\\par{\\frac{q\_\\p(z)}{p\_\\t(z)}\\cdot\\frac{1}{p\_\\t(x\\mid z)}}\\ \\d z \\\\
=\\ & \\int\_\\Z q\_\\p(z) \\log\\par{\\frac{q\_\\p(z)}{p\_\\t(z)}}\\ \\d z + \\int\_\\Z q\_\\p(z) \\log\\par{\\frac{1}{p\_\\t(x\\mid z)}}\\ \\d z  \\\\
=\\ &  \\kl{q\_\\p(z)}{p\_\\t(z)} + \\E\_{z\\sim q\_\\p(z)}\\left\[\\log\\par{1/p\_\\t(x \\mid z)}\\right\] \\,.
\\end{aligned}$$
