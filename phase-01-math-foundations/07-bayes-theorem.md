> Probability is about what you expect. Bayes' theorem is about what you learn.

## Bayes' Priority: is the hypothesis occurring before new evidence or data is considered.

* Maximum Likelihood Estimation (MLE): It turns data-fitting and parameter-learning problems into mathematical problems into mathematical optimization tasks that code can solve automatically.

* Maximum A Posteriori (MAP): Estimations helps in programming by acting as a regularized version of maximum likelihoo estimation(MLE). It combines raw data with built in prior belief to prevent models from overfitting or making wild guesses when data is scarce.

* Bayes’ theorem and its four parts

P(A|B) = P(B|A) × P(A) / P(B)

Part	Name	        Plain meaning
P(A|B)	Posterior	    Your updated belief after seeing the evidence
P(B|A)	Likelihood	    How likely the evidence is if your hypothesis is true
P(A)	Prior	        Your belief before seeing anything
P(B)	Evidence	    How likely the evidence is overall (a normalizer)

# NOTE: You have to build ML systems and understand them, else you will misinterpret model otuputs, set bad thresholds, and ship overcondifdent preictions.

* Less than 1%. The prior dominates. When a condition is rare, even accurate tests produce mostly false positives. This is why doctors order confirmation tests.

### Bayesian vs frequentist: the practical difference

Frequentists treat parameters as fixed unknowns. They ask: "If I repeated this experiment many times, what would happen?"

Bayesians treat parameters as distributions. They ask: "Given what I have observed, what do I believe about the parameters?"