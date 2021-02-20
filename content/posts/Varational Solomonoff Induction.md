---
date: '2021-02-20T10:16:45-06:00'
draft: false
tags:
- free energy
title: Varational Solomonoff Induction
---

$$
\\newcommand{\\mb}{\\mathbb}
\\newcommand{\\mc}{\\mathcal}
\\newcommand{\\E}{\\mb{E}}
\\newcommand{\\B}{\\mb{B}}
\\newcommand{\\R}{\\mb{R}}
\\newcommand{\\kl}[2]{D\_{KL}\\left(#1\\ \\| \\ #2\\right)}
\\newcommand{\\argmin}[1]{\\underset{#1}{\\mathrm{argmin}}\\ }
\\newcommand{\\argmax}[1]{\\underset{#1}{\\mathrm{argmax}}\\ }
\\newcommand{\\abs}[1]{\\left\\lvert#1\\right\\rvert}
\\newcommand{\\set}[1]{\\left\\{#1\\right\\}}
\\newcommand{\\ve}{\\varepsilon}
\\newcommand{\\t}{\\theta}
\\newcommand{\\T}{\\Theta}
\\newcommand{\\o}{\\omega}
\\newcommand{\\O}{\\Omega}
\\newcommand{\\sm}{\\mathrm{softmax}}
$$



The [free energy principle](https://en.wikipedia.org/wiki/Free_energy_principle) is a [variational Bayesian method](https://en.wikipedia.org/wiki/Variational_Bayesian_methods) for approximating posteriors. Can free energy minimization combined with program synthesis methods from machine learning tractably approximate [Solomonoff induction](https://en.wikipedia.org/wiki/Solomonoff%27s_theory_of_inductive_inference) (i.e. universal inference)? In these notes, I explore what the combination of these ideas looks like.

# Machine learning
I want to make an important clarification about "Bayesian machine learning". First, I'll briefly define some "modes" of machine learning.

 In parametric machine learning, we have a function $f\_\\t$ parametrized by $\\t\\in\\T$. Let $q\_\\t(D)$ be a probability distribution on datasets $D$ defined in terms of $f\_\\t$. For supervised learning, $q\_\\t(D) = \\prod\_{(x,y)\\in D} Pr(y; f\_\\t(x))$ is the product of probabilities of each target $y$ given distribution parameters $f\_\\t(x)$, e.g. $f\_\\t(x)$ returns the mean and variance of a Gaussian over $y$. For unsupervised learning, $f\_\\t(x)$ might return a real number which serves as the log-probability of each $x \\in D$. In general $f\_\\t$ can be any kind of parametric ML model, but these days it is likely to be a neural network.

Typical usage "modes" of $q\_\\t$ in machine learning:
- **MLE** ([maximum likelihood](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)): Training produces hypothesis with highest data likelihood.
    - $\\t\\in\\T$ is a hypothesis.
    - $\\t^\* = \\argmax{\\t}\\log q\_\\t(D)$ for dataset $D$.
- **MAP** ([maximum a posteriori](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation)): Training produces model with highest posterior probability.
    - $\\t\\in\\T$ is a hypothesis.
    - $\\t^\* = \\argmax{\\t}\\left[\\log q\_\\t(D) + \\log p(\\t)\\right]$ for dataset $D$ and prior $p(\\t)$.
    - $\\log p(\\t)$ can be viewed as a [regularizer](https://en.wikipedia.org/wiki/Regularization_(mathematics)). MAP is just MLE plus regularization - the most typical form of parametric machine learning.
- **Bayesian Inference**: Prior over the parameter induces a posterior over parameters given data. 
    - $\\t\\in\\T$ is a hypothesis.
    - $p(\\t \\mid D) = \\frac{q\_\\t(D) p(\\t)}{\\int\_\\T q\_\\t(D) p(\\t) d\\t}$ is the exact posterior on hypotheses $\\T$ given dataset $D$.
    - Unlike in MLE and MAP, there is no notion of optimal parameter $\\t^\*$. Instead we have much more information: $p(\\t \\mid D)$ "scores" every parameter in $\\T$, and all the scores taken together constitute our information.
- **Variational Bayes** (free energy minimization): training produces a (approximate) posterior distribution over hypotheses.
    - $z \\in \\mc{Z}$ is a hypothesis.
    - $\\tilde{\\t} = \\argmin{\\t}\\kl{q\_\\t(z)}{p(z \\mid D)}$ is the target parameter for dataset $D$ and model $p(D,z)$. This is assumed to be intractable to find.
    - $\\t^\* = \\argmin{\\t}\\kl{q\_\\t(z)}{p(z)} - \\E\_{z\\sim f\_\\t(z)}\\left[\\lg p(D \\mid z)\\right]$ is the approximation. This is what we find through optimization.

The variational Bayes "usage mode" is clearly different from the others. MLE and MAP are fitting $f\_\\t$ to the data, i.e. finding a single $\\t^\*\\in\\T$ that maximizes the probability of the data under $q\_\\t$. Bayesian inference is finding a distribution $p(\\t \\mid D)$ on $\\T$ which represents the model's beliefs about various parameters $\\t\\in\\T$ being likely or unlikely as explanations of the data. This is not the same as fitting $f\_\\t$ to data, since we are not choosing any particular parameter in $\\T$. Variational Bayes uses $q\_{\\t^\*}$ as an approximation of $p(\\t \\mid D)$, where $\\t^\*\\in\\T$ is the optimal parameter of distribution $q\_\\t(z)$ and $z\\in\\mc{Z}$ is a hypothesis.

In the first three modes, $\\T$ are hypotheses and we are either selecting one or finding a distribution over them. In the variational Bayes mode, $\\T$ are not hypotheses. Instead we introduce $\\mc{Z}$ as the hypothesis space and $\\T$ is the parameter space for the approximate posterior $q\_\\t(z)$ on $\\mc{Z}$, i.e. $q\_\\t(z)$ approximates $p(z\\mid D)$. We don't have $\\mc{Z}$ in the first three modes, and we are interested in $p(\\t \\mid D)$ rather than $p(z \\mid D)$. Also in the first three modes, $q\_\\t(D)$ is a distribution on what is observed, datasets $D$, rather than over latent $\\mc{Z}$.

## What is Bayesian machine learning?

Conventionally, a Bayesian model has a prior probability distribution over it's parameters, and inference involves finding posterior distributions. This corresponds to the Bayesian inference mode above. Out of the four modes, MLE is definitively non-Bayesian. MAP might be called semi-Bayesian, simply because there is a prior on parameters $p(\\t)$, but only the argmax of the posterior is being found, rather than a full posterior. The variational Bayes mode is where things get wonky. There are two models: $q\_\\t(z)$ and $p(z, D)$. The first is parametrized and is optimized greedily with something like gradient descent, as in the MLE or MAP cases. The second is Bayesian. 

Is variational Bayes a Bayesian ML method? In one sense yes, in another sense no. It's efficacy depends on $q\_\\t(z)$ being a good approximation of the posterior $p(z \\mid D)$, and whether $q\_\\t(z)$ is a good approximation depends on the efficacy of the chosen machine learning method (e.g. neural networks trained with gradient descent). I'd expect $q\_\\t(z)$ to be a non-Bayesian model (If it were Bayesian, how then do you tractably approximate it? That is the very thing we are trying to do with $p(z, D)$.) So then the efficacy of variational Bayes comes down to the properties of non-Bayesian machine learning. If at the end of the day, point-estimates of parameters are always doing the heavy lifting (i.e. generalizing well), why be Bayesian in the first place?

# Solomonoff induction
I learned about this topic from [An Introduction to Kolmogorov Complexity and Its Applications](https://www.springer.com/gp/book/9781489984456) and [Universal Artificial Intelligence](http://www.hutter1.net/ai/uaibook.htm). I recommend both books as references.

There are different formulations of Solomonoff induction, each utilizing a hypothesis space containing all programs - but different kinds of programs for each formulation. I outline three of them: [#Version 1](#version-1), [#Version 2](#version-2), [#Version 3](#version-3). Only an understanding of [#Version 2](#version-2) is needed for the subsequent sections.

## Notation

Let $\\B = \\{0,1\\}$ be the binary alphabet, $\\B^n$ be the set of all length-$n$ binary strings, and $\\B^\\infty$ be the set of all infinite binary strings.

Let $\\B^\* = \\B^0 \\times \\B^1 \\times \\B^2 \\times \\B^3 \\times\\ldots$ be the set of all finite binary strings of any length.
$\\epsilon$ is the empty string, i.e. $\\B^0 = \\{\\epsilon\\}$.

Let $x \\sqsubseteq y$ denote that binary string $x$ is a prefix of (or equal to) binary string $y$.
Let $x\`y$ denote the string concatenation of $x$ and $y$.
Let $x\_{a:b}$ denote the slice of $x$ from position $a$ to $b$ (inclusive).
Let $x\_{<n} = x\_{1:n-1}$ denote the prefix of $x$ up to $n-1$.
Let $x\_{>n} = x\_{n+1:\\infty}$ denote the "tail" of $x$ starting from $n+1$.

## Version 1
Let $U$ be a universal machine, i.e. if $z\\in\\B^\*$ is a program then $U(z) \\in \\B^\*$ is some binary string, or $U(z)$ is undefined because $U$ does not halt on $z$. We do not give program $z$ input, but $z$ can include "data", in the sense that it's program specifies a binary string that gets loaded into memory when the program starts.

Let $p(z)$  be a prior on finite binary strings.
Then for observation $x \\in \\B^\*$,
- $p(x \\mid z) = \\begin{cases}1 & x \\sqsubseteq U(z) \\\\ 0 & \\mathrm{otherwise}\\end{cases}$
- $p(z, x) = p(x \\mid z)p(z) = \\begin{cases}p(z) & x \\sqsubseteq U(z) \\\\ 0 & \\mathrm{otherwise}\\end{cases}$
- $p(x) = \\sum\_{z\\in\\B^\*} p(x,z) = \\sum\_{z \\in \\B^\*;\\ x \\sqsubseteq U(z)} p(z)$
- $p(z \\mid x) = p(z, x)/p(x) = \\begin{cases}p(z)/p(x) & x \\sqsubseteq U(z) \\\\ 0 & \\mathrm{otherwise}\\end{cases}$

$p(x)$ is the data probability.
$p(z)$ is the prior.
$p(z\\mid x)$ is the posterior.

If we observe $x \\in \\B^\*$, we may ask for the probability of subsequently observing some $y\\in\\B^\*$:

$$
\\begin{aligned}
p(y \\mid x) &= \\frac{1}{p(x)}\\sum\_{z\\in\\B^\*}p(x\`y,z) \\\\
&= \\frac{1}{p(x)}\\sum\_{z \\in \\B^\*;\\ x\`y \\sqsubseteq U(z)} p(z) \\\\
&= \\sum\_{z \\in \\B^\*;\\ x\`y \\sqsubseteq U(z)} p(z \\mid x)\\,.
\\end{aligned}
$$

What prior $p(z)$ should we choose? Solomonoff recommends 

$$
p(z) = 2^{-\\ell(z)}
$$

where $\\ell(z)$ is the length of program $z$. This has the effect of putting more prior probability on short programs, essentially encoding a preference for "simple" explanations of the data. This prior also has the benefit that it is fast to calculate $p(z)$ for any $z$. In general, choice of prior is a matter of taste, and should depend on practical considerations like tractability and regularizations such as "simplicity".

## Version 2

Let $\\mu$ be a probability measure on $\\B^\\infty$, meaning $\\mu$ maps (measurable) subsets of $\\B^\\infty$ to probabilities. $\\mu$ can be specified by defining it's value on the **cylinder sets** $\\Gamma\_x = \\set{\\o \\in \\B^\\infty \\mid x \\sqsubset \\o}$ for every $x\\in\\B^\*$, i.e. the set of all infinite binary strings starting with $x$. I'll let $\\mu(x)$ be a shorthand denoting $\\mu(\\Gamma\_x)$. Then $\\mu(x)$ is the probability of finite string $x$. For any such measure $\\mu$, it must be the case that

$$
\\mu(x) = \\mu(x\`0) + \\mu(x\`1)\\,,
$$

and

$$
\\mu(x) \\geq \\mu(x\`y)\\,,
$$

for all $x,y\\in\\B^\*$.

$\\mu$ is a **semimeasure** iff it satisfies

$$
\\mu(x) \\geq \\mu(x\`0) + \\mu(x\`1)
$$

for all $x \\in \\B^\*$. That is to say, if $\\mu$ is a semimeasure then probabilities may sum to less than one (this is like supposing that some probability goes missing).

The following are equivalent:
- $\\mu$ is **computable**
- There exists some program which computes the probability $\\mu(x)$ for all inputs $x$.
- There exists some program which outputs $x$ with probability $\\mu(x)$ (for all $x$) when given uniform random input bits.

$\\mu$ is **semicomputable** (a.k.a. enumerable) if there exists some program which approximates the probability $\\mu(x)$ (for all $x$) by outputting a sequence of rational numbers $\\set{\\hat{p}\_n}$ approaching $\\mu(x)$, but where it is impossible to determine how close the sequence is to $\\mu(x)$ at any point in time. That is to say, you cannot know the error sequence $\\varepsilon\_n = \\abs{\\mu(x) - \\hat{p}\_n}$, but you know that $\\varepsilon\_n \\to 0$ as $n\\to\\infty$. In contrast, if $\\mu$ is computable then there exists a program that outputs both the sequence of rationals $\\set{\\hat{p}\_n}$ AND the errors $\\set{\\varepsilon\_n}$ (computability implies there exists a program that takes a desired error $\\varepsilon>0$ as input and outputs in finite time (i.e. halts) the corresponding approximation $\\hat{p}$ s.t. $\\varepsilon>\\abs{\\mu(x)-\\hat{p}}$).

Let $\\mc{M}$ be the set of all semicomputable semimeasures on infinite binary sequences. Let $p(\\mu)$ be a prior on $\\mc{M}$.

Then for observation $x \\in \\B^\*$,
- $p(x \\mid \\mu) = \\mu(x)$
- $p(x, \\mu) = p(x \\mid \\mu)p(\\mu) = p(\\mu)\\mu(x)$
- $p(x) = \\sum\_{\\mu \\in \\mc{M}} p(x \\mid \\mu) = \\sum\_{\\mu \\in \\mc{M}} p(\\mu)\\mu(x)$
- $p(\\mu \\mid x) = p(\\mu)\\frac{\\mu(x)}{p(x)}$

$p(x)$ is the data probability.
$p(\\mu)$ is the prior.
$p(\\mu\\mid x)$ is the posterior.

If we observe $x \\in \\B^\*$, we may ask for the probability of subsequently observing some $y\\in\\B^\*$:

$$
\\begin{aligned}
p(y \\mid x) &= \\sum\_{\\mu \\in \\mc{M}} p(y,\\mu\\mid x) \\\\
&= \\sum\_{\\mu \\in \\mc{M}} p(\\mu\\mid x)\\mu(y \\mid x) \\\\
&= \\sum\_{\\mu \\in \\mc{M}}p(\\mu)\\frac{\\mu(x)}{p(x)}\\mu(y\\mid x)\\,.
\\end{aligned}
$$

$\\mc{M}$ is all semicomputable semimeasures, rather than all computable measures, because the former is a decidable set while the latter is not, i.e. in practice the former set of hypotheses can be feasibly enumerated by enumerating all programs, while the latter cannot be. If we required only measures, then we could not decide which programs produced proper measures (if the program doesn't halt on $x$, that is like saying the probability that would have gone to strings starting with $x$ "disappears"). Allowing non-halting programs means we don't have to filter out programs which don't halt. Similar issue for computable vs semicomputable.

Versions 1 and 2 are equivalent. That is to say, we can get the same data distribution $p(x)$ for the right choice of prior in each version.

A typical choice of the prior in this version is

$$
p(\\mu) = 2^{-K(\\mu)}
$$

where $K(\\mu)$ is the [**prefix-free Kolmogorov complexity**](https://www.math.wisc.edu/~jmiller/Notes/contrasting.pdf) of $\\mu$, i.e. the length of the shortest program that (semi)computes $\\mu$ (given a space of prefix-free programs, i.e. program strings contain their own length information).

## Version 3

As you might guess, this will also turn out to be (sorta) equivalent to the first two versions. This is like version 2, except instead of considering a hypothesis to be a program that samples data sequences given uniform random input bits, a hypothesis is such a program packaged together with a particular infinite input sequence. Thus, hypotheses are in a sense infinite programs.

Let $U$ be a **universal monotone machine**. That means $U$ can execute infinitely long programs in a streaming fashion by producing partial outputs as the program is read. Let $z \\in \\B^\\infty$. Then for every finite prefix $z\_{1:n}$, we get a partial output $U(z\_{1:n}) = \\o\_{1:m} \\in \\B^m$. We require that $U(z\_{1:n}) \\sqsubseteq U(z\_{1:n'})$ for $n \\leq n'$. The output of $z$ is infinite if $m\\to\\infty$ as $n\\to\\infty$, is finite if $m < \\infty$ for all $n$, or is undefined if $U$ does not halt on any $z\_{1:n}$.

Let $\\tilde{z}$ be a program that samples from $\\mu$ from version 2, i.e. $\\tilde{z}$ takes uniform random bits as input and outputs some $x\_{1:m}$ with probability $\\mu(x\_{1:m})$. Then we can produce an infinite "version 3" program by appending an infinitely long uniform random sequence $u$, i.e. $z = \\tilde{z}\`u$ where $U(\\tilde{z}) = \\epsilon$ (empty string, i.e. executing $\\tilde{z}$ outputs nothing), and $U(\\tilde{z}\`u\_{1:n'})$ outputs some prefix of $x$ (if we let $x$ be infinite) by running $\\tilde{z}$ on input $u\_{1:n'}$.

If we feed uniform random bits into $U$, then $U$ itself samples from a distribution over infinite data sequences. The induced distribution is $p(x\_{1:m})$ which is a Solomonoff distribution that we can use for universal inference. This is equivalent to putting a uniform prior on the infinite programs $\\B^\\infty$, i.e.

$$
p(z\_{1:n}) = 2^{-n}\\,.
$$

For partial observation $x\_{1:m} \\in \\B^\*$ (the remaining part of $x$ is the unobserved future),

$$
p(x\_{1:m}) = \\sum\_{\\zeta\\in\\Phi(x\_{1:m})} 2^{-\\ell(\\zeta)}\\,,
$$

where
- $\\ell(\\zeta)$ is the length of finite string $\\zeta$.
- $\\Phi(x\_{1:m})$ is a prefix-free set of all finite sequences $\\zeta$ which output at least $x\_{1:m}$ when fed into $U$ (i.e. for all $z\_{1:n} \\in \\B^\*$ if $x\_{1:m} \\sqsubseteq U(z\_{1:n})$ then $z\_{1:n} \\in \\bigcup\_{\\zeta\\in\\Phi(x\_{1:m})} \\Gamma\_\\zeta$).
 
To calculate $p(x\_{1:m})$, we ostensibly want to sum up the prior probabilities of all programs which output at least $x\_{1:m}$, but remember that our programs are infinitely long, and the prior probability of any infinite program is 0 (because $2^{-n}\\to 0$ as $n\\to\\infty$). The sum above performs a [Lebesgue integral](https://en.wikipedia.org/wiki/Lebesgue_integration) over the infinite programs $\\B^\\infty$ by dividing them into "intervals" (i.e. sets of programs sharing the same prefix - geometrically an interval if you consider an infinite binary sequence to be a real number between 0 and 1) and summing up the lengths (prior probabilities) of the intervals. The function $\\Phi$ is a convenient construction for producing this set of intervals for us. Finding $\\Phi(x\_{1:m})$ is complex, and not especially important to go into.

The joint distribution is

$$p(x\_{1:m}, z\_{1:n}) = \\sum\_{\\zeta\\in\\Phi(x);\\ z\_{1:n}\\sqsubseteq\\zeta} 2^{-\\ell(\\zeta)}\\,.$$

From here, we can straightforwardly compute the probability of the data under partial hypothesis $z\_{1:n}$:

$$p(x\_{1:m} \\mid z\_{1:n}) =p(x\_{1:m}, z\_{1:n})/p(z\_{1:n}) = \\sum\_{\\zeta\\in\\Phi(x);\\ z\_{1:n}\\sqsubseteq\\zeta} 2^{n-\\ell(\\zeta)}\\,.$$

And finally the data posterior of the future slice $x\_{m:s}$ given $x\_{<m}$ (for $m<s$):

$$
p(x\_{m:s}\\mid x\_{<m}) = \\frac{1}{p(x\_{<m})}\\sum\_{\\zeta\\in\\Phi(x\_{1:s})} 2^{-\\ell(\\zeta)}\\,.
$$

# Variational Solomonoff induction

Suppose we observe finite sequence $x\_{1:t} \\in \\B^\*$ and we want to find the posterior $p(h \\mid x\_{1:t})$. Usually this is intractable to calculate, and in the case of Solomonoff induction, the posterior is not even computable. We can get around this limitation by approximating the posterior with a parametrized distribution $q\_\\t(h)$ over hypotheses $h\\in\\mc{H}$. For now I will be agnostic as to what kind of hypothesis space $\\mc{H}$ is, and it can be any of the hypothesis spaces discussed above: [#Version 1](#version-1), [#Version 2](#version-2), [#Version 3](#version-3).

In this case, let's find $\\t^\*\\in\\T$ that minimizes the KL-divergence $\\kl{q\_\\t(h)}{p(h\\mid x\_{1:t})}$ so that $q\_\\t(h)$ is as close as possible to $p(h\\mid x\_{1:t})$. Note that $q\_\\t(h)$ does not depend on $x\_{1:t}$ because we find $\\t^\*$ after $x\_{1:t}$ is already observed ($x\_{1:t}$ is like a constant w.r.t. this optimization), whereas the joint distribution $p(h, x)$ is defined up front before any data is observed.

However, if $p(h \\mid x\_{1:t})$ is intractable to calculate, then so is $\\kl{q\_\\t(h)}{p(h\\mid x\_{1:t})}$. With a few tricks, we can find an alternative optimization target that is tractable. Rewriting the KL-divergence:

$$
\\begin{aligned}
&\\kl{q\_\\t(h)}{p(h\\mid x\_{1:t})} \\\\
&\\quad= \\E\_{h \\sim q\_\\t}\\left[\\lg\\left(\\frac{q\_\\t(h)}{p(h\\mid x\_{1:t})}\\right)\\right] \\\\
&\\quad= \\E\_{h \\sim q\_\\t}\\left[\\lg\\left(\\frac{q\_\\t(h)}{p(h)}\\right)-\\lg p(x\_{1:t} \\mid h) + \\lg p(x\_{1:t})\\right] \\\\
&\\quad= \\kl{q\_\\t(h)}{p(h)} - \\E\_{h\\sim q\_\\t}\\left[\\lg p(x\_{1:t} \\mid h)\\right] - \\lg \\frac{1}{p(x\_{1:t})} \\\\
&\\quad= \\mc{F}[q\_\\t] - \\lg \\frac{1}{p(x\_{1:t})} \\,.
\\end{aligned}
$$

where $\\mc{F}[q\_\\t]$ is defined as

$$
\\begin{aligned}
\\mc{F}[q\_\\t] &= \\kl{q\_\\t(h)}{p(h)} - \\E\_{h\\sim q\_\\t}\\left[\\lg p(x\_{1:t} \\mid h)\\right] \\\\
&= \\E\_{h \\sim q\_\\t}\\left[\\lg\\left(\\frac{q\_\\t(h)}{p(h)}\\right)-\\lg p(x\_{1:t} \\mid h)\\right] \\\\
&= \\E\_{h \\sim q\_\\t}\\left[\\lg\\left(\\frac{q\_\\t(h)}{p(h,x\_{1:t})}\\right)\\right]\\,.
\\end{aligned}
$$

$\\mc{F}[q\_\\t]$ is called the **variational free energy**. It depends explicitly on choice of parameter $\\t$, but also keep in mind it depends implicitly on the observation $x\_{1:t}$ and distribution $p(h, x\_{1:t})$.

Because $\\lg \\frac{1}{p(x\_{1:t})}$ (called the **surprise** of $x\_{1:t}$) is positive and constant (because observation $x\_{1:t}$ is constant), then minimizing $\\mc{F}[q\_\\t]$ to $\\lg \\frac{1}{p(x\_{1:t})}$ guarantees that $\\kl{q\_\\t(h)}{p(h\\mid x\_{1:t})}$ is 0 (KL-divergence cannot be negative), which in turn guarantees that $q\_\\t(h)$ and $p(h\\mid x\_{1:t})$ are equal distributions on $\\mc{H}$. If our optimization process does not fully minimize $\\mc{F}[q\_\\t]$, then $q\_\\t(h)$ will approximate $p(h\\mid x\_{1:t})$ with some amount of error.

The optimization procedure we want to perform is

$$
\\begin{aligned}
&\\argmin{\\t\\in\\T} \\mc{F}[q\_\\t] \\\\
=\\ & \\argmin{\\t\\in\\T} \\E\_{h \\sim q\_\\t}\\left[\\lg\\left(\\frac{q\_\\t(h)}{p(h,x\_{1:t})}\\right)\\right] \\\\
=\\ & \\argmax{\\t\\in\\T}\\set{ \\E\_{h \\sim q\_\\t}\\left[R(h)\\right] + \\mb{H}\_{h \\sim q\_\\t}[q\_\\t(h)]}
\\end{aligned}
$$

This now has the form of a one-timestep reinforcement learning objective, where $R(h) = \\lg p(h,x\_{1:t})$ is the reward for "action" $h$, and $\\mb{H}\_{h \\sim q\_\\t}[q\_\\t(h)]$ is the entropy of $q\_\\t(h)$. Here $q\_\\t(h)$ is called the **policy**, i.e. the distribution actions are sampled from. Maximizing this objective jointly maximizes expected reward under the policy and entropy of the policy. An entropy term is typically added to RL objectives as a regularizer to encourage exploration (higher entropy policy means more random actions), but in this case the entropy term comes included.

We can use standard [policy gradient methods](https://lilianweng.github.io/lil-log/2018/04/08/policy-gradient-algorithms.html) (e.g. [IMPALA](https://deepmind.com/research/publications/impala-scalable-distributed-deep-rl-importance-weighted-actor-learner-architectures)) to maximize the above RL objective (equivalent to minimizing free energy), so long as $q\_\\t(h)$ is fast to sample from, and the reward $R(h) = \\lg p(h,x\_{1:t})$ is fast to compute. We can control both.

# Tractability
Tractability depends on our choice of $\\mc{H}$ and prior $p(h)$. What operations do we want to be tractable? Typically we want:
1. To approximate hypothesis posteriors: $q\_{\\t^\*}(h) \\approx p(h \\mid x\_{1:t})$.
2. To approximate predictive data distributions (data posterior): $p(x\_{>t} \\mid x\_{1:t})$.

## Hypothesis posterior
The approximation $q\_{\\t^\*}(h)$ allows us to do this. The tractability of finding a good parameter $\\t^\*$ for $q$ using policy gradient methods will require that the reward $R(h) = \\lg p(h,x\_{1:t})$ is fast to calculate.

We can write the reward as the sum of two terms:

$$
\\lg p(h,x\_{1:t}) = \\lg p(h) + \\lg p(x\_{1:t} \\mid h)\\,.
$$

Then we need fast calculation of prior probabilities $p(h)$, and data probabilities under hypotheses, $p(x\_{1:t} \\mid h)$.

## Data posterior
We want to approximate $p(y \\mid x)$, i.e. the probability of observing string $y$ after observing $x$. This is similar to the problem of calculating $p(x)$, the data probability.

$$
p(x) = \\E\_{h\\sim p(h)} [p(x\\mid h)]\\,.
$$

If it were fast to compute $p(x\\mid h)$ for a given $h$, and fast to sample from the prior $p(h)$, then we can approximate the data probability with Monte Carlo sampling:

$$
p(x) \\approx \\hat{p}(x) = \\sum\_{h \\in H^{(k)}} p(x\\mid h)
$$

where $H^{(k)} = \\set{h\_1, h\_2, \\ldots, h\_k} \\sim p(h)$ is an i.i.d. sample from $p(h)$ of size $k$.

In the same way, we can approximate the data posterior using the identity

$$
p(y \\mid x) = \\E\_{h\\sim p(h \\mid x)} [p(y\\mid x, h)]\\,.
$$

The Monte Carlo approximation is:

$$
p(y\\mid x) \\approx \\hat{p}(y\\mid x) = \\sum\_{h \\in H^{(k)}} p(y\\mid x, h)
$$

where $H^{(k)} = \\set{h\_1, h\_2, \\ldots, h\_k} \\sim q\_{\\t^\*}(h)$ is an i.i.d. sample drawn from the optimized approximate posterior $q\_{\\t^\*}(h)$. So approximating the data posterior requires approximating the hypothesis posterior.

$p(y\\mid x, h)$ is the conditional data distribution under hypothesis $h$. If $h$ is a probability measure, then $p(x \\mid h) = h(x)$ and $p(y\\mid x, h) = h(y\\mid x)$.

For approximating the data distribution, we need fast sampling from hypothesis priors $p(h)$ and fast data-under-hypothesis probabilities $p(x \\mid h)$.

For approximating the data posterior, we need fast approximate posteriors $q\_{\\t^\*}(h)$, and we need hypothesis data-conditionalization $p(y\\mid x, h)$ to be fast.

## Generalization

Speed is necessary but not sufficient for tractability. The approximations we find need to be good ones. Choosing an appropriate model $q$, which is a distribution over programs, is within the realm of program synthesis and machine learning. These days, program synthesis is done with neural language models on code tokens.

Can neural networks approximate the true posterior $p(h \\mid x)$? This is a generalization problem. The optimized generative model on programs, $q\_{\\t^\*}(h)$, will have been trained on finitely many programs. Whether $q\_{\\t^\*}(h') \\approx p(h' \\mid x)$ for some program $h'$ unseen during training will depend entirely on the generalization properties of the particular program synthesizer that is used in $q\_\\t$.

The difficulty of applying machine learning to program synthesis is dealing with reward sparsity and generalizing highly non-smooth functions. To maximize reward $R(h) = \\lg p(h,x\_{1:t})$, the model $q$ needs to upweight programs $h$ that jointly have a high prior $p(h)$ and high likelihood $p(x\_{1:t} \\mid h)$. If the prior $p(h)$ is simple, perhaps $q$ can learn that function. On the other hand, if this prior encodes information about how long $h$ runs for (as I discuss in the [#Prior](#prior) section), the prior is then not even computable. Same for $p(x\_{1:t} \\mid h)$. Without actually running $h$ on $x\_{1:t}$, determining the output will not be possible in general. For $q$ to predict these things based on $h$'s code but without running $h$ is in general impossible. The function $p(h \\mid x\_{1:t})$ (as a function of $h$) highly chaotic, and we cannot expect $q$ to generalize in any strong sense. Innovations in program synthesis are still needed to do even somewhat well.

As a reinforcement learning problem, maximizing this reward suffers from sparsity issues. Most programs will be trivial, in the sense that they just output constant values, or nothing. I expect that Solomonoff induction doesn't start to become effective until you get to programs of moderate length that exhibit interesting behavior. In the context of this reinforcement learning problem, that means the policy $q$ needs to find moderately long programs with moderately high reward. When training first starts, it can take an excessive amount of episodes before any non-trivial reward is discovered. This can make reinforcement learning intractable. Innovations are needed here too.

# Choices
To summarize the requirements we found above:
Is there a choice of $\\mc{H}$ and $p(x,h)$ s.t.
- Prior $p(h)$ is fast to calculate and sample from.
- Approximate hypothesis posterior $q\_{\\t^\*}(h)$ is fast to sample from.
- Hypothesis data-probability $p(x\\mid h)$ is fast to calculate.
- Hypothesis data-conditionalization $p(y\\mid x, h)$ is fast to calculate.




## Program space
Hypotheses can be deterministic or stochastic. Deterministic hypotheses would be represented by deterministic programs. Stochastic hypotheses can either be represented by stochastic programs (output is non-deterministic) or by deterministic programs that output probabilities. I think we should choose the latter.

If our hypotheses are deterministic, then we get Solomonoff induction [#Version 1](#version-1). Conditionalization is easy because $p(y \\mid x, h) = p(y\`x \\mid h) = 1$ if $h$ outputs $x$ and $0$ otherwise. However, the vast majority of programs will not output $x$, so the reward $R(h) = \\lg p(h,x)$ will be very sparse. That is to say, the reward will be $-\\infty$ most of the time (in practice you would clip and scale the reward to something reasonable). This is bad for policy gradient methods and will result in high gradient variance (learning will be extremely slow).

We should use stochastic hypotheses. If we use non-deterministic programs, conditionalization is hard. Thus we should use programs that output their probabilities.

The choice of $\\mc{H}$ is equivalent to choosing a programming language plus syntax rules so that only valid programs can be constructed. In this case, we want to restrict ourselves to programs that will obey the properties of probability measures $\\mu$ on infinite sequences: $\\mu(x) = \\mu(x\`0) + \\mu(x\`1)$ and  $\\mu(x) \\geq \\mu(x\`y)$.

To ensure this, I propose that programs $h$ take the form of auto-regressive language models. That is to say these programs read in a sequence of input tokens and for each token output a vector of real numbers with the same length as the token space. Passing that vector through a softmax induces a probability distribution over the next input token. The programs maintain their own internal state. A language should be chosen such that all generated programs can be guaranteed to take this form.

If the program has output probabilities $\\hat{p}\_1, \\ldots, \\hat{p}\_t$ for input $x\_{1:t}$ but does not halt to produce $\\hat{p}\_{t+1}$, then the probability $\\mu\_h(x\_{1:n})$ for $n>t$ is undefined, and the induced measure $\\mu\_h$ becomes a semimeasure.



## Prior

Weighting by program length suffices as a prior:

$$
p(h) = 2^{-\\ell(h)}
$$

One difficulty in working with programs is long-running execution. This can make computing data probabilities take a long time. One remedy is to down-weight long-running programs in the prior. [Levin search](http://www.scholarpedia.org/article/Universal_search) is an alternative to Solomonoff induction where the prior is weighted solely by runtime. We can mix both kinds of priors.

This is straightforward in Solomonoff induction [#Version 1](#version-1) where each program takes no input and outputs a deterministic string. Let $p(h) = 2^{-\\ell(h)} / f(\\tau(h))$ where $\\tau(h)$ is the total runtime of $h$, and $f$ is an increasing function that goes to infinity. For example, if $f(t) = 2^{t}$, then we have prior $2^{-\\ell(h)-\\tau(h)}$. If you wanted to compute $p(x)$ within some precision $\\ve > 0$, you can enumerate all programs $h\\in\\mc{H}$ by length and run them in parallel (called dovetailing). For each program, stop execution when $2^{-\\ell(h)-\\tau(h)} < \\ve$. Shorter programs will be given more runtime over longer programs. (Thank you Lance Roy for the helpful discussion about this.)

However, if we are using the programs I previously suggested that output data probabilities, then these programs may be fast on some inputs and slow on others. I don't have a solution, but a reasonable suggestion is to do some kind of heuristic analysis of the programs on some sample inputs and assign a slowness penalty in the prior.


# Lifelong learning
Solomonoff induction is a framework for general-purpose life-long learning, which is a paradigm where an intelligent agent learns to predict it's future (or gain reward) from only one continuous data stream. The agent must learn on-line, and there are no independence assumptions (the data is a timeseries).

In the variational setup outlined above, we converted the problem of Bayesian inference into a reinforcement learning problem. At time $t$, data $x\_{1:t}$ is observed, and a policy $q\_{\\t^\*}$ on programs is trained using policy gradient methods. However, every $t$ requires its own $q\_{\\t\_t^\*}$, thus we would need to perform RL training at every timestep. One way to speed this up is to reuse policies from previous timesteps. That is to say, at time $t+1$ perform $\\argmax{\\t\\in\\T}\\set{ \\E\_{h \\sim q\_\\t}\\left[R(h)\\right] + \\mb{H}\_{h \\sim q\_\\t}[q\_\\t(h)]}$ using Monte Carlo gradient descent starting from the previous parameter $\\t\_t^\*$. This can be considered fine-tuning. However, this may fail to work if the posterior changes drastically between timesteps.

