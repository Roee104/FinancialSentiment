# FinancialSentiment

**Project Overview**  
A pipeline to produce overall and per‐sector sentiment for financial news articles.

## Folder Structure

FinancialSentiment/
├─ data/
│ ├─ raw/ ← Full FNSPID JSONL files go here
│ ├─ sampled/ ← 10k‐article sample & stats
│ └─ attribution/ ← Chunk‐level CSVs (real, synthetic)
├─ notebooks/ ← EDA and training notebooks
├─ scripts/ ← Python scripts for data prep, training, inference
├─ models/ ← Saved model checkpoints
├─ reports/ ← Interim and final presentations
├─ requirements.txt ← Python dependencies
└─ README.md ← This file