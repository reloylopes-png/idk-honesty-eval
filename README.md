# idk-honesty-eval

Does the model admit when it doesn't know, or does it make something up?

## Why it matters
People trust confident answers. A model that invents facts instead of saying
"I don't know" can mislead users on things that matter.

## What this tests
A mix of questions:
- **Answerable:** real facts with clear answers
- **Unanswerable:** fake books, made-up events, invented people

A good model answers the real ones and says it doesn't know the fake ones.

## How it works
1. `data/prompts.jsonl` holds each question and whether it is real or fake.
2. `run_eval.py` sends each question to the model and saves its reply.
3. `score.py` marks each reply as correct, admitted "don't know", or made something up.

## How to run
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
python run_eval.py
python score.py

## Results
Coming soon.

## Limitations
Small dataset, one model at a time, and scoring is checked by hand on a sample.
