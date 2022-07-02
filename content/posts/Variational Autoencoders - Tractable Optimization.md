---
date: 2022-07-01
lastmod: '2022-07-01T17:09:07-07:00'
tags:
- machine-learning
title: Variational Autoencoders - Tractable Optimization
---

This is my multi-part review of the innovation in [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf), which introduces something called the variational autoencoder (VAE), a class of generative model (e.g. for image generation) that has proved quite successful. However, the paper also introduces an entire methodology, of which the VAE is one instance (though given heavy focus). Specifically, this paper provides a method for fitting continuous latent variable models to data with maximum marginal likelihood via gradient descent (the meaning of these words will hopefully become clear as you read this article). <!--more-->

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
\\newcommand{\\M}{\\mc{M}}
\\newcommand{\\Er}{\\mc{E}}
\\newcommand{\\ht}{\\hat{\\t}}
\\newcommand{\\D}{\\mc{D}}
\\newcommand{\\softmax}{\\text{softmax}}
$$






For an explanation of what the term "variational" means here, see {{< locallink "Machine Learning Jargon - Variational Bayes" >}}.

# Maximum Marginal Likelihood Objective
[Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) is concerned with the following problem: We have a dataset $X = (x\_1,x\_2,\\dots,x\_n) \\in \\X^n$ which we are modeling as being sampled i.i.d. from some unknown distribution over $\\X$. We define some other set $\\Z$ (called the latent space) and define our model in two pieces as probability distributions, $p\_\\t(z)$ and $p\_\\t(x\\mid z)$, parameterized by $\\t\\in\\T$. This fully specifies the relationship between the random variables $x$ and $z$ by the joint distribution $p\_\\t(x,z) = p\_\\t(z)p\_\\t(x\_i\\mid z)$.

The marginal probability of the dataset under our model (the marginal likelihood) given parameters $\\t$ is

$$\\begin{aligned}
p\_\\t(X) &= \\prod\_{i=1}^n p\_\\t(x\_i) \\\\
&= \\prod\_{i=1}^n \\int\_\\Z p\_\\t(z)p\_\\t(x\_i\\mid z)\\ \\d z \\\\
&= \\prod\_{i=1}^n \\E\_{z\\sim p\_\\t(z)}\\left\[p\_\\t(x\_i\\mid z)\\right\]\\,.
\\end{aligned}$$

(Replace the integral with a sum when $\\Z$ is discrete.)

Maximizing the marginal likelihood $p\_\\t(X)$ "fits" our model to the data. Once our model is fit to the data, we can use it to generate new data that "looks like" (i.e. is distributed like) the training data.

Suppose the fit parameters are $\\ht$. Then our generation procedure is,
1. sample a latent code from the marginal distribution, $z \\sim p\_\\ht(z)$,
2. then sample from the decoder, $x \\sim p\_\\ht(x\_i\\mid z)$. 

This way, $x$ is marginally distributed according to $p\_\\ht(x\_i)$.




## Log-Likelihood Loss

