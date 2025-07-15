# RAG-System-Evaluation

### Lightweight Evaluation Tools for Retrieval-Augmented Generation Systems

> **University Project – Data Architecture**
> 
> Authors: *Falbo Andrea*, *Tenderini Ruben* 

## Table of Contents

### [Overview](#overview)

### [Repository Structure](#repository-structure)

### [Methodology](#methodology)

### [Run](#run)

### [Key Insights](#key-insights)

### [Author](#author)

### [License](#license)

## Overview

This project aims to provide a **modular and extensible** evaluation tool that can benchmark various RAG (Retrieval-Augmented Generation) systems against standard datasets and custom configurations.

The tool is structured around **Jupyter Notebooks** that allow users to run experiments, save and visualize results to compare different configurations of RAG systems.

## Repository Structure

```
├── configs/                                    <- Configuration files
│   ├── beir_benchmark_config.json              <- BEIR benchmark base configuration
│   ├── custom_benchmark_config.json            <- Custom benchmark base configuration
│   └── prompt_templates.py                     <- Prompt configuration for llm models
├── .gitignore                                  <- Files and directories to ignore in git
├── LICENSE                                     <- License file
├── beir_benchmark.ipynb                        <- BEIR benchmark evaluation notebook
├── custom_benchmark_plotter.ipynb              <- Benchmark plotter notebook
├── custom_benchmark.ipynb                      <- Custom benchmark evaluation notebook
├── retrieval_plotter.ipynb                     <- Retrieval metrics plotter
├── presentazione.pdf                           <- Presentation of the work done (in Italian)
├── requirements.txt                            <- Python dependencies
├── relazione.pdf                               <- Report of the work done (in Italian)
└── README.md                                   <- This file
```

## Methodology

For a split of the dataset [Natural Questions](https://huggingface.co/datasets/google-research-datasets/natural_questions), the custom implementation retrieves and generates the response from the given context, compares it to ground truth and computes performance metrics.

The **retrieval metrics** are:
* **MAP (Mean Average Precision)**: Measures the mean of the average precision scores for each query, reflecting both precision and recall across ranked results.
* **NDCG (Normalized Discounted Cumulative Gain)**: Evaluates the ranking quality by considering the position of relevant documents in the result list.
* **Precision**: The proportion of retrieved documents that are relevant.
* **Recall**: The proportion of relevant documents that are successfully retrieved.

The **syntactic metrics for generation** are:
* **RougeL**: Measures the overlap in terms of the longest common subsequence between the generated response and the ground truth.
* **Bleu**: Evaluates the n-gram precision of the prediction with respect to the ground truth.
* **Longest Match**: Custom metric that measures the length of the longest continuous substring of the ground truth present in the prediction.

The **semantic metrics for generation** are:
* **Cosine Similarity**: Measures the cosine similarity between the embeddings of the generated response and the ground truth, capturing semantic closeness.
* **Semantic Evaluation LLM**: Uses a large language model to assess the semantic similarity or adequacy of the generated response compared to the ground truth.

For the BEIR benchmark, see the official [BEIR repository](https://github.com/beir-cellar/beir?tab=readme-ov-file) for details on datasets and evaluation metrics. The runs were performed on the following datasets:
* **Scidocs**
* **SciFact**
* **Fiqa**

All evaluation and visualization logic is implemented in the provided Jupyter Notebooks.

## Run

1. Clone the repository:

   ```bash
   git clone https://github.com/Ruben-2828/rag-system-evaluation
   cd rag-system-evaluation
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure your `.env` with the HuggingFace API key.

4. Run experiments using the provided Jupyter Notebooks.

## Key Insights

* Refer to [relazione.pdf](./relazione.pdf) (in Italian) for detailed analysis and insights from the experiments, or to [presentazione.pdf](./presentazione.pdf) for a summary presentation.

## Author

* [**Falbo Andrea**](https://github.com/LilQuacky)
* [**Tenderini Ruben**](https://github.com/Ruben-2828)

## License

This project is licensed under the MIT License – see the [LICENSE](./LICENSE) file for details.
