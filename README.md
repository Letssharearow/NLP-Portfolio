# Natural Language Processing Portfolio

This is our Portfolio submission for the course Natural Language Processing at the Technical University Würzburg-Schweinfurt  
Submission date: 16.01.2026

**Group:**
Felix Bauer, Julian Sehne, Steffen Schwab, Ivan Zelin

## Portfolio 1 - Paper Presentation
| Contributors | Felix Bauer | Julian Sehne | Steffen Schwab | Ivan Zelin |
|--------------|-------------|--------------|----------------|------------|
| Presentation | 25%         | 25%          | 25%            | 25%        |

We presented the key ideas
from [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473). Our presentation slides can be found [here](<Paper Presentation Attention.pdf>).

## Portfolio 2 - Class activities

| Contributors         | Felix Bauer | Julian Sehne                 | Steffen Schwab               | Ivan Zelin |
|----------------------|-------------|------------------------------|------------------------------|------------|
| Huggingface tutorial | 33%         | 33%                          | 33%                          | 0%         |
| Poet                 | 33%         | 33%                          | 33%                          | 0%         |
| Hackathon            | Yes         | No (Couldn't register... :/) | No (Couldn't register... :/) | Networked  |

### 1) [Huggingface tutorial](<Huggingface tutorial>)

Presented tutorials:

1. A full training loop: https://huggingface.co/learn/llm-course/chapter3/4
2. Understanding learning curves: https://huggingface.co/learn/llm-course/chapter3/5

We also opened (and merged) a Pull request, fixing a bug in the
notebook: https://github.com/huggingface/notebooks/pull/610

### 2) [Poem generator](<Poem generator>)
We finetuned a [distilGPT](https://huggingface.co/distilbert/distilgpt2) model to generate poems. For training, we used the following approach:
1. Load poem datasets:
    - [tgdivy/poetry-foundation-poems](https://www.kaggle.com/datasets/tgdivy/poetry-foundation-poems): Large collection, but mixed quality
    - [merve/poetry](https://huggingface.co/datasets/merve/poetry): Smaller collection, but higher quality
1. Extract keywords: Run spaCy noun extraction on each poem. Nouns tend to capture the core content words, so we use them as keywords.
1. Generate training data: For each poem we create training data by sampling 3 random nouns and prepending them as a prompt: `Words: <word1>, <word2>, <word3>\nPoem:\n<poem>`
1. Fine-tune model:
    1. Stage 1: Fine-tune on tgdivy/poetry-foundation-poems to learn general poetic structure and style
    1. Stage 2: Initialize from the Stage-1 model and fine-tune on merve/poetry to improve overall poem quality

#### Example result
```
Words: bottle, water, cat
Poem:
In the spring of 1958, I was
called The Great Yellow Bird
of the Night
by one of the women
who
who wore a white coat to the dog
in a hospital bed
and then my husband
started to see what
```

### 3) Hackathon
Link to hackathon repository: https://git.fiw.fhws.de/k70805/human-centered-ai-hackathon

## Portfolio 3 - [Tunix Competition](<Tunix Competition>)

| Contributors | Felix Bauer | Julian Sehne | Steffen Schwab | Ivan Zelin |
|--------------|-------------|--------------|----------------|------------|
| Competition  | 33%         | 33%          | 33%            | 0%         |

Link to submission: https://www.kaggle.com/code/felixbauer26/google-tunix-hack-submission   
Link to writeup: https://www.kaggle.com/competitions/google-tunix-hackathon/writeups/team-tuwas-submission    
Link to video: https://www.youtube.com/watch?v=LrknwuCJE8U

## Portfolio 4 - Capstone project

| Contributors | Felix Bauer | Julian Sehne | Steffen Schwab | Ivan Zelin |
|--------------|-------------|--------------|----------------|------------|
| Capstone     | 25%         | 25%          | 25%            | 25%        |

Link to Github: https://github.com/flix2612/politics-nlp
