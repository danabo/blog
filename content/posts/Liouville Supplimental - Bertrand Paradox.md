---
date: 2022-04-05
lastmod: '2022-04-06T15:42:46-07:00'
tags:
- thermodynamics
- physics
title: 'Liouville Supplimental: Bertrand Paradox'
---

I reframe the [Bertrand paradox](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)) as the statement that uniformity of measure is relative to choice of coordinate system.

The objective-Bayesian approach to the  [problem of priors](https://en.wikipedia.org/wiki/Bayesian_epistemology#Problem_of_priors) is to assign a maximally uninformative prior to the given possibility space. What is considered maximally uninformative can be derived with the [maximum entropy principle](https://en.wikipedia.org/wiki/Principle_of_maximum_entropy) - a generalization of the [principle of indifference](https://en.wikipedia.org/wiki/Principle_of_indifference#Application_to_continuous_variables). In many cases this ends up being a uniform prior. However, we run into a problem since uniformity is relative to choice of coordinates. This is relevant to physics since there is no preferred coordinate system to work in.

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
\\newcommand{\\b}{\\beta}
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
\\newcommand{\\r}{\\rho}
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


---

A measure is **uniform** if its corresponding density function is constant. We need to specify which coordinate system the density is constant with respect to.

In the Bertrand paradox, we are asked to randomly draw chords (a line connecting two points on the circumference of a circle) from the unit circle. The paradox is that depending on how we construct our chords, the sampling statistics of the chords will be different. Is it implied that the phrase "random draw" implies a uniform sampling distribution.

We are given three different sampling methods as a demonstration.
1. Pick two points on the circumfrence and draw a chord
2. Pick a radius (angle of the radius) and a point on the radius and draw a chord perpendicular to the radius
3. Pick a point in the circle and make that the midpoint of the chord


We can reframe these sampling methods as different coordinate systems over the same space of chords:
1. $(\\a, \\b) \\in \\set{(\\a',\\b')\\in\[0,2\\pi)^2 \\mid \\b' \\geq \\a'}$
2. $r \\in (0,1\],\\ \\th \\in \[0,2\\pi)$
3. $(x, y) \\in \\overline{B}\_1(0,0) = \\set{(x',y') \\in \\R^2 \\mid x'^2+y'^2 \\leq 1}$


Let's calculate the Jacobians for some of the transformations between these coordinates.

$(1 \\longrightarrow 2)$
$\\th(\\a,\\b)=\\frac{\\a+\\b}{2}$
$r(\\a,\\b)=\\sqrt{\\frac{1}{2}+\\frac{1}{2}\\cos(\\b-\\a)}$
([Law of cosines](https://en.wikipedia.org/wiki/Law_of_cosines),  where $c$ is the chord length and $r^2 = 1-(c/2)^2$)
$$\\begin{aligned}
\\pdiff{(\\th,r)}{(\\a,\\b)}&=\\det\\pmatrix{\\pdiff{\\th}{\\a}&\\pdiff{\\th}{\\b}\\\\\\pdiff{r}{\\a}&\\pdiff{r}{\\b}}\\\\&=\\det\\pmatrix{\\frac{1}{2}&\\frac{1}{2}\\\\ -\\frac{\\sin (\\alpha -\\beta )}{2^{3/2} \\sqrt{\\cos (\\alpha -\\beta )+1}} & \\frac{\\sin (\\alpha -\\beta )}{2^{3/2} \\sqrt{\\cos (\\alpha -\\beta )+1}}}\\\\&=\\frac{\\sin (\\alpha -\\beta )}{2^{3/2} \\sqrt{\\cos (\\alpha -\\beta )+1}}
\\end{aligned}$$

$(2 \\longrightarrow 3)$
$x(r,\\th) = r\\cos\\th$
$y(r,\\th) = r\\sin\\th$
$$\\begin{aligned}
\\pdiff{(x,y)}{(\\th,r)}&=\\pdiff{(x,y)}{(r,\\th)}\\\\&=\\det\\pmatrix{\\pdiff{x}{r}&\\pdiff{x}{\\th}\\\\\\pdiff{y}{r}&\\pdiff{y}{\\th}}\\\\&=\\det\\pmatrix{\\cos\\th & -r\\sin\\th \\\\ \\sin\\th & r\\cos\\th} \\\\&= r\\cos^2\\th + r\\sin^2\\th \\\\&= r
\\end{aligned}$$

$(1 \\longrightarrow 3)$
$x(\\a,\\b)=r\\cos\\th=\\sqrt{\\frac{1}{2}+\\frac{1}{2}\\cos(\\b-\\a)}\\cdot \\cos\\tup{\\frac{\\a+\\b}{2}}$
$y(\\a,\\b)=r\\sin\\th=\\sqrt{\\frac{1}{2}+\\frac{1}{2}\\cos(\\b-\\a)}\\cdot \\sin\\tup{\\frac{\\a+\\b}{2}}$
$$\\begin{aligned}
\\pdiff{(x,y)}{(\\a,\\b)}&=\\pdiff{(\\th,r)}{(\\a,\\b)}\\cdot\\pdiff{(x,y)}{(\\th,r)}\\\\&=\\frac{\\sin (\\alpha -\\beta )}{2^{3/2} \\sqrt{\\cos (\\alpha -\\beta )+1}}\\cdot r\\\\&=\\frac{\\sin (\\alpha -\\beta )}{2^{3/2} \\sqrt{\\cos (\\alpha -\\beta )+1}} \\cdot \\sqrt{\\frac{1}{2}+\\frac{1}{2}\\cos(\\b-\\a)} \\\\&= \\frac{1}{4} \\sin (\\alpha -\\beta )
\\end{aligned}$$


Inverse Jacobians are just reciprocals, so $\\pdiff{(\\a,\\b)}{(x,y)}=1/\\pdiff{(x,y)}{(\\a,\\b)}$ and $\\pdiff{(r,\\th)}{(x,y)}=1/\\pdiff{(x,y)}{(r,\\th)}$.
Swapping variables negates the Jacobian, so $\\pdiff{(r,\\th)}{(\\a,\\b)}=-\\pdiff{(\\th,r)}{(\\a,\\b)}$.


Useful coordinate relationships:
$r = \\sqrt{x^2+y^2}$
$\\frac{1}{4} \\sin (\\alpha -\\beta ) = \\frac{1}{2} \\sqrt{x^2+y^2}\\sqrt{1-x^2-y^2}$


Let $\\l\_1$ be a uniform measure in coordinate #1 with constant density $\\r\_1$.
Let $\\l\_2$ be a uniform measure in coordinate #2 with constant density $\\r\_2$.
Let $\\l\_3$ be a uniform measure in coordinate #3 with constant density $\\r\_3$.

If $R$ is a set of points in Cartesian coordinates (#3), let $\\vtup{r,\\th}(R) = \\set{(r(x,y),\\th(x,y)) \\mid (x,y) \\in R}$ and $\\vtup{\\a,\\b}(R) = \\set{(\\a(x,y),\\b(x,y)) \\mid (x,y) \\in R}$ be the transformed set into the other coordinate systems.

The measure of a set $R$ in Cartesian coordinates (#3), according to each measure $\\l\_1,\\l\_2$ and $\\l\_3$, is
$$
\\l\_3(R) = \\int\_R \\r\_3\\ \\dd x\\ \\dd y
$$

$$\\begin{aligned}
\\l\_2(R) &= \\int\_{\\vtup{r,\\th}(R)} \\r\_2\\ \\dd r\\ \\dd \\th \\\\&= \\int\_R \\r\_2\\abs{\\pdiff{(r,\\th)}{(x,y)}}\\ \\dd x\\ \\dd y \\\\&= \\int\_R \\frac{\\r\_2}{r}\\ \\dd x\\ \\dd y \\\\&=\\int\_R \\frac{\\r\_2}{\\sqrt{x^2+y^2}}\\ \\dd x\\ \\dd y 
\\end{aligned}$$

$$\\begin{aligned}
\\l\_1(R) &= \\int\_{\\vtup{\\a,\\b}(R)} \\r\_1\\ \\dd \\a\\ \\dd \\b \\\\&= \\int\_R \\r\_1\\abs{\\pdiff{(\\a,\\b)}{(x,y)}}\\ \\dd x\\ \\dd y \\\\&= \\int\_R \\frac{4\\r\_1}{\\sin (\\alpha -\\beta )}\\ \\dd x\\ \\dd y \\\\&=\\int\_R \\frac{2\\r\_1}{\\sqrt{x^2+y^2}\\sqrt{1-x^2-y^2}}\\ \\dd x\\ \\dd y
\\end{aligned}$$



Thus the density function for $\\l\_1$ in Cartesian is $\\tilde{\\r}\_1(x,y)=\\frac{2\\r\_1}{\\sqrt{x^2+y^2}\\sqrt{1-x^2-y^2}}$ and the density function for $\\l\_2$ in Cartesian is $\\tilde{\\r}\_2(x,y)=\\frac{\\r\_2}{\\sqrt{x^2+y^2}}$. The measures $\\l\_1$ and $\\l\_2$ have non-constant density functions in Cartesian coordinates, and so are non-uniform in Cartesian coordinates. Clearly what is considered a random draw depends on our choice of coordinates.