Let $h\_\\t(x) = \\log\\par{1/p\_\\t(x)}$. This quantity is called the [self-information](https://en.wikipedia.org/wiki/Information_content) (or *surprisal*) of $x$ w.r.t. $p\_\\t$. We can see from the definition that $h\_\\t(x)$ is always non-negative, and $h\_\\t(x) = 0$ iff $p\_\\t(x)=1$. That means minimizing $h\_\\t(x)$ is equivalent to maximizing $p\_\\t(x)$. Since $\\log$ is monotonically increasing, any decrease in $h\_\\t(x)$ necessarily implies an increase in $p\_\\t(x)$. In this way, the following loss function (to be minimized) is essentially equivalent to our maximum likelihood objective above,

$$\\begin{aligned}
\\M(\\t;\\ X) &= h\_\\t(X) \\\\
&= \\log\\par{1/p\_\\t(X)} \\\\
&= -\\sum\_{i=1}^n \\log p\_\\t(x\_i) \\\\
&= -\\sum\_{i=1}^n  \\E\_{z\\sim p\_\\t(z)}\\left\[p\_\\t(x\_i\\mid z)\\right\]\\,.
\\end{aligned}$$

Minimizing a positive number to zero, rather than maximizing a negative number to 0, is a bit more intuitive in my opinion. Also, a minimization objective (a loss) conforms to the standard paradigm of deep learning, where the training objective is always a loss to be minimized via gradient descent.

A more practical reason to prefer to use log-likelihood (positive or negative) over likelihood is that the former is numerically stable to optimize with gradient ascent/descent. The probabilities involved in the product over $x\_i$ can be quite small which can lead to loss of precision, which log-scale avoids.

# Tractable Optimization
The marginal likelihood loss $\\M(\\t;\\ X)$ is generally intractable to optimize via gradient descent when the latent space is large (e.g. uncountable) due to the integral/sum over the latent space being intractable, with either numerical methods or exact methods. [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) is interested in making these situations tractable.





The approach of [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) is to find an approximation $q\_\\p(z \\mid x)\\approx p\_\\t(z\\mid x\_i)$ and use that to define a tractable proxy loss which we minimize instead of the target loss $\\M(\\t;\\ X)$. The defining feature of a proxy loss is that it has the same global minima as our target loss.

Define our proxy loss as

$$\\begin{aligned}
\\L(\\t,\\p;\\ X) = \\sum\_{i=1}^n\\Big\\{ \\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z)} + \\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\Big\\}\\,.
\\end{aligned}$$

Why $\\L(\\t,\\p;\\ X)$ is a proxy for $\\M(\\t;\\ X)$ will be explained in the next section, but for now take as given that it is. We know how to calculate exactly all the probabilities involved. The probabilities $p\_\\t(x\_i \\mid z)$ and $p\_\\t(z)$ are assumed to be given as the definition of our model, and we define $q\_\\p(z\\mid x\_i)$ explicitly to be a tractable quantity.

However, we are not out of the woods yet. We still need to make sure the two terms, KL-divergence on the left and expectation on the right, are tractable quantities too. [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) deals with instances (namely where $q\_\\p(z\\mid x\_i)$ and $p\_\\t(z)$ are made to be Gaussian) where the KL-divergence $\\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z)}$ has a known closed form expression. Unfortunately, the expectation term $\\sum\_{i=1}^n\\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\]$ is intractable to calculate exactly because it is yet another integral over $\\Z$.

