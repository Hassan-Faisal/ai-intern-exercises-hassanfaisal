Q.1: What is Generative AI?

Ans: Generative AI refers to a class of machine learning models that can create new content such as text, images, audio, or even code. Instead of just analyzing or predicting outcomes from data (like traditional machine learning), generative models learn patterns in data and use those patterns to generate something new.

The key difference between Generative AI and traditional machine learning is that traditional models are mostly focused on prediction tasks (e.g., classification or regression), while generative models aim to produce new data that resembles the training data.

For example, a traditional model might classify emails as spam or not spam, whereas a generative model can write a full email from scratch.

In short, Generative AI doesn’t just understand — it creates. That’s why it feels magical and is changing how we work and create every day.



Q.2: Self-Attention Explained (With Example)

Using the sentence: "The cat sat on the mat"

In self-attention, every word is converted into a vector (embedding). For each word we create three new vectors: Query (Q), Key (K), and Value (V). These are just linear projections of the original embedding.

Query (Q): Represents the current word we are focusing on.
Key (K): Represents all words in the sentence.
Value (V): Contains the actual information of the words.

We compute attention scores by taking the dot product of the Query of one word with the Key of every word (including itself). This tells us how relevant each word is to the current one. For the word “cat”, its Query will have a strong match with the Key of “sat” and “mat” because they are related in the sentence.

We scale the scores by dividing by √d_k (where d_k is the dimension of the Key vectors). This scaling stops the dot products from becoming too large when the dimension is high, which would push the softmax into extreme values (almost 1 or 0) and kill the gradients.

Then we apply softmax to turn the scaled scores into probabilities that sum to 1. Finally we multiply those probabilities by the Value vectors and sum them up. The result is a new representation for “cat” that has gathered useful context from the whole sentence.

This is exactly what solves the big problem RNNs struggled with: long-range dependencies. RNNs process words one by one and suffer from vanishing gradients, so distant words lose influence. Self-attention connects every word directly to every other word in one step — no sequential bottleneck.

Q.3: Encoder vs. Decoder Comparison
Component                      Encoder                                    Decoder
Core Goal                   Understanding context                  Generating new tokens
Attention Pattern       Bidirectional (sees all words)     Unidirectional (sees past words)
Special Mechanism               None                            Masked Self-Attention

Q.4: Vision Transformers (ViT) – High-Level Explanation

Vision Transformers (ViT) apply the transformer architecture to image data instead of text.

Instead of processing the whole image at once, the image is divided into smaller patches (like 16x16 pixels). These patches act like “tokens,” similar to words in a sentence.

Each patch is flattened and converted into a vector representation, which is then passed into the transformer.

Since transformers do not inherently understand spatial order, positional embeddings are added to each patch so the model knows where each patch is located in the image.

This approach is different from CNNs. CNNs focus on local patterns using convolution filters, while Vision Transformers look at global relationships between patches using attention mechanisms.

