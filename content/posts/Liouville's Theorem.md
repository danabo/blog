---
date: 2022-04-05
lastmod: '2022-11-20T21:11:20-08:00'
tags:
- thermodynamics
- physics
title: Liouville's Theorem
---

Liouville's Theorem states that the size of a state region of any closed system remains constant as the system evolves through time. This has consequences for connections between information and physics.
<!--more-->

$$
\\newcommand{\\0}{\\mathrm{false}}
\\newcommand{\\1}{\\mathrm{true}}
\\newcommand{\\mb}{\\mathbb}
\\newcommand{\\mc}{\\mathcal}
\\newcommand{\\mf}{\\mathfrak}
\\newcommand{\\and}{\\wedge}
\\newcommand{\\or}{\\vee}
\\newcommand{\\a}{\\alpha}
\\newcommand{\\s}{\\sigma}
\\newcommand{\\t}{\\tau}
\\newcommand{\\th}{\\theta}
\\newcommand{\\T}{\\Theta}
\\newcommand{\\D}{\\Delta}
\\newcommand{\\d}{\\delta}
\\newcommand{\\dd}{\\text{d}}
\\newcommand{\\pd}{\\partial}
\\newcommand{\\o}{\\omega}
\\newcommand{\\O}{\\Omega}
\\newcommand{\\x}{\\xi}
\\newcommand{\\z}{\\zeta}
\\newcommand{\\fa}{\\forall}
\\newcommand{\\ex}{\\exists}
\\newcommand{\\X}{\\mc{X}}
\\newcommand{\\Y}{\\mc{Y}}
\\newcommand{\\Z}{\\mc{Z}}
\\newcommand{\\P}{\\Psi}
\\newcommand{\\y}{\\psi}
\\newcommand{\\p}{\\phi}
\\newcommand{\\l}{\\lambda}
\\newcommand{\\G}{\\Gamma}
\\newcommand{\\B}{\\mb{B}}
\\newcommand{\\m}{\\times}
\\newcommand{\\E}{\\mb{E}}
\\newcommand{\\R}{\\mb{R}}
\\newcommand{\\H}{\\mc{H}}
\\newcommand{\\L}{\\mc{L}}
\\newcommand{\\e}{\\varepsilon}
\\newcommand{\\set}\[1\]{\\left\\{#1\\right\\}}
\\newcommand{\\tup}\[1\]{\\left(#1\\right)}
\\newcommand{\\abs}\[1\]{\\left\\lvert#1\\right\\rvert}
\\newcommand{\\vtup}\[1\]{\\left\\langle#1\\right\\rangle}
\\newcommand{\\btup}\[1\]{\\left\[#1\\right\]}
\\newcommand{\\inv}\[1\]{{#1}^{-1}}
\\newcommand{\\ceil}\[1\]{\\left\\lceil#1\\right\\rceil}
\\newcommand{\\dom}\[2\]{#1\_{\\mid #2}}
\\newcommand{\\df}{\\overset{\\mathrm{def}}{=}}
\\newcommand{\\up}\[1\]{^{(#1)}}
\\newcommand{\\restr}\[1\]{\_{\\mid{#1}}}
\\newcommand{\\dt}{{\\D t}}
\\newcommand{\\Dt}{{\\D t}}
\\newcommand{\\ddT}{{\\delta T}}
\\newcommand{\\Mid}{\\,\\middle|\\,}
\\newcommand{\\qed}{\\ \\ \\blacksquare}
\\newcommand{\\diff}\[2\]{\\frac{\\dd #1}{\\dd #2}}
\\newcommand{\\diffop}\[1\]{\\frac{\\dd}{\\dd #1}}
\\newcommand{\\pdiff}\[2\]{\\frac{\\pd #1}{\\pd #2}}
\\newcommand{\\pdiffop}\[1\]{\\frac{\\pd}{\\pd #1}}
\\newcommand{\\evalat}\[1\]{\\left. #1 \\right|}
$$


$\\newcommand{\\r}{\\rho}$  




# Preliminaries

## Hamiltonian Mechanics

(I also briefly described Hamiltonian mechanics in {{< locallink "The Reversibility Problem" "setup" >}}.)

Let the state of some system be described by a real-valued tuple $\\o  = (\\o\_1,\\o\_2,\\dots,\\o\_{2n}) = (q\_1, q\_n, p\_1, p\_n) \\in \\O$, where $\\O$ is the system's state space (set of all valid states) which is typically called its [phase space](https://en.wikipedia.org/wiki/Phase_space). We distinguish between the $q\_i$ and $p\_i$ coordinates. The subspace consisting of the tuples $(q\_1,\\dots,q\_n)$ called [configuration space](https://en.wikipedia.org/wiki/Configuration_space_(physics)). For each $q\_i$ there is a corresponding [conjugate momentum](https://en.wikipedia.org/wiki/Phase_space#Conjugate_momenta) $p\_i$. The $q\_i$ are not called positions, but rather, configuration or [generalized coordinates](https://en.wikipedia.org/wiki/Generalized_coordinates), since they can represent arbitrary internal degrees of freedom of a system, such as distance between parts, their orientations in space, etc. The relationship between the pairs $(q\_i,p\_i)$ is determined by the Hamiltonian of the system, which I'll get to in a moment.

In Cartesian coordinates where $q\_i$ represents a position in space, we get the usual definition of momentum, $p\_i = m\_i\\diffop{t}q\_i$, but this need not be the case in general. For example, if $q\_i$ is an angle of rotation then its conjugate momentum $p\_i$ is an [angular momentum](https://en.wikipedia.org/wiki/Angular_momentum) which has a different relationship with $q\_i$.

For our purposes, a [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics#Phase_space_coordinates_(p,q)_and_Hamiltonian_H) is a function $H : \\O\\times\\R \\to \\R$ mapping phase space coordinates and time to a real number which we will take to be the total energy of the system in question. So $H(\\vec{q},\\vec{p},t)$ is the total energy of the system when it is in state $(\\vec{q},\\vec{p})$ at time $t$. If $H$ is constant through time, i.e. $H(\\vec{q},\\vec{p},t)=H(\\vec{q},\\vec{p},t')$ for all $(\\vec{q},\\vec{p})\\in\\O$ and $t,t' \\in \\R$, then we call $H$ time-independent and drop the time input, i.e. we can just write $H(\\vec{q},\\vec{p})$. Otherwise, we call $H$ time-dependent. Time-independent systems satisfy [time-translational invariance](https://en.wikipedia.org/wiki/Time_translation_symmetry), i.e. time-shifting the system does not alter its dynamics.

The Hamiltonian $H$ contains all the information we need to derive equations of motion of the system, which are explicit functions from time to phase state of the system $\\s : \\R \\to \\O$ which I call trajectories. So $\\s(t)$ gives the state of an instance of the system at time $t$ following the trajectory $\\s$.

We can derive these trajectories directly from $H$ using [Hamilton's equations](https://en.wikipedia.org/wiki/Hamiltonian_mechanics#From_Euler-Lagrange_equation_to_Hamilton's_equations):

$$
\\diff{q\_i}{t}=\\pdiff{H}{p\_i},\\qquad \\diff{p\_i}{t}=-\\pdiff{H}{q\_i}\\,.
$$


These two equations are the only way $q\_i$ and $p\_i$ are distinguished mathematically. The possible trajectories of the system are all the solutions to this system of partial differential equations.


The above math conflates coordinates $\\vec{q},\\vec{p}$ as free variables with trajectories $\\s : \\R\\to\\O$ which are functions from time to phase space. That is to say, the DiffEQs above take $\\vec{q}(t),\\vec{p}(t)$ to be functions of time, but the same $\\vec{q},\\vec{p}$ are also used as free coordinate variables in other contexts. So in instances where it is helpful to be more precise, we can rewrite Hamilton's equations in terms of trajectories.

But first we need some notation. If $\\s$ is a trajectory with $\\s(t) = (\\vec{q}\\up{t},\\vec{p}\\up{t})=(q\_1\\up{t},\\dots,q\_n\\up{t},p\_1\\up{t},\\dots,p\_n\\up{t})$ being the state of the system along that trajectory at time $t$, then let $\\s\_\\vec{q}(t) = \\vec{q}\\up{t}$ and $\\s\_\\vec{p}(t) = \\vec{p}\\up{t}$ be the sub-dimensions of the output of $\\s(t)$ corresponding to the configuration and conjugate momenta coordinates respectively. Furthermore, let $\\s\_{q\_i}(t)=q\_i\\up{t}$ and $\\s\_{p\_i}(t)=p\_i\\up{t}$ select specific configuration and momentum coordinates on the output of $\\s(t)$.

Let $\\Sigma$ be the set of all trajectories $\\s$ s.t.

$$
\\evalat{\\diff{\\s\_{q\_i}}{t}}\_{t=\\hat{t}} = \\evalat{\\pdiff{H}{p\_i}}\_{(\\vec{q},\\vec{p})=\\s(t),\\ t=\\hat{t}} \\quad\\textrm{and}\\quad  \\evalat{\\diff{\\s\_{p\_i}}{t}}\_{t=\\hat{t}} = \\evalat{-\\pdiff{H}{q\_i}}\_{(\\vec{q},\\vec{p})=\\s(t),\\ t=\\hat{t}}
$$

for all $i=1,\\dots,n$ and for all $\\hat{t}\\in\\R$. Then $\\Sigma$ is the set of all solutions to Hamilton's equations, which I call the set of valid trajectories w.r.t. $H$.

It is useful to work explicitly in terms of functions that map states between times, called propagators. Let $\\t\_{t\\to t'} : \\O\\to\\O$ be a propagator mapping states at time $t$ to states at time $t'$ (if $t'<t$ then we are propagating state backwards in time). We can define the behavior of the propagator in terms of the valid trajectories of $H$:

$$
\\t\_{t\\to t'}(\\s(t)) = \\s(t')
$$

for all $\\s \\in \\Sigma$ and all $t,t' \\in \\R$.

Note that propagators are bijections where $\\t^{-1}\_{t\\to \\t'} = \\t\_{t' \\to t}$. 

If $H$ is time-independent, then we can just specify propagators in terms of their delta time, where $\\t\_\\Dt(\\s(t))=\\s(t+\\Dt)$ for all $t,\\Dt \\in\\R$.

## Measure

Liouville's theorem is a statement about measures on phase space which obey Hamilton's equations. Let's make all that precise.


Briefly, a [measure](https://en.wikipedia.org/wiki/Measure_(mathematics)) $\\mu$ is a function from subsets of $\\O$ to non-negative real numbers which is only defined on certain so-called measurable subset (as a [partial function](https://en.wikipedia.org/wiki/Partial_function) $\\mu$ has the type signature $\\mu:2^\\O \\to \\R\_{\\geq 0}$). We assume that $\\O$ is a [measurable space](https://en.wikipedia.org/wiki/Measurable_space). For a primer on measure theory, see my [post on probability theory](http://zhat.io/articles/primer-probability-theory#primer-to-measure-theory).

Throughout this post we suppose we are given a measure $\\mu$ on phase space $\\O$. Everything that follows does not assume any particular interpretation to the meaning of $\\mu$. Normalized measures can typically represent an i.i.d. stochastic drawing of the state of the system (i.e. frequentist interpretation), or the modeler's (you and I) state of belief about the system's state (called the Bayesian interpretation). I tend to think of these measures as simply providing a way to quantify the sizes (e.g. areas, volumes) of phase space regions (subsets of phase space). See {{< locallink "Bayesian information theory" >}} and {{< locallink "Physical Information" >}} for details on this interpretation. That means that I don't assume $\\mu$ is normalized (which is required for $\\mu$ to be a probability measure), i.e. $\\mu(\\O)$ need not be $1$ and need not even be defined ($\\mu$ need not be not normalizable).

To talk about time-evolving a measure, we need to assign a measure $\\mu\_t$ to every moment of time $t\\in\\R$. Let $R \\subseteq \\O$ be any measurable subset of phase space $\\O$, which I will henceforth simply refer to as a region, or phase region.

We require that
$$
\\mu\_{t}(R) = \\mu\_{t'}(\\t\_{t \\to t'}(R))\\,,
$$

for all regions $R$ and all $t,t' \\in \\R$.  

Note that everything described here is deterministic time-evolution. That is to say, if the measure $\\mu\_t$ at time $t$ represents uncertainty (Bayesian) or randomness (frequentist) due to the choice of the state of the system at time $t$, then every state before and after is uniquely determined by that choice. This is in contrast to stochastic time-evolution, which destroys information that states of the system share about each other across time, and involves a different sort of time-evolution of measure. 

Note that putting a measure on state space at some time $t$, and then deterministically time-evolving that measure according to the propagators $\\t\_{t\\to t'}$, is equivalent to putting a measure on the valid trajectories in $\\Sigma$. So an equivalent formulation would be to define $\\Sigma$ as a measurable space and put a measure $M$ on $\\Sigma$. This is equivalent to time-evolving measures on $\\O$ as described. See {{< locallink "Causality For Physics" "incorporating-probability" >}} for details.


Given that $\\mu\_t$ is time-evolved in this way, Liouville's Theorem makes a statement about how density behaves over time, given that the system is closed and conserves energy (according to its given Hamiltonian). It is easier to state the theorem in terms of density functions rather than measures. Though density functions may not exist for any measure on any measurable space, we can assume they do for phase spaces that represent Hamiltonian systems. In that case we can define the conversion between measure and density.

Supposing $\\O$ is an $N$-dimensional parametrized measurable space (for our purposes $N=2n$) where differentiation and integration is well defined (basically always the case for physical systems) with a measure $\\mu\_t$. Then the corresponding density function $\\r:\\O\\times\\R \\to \\R$ satisfies

$$
\\mu\_t(R) = \\int\_R \\r(\\vec{\\o},t)\\ \\dd{\\o\_1}\\dots\\dd{\\o\_{N}}\\,,
$$

for all regions $R$ and times $t\\in\\R$. We can [explicitly derive the density](https://en.wikipedia.org/wiki/Probability_density_function#Densities_associated_with_multiple_variables) in terms of measure $\\mu\_t$ as 

$$\\r(\\o, t) = \\frac{\\dd^{N}}{\\dd \\o\_1\\dots \\dd \\o\_{N}}\\mu\_t\\big(\\G(\\o\_1,\\dots,\\o\_{N})\\big)\\,,$$

where $\\G(\\o\_1,\\dots,\\o\_{N}) = \\prod\_{i=1}^{N}(-\\infty,\\o\_i\]$ is a hyper-quadrant with origin at $(\\o\_1,\\dots,\\o\_{N})$.




# Liouville's Theorem
As outlined above, suppose we have a system described by [canonical coordinates](https://en.wikipedia.org/wiki/Canonical_coordinates) $\\vec{\\o}=(\\vec{q},\\vec{p})=(q\_1,\\dots,q\_n,p\_1,\\dots,p\_n)$ and a [Hamiltonian](https://en.wikipedia.org/wiki/Hamiltonian_mechanics) $H$. Also suppose we are given some density function $\\r(\\vec{q},\\vec{p},t)$, a function of coordinates and time, which obeys the time-evolution induced by $H$ (as explained above in [#Measure](#measure)). That is to say, the density must satisfy $\\int\_R \\r(\\vec{\\o}, t)\\ \\dd^{2n}{\\vec{\\o}}=\\int\_{R'} \\r(\\vec{\\o}, t')\\ \\dd^{2n}{\\vec{\\o}}$ for all regions $R$ and times $t,t'$, where $R'={\\t\_{t\\to t'}(R)}$ and $\\t\_{t\\to t'}$ is the propagator induced by $H$ mapping time $t$ to time $t'$.



If the system is isolated and has constant total energy (obeys conservation of energy), then [Liouville's Theorem states](https://en.wikipedia.org/wiki/Liouville%27s_theorem_(Hamiltonian)#Liouville_equations)

$$
\\diff{\\r}{t} = 0\\,.
$$
 
 
 We have to be careful here.  It might look like we are stating that $\\r$ is constant through time, but that's actually not what that means. We must make the important distinction between the partial derivative $\\pdiff{\\r}{t}$ which gives the change in $\\r$ through time at some fixed point in phase space, and the single-variable derivative $\\diff{\\r}{t}$, which treats $\\r$ as a single-variable function - specifically, $\\r$ along some parametric curve $(\\vec{q}(t),\\vec{p}(t),t)$, i.e. $\\r(t) = \\r(\\vec{q}(t),\\vec{p}(t),t)$. This allows us to expand out the single-variable derivative using the multi-variate chain rule, thus rewriting Liouville's theorem like this:
 
 $$
\\diffop{t}\\r(\\vec{q}(t),\\vec{p}(t),t) = \\sum\_{i=1}^n \\pdiff{\\r}{q\_i}\\diff{q\_i}{t} + \\sum\_{i=1}^n \\pdiff{\\r}{p\_i}\\diff{p\_i}{t} + \\pdiff{\\r}{t} = 0\\,,
$$

where all derivatives are evaluated at the point $(\\vec{q}(t),\\vec{p}(t),t)$ for some chosen time $t$.

We further assume this parametric curve $(\\vec{q}(t),\\vec{p}(t),t)$ satisfies Hamilton's equations, i.e. $(\\vec{q}(t),\\vec{p}(t))=\\sigma(t)$ for all $t$, for some valid trajectory $\\s\\in\\Sigma$. Then we can plugin and rewrite Liouville's theorem as

$$
\\diff{\\r}{t} = \\pdiff{\\r}{t} + \\sum\_{i=1}^n \\tup{\\pdiff{\\r}{q\_i}\\pdiff{H}{p\_i} - \\pdiff{\\r}{p\_i}\\pdiff{H}{q\_i}} = 0\\,,
$$

making implicit dependence on the valid trajectories of the system and explicit dependence on the given Hamiltonian $H$.

We could also rewrite Liouville's theorem using our trajectory notation from above:

$$
\\evalat{\\diff{\\r}{t}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}),t=\\hat{t}} = \\evalat{\\btup{\\sum\_{i=1}^n \\pdiff{\\r}{q\_i}\\diff{\\s\_{q\_i}}{t} + \\sum\_{i=1}^n \\pdiff{\\r}{p\_i}\\diff{\\s\_{p\_i}}{t} + \\pdiff{\\r}{t}} }\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}),t=\\hat{t}} = 0
$$

holds for all valid trajectories $\\s\\in\\Sigma$ and all times $\\hat{t}$.
 


### Intuition Pump

Let's look at a fairly typical class of Hamiltonians: $H = \\sum\_{i=1}^n \\frac{1}{2m\_i}p\_i^2 + U(q)$. This is just the standard form of a time-independent Hamiltonian of a system in the presence of some constant potential field $U$, where $m\_i$ is the mass of the $i$-th coordinate. Then Hamilton's equations tell us

$$
\\diff{q\_i}{t} = \\pdiff{H}{p\_i} = \\frac{p\_i}{m\_i}\\,,\\qquad \\diff{p\_i}{t} = -\\pdiff{H}{q\_i} = -\\pdiff{U}{q\_i}
$$

where the first equation relates coordinates $q\_i$ to conjugate momenta $p\_i$ in the obvious way (i.e. $p\_i =  \\diffop{t}(m\_iq\_i)$ is taken as the definition of momentum in Newtonian physics), and the second equation states that the time derivative of momentum (in the $i$-th direction) is the negative coordinate derivative of the [potential field](https://en.wikipedia.org/wiki/Force#Potential_energy) $U$ which gives the force along the $i$-th direction, i.e. $\\diff{p\_i}{t} = -\\pdiff{U}{q\_i}$ is just a restatement of Newton's second law, i.e. change in momentum is due to a force generated by a [change in potential energy](http://hyperphysics.phy-astr.gsu.edu/hbase/pegrav.html).

Plugging in, Liouville's theorem then becomes

$$
\\diff{\\r}{t} = \\pdiff{\\r}{t} + \\sum\_{i=1}^n \\tup{\\pdiff{\\r}{q\_i}\\frac{p\_i}{m\_i} - \\pdiff{\\r}{p\_i}\\pdiff{U}{q\_i}} = 0\\,.
$$


## Uniform Measure

It may at a glance look like Liouville is just restating our starting definition for how density gets time-evolved. That is to say, we took as given that $\\int\_R \\r(\\vec{\\o}, t)\\ \\dd^{2n}{\\vec{\\o}}=\\int\_{R'} \\r(\\vec{\\o}, t')\\ \\dd^{2n}{\\vec{\\o}}$, or equivalently $\\mu\_t(R) = \\mu\_{t'}(R')$, which is stating that the measure of region $R$ is preserved when it is transformed to $R'= \\t\_{t\\to t'}(R)$, because we transform the measure/density along with it. However, this statement tells us nothing about how $\\r$ will change as individual states are time-evolved, i.e. how $\\r(\\s(t),t)$ will differ from $\\r(\\s(t'),t')$ along a given trajectory $\\s$. The Liouville statement $\\diff{\\r}{t}=0$ is telling us that density is constant along valid trajectories, i.e. $\\r(\\s(t),t)=\\r(\\s(t'),t')$ for all $t,t' \\in \\R$, for all valid $\\s\\in\\Sigma$ (hence we could instead just assign time-independent density to the trajectories themselves, i.e. make $\\r$ a function on $\\Sigma$).

A common colloquial understanding is that Liouville's theorem states that the size of phase regions remains visually constant through time, where a Euclidean, i.e. uniform, measure on phase space is implied. This is indeed a very useful consequence of Liouville.

Formally, a uniform measure is derived from a constant density function, i.e. $\\r(\\vec{\\o},t) = \\r(\\vec{\\o}',t)$ for any two $\\vec{\\o},\\vec{\\o}' \\in \\O$. Suppose $\\r$ is uniform with $\\r(\\vec{\\o},t\_0)=\\r\_0$ at time $t\_0$. Since by Liouville $\\r(\\s(t),t)=\\r(\\s(t'),t')$ for all times $t,t'\\in\\R$, then $\\r(\\s(t),t)=\\r(\\s(t\_0),t\_0)=\\r\_0$ holds for all valid trajectories $\\s\\in\\Sigma$ for all times $t$. Thus $\\r(\\vec{\\o},t)=\\r\_0$ is uniform at all times $t$, since there will be some trajectory passing through any $\\vec{\\o}\\in\\O$. We conclude that $\\r = \\r\_0$ is constant in phase space and time when time-evolved.

Preservation of phase volume under a measure/density which is constant through time is an interesting result of Liouville.



# Coordinate Agnostic Ignorance

Liouville's theorem is actually a special case of a more general phenomenon (the generalized Liouville theorem), and one of the usual proofs given for Liouville is actually a proof for the more general case. Rather than just time-evolution preserving density, the stronger result states that a certain class of coordinate transformations preserves density. Viewing time-evolution as such a coordinate transformation from time $t$ to new coordinates describing time $t'$, we see that Liouville becomes a special case.

This more general form of Liouville is relevant to my interest in the relationship between information and thermodynamic entropy. Specifically, it allows us to bypass the [Bertrand paradox](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)) and have a unique maximally ignorance way to quantify information. The Boltzmann formulation of entropy utilizes this same quantification (?)

## Canonical Coordinates

Some references that I found useful for this topic:
- [Wikipedia: Canonical transformation](https://en.wikipedia.org/wiki/Canonical_transformation)
- [The generating function of a canonical transformation](http://www.scielo.org.mx/pdf/rmfe/v57n2/v57n2a4.pdf)
- [Canonical Transformations in Hamiltonian Mechanics](https://phys.libretexts.org/Bookshelves/Classical_Mechanics/Variational_Principles_in_Classical_Mechanics_(Cline)/15%3A_Advanced_Hamiltonian_Mechanics/15.03%3A_Canonical_Transformations_in_Hamiltonian_Mechanics)
- [Goldstein, Poole & Safko, Classical Mechanics 3rd ed.](https://www.pearson.com/us/higher-education/program/Goldstein-Classical-Mechanics-3rd-Edition/PGM170105.html), section 9.4
- [Landau & Lifshitz, Mechanics - Volume 1, 3rd ed.](https://www.elsevier.com/books/mechanics/landau/978-0-08-050347-9)
    - A good summary [here](https://galileoandeinstein.phys.virginia.edu/7010/CM_10_Canonical_Transformations.html) and [here](https://galileoandeinstein.phys.virginia.edu/7010/CM_11_Introduction_to_Liouville.html))
- [No-Nonsense Classical Mechanics](https://nononsensebooks.com/cm/), section 7.3.2.

In particular this discussion takes inspiration from the derivations in section 7.3.1 of [No-Nonsense Classical Mechanics](https://nononsensebooks.com/cm/).

Consider a time-independent coordinate transformation specified by a set of bijective functions $Q\_i(\\vec{q},\\vec{p})$ and $P\_i(\\vec{q},\\vec{p})$ for $i=1,\\dots,n$, where $\\vec{q} = (q\_1,\\dots,q\_n)$ and $\\vec{p}=(p\_1,\\dots,p\_n)$, written more compactly as vector-valued function $\\vec{Q}(\\vec{q},\\vec{p})$ and $\\vec{P}(\\vec{q},\\vec{p})$. Notice that we are allowing intermingling of position and momentum coordinates. For example, we could swap position and momentum where $Q\_i = p\_i$ and $P\_i=-q\_i$ for all $i$.

Our Hamiltonian $H(\\vec{q},\\vec{p}, t)$ is a function of the original coordinates and time (a time-dependent Hamiltonian). We obtain the Hamiltonian in the new coordinate system by plugging in the inverse mappings: $\\tilde{H}(\\vec{Q},\\vec{P},t) = H(\\vec{q}(\\vec{Q},\\vec{P}),\\vec{p}(\\vec{Q},\\vec{P}),t)$, where $\\tilde{H}$ is a function of the new coordinates $(\\vec{Q},\\vec{P})$ and time.

Note that I am only considering time-independent coordinate transformations. Canonical transformations are allowed to be time-dependent, where $\\vec{Q}(\\vec{q},\\vec{p},t)$ and $\\vec{P}(\\vec{q},\\vec{p},t)$ are functions of time as well. However this is more complex to deal with, especially since the Hamiltonian $\\tilde{H}$ derived by naively plugging in the coordinate transformation may not be the valid Hamiltonian for the system in the transformed coordinates. [Generating functions](https://en.wikipedia.org/wiki/Generating_function_(physics)) are needed to deal with time-dependent transformations which I won't get into here. Many of the sources I listed above explain them in detail. So for this post assume time-independent coordinate transformations.

A **canonical** coordinate transformation is defined as a transformation that preserves Hamilton's equations, i.e. 

$$\\diff{Q\_i}{t}=\\pdiff{\\tilde{H}}{P\_i}\\,,\\qquad \\diff{P\_i}{t}=-\\pdiff{\\tilde{H}}{Q\_i}$$ 

holds in the new coordinate system.  To be more precise, given the set of valid trajectories $\\Sigma$ in coordinates $\\vec{q},\\vec{p}$, we want the transformed trajectories to also obey Hamilton's equations. For $\\s\\in\\Sigma$, let $\\tilde{\\s}(t) = \\vtup{\\vec{Q},\\vec{P}}(\\s(t))$, which is a shorthand for the pair of relationships: $\\tilde{\\s}\_{\\vec{Q}}(t)=\\vec{Q}(\\s(t))$ and $\\tilde{\\s}\_{\\vec{P}}(t)=\\vec{P}(\\s(t))$. Let $\\tilde{\\Sigma} = \\vtup{\\vec{Q},\\vec{P}}(\\Sigma)$ be the set of all transformed trajectories in $\\Sigma$. Then the coordinate transform is canonical iff

$$
\\evalat{\\diff{\\tilde{\\s}\_{Q\_i}}{t}}\_{t=\\hat{t}} = \\evalat{\\pdiff{\\tilde{H}}{P\_i}}\_{(\\vec{Q},\\vec{P})=\\tilde{\\s}(t),\\ t=\\hat{t}} \\quad\\textrm{and}\\quad  \\evalat{\\diff{\\tilde{\\s}\_{P\_i}}{t}}\_{t=\\hat{t}} = \\evalat{-\\pdiff{\\tilde{H}}{Q\_i}}\_{(\\vec{Q},\\vec{P})=\\tilde{\\s}(t),\\ t=\\hat{t}}
$$

for all $\\tilde{\\s} \\in \\tilde{\\Sigma}$, all $i=1,\\dots,n$ and all $\\hat{t}\\in\\R$.

A coordinate system is canonical if Hamilton's equations hold in that coordinate system, and a canonical transformation applied to canonical coordinates produces canonical coordinates.

For some intuition pumps, see {{< locallink "Liouville Supplemental - Coordinate Transformations" "example-2d-phase-space" >}} and {{< locallink "Liouville Supplemental - Coordinate Transformations" "example-non-canonical" >}}




## Measure Preservation
Here we prove that coordinate transformations which preserve Hamilton's equations (i.e. canonical transformations) have a constant Jacobian equal to 1, implying that density is preserved under these transformations.

References:
- [Goldstein, Poole & Safko, Classical Mechanics 3rd ed.](https://www.pearson.com/us/higher-education/program/Goldstein-Classical-Mechanics-3rd-Edition/PGM170105.html) section 9.4
- https://en.wikipedia.org/wiki/Canonical_transformation#Liouville's_theorem



Remember that $\\vec{Q}$ is a function of $(\\vec{q},\\vec{p})$. Using chain rule, we have

$$\\begin{aligned}
\\diffop{t}Q\_i
    &= \\sum\_{j=1}^n \\btup{\\pdiff{Q\_i}{q\_j}\\diff{q\_j}{t}+\\pdiff{Q\_i}{p\_j}\\diff{p\_j}{t}} \\\\
    &= \\sum\_{j=1}^n \\btup{\\pdiff{Q\_i}{q\_j}\\pdiff{H}{p\_j}-\\pdiff{Q\_i}{p\_j}\\pdiff{H}{q\_j}}\\,.
\\end{aligned}$$

Using $\\tilde{H}(\\vec{Q},\\vec{P})=H(\\vec{q}(\\vec{Q},\\vec{P}),\\vec{p}(\\vec{Q},\\vec{P}))$, we have

$$
\\pdiff{\\tilde{H}}{P\_i} = \\sum\_{j=1}^n\\btup{\\pdiff{H}{q\_j}\\pdiff{q\_j}{P\_i} + \\pdiff{H}{p\_j}\\pdiff{p\_j}{P\_i}}\\,.
$$

We want to satisfy

$$\\begin{aligned}
\\diff{Q\_i}{t} &= \\pdiff{\\tilde{H}}{P\_i} 
\\\\
\\implies \\sum\_{j=1}^n \\btup{\\pdiff{H}{q\_j}\\tup{-\\pdiff{Q\_i}{p\_j}}+\\pdiff{H}{p\_j}\\pdiff{Q\_i}{q\_j}} &= \\sum\_{j=1}^n\\btup{\\pdiff{H}{q\_j}\\pdiff{q\_j}{P\_i} + \\pdiff{H}{p\_j}\\pdiff{p\_j}{P\_i}}\\,,
\\end{aligned}$$

giving us a the constraints

$$
\\pdiff{Q\_i}{q\_j} = \\pdiff{p\_j}{P\_i}\\,,\\qquad \\pdiff{Q\_i}{p\_j} = -\\pdiff{q\_j}{P\_i}
$$

for all $i=1,\\dots,n$.

The determinant [Jacobian](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant) of our transformation $\\tup{\\vec{Q}(\\vec{q},\\vec{p}),\\vec{P}(\\vec{q},\\vec{p})}$ determines the relationship between our density $\\r(\\vec{q},\\vec{p},t)$ and the transformed density $\\tilde{\\r}(\\vec{Q},\\vec{P},t)=\\pdiff{(\\vec{Q},\\vec{P})}{(\\vec{q},\\vec{p})}\\r\\tup{\\vec{q}(\\vec{Q},\\vec{P}),\\vec{p}(\\vec{Q},\\vec{P}),t)}$, where

$$
\\pdiff{(\\vec{Q},\\vec{P})}{(\\vec{q},\\vec{p})} \\df \\det\\begin{bmatrix}\\pdiff{Q\_1}{q\_1} & \\dots & \\pdiff{Q\_1}{p\_n} \\\\ \\vdots & \\ddots & \\vdots \\\\ \\pdiff{P\_n}{q\_1} & \\dots & \\pdiff{P\_n}{p\_n}\\end{bmatrix}
$$

The [multivariate chain rule](https://en.wikipedia.org/wiki/Chain_rule#General_rule) tells us
$$\\begin{aligned}
\\pdiff{(\\vec{Q},\\vec{P})}{(\\vec{q},\\vec{p})} &= \\pdiff{(\\vec{Q},\\vec{P})}{(\\vec{q},\\vec{P})} \\pdiff{(\\vec{q},\\vec{P})}{(\\vec{q},\\vec{p})} \\\\
&= \\left. \\pdiff{(\\vec{Q},\\vec{P})}{(\\vec{q},\\vec{P})}  \\middle/ \\pdiff{(\\vec{q},\\vec{p})}{(\\vec{q},\\vec{P})} \\right. \\\\
&= \\left. \\pdiff{(\\vec{Q})}{(\\vec{q})}  \\middle/ \\pdiff{(\\vec{p})}{(\\vec{P})} \\right.
\\end{aligned}$$

The middle step uses the fact that the Jacobian of the inverse of a transformation is the inverse of the Jacobian matrix, whose determinant is the reciprocal of the original determinant. The last step makes use of the cancellation of same variables.  


Plugging in our constraints, we have

$$\\begin{aligned}
\\pdiff{(\\vec{Q})}{(\\vec{q})}
&= \\det\\begin{bmatrix}\\pdiff{Q\_1}{q\_1} & \\dots & \\pdiff{Q\_1}{q\_n} \\\\ \\vdots & \\ddots & \\vdots \\\\ \\pdiff{Q\_n}{q\_1} & \\dots & \\pdiff{Q\_n}{q\_n}\\end{bmatrix} \\\\
&= \\det\\begin{bmatrix}\\pdiff{p\_1}{P\_1} & \\dots & \\pdiff{p\_1}{P\_n} \\\\ \\vdots & \\ddots & \\vdots \\\\ \\pdiff{p\_n}{P\_1} & \\dots & \\pdiff{p\_n}{P\_n}\\end{bmatrix} \\\\
&= \\pdiff{(\\vec{p})}{(\\vec{P})}
\\end{aligned}$$

and so $\\left. \\pdiff{(\\vec{Q})}{(\\vec{q})}  \\middle/ \\pdiff{(\\vec{p})}{(\\vec{P})} \\right. = 1$. Thus $\\pdiff{(\\vec{Q},\\vec{P})}{(\\vec{q},\\vec{p})}= 1$.

Let $T$ be a canonical coordinate transformation on $\\O$. Then $\\pdiff{(T(\\vec{\\o}))}{(\\vec{\\o})}=1$. By the change of variable rule,

$$\\begin{aligned}
\\int\_R \\r(\\vec{\\o},t)\\ \\dd^{2n} \\vec{\\o} &= \\int\_{T(R)} \\pdiff{(T(\\vec{\\o}))}{(\\vec{\\o})}\\r\\tup{T^{-1}\\tup{\\vec{z}},t}\\ \\dd^{2n} \\vec{z} \\\\&= \\int\_{T(R)} \\r\\tup{T^{-1}\\tup{\\vec{z}},t}\\ \\dd^{2n} \\vec{z}\\,,
\\end{aligned}$$

and so naively applying the coordinate change to $\\r$ s.t. $\\tilde{\\r}(\\vec{z},t)=\\r\\tup{T^{-1}\\tup{\\vec{z}},t}$ gives us the correct density in the transformed coordinates. If $\\r=\\r\_0$, then $\\tilde{\\r}=\\r\_0$, and so the uniform density is preserved under the transformation.


### Liouville proof sketch

Liouville's theorem is a special case of the above result. Time-evolution ends up being a canonical transformation, so long as energy is conserved in the system (i.e. the Hamiltonian is constant along every trajectory). Thus density is preserved through time-evolution, i.e. density is constant along a given trajectory. That is Liouville's theorem.

There is a simple argument for why time-evolution is a canonical transformation. Since, for a valid physical model, we take as given that Hamilton's equations are obeyed at all times and phase coordinates, then transforming the system through time preserves Hamilton's equations, making that transformation canonical (by definition). This argument may seem a bit handwavy. There are formal proofs for this which go a bit out of scope of this post. However, I can outline a straightforward proof sketch. 

Note that, unlike the canonical transformations we considered above, time-evolution is a not universally canonical transformation (canonical w.r.t. all Hamiltonians). One Hamiltonian's time-evolution generally does not produce transformations that are canonical w.r.t. all Hamiltonians. So these time-translation transformations are examples of Hamiltonian-specific canonical transformations. See {{< locallink "Liouville Supplemental - Coordinate Transformations" "example-hamiltonian-specific" >}}.



Suppose we are given a time-independent Hamiltonian $H(\\vec{q},\\vec{p})$ which induces propagators $\\t\_{\\Dt}$ for $\\Dt\\in\\R$. As I mentioned earlier, dealing with time-dependent transformations is out of scope of this post, and time-evolution will only be time-independent if the Hamiltonian is.

Fix a particular $\\Dt\\in\\R$ and define the following coordinate transformation:

$$\\tup{\\vec{Q}(\\vec{q},\\vec{p}),\\vec{P}(\\vec{q},\\vec{p})}=\\t\_\\Dt\\tup{\\vec{q},\\vec{p}}\\,,$$

giving us the inverse transformation,
$$\\tup{\\vec{q}(\\vec{Q},\\vec{P}),\\vec{p}(\\vec{Q},\\vec{P})}=\\t\_{-\\Dt}\\tup{\\vec{Q},\\vec{P}}\\,.$$

Then the transformed Hamiltonian is $\\tilde{H}(\\vec{Q},\\vec{P})=H(\\vec{q}(\\vec{Q},\\vec{P}),\\vec{p}(\\vec{Q},\\vec{P}))$.

Hamilton's equations in terms of trajectories $\\s:\\R\\to\\O$ are

$$
\\evalat{\\diff{\\s\_{q\_i}}{t}}\_{t=\\hat{t}} = \\evalat{\\pdiff{H}{p\_i}}\_{(\\vec{q},\\vec{p})=\\s(t),\\ t=\\hat{t}} \\quad\\textrm{and}\\quad  \\evalat{\\diff{\\s\_{p\_i}}{t}}\_{t=\\hat{t}} = \\evalat{-\\pdiff{H}{q\_i}}\_{(\\vec{q},\\vec{p})=\\s(t),\\ t=\\hat{t}}
$$

The set of trajectories $\\Sigma$ satisfying this system of partial differential equations constitute the valid trajectories of the system.

We can write down what the transformed trajectories look like:

$$\\tilde{\\s}(\\hat{t}) = \\vtup{\\vec{Q},\\vec{P}}(\\s(\\hat{t})) = \\s(\\hat{t}+\\Dt)$$
for all $\\s \\in \\Sigma$ and all $\\hat{t}\\in\\R$.

Then we have

$$
\\evalat{\\diff{\\tilde{\\s}\_{Q\_i}}{t}}\_{t=\\hat{t}} = \\evalat{\\diff{\\s\_{q\_i}}{t}}\_{t=\\hat{t}+\\Dt} = \\evalat{\\pdiff{H}{p\_i}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}+\\Dt)}$$

$$
\\evalat{\\diff{\\tilde{\\s}\_{P\_i}}{t}}\_{t=\\hat{t}} = \\evalat{\\diff{\\s\_{p\_i}}{t}}\_{t=\\hat{t}+\\Dt} = -\\evalat{\\pdiff{H}{q\_i}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}+\\Dt)}$$

The next step in this proof requires that the Hamiltonian be invariant to time-translation, i.e. $\\tilde{H}(\\vec{q},\\vec{p})=H(\\vec{q},\\vec{p})$. This ends up being the case for all Hamiltonians that obey conservation of energy, i.e. the Hamiltonian is constant along its valid trajectories, i.e. $H(\\s(t))=H(\\s(t'))$ for all $\\s\\in\\Sigma$ and $t,t'\\in\\R$. I won't prove this here, but time-translation symmetry is a well known result in physics.

Then we complete our proof with

$$
\\evalat{\\pdiff{H}{q\_i}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}+\\Dt)} = \\evalat{\\pdiff{\\tilde{H}}{q\_i}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}+\\Dt)} = \\evalat{\\pdiff{\\tilde{H}}{Q\_i}}\_{(\\vec{Q},\\vec{P})=\\tilde{\\s}(\\hat{t})}
$$

$$
\\evalat{\\pdiff{H}{p\_i}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}+\\Dt)} = \\evalat{\\pdiff{\\tilde{H}}{p\_i}}\_{(\\vec{q},\\vec{p})=\\s(\\hat{t}+\\Dt)} = \\evalat{\\pdiff{\\tilde{H}}{P\_i}}\_{(\\vec{Q},\\vec{P})=\\tilde{\\s}(\\hat{t})}
$$

And so we have Hamilton's equations in the transformed coordinates:

$$
\\evalat{\\diff{\\tilde{\\s}\_{Q\_i}}{t}}\_{t=\\hat{t}} = \\evalat{\\pdiff{\\tilde{H}}{P\_i}}\_{(\\vec{Q},\\vec{P})=\\tilde{\\s}(\\hat{t})}\\,,\\qquad \\evalat{\\diff{\\tilde{\\s}\_{P\_i}}{t}}\_{t=\\hat{t}} = -\\evalat{\\pdiff{\\tilde{H}}{Q\_i}}\_{(\\vec{Q},\\vec{P})=\\tilde{\\s}(\\hat{t})}
$$



## Configuration Space Coordinate Transformations

A surprising result is that phase space measure is preserved under arbitrary change of configuration space coordinates, so long as we choose the right corresponding momentum transformation so that the phase space transformation is canonical.

See {{< locallink "Liouville Supplemental - Coordinate Transformations" "arbitrary-configuration-space-transformations" >}}.

## Hamiltonian specific canonical transformations

Previously we derived transformations that are canonical for all Hamiltonians. However, there are yet more canonical transformations, specifically those which are specific to a given Hamiltonian.

See {{< locallink "Liouville Supplemental - Coordinate Transformations" "hamiltonian-specific-canonical" >}}.

# Entropy And The Bertrand Paradox

[Boltzmann entropy](https://en.wikipedia.org/wiki/Entropy_(statistical_thermodynamics)#Boltzmann's_principle) is proportional to the log of the size of a phase region. Entropy as such already appears to have an observer-arbitrary aspect to it, since the choice of phase region that describes a system depends on the observer's state of knowledge (or their goals, see {{< locallink "The Reversibility Problem" "the-interpretation-of-state-regions" >}}). The observer-arbitrariness of entropy is only compounded further if the choice of measure, for measuring sizes of phase regions, is also unconstrained and arbitrarily chosen. Luckily, canonical coordinates get us out of the latter conundrum.

It would make sense to follow the [principle of indifference](https://en.wikipedia.org/wiki/Principle_of_indifference#Application_to_continuous_variables) and always require a uniform measure on phase space. However, uniformity of measure depends on our chosen coordinate system. This problem can be viewed as a generalization of the [Bertrand paradox](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)). See {{< locallink "Liouville Supplemental - Bertrand Paradox" >}}. This poses a problem since physics is coordinate system agnostic - there is no preferred coordinate system. 

You might be tempted to propose that we express everything in Cartesian coordinates, but what is considered as "Cartesian" is not in general well defined. While we might be able to take as primitive the idea that space around us (without relativistic gravitational forces) is flat, and so placing a grid on 3D space gives us Cartesian coordinates. However, when dealing with the generalized coordinates of an arbitrary system, the relationship between those coordinates and physical 3D space becomes complex. For example, we could have coordinates representing the orientations and positions of movable rigid parts in a compound structure. Or, we might be modeling the configuration of molecular structures, with various intermolecular orientations and relationships. Expressing any of that in Cartesian spatial coordinates is difficult to say the least.

Luckily, we don't need to bother with any of that. The result above in [#Measure Preservation](#measure-preservation), and moreover in {{< locallink "Liouville Supplemental - Coordinate Transformations" "arbitrary-configuration-space-transformations" >}}, tells us that no matter what coordinate system we put on configuration space, uniform measure in *phase space* will be preserved if we change configuration coordinates to anything else. Our only condition is that our phase space coordinates be canonical for the system in question, which is already taken as given in most circumstances (and if that is not true, there are many other complications to deal with).

This neat property of classical mechanics also allows us to uniquely quantify information about physical systems. In {{< locallink "Physical Information" >}} I define what it means to have information about a system. Basically, if we've narrowed down the state of the system to some subset of state space (phase space), then we have information. But if we want to quantify how much information we have (allowing us to invoke all of the machinery of Shannon's information theory, see {{< locallink "Physical Information" "shannon-quantities" >}}), we need to choose a measure on state space. If there is nothing constraining our choice of measure, our quantities of information are not very ... informative.

But with the results above, in classical mechanics, we can safely put a uniform measure/density on phase space, in our chosen configuration coordinate system (assuming our phase coordinates are canonical). That measure/density will remains uniform in any other configuration coordinate system (assuming still in canonical phase coordinates). For example, suppose we have a system described with phase space $\\O$ and Hamiltonian $H$. Let $\\r = \\r\_0$ be a constant density function on $\\O$ and time. Let $\\mu\_{\\r\_0}$ be the corresponding uniform measure. The information gained by narrowing down the state of a system from phase region $R$ to region $R'$ is

$$\\begin{aligned}
h(R' \\mid R) &= -\\lg\\frac{\\mu\_{\\r\_0}(R')}{\\mu\_{\\r\_0}(R)} \\\\
  &= -\\lg\\frac{\\int\_{R'} \\r\_0\\ \\dd^{2n}\\vec{\\o}}{\\int\_{R} \\r\_0\\ \\dd^{2n}\\vec{\\o}}  \\\\
  &= -\\lg\\frac{\\r\_0\\int\_{R'}\\dd^{2n}\\vec{\\o}}{\\r\_0\\int\_{R}\\dd^{2n}\\vec{\\o}}  \\\\
  &= -\\lg\\frac{\\int\_{R'}\\dd^{2n}\\vec{\\o}}{\\int\_{R}\\dd^{2n}\\vec{\\o}} \\,.
\\end{aligned}$$

So our information gain (and similarly change in entropy - see {{< locallink "Connecting Entropy And Information" >}}) of the system does not depend on $\\r\_0$. We can go ahead and use the Euclidean measure $\\l=\\mu\_1$ with $\\r\_0=1$. Note that even if the measure of the entire phase space is infinite, i.e. $\\l(\\O)=\\infty$, we still get finite quantities of information gain so long as the starting region $R$ has finite measure. That is to say, going from knowing that a gas is in a box to knowing that the gas is in a smaller box gives us finitely many bits of information. On the other hand, going from knowing nothing to knowing there is a gas in a box gives us infinite information, since in that case $R=\\O$. Since we are not supposing we are randomly drawing states of the system, we do not need to work with normalizable measures. The measure here simply measures sizes of regions.

Note that statistical thermodynamics makes use of this coordinate-invariant measure result to justify using uniform measures on phase space. E.g. see [Statistical Mechanics 4th ed.](https://www.elsevier.com/books/statistical-mechanics/beale/978-0-12-382188-1) (Pathria & Beale) section 2.2. This relieves us from being restricted to equilibrium processes (which are ergodic) where the choice of measure is determined by [measure invariance through time](https://en.wikipedia.org/wiki/Ergodicity#Measure-preserving_dynamical_systems). Here the measure actually represents a frequentist distribution of states over time, via [ergodicity](https://en.wikipedia.org/wiki/Ergodicity). However, we can freely put a uniform measure on the phase space of an arbitrary non-equilibrium process, where that measure represents sizes of phase regions and is used to quantify information gain. This doesn't, however, resolve the open problems in statistical mechanics and statistical thermodynamics, which have more to do with course-graining complexity. See https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics#Difference_between_equilibrium_and_non-equilibrium_thermodynamics and https://en.wikipedia.org/wiki/Renormalization_group.