The usual trick at this point is to use a [Monte Carlo approximation](https://en.wikipedia.org/wiki/Monte_Carlo_integration) of the expectation, which in this case is

$$
\\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\approx \\frac{1}{k}\\sum\_{j=1}^k \\log\\par{1/p\_\\t(x\_i \\mid z\_j)}
$$

where $z\_1,\\dots,z\_k$ are sampled i.i.d. from $q\_\\p(z \\mid x\_i)$, which we assume is a tractable operation. (Surprisingly, most implementations of the VAE use $k=1$, e.g. [example 1](https://gist.github.com/williamFalcon/1da585dd427002bca915f9ec323fbbbe#file-vae-py-L71) and [example 2](https://github.com/keras-team/keras-io/blob/b8d1e05f4c9193cefd8137caf000fde6597d2d79/examples/generative/vae.py#L31).)

We want to jointly minimize $\\L(\\t,\\p;\\ X)$ w.r.t. $\\t$ and $\\p$ using gradient descent. That requires us to calculate or approximate the gradient of this loss w.r.t. the parameters. Using our MC approximation for the expectation, we get MC gradients w.r.t. $\\t$,

$$\\begin{aligned}
&\\nabla\_\\t\\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\\\
=\\ & \\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\nabla\_\\t\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\\\
\\approx\\ & \\frac{1}{k}\\sum\_{j=1}^k \\nabla\_\\t\\log\\par{1/p\_\\t(x\_i \\mid z\_j)}
\\end{aligned}$$

and w.r.t. $\\p$ (using the [log-derivative trick](https://danieltakeshi.github.io/2017/03/28/going-deeper-into-reinforcement-learning-fundamentals-of-policy-gradients/)),

$$\\begin{aligned}
&\\nabla\_\\p\\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\\\
=\\ & \\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\nabla\_\\p\\log q\_\\p(z \\mid x\_i) \\right\] \\\\
\\approx\\ & \\frac{1}{k}\\sum\_{j=1}^k \\log\\par{1/p\_\\t(x\_i \\mid z\_j)}\\nabla\_\\p\\log q\_\\p(z \\mid x\_i)\\,.
\\end{aligned}$$

[Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) reports that *"gradient estimator \[w.r.t. $\\p$\] exhibits exhibits very high variance (see e.g. [BJP12](https://arxiv.org/abs/1206.6430)) and is impractical for our purposes."*

Instead, [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) offers an alternative approach using the so-called [reparameterization trick](https://en.wikipedia.org/wiki/Variational_autoencoder#Reparameterization) to "pass gradients" through the expectation to $\\p$. I won't go into the reparameterization trick here, but I suggest reading the paper or [this post](https://gregorygundersen.com/blog/2018/04/29/reparameterization) to learn more. 



# Proxy Loss Derivation

This derivation follows slightly different reasoning than [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf), but is in my opinion the most straightforward way to derive and understand the proxy loss $\\L(\\t,\\p;\\ X)$ which we defined above.

Recall that our proxy loss uses and approximation $q\_\\p(z\\mid x\_i)$ for the intractable distribution $p\_\\t(z\\mid x\_i)$ (because it involves an integral over $\\Z$). Then as a result we have a dual optimization objective. In addition to minimizing the log-likelihood loss, 
$$\\M(\\t;\\ X) \\df \\sum\_{i=1}^n\\log \\par{1/p\_\\t(x\_i)}\\,,$$
w.r.t. $\\t$, we want to simultaneously minimize the approximation error,

$$\\begin{aligned}
\\Er(\\t,\\p;\\ X) &\\df \\sum\_{i=1}^n\\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z\\mid x\_i)} \\\\&= \\sum\_{i=1}^n\\int\_\\Z q\_\\p(z\\mid x\_i)\\log\\par{\\frac{q\_\\p(z\\mid x\_i)}{p\_\\t(z\\mid x\_i)}}\\ \\d z\\,,
\\end{aligned}$$

w.r.t. $\\p$, where $\\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z\\mid x\_i)}$ is the [KL-divergence](https://en.wikipedia.org/wiki/Kullback–Leibler_divergence) between $q\_\\p(z\\mid x\_i)$ and $p\_\\t(z\\mid x\_i)$ w.r.t. $z$. KL-divergence acts like a distance function between probability distributions (though asymmetric w.r.t. the ordering of its two arguments). Conveniently, KL-divergence is always non-negative, and $0$ iff the two distributions are equal. In this way $\\Er(\\t,\\p;\\ X)$ is also well suited as a loss function.



Unfortunately, $\\Er(\\t,\\p;\\ X)$ is also intractable to directly calculate and minimize for the same reason as $\\M(\\t;\\ X)$ - specifically because $\\Er(\\t,\\p;\\ X)$ makes use of $p\_\\t(z\\mid x\_i)$ which is calculated with an intractable integral over $\\Z$.

However, something miraculous happens when we sum our two objectives. Let $\\L(\\t,\\p;\\ X)$ be that sum. Then we have
$$\\begin{aligned}
\\L(\\t,\\p;\\ X)&\\df\\M(\\t;\\ X) + \\Er(\\t,\\p;\\ X) \\\\
&=\\sum\_{i=1}^n\\Big\\{ \\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z)} + \\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\Big\\}\\,,
\\end{aligned}$$

