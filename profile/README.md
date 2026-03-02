# LMMs-Lab: Building Multimodal Intelligence

We are a group of researchers, with a focus on large multimodal models (LMMs). We wish to bring insights to community with our research. 

[Discord](https://discord.gg/8xTM6jWnXa)

![GitHub User's stars](https://img.shields.io/github/stars/EvolvingLMMs-Lab)

---

## 🏗️ Models & Training

### [LLaVA-OneVision 1.5](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5) ⭐ 754

A fully open-source family of Large Multimodal Models achieving state-of-the-art performance at substantially lower cost. Trains on native resolution images with an end-to-end MegatronLM-based framework supporting MoE, FP8, and long sequence parallelization — all for under $16,000 on A100 GPUs. Outperforms Qwen2.5-VL on most benchmarks. Includes open pre-training & SFT data, training code, recipes, and full logs.

🤗 [Models & Datasets](https://huggingface.co/collections/lmms-lab/llava-onevision-15-68d385fe73b50bd22de23713) | 🖥️ [Demo](https://huggingface.co/spaces/lmms-lab/LLaVA-OneVision-1.5) | 📄 [Tech Report](https://arxiv.org/abs/2509.23661)

### [NEO](https://github.com/EvolvingLMMs-Lab/NEO) ⭐ 653 `ICLR 2026`

NEO Series: Native Vision-Language Models built from first principles. Rethinks the multimodal architecture by deeply integrating vision and language capabilities within a dense, monolithic model architecture, rather than bolting a vision encoder onto a language model. With merely 390M image-text examples, NEO develops strong visual perception from scratch, rivaling top-tier modular VLMs and outperforming native ones.

📄 [Paper](https://arxiv.org/abs/2510.14979) | 🤗 [Models](https://huggingface.co/collections/Paranioar/neo1-0-68f0db9cbac952be3eca7089)

### [OneVision-Encoder](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder) ⭐ 269 

A vision encoder designed around codec-aligned sparsity as a foundational principle for multimodal intelligence. Abandons uniform computation to selectively encode only 3.1%-25% of regions rich in signal entropy, consistently outperforming Qwen3-ViT and SigLIP2 across 16 image, video, and document understanding benchmarks despite using substantially fewer visual tokens.

🌐 [Project Page](https://www.lmms-lab.com/onevision-encoder/index.html) | 📄 [Paper](https://arxiv.org/abs/2602.08683) | 🤗 [Models](https://huggingface.co/collections/lmms-lab-encoder/onevision-encoder)

### [Otter](https://github.com/EvolvingLMMs-Lab/Otter) ⭐ 3.3k `IEEE TPAMI 2025`

A multi-modal model based on OpenFlamingo (the open-sourced version of DeepMind's Flamingo), trained on the MIMIC-IT dataset with 2.8M multimodal in-context instruction-response pairs. Demonstrates improved instruction-following and in-context learning capabilities across vision-language tasks and served as an early exploration into instruction-tuned multimodal models.

📄 [Otter Paper](https://arxiv.org/abs/2305.03726) | 📄 [MIMIC-IT Paper](https://arxiv.org/abs/2306.05425) | 🤗 [Models](https://huggingface.co/luodian/OTTER-Image-MPT7B) | 🤗 [MIMIC-IT Dataset](https://huggingface.co/datasets/pufanyi/MIMICIT)

### [LongVA](https://github.com/EvolvingLMMs-Lab/LongVA) ⭐ 402 `TMLR 2025`

Transfers long-context capabilities from language to vision. LongVA can process 2000 frames or over 200K visual tokens, achieving state-of-the-art performance on Video-MME among 7B models — demonstrating that long context capability can zero-shot transfer from language to vision.

🌐 [Blog](https://lmms-lab.github.io/posts/longva/) | 📄 [Paper](https://arxiv.org/abs/2406.16852) | 🤗 [Models](https://huggingface.co/collections/lmms-lab/longva-667538e09329dbc7ea498057) | 🎥 [Demo](https://longva-demo.lmms-lab.com/)

### [RelateAnything](https://github.com/EvolvingLMMs-Lab/RelateAnything) ⭐ 462

The Relate Anything Model (RAM) takes an image as input and leverages SAM to identify corresponding masks, then reasons about relationships between any detected objects. Built on the Panoptic Scene Graph Generation work (ECCV 2022).

🤗 [Demo](https://huggingface.co/spaces/mmlab-ntu/relate-anything-model) | 📦 [PSG Dataset](https://psgdataset.org/)

---

## 🧠 Reasoning & Reinforcement Learning

### [OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal) ⭐ 1.5k

A speed-run investigation of R1's paradigm applied to multimodal models. Built on top of `open-r1` and `trl`, this project adds multimodal model training with the GRPO algorithm, open-sourcing 8K multimodal RL training examples, trained models, and training scripts for community study on multimodal reasoning.

🤗 [Models](https://huggingface.co/lmms-lab/Qwen2-VL-2B-GRPO-8k) | 🤗 [Datasets](https://huggingface.co/datasets/lmms-lab/multimodal-open-r1-8k-verified) | 📊 [Wandb Logs](https://api.wandb.ai/links/libo0013/lz60ml8h)

### [OpenMMReasoner](https://github.com/EvolvingLMMs-Lab/OpenMMReasoner) ⭐ 145 `CVPR 2026`

A fully transparent two-stage recipe (SFT + RL) for pushing the frontiers of multimodal reasoning. Constructs an 874K-sample cold-start dataset with step-by-step validation and a 74K-sample RL dataset, achieving 11.6% improvement over Qwen2.5-VL-7B-Instruct across nine multimodal reasoning benchmarks.

📄 [Paper](https://arxiv.org/abs/2511.16334) | 🌐 [Project Page](https://evolvinglmms-lab.github.io/OpenMMReasoner/) | 🤗 [Models](https://huggingface.co/OpenMMReasoner/OpenMMReasoner-RL) | 🤗 [Data](https://huggingface.co/collections/lmms-lab/openmmreasoner) | 🌐 [Blog](https://www.lmms-lab.com/posts/openmmreasoner/)

### [MMSearch-R1](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) ⭐ 402

An end-to-end RL framework that enables LMMs to perform on-demand, multi-turn search with real-world multimodal search tools. Integrates both image and text search capabilities, training models to autonomously reason about when and how to invoke external search tools.

📄 [Paper](https://arxiv.org/abs/2506.20670) | 🌐 [Blog](https://www.lmms-lab.com/posts/mmsearch_r1) | 🤗 [Model](https://huggingface.co/lmms-lab/MMSearch-R1-7B) | 🤗 [Data](https://huggingface.co/datasets/lmms-lab/FVQA)

### [LongVT](https://github.com/EvolvingLMMs-Lab/LongVT) ⭐ 195 `CVPR 2026`

Incentivizes "Thinking with Long Videos" via native tool calling. LongVT exploits LMMs' inherent temporal grounding ability as a native video cropping tool, enabling a global-to-local reasoning loop where the model skims globally and examines relevant clips for details until answers are grounded in visual evidence.

📄 [Paper](https://arxiv.org/abs/2511.20785) | 🌐 [Project Page](https://evolvinglmms-lab.github.io/LongVT/) | 🤗 [Models](https://huggingface.co/collections/lmms-lab/longvt) | 🤗 [Data](https://huggingface.co/datasets/longvideotool/LongVT-Parquet) | 🖥️ [Demo](https://huggingface.co/spaces/longvideotool/LongVT-Demo) | 🌐 [Blog](https://www.lmms-lab.com/posts/longvt/)

---

## 📊 Evaluation & Analysis

### [LMMS-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) ⭐ 3.8k

The unified evaluation toolkit for large multimodal models, covering 100+ tasks across text, image, video, and audio. Supports 30+ models with reproducible, efficient, and statistically grounded benchmarking. Available on PyPI and translated into 17 languages.

🏠 [Homepage](https://www.lmms-lab.com/) | 📚 [Documentation](https://github.com/EvolvingLMMs-Lab/lmms-eval/blob/main/docs/README.md) | 📦 [PyPI](https://pypi.org/project/lmms-eval)

### [Multimodal-SAE](https://github.com/EvolvingLMMs-Lab/multimodal-sae) ⭐ 183 `ICCV 2025`

For the first time in the multimodal domain, demonstrates that features learned by Sparse Autoencoders (SAEs) in a smaller LMM can be interpreted by a larger LMM. Provides a complete auto-interpretation pipeline for analyzing open-semantic features and steering model behavior.

📄 [Paper](https://arxiv.org/abs/2411.14982) | 🤗 [Models & Data](https://huggingface.co/collections/lmms-lab/llava-sae-674026e4e7bc8c29c70bc3a3)

---

## 🔬 Training Frameworks

### [LMMs-Engine](https://github.com/EvolvingLMMs-Lab/lmms-engine) ⭐ 735

A simple, unified multimodal model training engine. Supports FSDP2, USP, Muon optimizer, Liger kernel, packing, and expert parallelism across models like Qwen2.5-VL, Qwen3-VL, BAGEL, WanVideo, and more. Lean, flexible, and built for hacking at scale.

🐳 [Docker](https://hub.docker.com/r/fatbao55/lmms-engine/tags) | 📦 [PyPI](https://pypi.org/project/lmms-engine)

---

## 🌍 Datasets & Benchmarks

### [EgoLife](https://github.com/EvolvingLMMs-Lab/EgoLife) ⭐ 399 `CVPR 2025`

For one week, six individuals lived together, capturing every moment through AI glasses, creating the EgoLife dataset. Includes EgoGPT (omni-modal clip-level understanding) and EgoRAG (long-context QA with hierarchical memory). Built to drive the future of egocentric AI life assistants.

📄 [Paper](https://arxiv.org/abs/2503.03803) | 🌐 [Project Page](https://egolife-ai.github.io/) | 🤗 [Data](https://huggingface.co/collections/lmms-lab/egolife-67c04574c2a9b64ab312c342)
