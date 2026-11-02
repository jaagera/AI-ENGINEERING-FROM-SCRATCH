> Floating point is a leaky abstraction. It will bite you during training, and you will not see it coming.
 
 * NaN and Inf: Detection and Prevention

nan (Not a Number) and inf (infinity) propagate virally through computation. One nan in a gradient update makes the weight nan, which makes every subsequent output nan. Training is dead within one step.

* How inf appears:

    exp() of a large positive number
    Division by zero: 1.0 / 0.0
    float32 overflow in accumulations

* How nan appears:

    0.0 / 0.0
    inf - inf
    inf * 0
    sqrt() of a negative number
    log() of a negative number
    Any arithmetic involving an existing nan

 > TYPES OF CLIPPING:

 * Clip by value: clamp each gradient element independently.

 * Clip by norm: scale the entire gradient vector so its norm does not exceed a threshold. The learned parameters gamma and beta let the network restore any scale it needs.

 > Without normalization, activations can grow or shrink exponentially through layers.

 Common ML Numerical Bugs

Bug: Loss is NaN after a few epochs.

Cause: logits grew too large, softmax overflowed. Or learning rate is too high and weights diverged.

Fix: use stable softmax (max subtraction), reduce learning rate, add gradient clipping.

Bug: Loss is stuck at log(num_classes).

Cause: model outputs are near-uniform probabilities. Often means gradients are vanishing or the model is not learning at all.

Fix: check that data labels are correct, verify the loss function, check for dead ReLUs.

Bug: Validation accuracy is lower than expected by 1-3%.

Cause: mixed precision without proper loss scaling. Gradient underflow silently zeroes out small updates.

Fix: enable dynamic loss scaling, or switch to bfloat16.

Bug: Gradient norms are 0.0 for some layers.

Cause: dead ReLU neurons (all inputs negative), or float16 underflow.

Fix: use LeakyReLU or GELU, use gradient scaling, check weight initialization.

Bug: Model works on one GPU but gives different results on another.

Cause: non-deterministic floating point accumulation order. GPU parallel reductions sum in different orders on different hardware, and floating point addition is not associative.

Fix: accept small differences (1e-6), or set torch.use_deterministic_algorithms(True) and accept the speed penalty.

Bug: exp() returns inf in loss computation.

Cause: raw logits passed to exp() without the max-subtraction trick.

Fix: use torch.nn.functional.log_softmax() which implements log-sum-exp internally.

Bug: Training diverges after switching from float32 to float16.

Cause: float16 cannot represent gradient magnitudes below 6e-8 or activations above 65,504.

Fix: use mixed precision with loss scaling (AMP), or use bfloat16 instead.

> bfloat16 vs float16
N.B = A float is a number with a limited "range".

float16 has more precision but a small range (max 65,504). bfloat16 has the same range as float32 but less precision. For training, range matters more, so bfloat16 usually wins and needs no loss scaling.

> A float has three parts: a sign bit, an exponent, and a mantissa (significand).

* float32 gives you about 7 decimal digits of precision. That means it can tell apart 1.0000001 and 1.0000002, but not 1.00000001 and 1.00000002. After 7 digits, everything is rounding noise.

* float16 gives you about 3 digits. The largest number it can represent is 65,504. That is disturbingly small for ML where logits, gradients, and activations routinely exceed this.

* bfloat16 is Google's answer to float16's range problem. It has the same 8-bit exponent as float32 (same range, up to 3.4e38) but only 7 mantissa bits (less precision than float16). For training neural networks, range matters more than precision, so bfloat16 usually wins.




