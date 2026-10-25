Every AI model is just matrix math wearing a fancy hat.
In AI, everything gets turned into a vector:
* A word becomes ~768 numbers describing its “meaning” (this is called an embedding).
* An image becomes a long list of pixel values.
* A user becomes a list of their preferences.

# The main aim
To help you see what the math inside AI models is actually doing, so the symbols stop looking scary.
# NOTE:
Dot product: how aligned two arrows are
Projection: the shadow of one arrow on another
Gram-Schmidt: a way to clean up a set of arrows so they’re all perpendicular and length 1

# Concept	        Where it shows up in AI
Vectors	        Embeddings (words, images, users as numbers)
Dot product	    Attention scores and similarity search
Rank	        LoRA (cheap fine-tuning of big models)
# What AI math do:
Vectors = the things being moved (data)
Matrices = the machines that move them (the model)
Dot product = the “how similar?” meter
Independence/rank = a check for redundancy
Projection/Gram-Schmidt = tools for splitting and cleaning directions