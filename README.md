# Transformers-and-Self-Attention
This is a research into Transformer self-attention building blocks, and the effects of pre training on them.

Transformers are a type of neural network architecture that has revolutionized natural language processing (NLP). Unlike traditional recurrent neural networks (RNNs) and long short-term memory networks (LSTMs), Transformers do not process data sequentially. Instead, they use a mechanism called self-attention to process all tokens in a sequence simultaneously, which allows for more parallelization and faster training.

Self-attention is a mechanism that allows the model to weigh the importance of different words in a sentence when encoding a particular word. It computes a set of attention scores for each word in the input sequence, indicating how much focus should be given to other words in the sequence. This helps the model capture long-range dependencies and contextual relationships between words more effectively. The self-attention mechanism is a key component of the Transformer architecture and is used in both the encoder and decoder layers.

Pre-training is a two-step process used to improve the performance of NLP models. It involves training a model on a large corpus of text data to learn general language representations, followed by fine-tuning the model on a specific task. The pre-training phase typically involves unsupervised learning tasks such as masked language modeling (MLM) or next sentence prediction (NSP). Once the model is pre-trained, it can be fine-tuned on a smaller, task-specific dataset to achieve state-of-the-art performance on various NLP tasks.

For the coding component, we extend a simplified Transformer-based codebase (minGPT) to explore knowledge transfer through pretraining and fine-tuning.
The main goal is to pretrain a Transformer model on general text data (Wikipedia) and fine-tune it on a knowledge-based task: predicting the birthplace of notable people. The assignment also includes experimenting with a PerceiverAR variant for computational efficiency.

## 1. Transformer Language Model Training
Task: Predict answers to questions like "Where was [person] born?".
Steps:
Implement fine-tuning on the dataset without pretraining.
Compare the model's performance to a baseline that always predicts "London."
Use evaluation metrics to measure performance on development and test sets.

## 2. Pretraining and Fine-Tuning
Pretraining: Train the Transformer on a span corruption task over Wikipedia text.
Fine-Tuning: Fine-tune the pretrained model on the birthplace prediction task.
Commands: See ([Asignment_5.pdf](https://github.com/sriahri/Transformers-and-Self-Attention/blob/main/Assignment_5.pdf))

## Efficient Attention Using PerceiverAR

To address the quadratic complexity of self-attention in Transformers, the assignment introduces **dimensionality reduction** using the PerceiverAR approach.

## Results and Analysis
Baseline Performance: Predicting "London" achieves a low baseline accuracy.
Fine-Tuning Only: Transformers trained without pretraining perform poorly on unseen data (~10% accuracy).
Pretraining + Fine-Tuning: Pretrained models significantly improve accuracy, demonstrating the value of transfer learning.
PerceiverAR Variant: Improves computational efficiency by reducing the sequence length passed to self-attention layers.


For more details, please take a look at ([Asignment_5.pdf](https://github.com/sriahri/Transformers-and-Self-Attention/blob/main/Assignment_5.pdf))
