---
date: 2022-07-01
lastmod: '2022-07-01T17:11:33-07:00'
tags:
- machine-learning
title: Variational Bayesian Inference
---

What is variational Bayesian inference, a.k.a. variational Bayes? <!--more-->

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
\\newcommand{\\t}{\\theta}
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
\\newcommand{\\P}{\\Psi}
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
\\newcommand{\\F}{\\mc{E}}
$$




Further reading:
- {{< locallink "Variational Solomonoff Induction" "machine-learning" >}}
- https://en.wikipedia.org/wiki/Variational_Bayesian_methods
- [Variational Bayesian Inference with Stochastic Search](https://arxiv.org/abs/1206.6430)

For an explanation of what "variational" means here, see {{< locallink "Machine Learning Jargon - Variational Bayes" >}}.

## Bayesian Inference

First, we need to define the "Bayesian" paradigm. Bayesian inference operates in a paradigm (I would call this paradigm "Bayesian epistemology") where we have a set of hypotheses $\\mc{H}$ and a set of data sequences $\\X^\\infty$.

We we suppose we are given a distribution $p(h)$ over hypotheses, called the prior, and a family of distributions $p(x\_{1:n} \\mid h)$ over arbitrary length (finite) data sequence (for all $n,\\ x\_{1:n}$) indexed by hypotheses $h$. Each distribution $p(x\_{1:n} \\mid h)$ for a given $h$ called the likelihood of the data $x\_{1:n}$ under $h$. These two distributions together give us a full joint distribution $p(x\_{1:n}, h)=p(x\_{1:n} \\mid h)p(h)$.

We also suppose we observe a finite data sequence $x\_{1:n}$. There are then two probability distributions of interest, the data posterior $p(x\_{m:n+1} \\mid x\_{1:n})$ (for some $m > n$) and the hypothesis posterior $p(h \\mid x\_{1:n})$, which can be derived from the full joint distribution using the rules of probability (particularly the [chain rule](https://en.wikipedia.org/wiki/Chain_rule_(probability)), see {{< locallink "Deconstructing Bayesian Inference" "defining-bayesian-inference" >}}.)

It is important to stress that in this paradigm, $p(h)$ and $p(x\_{1:n}\\mid h)$ are not just known, but are chosen by the "user". This is the essential philosophical distinction between Bayesian inference and other sorts of statistical inference. The probabilities given here do not represent some objective description of reality. The Bayesian perspective is that there is no well-defined and objective probabilistic description of the world, i.e. these probabilities don't exist out there in the world. Instead these probabilities represent the user's beliefs about the world (specifically, uncertainty about the world relative to the "user"). Then the data posterior is the user's prediction about the future data given beliefs and past data, and the hypothesis posterior is the user's current state of belief given the prior and past data.


In this paradigm data is streamed to the user over time, so that $n$ keeps growing. However, hypotheses are never directly observed. As more data comes in, the user's hypothesis posterior changes, corresponding to how the user's beliefs (probability assignment to hypotheses) changes as more data is observed.

## Variational Inference

In practice, calculating the posterior from the given joint distribution,

$$\\begin{aligned}p(h \\mid x\_{1:n}) &= \\frac{p(x\_{1:n},h)}{p(x\_{1:n})}
\\\\ &=\\frac{p(x\_{1:n},h)}{\\int\_{\\mc{H}} p(x\_{1:n},h)\\ \\d h}\\,,\\end{aligned}$$

is intractable because the integral in the denominator is intractable to approximate (a sum when $\\mc{H}$ is countable or finite). That integral, $p(x\_{1:n})=\\int\_{\\mc{H}} p(x\_{1:n},h)\\ \\d h$, is the marginal probability of the data, called the subjective data distribution. Again, this is not an objective probability of the data, but represents the users aggregate beliefs (prior-weighted average likelihood).

We can instead formulate this posterior calculation as an optimization problem and then find an approximate solution via numerical optimization (e.g. gradient descent). This is called a "variational" approximation of Bayesian inference (for now, don't worry about why it's call that).

To achieve this approximation, we define some family of distributions, $q\_\\t(h \\mid x\_{1:n})$, one for every $x\_{1:n}$ and $n\\in\\N$, parametrized by $\\t$ (I use $q$ instead of $p$ to signify a different probability distribution from $p(x\_{1:n}, h)$). We want to find $\\t$ s.t. $q\_\\t(h \\mid x\_{1:n})$ is as close as possible to $p(h \\mid x\_{1:n})$ for all $h$, $x\_{1:n}$ and $n\\in\\N$. That requires that we have a notion of distance between two probability distributions. [KL-divergence](https://en.wikipedia.org/wiki/Kullback–Leibler_divergence) serves as a suitable distance function, defined as

$$
\\kl{q\_\\t(h \\mid x\_{1:n})}{p(h \\mid x\_{1:n})} = \\int\_\\mc{H} q\_\\t(h \\mid x\_{1:n}) \\log\\par{\\frac{q\_\\t(h \\mid x\_{1:n})}{p(h \\mid x\_{1:n})}}\\ \\d h\\,,
$$

which is always non-negative, and $\\kl{q\_\\t(h \\mid x\_{1:n})}{p(h \\mid x\_{1:n})} = 0$ iff $q\_\\t(h \\mid x\_{1:n}) = p(h \\mid x\_{1:n})$.

(Note that there is no full joint $q\_\\t(h, x\_{1:n})$. We are only interested in distributions over hypotheses given various data sequences. Technically this is an abuse of notation and we should instead index these distributions by the data, like this, $q\_{\\t, x\_{1:n}}(h)$. But that notation tends to be more confusing and cluttered, so I am going with the former.)

Then, given observation $x\_{1:n}$, our optimization goal is

$$\\tilde{\\t} = \\argmin{\\t}\\kl{q\_\\t(h \\mid x\_{1:n})}{p(h \\mid x\_{1:n})}\\,.$$

However, this alone buys us nothing. If $p(h \\mid x\_{1:n})$ is intractable to calculate, then so is $\\kl{q\_\\t(h \\mid x\_{1:n})}{p(h \\mid x\_{1:n})}$.

We can get around this by instead considering a proxy objective which is minimized iff the target objective is minimized. In this case,

$$\\t^\* = \\argmin{\\t}\\Big\\{\\kl{q\_\\t(h\\mid x\_{1:n})}{p(h)} - \\E\_{h\\sim q\_\\t(h\\mid x\_{1:n})}\\left\[\\log p(x\_{1:n} \\mid h)\\right\]\\Big\\}\\,.$$

This expression involves only objects we are explicitly given, $p(h),\\ p(x\_{1:n} \\mid h)$ and $q\_\\t(h\\mid x\_{1:n})$, and thus we can assume these probabilities are readily obtainable. However, that expectation may still be intractable since it is another integral over hypotheses. If we can get away with approximating the expectation via Monte Carlo (MC) sampling, we are in business.

(If we are using gradient descent to minimize this objective, we need to "pass gradients" through the MC approximation of the expectation, which is a non-trivial proposition. We could employ tricks, such as the [reparametrization trick](https://gregorygundersen.com/blog/2018/04/29/reparameterization/) or the [log-derivative trick](https://danieltakeshi.github.io/2017/03/28/going-deeper-into-reinforcement-learning-fundamentals-of-policy-gradients/).)

We can see why that objective acts as a proxy with the following relationship. Letting $\\F(\\t;\\ x\_{1:n})$ be the target objective and $\\mc{L}(\\t;\\ x\_{1:n})$ be the proxy objective, we have

$$\\begin{aligned}
&\\F(\\t;\\ x\_{1:n}) + \\log\\par{1/p(x\_{1:n})} \\\\
&\\quad= \\kl{q\_\\t(h \\mid x\_{1:n})}{p(h \\mid x\_{1:n})} + \\log\\par{1/p(x\_{1:n})} \\\\
&\\quad= \\E\_{h\\sim q\_\\t(h \\mid x\_{1:n})}\\left\[\\log\\par{\\frac{q\_\\t(h\\mid x\_{1:n})}{p(h,x\_{1:n})}}\\right\] \\\\
&\\quad= \\kl{q\_\\t(h\\mid x\_{1:n})}{p(h)} - \\E\_{h\\sim q\_\\t(h \\mid x\_{1:n})}\\left\[\\log p(x\_{1:n} \\mid h)\\right\] \\\\
&\\quad= \\mc{L}(\\t;\\ x\_{1:n})\\,.
\\end{aligned}$$

Note that $\\log\\par{1/p(x\_{1:n})}$ is necessarily nonnegative and is constant w.r.t. $\\t$ (because $0\\leq p(x\_{1:n}) \\leq 1$). This implies
$$\\mc{L}(\\t;\\ x\_{1:n}) \\geq \\F(\\t;\\ x\_{1:n})$$
with equality iff $p(x\_{1:n}) = 1$. Pushing down the LHS then pushes down the RHS, and minimizing the LHS minimizes the RHS, making this a suitable proxy objective.

Since KL-divergence is [always non-negative](https://en.wikipedia.org/wiki/Gibbs%27_inequality#Gibbs'_inequality), then $\\F(\\t;\\ x\_{1:n})$ is non-negative, which means $\\mc{L}(\\t;\\ x\_{1:n})$ must also be non-negative. We can also see that from the definition of $\\mc{L}(\\t;\\ x\_{1:n})$, since it is the sum of a KL-divergence (always non-negative) and $-\\E\_{h\\sim q\_\\t(h \\mid x\_{1:n})}\\left\[\\log p(x\_{1:n} \\mid h)\\right\]=\\E\_{h\\sim q\_\\t(h \\mid x\_{1:n})}\\left\[\\log \\par{1/p(x\_{1:n} \\mid h)}\\right\]$ which is also non-negative because $0\\leq p(x\_{1:n} \\mid h)\\leq 1$ for all $h$.

Another way to show that $\\mc{L}(\\t;\\ x\_{1:n})$ is a proxy objective for $\\F(\\t;\\ x\_{1:n})$ is by rewriting their relationship as 

$$
\\F(\\t;\\ x\_{1:n}) - \\mc{L}(\\t;\\ x\_{1:n}) = \\log p(x\_{1:n}) = \\text{constant}\\,.
$$

Then pushing down $\\mc{L}(\\t;\\ x\_{1:n})$ must also push down $\\F(\\t;\\ x\_{1:n})$ since their gap is constant w.r.t. $\\t$.


Under the variational inference scheme, we would train a new model $q\_\\t(h\\mid x\_{1:n})$ (e.g. a neural network) every time $n$ increases and we have new data, by minimizing the loss $\\mc{L}(\\t;\\ x\_{1:n})$ w.r.t. $\\t$ (e.g. using gradient descent). (A NN can act as a probability distribution if it outputs the parameters of some common probability distribution, like a Gaussian or categorical distribution.)

