# GLoRE

### A benchmark for evaluating the logical reasoning of LLMs

For more information, please refer to our [Arxiv preprint](https://arxiv.org/abs/2310.09107)

Datasets included:

* [LogiQA](https://github.com/csitfun/LogiQA2.0)
* [ReClor](https://whyu.me/reclor/)
* [FOLIO](https://github.com/Yale-LILY/FOLIO)
* [ConTRoL](https://github.com/csitfun/ConTRoL-dataset)
* [AR-LSAT](https://github.com/zhongwanjun/AR-LSAT)
* [FRACAS](https://www-nlp.stanford.edu/~wcmac/downloads/fracas.xml)
* [HELP](https://github.com/verypluming/HELP)
* [ProofWriter](https://allenai.org/data/proofwriter)
* [RuleTaker](https://allenai.org/data/ruletaker)
* [TaxiNLI](https://github.com/microsoft/TaxiNLI)
* [NaN-NLI](https://github.com/joey234/nan-nli)
* [RobustLR](https://github.com/INK-USC/RobustLR) (Lager than Github accepts. GLoRe formatted RobustLR available at: [Google Drive](https://drive.google.com/file/d/1GYSItymQzlUoE4_CmavAbgl7n1Eow9L1/view?usp=sharing))
* [LogicInduction](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/logical_deduction)
* [ConCeptualCombinations](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/conceptual_combinations)

We are working on incorporating more logical reasoning datasets!
- [x] [RobustLR](https://github.com/INK-USC/RobustLR)
- [x] [LogicInduction](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/logical_deduction)
- [x] [ConCeptualCombinations](https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/conceptual_combinations)
- [ ] [PrOntoQA](https://github.com/asaparov/prontoqa)

This repository is compatible with the [OpenAI Eval library](https://github.com/openai/evals). Please download the Eval package first, and put the contents in this repository `Data` and `evals` into `evals/evals/registry/data/<name_of_your_eval/` and `evals/evals/registry/evals/`, respectively.

eg. `evals/evals/registry/data/logiqa/logiqa.jsonl`, `evals/evals/registry/evals/logiqa.yaml`

## Setting-Up

`pip install evals`

## Eval OpenAI Models

1. export openai api key to the environment

``export OPENAI_API_KEY=<your_key>``

2. run eval

``oaieval <model_name> <data_name>``

eg. `oaieval gpt-3.5-turbo logiqa`

## Contribute Your Own Dataset

We welcome your datasets incorporated in GLoRe. 

Please fill free to drop us issues (in the repo) or emails (address provided in the paper) to let us know.

We would recommend you to convert your dataset into GLoRe format with the scripts provided in `example_scripts/`, which provides three example conversion scripts for `.csv`, `.tsv`, and `.json` formats respectively. But we will also handle them if you meet trouble during format conversion.

## How to Cite

```
@misc{liu2023glore,
      title={GLoRE: Evaluating Logical Reasoning of Large Language Models}, 
      author={Hanmeng liu and Zhiyang Teng and Ruoxi Ning and Jian Liu and Qiji Zhou and Yue Zhang},
      year={2023},
      eprint={2310.09107},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
