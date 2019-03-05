import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt


# Plotting a Binomial Distribution
def __binomial_distribution__():
    """

    """
    n = 10
    x = np.arange(0, 11)
    p1 = 0.1
    px1 = st.binom.pmf(x, n, p1)
    p2 = 0.5
    px2 = st.binom.pmf(x, n, p2)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, px1, 'k', label='p = 0.1')
    plt.plot(x, px2, 'r', label='p = 0.5')
    plt.title('Binomial distribution')
    plt.legend()
    plt.show()


# Plotting a Poisson distribution
def __poisson_distribution__():
    """

    """
    poisson_lambda = 2.4
    x = np.arange(0, 11)
    px = st.poisson.pmf(x, poisson_lambda)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, px, 'k', label='lambda = 2.4')
    plt.title('Poisson distribution')
    plt.legend()
    plt.show()


# Plotting a Negative distribution
def __negative_distribution__():
    """

    """
    p = 0.3
    x = np.arange(0, 11)
    r1 = 2
    px1 = st.nbinom.pmf(x, r1, p)
    r2 = 3
    px2 = st.nbinom.pmf(x, r2, p)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, px1, 'k', label='p = 0.3, r = 2')
    plt.plot(x, px2, 'r', label='p = 0.3, r = 3')
    plt.title('Negative distribution')
    plt.legend()
    plt.show()


# Plotting a Normal distribution
def __normal_distribution__():
    """
    The normal, or Gaussian, distribution is hugely important in
    statistical and data science work (although it has its limitations!)
    - one of its primary applications is in what's known as the Central Limit Theorem
    """
    x = np.arange(-5, 5, 0.01)
    mu = 0
    sigma = 1
    # calculate f(x)
    f = 1 / np.sqrt((2 * np.pi * sigma ** 2)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, f, 'k')
    plt.title('Normal distribution')
    plt.show()


def __exponential_distributon__():
    """
    The exponential distribution is related to the Poisson process which underlies
    the Poisson distribution (a Poisson process is simply one in which events occur
    at the rate of 𝜆 per time period).
    Here, instead of modelling the number of events in a time period, as we did
    with the Poisson, we are interested in the time interval between events.
    Unlike the Poisson distribution, therefore, this is a continuous random variable.
    With 𝜆 defined as before, then the PDF for 𝑋∼𝐸(𝜆) measuring the time between events is:
    """
    poisson_lambda = 0.3
    x = np.arange(0, 5, 0.01)
    dx = st.expon.pdf(x, scale=1 / poisson_lambda)
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.plot(x, dx, 'k')
    plt.title('Exponential distribution')
    plt.show()
    # Let's calculate the probability of a time interval of less than half an hour
    # between consecutive lecturer appearances
    print(st.expon.cdf(0.5, scale=1 / poisson_lambda))


def __uniform_distribution__():
    """
     uniformly distributed random variable will take on any value in a given
     interval with equal probability. The two key parameters are therefore
     the lower and upper points of the interval, usually denoted 𝑎 and 𝑏 respectively,
     and 𝑋∼𝑈(𝑎,𝑏) has PDF:
    """
    a = 0
    b = 5
    c = 2
    d = 3
    st.uniform.cdf(d, loc=a, scale=b - a) - st.uniform.cdf(c, loc=a, scale=b - a)


def __logistic_function__():
    """
    Logistic Regression is the most fundamental algorithm for classification problems.
    t's the basis of the most fundamental of classification techniques, logistic regression,
    and has applications in a wide variety of machine learning and artificial intelligence
    techniques, including artificial neural networks.
    The logistic function produces what is known as a sigmoid curve, an S-shaped curve which
    shows exponential growth initially, gradually tapering off and slowing significantly to the right
    """
    x = np.arange(-5, 5, 0.01)  # range of values for z
    x0 = np.zeros(len(x))
    x1 = np.ones(len(x))
    x12 = x1 / 2

    # now calculate f(x)
    f = 1 / (1 + np.exp(-x))

    plt.rcParams["figure.figsize"] = (6, 6)
    plt.plot(x, f, 'k')
    plt.plot(x, x0, '--r')
    plt.plot(x, x12, '--r')
    plt.plot(x, x1, '--r')
    plt.show()


def normal_prob(x1, x2, mu, sigma):
    return st.norm.cdf(x2, mu, sigma) - st.norm.cdf(x1, mu, sigma)


__binomial_distribution__()
__poisson_distribution__()
__negative_distribution__()
__normal_distribution__()
__exponential_distributon__()
__uniform_distribution__()
__logistic_function__()
print(normal_prob(2, 5, 0, 1))
