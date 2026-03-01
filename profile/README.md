# LMMs-Lab: Building Multimodal Intelligence

We are a group of researchers, with a focus on large multimodal models (LMMs). We wish to bring insights to community with our research. 

[Discord](https://discord.gg/8xTM6jWnXa)

![GitHub User's stars](https://img.shields.io/github/stars/EvolvingLMMs-Lab)

---

## 🏗️ Models & Training

### [LLaVA-OneVision 1.5](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5) ⭐ 754

A fully open-source family of Large Multimodal Models achieving state-of-the-art performance at substantially lower cost. Trains on native resolution images with an end-to-end MegatronLM-based framework supporting MoE, FP8, and long sequence parallelization — all for under $16,000 on A100 GPUs. Outperforms Qwen2.5-VL on most benchmarks. Includes open pre-training & SFT data, training code, recipes, and full logs.

🤗 [Models & Datasets](https://huggingface.co/collections/lmms-lab/llava-onevision-15-68d385fe73b50bd22de23713) | 🖥️ [Demo](https://huggingface.co/spaces/lmms-lab/LLaVA-OneVision-1.5) | 📄 [Tech Report](https://github.com/anxiangsir/asset/blob/main/paper/LLaVA_OneVision_1_5.pdf)

### [NEO](https://github.com/EvolvingLMMs-Lab/NEO) ⭐ 653 `NeurIPS 2025`

NEO Series: Native Vision-Language Models built from first principles. Rethinks the multimodal architecture by deeply integrating vision and language capabilities rather than bolting them together, resulting in a more coherent and capable vision-language model.

### [OneVision-Encoder](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder) ⭐ 269 `CVPR 2025`

A vision encoder designed around codec-aligned sparsity as a foundational principle for multimodal intelligence. Provides an efficient visual backbone that aligns with how information is compressed and represented, improving downstream LMM performance.

🌐 [Project Page](https://lmms-lab.com/onevision-encoder/index.html)

### [Otter](https://github.com/EvolvingLMMs-Lab/Otter) ⭐ 3.3k `IEEE TPAMI 2025`

A multi-modal model based on OpenFlamingo (the open-sourced version of DeepMind's Flamingo), trained on the MIMIC-IT dataset. Demonstrates improved instruction-following capabilities across vision-language tasks and served as an early exploration into instruction-tuned multimodal models.

### [LongVA](https://github.com/EvolvingLMMs-Lab/LongVA) ⭐ 402 `TMLR 2025`

Transfers long-context capabilities from language to vision. Enables multimodal models to handle extended visual contexts by leveraging the long-context understanding already developed in LLMs, achieving strong performance on long-form video and multi-image understanding tasks.

### [RelateAnything](https://github.com/EvolvingLMMs-Lab/RelateAnything) ⭐ 462

The Relate Anything Model (RAM) takes an image as input and leverages SAM to identify corresponding masks, then reasons about relationships between any detected objects. An early exploration into open-vocabulary visual relationship understanding.

---

## 🧠 Reasoning & Reinforcement Learning

### [OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal) ⭐ 1.5k

A speed-run investigation of R1's paradigm applied to multimodal models. Built on top of `open-r1` and `trl`, this project adds multimodal model training with the GRPO algorithm, enabling reasoning capabilities in vision-language models through reinforcement learning.

### [OpenMMReasoner](https://github.com/EvolvingLMMs-Lab/OpenMMReasoner) ⭐ 145 `CVPR 2026`

An open and general recipe for pushing the frontiers of multimodal reasoning. Provides a systematic framework for training LMMs with enhanced reasoning abilities across diverse visual and multimodal tasks.

### [MMSearch-R1](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) ⭐ 402

An end-to-end RL framework that enables LMMs to perform on-demand, multi-turn search with real-world multimodal search tools. Trains models to autonomously decide when and how to search for information during multimodal reasoning.

### [LongVT](https://github.com/EvolvingLMMs-Lab/LongVT) ⭐ 195 `CVPR 2026`

Incentivizes "Thinking with Long Videos" via native tool calling. Teaches multimodal models to actively use tools (e.g., frame extraction, temporal search) while reasoning over long video content, rather than passively processing all frames.

---

## 📊 Evaluation & Analysis

### [LMMS-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) ⭐ 3.8k

A one-for-all evaluation framework for large multimodal models, covering text, image, video, and audio tasks. Designed for consistent and efficient benchmarking, lmms-eval supports a wide variety of evaluation benchmarks and models, serving as the community standard for measuring LMM capabilities.

### [Multimodal-SAE](https://github.com/EvolvingLMMs-Lab/multimodal-sae) ⭐ 183 `ICCV 2025`

An auto interpretation pipeline and toolkit for multimodal Sparse Autoencoder (SAE) analysis. Enables researchers to understand what multimodal models learn internally by decomposing representations into interpretable features.

---

## 🔬 Training Frameworks

### [LMMs-Engine](https://github.com/EvolvingLMMs-Lab/lmms-engine) ⭐ 735

A simple, unified multimodal model training engine. Lean, flexible, and built for hacking at scale — designed to make multimodal model training accessible and efficient without the complexity of heavyweight frameworks.

---

## 🌍 Datasets & Benchmarks

### [EgoLife](https://github.com/EvolvingLMMs-Lab/EgoLife) ⭐ 399 `CVPR 2025`

For one week, six individuals lived together, capturing every moment through AI glasses, creating the EgoLife dataset. Built to drive the future of AI life assistants capable of recalling past events, tracking habits, and providing personalized, long-context assistance. This multi-personal, multi-view, multimodal, long-term setting unlocks new frontiers for AI assistants with deeper understanding.