which is the loss that [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) shows how to tractably minimize. See [#Appendix](#appendix) for the derivation.

## Variational Bounds

Now we can answer why $\\L(\\t,\\p;\\ X)$ is a suitable proxy loss for $\\M(\\t;\\ X)$. [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) calls $\\L(\\t,\\p;\\ X)$ a "variational bound" of $\\M(\\t;\\ X)$ (specifically an upper bound). To see why $\\L(\\t,\\p;\\ X)$ is an upper bound, first recall from the previous section that $\\M(\\t;\\ X)$ and $\\Er(\\t,\\p;\\ X)$ are always non-negative and achieve their global minima at $0$. Then the relationship $\\L(\\t,\\p;\\ X) = \\M(\\t;\\ X) + \\Er(\\t,\\p;\\ X)$ becomes the inequality

$$
\\L(\\t,\\p;\\ X) \\geq \\M(\\t;\\ X)
$$

with the gap being the non-negative difference $\\Er(\\t,\\p;\\ X)$. Then minimizing $\\L(\\t,\\p;\\ X)$ to $0$ necessarily minimizes $\\M(\\t;\\ X)$ to $0$, fulfilling the requirements of a proxy loss.

Inspiration for this proxy loss, and the terms "variational bound" and "variational Bayes", come directly from the paper [Paisley et al.](https://arxiv.org/abs/1206.6430) which discusses an instance of {{< locallink "Variational Bayesian Inference" >}}. However, the adaptation of variational Bayesian inference in [Kingma et al.](https://arxiv.org/pdf/1312.6114.pdf) does not have quite the same properties - see the next section, [#Variational Bayes](#variational-bayes).

(For a broader explanation of the terms "variational" and "Bayesian" in machine learning, see {{< locallink "Machine Learning Jargon - Variational Bayes" >}}.)



### Variational Bayes

To match the template of variational Bayesian inference (see {{< locallink "Variational Bayesian Inference" "variational-inference" >}}), we want to use the relationship $\\L(\\t,\\p;\\ X) = \\M(\\t;\\ X) + \\Er(\\t,\\p;\\ X)$ to establish the inequality

$$
\\L(\\t,\\p;\\ X) \\geq \\Er(\\t,\\p;\\ X)
$$

(since $\\M(\\t;\\ X)=\\log\\par{1/p\_\\t(X)}$ is non-negative), where $\\t$ is held fixed and $z \\in \\Z$ takes the place of the hypotheses $h \\in \\mc{H}$. In this perspective, $\\L(\\t,\\p;\\ X)$ is a proxy loss for $\\Er(\\t,\\p;\\ X)$ w.r.t. $\\p$. 

As in {{< locallink "Variational Bayesian Inference" "variational-inference" >}}, we have the nice property that decreasing $\\L(\\t,\\p;\\ X)$ w.r.t. $\\p$, even slightly (while holding $\\t$ fixed), results in $\\Er(\\t,\\p;\\ X)$ necessarily decreasing as well, because their difference is a constant w.r.t. $\\p$. Furthermore, when $\\L(\\t,\\p;\\ X)$ is at its global minimum w.r.t. $\\p$ iff $\\Er(\\t,\\p;\\ X)$ is also at its global minimum w.r.t. $\\p$ (again holding $\\t$ fixed).

However, when we use $\\L(\\t,\\p;\\ X)$ as a proxy loss for $\\M(\\t;\\ X)$ w.r.t. $\\t$, we don't get the same nice property. As we minimize $\\L(\\t,\\p;\\ X)$ w.r.t. $\\t$, the difference $\\L(\\t,\\p;\\ X)-\\M(\\t;\\ X)=\\Er(\\t,\\p;\\ X)$ is not constant w.r.t. $\\t$. The only guarantee we have is that the upper bound on $\\M(\\t;\\ X)$ has shrunk. It's technically possible that $\\M(\\t;\\ X)$ may even increase in some instances where $\\L(\\t,\\p;\\ X)$ is incrementally decreased w.r.t. $\\t$, so we don't get the lockstep decrease as before.

However, we can reliably lessen the gap between $\\L(\\t,\\p;\\ X)$ and $\\M(\\t;\\ X)$ by incrementally decreasing $\\L(\\t,\\p;\\ X)$ w.r.t. $\\p$, taking advantage of the lockstep relationship between $\\L(\\t,\\p;\\ X)$ and $\\Er(\\t,\\p;\\ X)$ with fixed $\\t$.

In the Bayesian paradigm described in {{< locallink "Variational Bayesian Inference" >}}, updating $\\L(\\t,\\p;\\ X)$ w.r.t. $\\t$ is like altering the Bayesian distribution (both priors and likelihoods of the hypotheses) in the middle of optimizing the approximate posterior $q\_\\p(z \\mid x)$ w.r.t. $\\p$. In this light, $\\Er(\\t,\\p;\\ X)$ is a non-stationary optimization objective w.r.t. $\\p$, where $\\t$ controls how the objective changes over time.

### Approximate Likelihood

Another way to derive $\\L(\\t,\\p;\\ X)$ as a proxy for $\\M(\\t;\\ X)$ is to observe that 

$$\\sum\_{i=1}^n \\log p\_\\t(x\_i) = \\sum\_{i=1}^n\\log\\par{\\frac{p\_\\t(x\_i\\mid z)p\_\\t(z)}{p\_\\t(z\\mid x\_i)}}$$

for all $z\\in\\Z$. This moves the intractable integral over $\\Z$ into $p\_\\t(z\\mid x\_i)$.

From here we can substitute $p\_\\t(z\\mid x\_i)$ with our approximation $q\_\\p(z\\mid x\_i)$ and define the approximate loss

$$
\\mc{A}(\\t,\\p;\\ X, z) = -\\sum\_{i=1}^n\\log\\par{\\frac{p\_\\t(x\_i\\mid z)p\_\\t(z)}{q\_\\p(z\\mid x\_i)}}
$$

on some choice of $z\\in\\Z$. This loss depends only on quantities we know how to calculate. However, now the problem is that when $q\_\\p(z\\mid x\_i) \\neq p\_\\t(z\\mid x\_i)$, it is not clear what minimizing this loss w.r.t. $\\t$ will end up doing (we cannot yet call $\\mc{A}(\\t,\\p;\\ X, z)$ a proxy loss).

It also now matters which $z\\in \\Z$ we choose for this loss, since $q\_\\p(z\\mid x\_i)$ can be a more or less accurate approximation of $p\_\\t(z\\mid x\_i)$ on different $z$. One mitigation would be to take the expectation w.r.t. $z \\sim q\_\\p(z\\mid x\_i)$, with the hand-wavy idea that we care more about this optimization where $z$ is more likely. Sure enough, if we naively run with that idea, we get

$$\\begin{aligned}
&\\E\_{z\\sim q\_\\p(z\\mid x\_i)}\[\\mc{A}(\\t,\\p;\\ X, z)\] \\\\
&=-\\sum\_{i=1}^n\\E\_{z\\sim q\_\\p(z\\mid x\_i)}\\left\[\\log\\par{\\frac{p\_\\t(x\_i \\mid z)p\_\\t(z)}{q\_\\p(z\\mid x\_i)}}\\right\] \\\\
&= -\\sum\_{i=1}^n\\E\_{z\\sim q\_\\p(z\\mid x\_i)}\\left\[\\log\\par{\\frac{p\_\\t(z)}{q\_\\p(z\\mid x\_i)}} + \\log p\_\\t(x\_i \\mid z)\\right\] \\\\
&= \\sum\_{i=1}^n\\Big\\{\\kl{q\_\\p(z\\mid x\_i)}{p(z)}-\\E\_{z\\sim q\_\\p(z\\mid x\_i)}\\big\[\\log p\_\\t(x\_i \\mid z)\\big\]\\Big\\} \\\\
&= \\L(\\t,\\p;\\ X)\\,,
\\end{aligned}$$

which is the same proxy loss we derived twice before!

Thinking about it like this, the relationship

$$
\\L(\\t,\\p;\\ X) - \\M(\\t;\\ X) = \\Er(\\t,\\p;\\ X)
$$

takes on a slightly different meaning, where $\\Er(\\t,\\p;\\ X)$ is the error term due to using $\\L(\\t,\\p;\\ X)$ as an approximation of $\\M(\\t;\\ X)$. This gives us a way to answer to the question of what minimizing $\\mc{A}(\\t,\\p;\\ X, z)$ w.r.t. $\\t$ does when $q\_\\p(z\\mid x\_i) \\neq p\_\\t(z\\mid x\_i)$.

Notice that the error term $\\Er(\\t,\\p;\\ X)$ is entirely due to $q\_\\p(z\\mid x\_i)$ being an imperfect approximation of $p\_\\t(z\\mid x\_i)$. Just by minimizing the approximation $\\L(\\t,\\p;\\ X)$ w.r.t. $\\t$ and $\\p$ jointly, we minimize the approximation error due to $q\_\\p(z\\mid x\_i)$ in the process.


# Appendix 

Proof that $\\Er(\\t,\\p;\\ X) + \\M(\\t;\\ X) = \\L(\\t,\\p;\\ X)$,


$$\\begin{aligned}
& \\Er(\\t,\\p;\\ X) + \\M(\\t;\\ X) \\\\
=\\ & \\sum\_{i=1}^n\\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z\\mid x\_i)} + \\sum\_{i=1}^n\\log \\par{1/p\_\\t(x\_i)} \\\\
=\\ & \\sum\_{i=1}^n\\Big\[\\int\_\\Z q\_\\p(z\\mid x\_i) \\log\\par{\\frac{q\_\\p(z\\mid x\_i)}{p\_\\t(z\\mid x\_i)}}\\ \\d z - \\int\_\\Z q\_\\p(z\\mid x\_i)\\log p\_\\t(x\_i)\\ \\d z \\Big\] \\\\
=\\ & \\sum\_{i=1}^n \\int\_\\Z q\_\\p(z\\mid x\_i) \\log\\par{\\frac{q\_\\p(z\\mid x\_i)}{p\_\\t(x\_i\\mid z)p\_\\t(z)/p\_\\t(x\_i)}\\cdot\\frac{1}{p\_\\t(x\_i)}}\\ \\d z \\\\
=\\ & \\sum\_{i=1}^n\\int\_\\Z q\_\\p(z\\mid x\_i) \\log\\par{\\frac{q\_\\p(z\\mid x\_i)}{p\_\\t(z)}\\cdot\\frac{1}{p\_\\t(x\_i\\mid z)}}\\ \\d z \\\\
=\\ & \\sum\_{i=1}^n\\Big\[ \\int\_\\Z q\_\\p(z\\mid x\_i) \\log\\par{\\frac{q\_\\p(z\\mid x\_i)}{p\_\\t(z)}}\\ \\d z + \\int\_\\Z q\_\\p(z\\mid x\_i) \\log\\par{\\frac{1}{p\_\\t(x\_i\\mid z)}}\\ \\d z \\Big\] \\\\
=\\ & \\sum\_{i=1}^n\\Big\[ \\kl{q\_\\p(z\\mid x\_i)}{p\_\\t(z)} + \\E\_{z\\sim q\_\\p(z \\mid x\_i)}\\left\[\\log\\par{1/p\_\\t(x\_i \\mid z)}\\right\] \\Big\] \\\\
=\\ & \\L(\\t,\\p;\\ X)\\,.
\\end{aligned}$$