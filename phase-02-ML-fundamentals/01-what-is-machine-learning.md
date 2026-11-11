> Machine learning is teaching computers to find patterns in data instead of writing rules by hand.

* THREE TYPES OF MACHINE LEARNING:
1. Supervised Learning: You have input-output pairs. The model learns to map inputs to outputs.

    "Here are 10,000 photos labeled cat or dog. Learn to tell them apart."
    "Here are house features and prices. Learn to predict the price."

2. Unsupervised Learning: You have inputs only. No labels. The model finds structure on its own.

    "Here are 10,000 customer purchase histories. Find natural groupings."
    "Here are 1,000 dimensional data points. Reduce to 2 dimensions while keeping structure."

3. Reinforcement Learning: An agent takes actions in an environment and receives rewards or penalties. It learns a strategy (policy) to maximize total reward.

    "Play this game. +1 for winning, -1 for losing. Figure out a strategy."
    "Control this robot arm. +1 for picking up the object, -0.01 for each second wasted."

## Reinforcement Learning from Human Feedback(RLHF) ###
## BERT (Bidirectional Encoder Representations from Transformers) ###(Introduced by google in 2018.)
## GPT (Generative Pre-trained Transformer) ## (OpenAI, designed to generate human-like text and code by predicting the next token in a sequence. )
> Underfitting: The model is too simple to capture the patterns in the data. A straight line trying to fit a curved relationship. Training error is high. Test error is high.

> Overfitting: The model is too complex and memorizes the training data, including its noise. A wiggly curve that passes through every training point but fails on new data. Training error is low. Test error is high.

* WHEN NOT TO USE MACHINE LEARNING
1. Rules are simple and well-defined
2. You have no data or very little data. ML needs examples to learn from.
3. The cost of being wrong is catastrophic and you need guaranteed correctness. 
4. A lookup table or heuristic solves the problem.
5. You cannot explain the decision and explainability is required. 
6. The problem changes faster than you can retrain. 

* REGRESSION: Answers "how much"?(the price)
* CLASSIFICATION: Answers "which category?"(spam or not)

NOTE:
* Training (~70%): the model learns here.
* Validation (~15%): tune settings and compare models.
* Test (~15%): look at it once, at the end. If you keep tweaking based on test results, you’ve effectively trained on it and your numbers mean nothing.

N.B: For small datasets, use k-fold cross-validation: rotate which chunk is held out and average. IT EVALUATES HOW ACCURATELY A PREDICTIVE MODEL PERFORMS ON UNSEEN DATA.

> When not to use ML

Skip ML when rules are simple (tax math, unit conversion), when you have little or no data, when you need guaranteed correctness, when a lookup table works, when decisions must be fully explainable, or when the problem changes faster than you can retrain.