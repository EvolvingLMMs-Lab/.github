# LMMs-Lab

LMMs-Lab is a research group working on large multimodal models. The public repositories cover models, training recipes, reasoning and reinforcement learning, evaluation, a shared training engine, and datasets. This page maps those entry points for someone arriving for the first time. The public name is LMMs-Lab, and model and dataset releases also appear under lmms-lab.

[![GitHub stars](https://img.shields.io/github/stars/EvolvingLMMs-Lab?style=flat&label=GitHub%20stars)](https://github.com/EvolvingLMMs-Lab)

## Start here

| If you want to | Go to |
| --- | --- |
| Read what the group publishes | [Website](https://www.lmms-lab.com/) and [posts](https://www.lmms-lab.com/posts/) |
| Evaluate a model | [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval) and the [documentation](https://docs.lmms-lab.com/docs/latest) |
| Train or fine-tune | [lmms-engine](https://github.com/EvolvingLMMs-Lab/lmms-engine), then the recipe in a model repository |
| Follow the current model line | [LLaVA-OneVision](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2), [NEO](https://github.com/EvolvingLMMs-Lab/NEO), and [OneVision-Encoder](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder) |
| Browse released weights and data | [Hugging Face](https://huggingface.co/lmms-lab) |
| Join the public chat | [Discord](https://discord.gg/zdkwKUqrPy) |

The portfolio below is grouped into models and training, reasoning and reinforcement learning, evaluation, training frameworks, and datasets.

## Models and training

### [LLaVA-OneVision](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2)

LLaVA-OneVision is an open model series for image, video, and spatial understanding. The 1.5 technical report describes a training release built around an 85-million-example concept-balanced mid-training set, a 22-million-example instruction set, and an end-to-end training framework, with 4-billion- and 8-billion-parameter models and a later reinforcement-learning post-training stage. LLaVA-OneVision-2 is an 8-billion-parameter model that uses OneVision-Encoder, windowed attention, and native-resolution inputs. Its technical report describes codec-stream tokenization, which spends a limited visual-token budget on motion and residual evidence, and a shared 3D rotary position embedding for codec canvases, sampled frames, and images. The 2.0 repository releases models, datasets, the report, and training code, including a Megatron quickstart.

1.5: [Paper](https://arxiv.org/abs/2509.23661) · [Post](https://www.lmms-lab.com/posts/llava_onevision_1_5/) · [Models and data](https://huggingface.co/collections/lmms-lab/llava-onevision-15) · [Reinforcement-learning code](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5-RL)

2.0: [Paper](https://arxiv.org/abs/2605.25979) · [Project page](https://evolvinglmms-lab.github.io/LLaVA-OneVision-2/) · [Post](https://www.lmms-lab.com/posts/llava_onevision_2/) · [Model](https://huggingface.co/lmms-lab-encoder/LLaVA-OneVision-2-8B-Instruct) · [Data](https://huggingface.co/datasets/mvp-lab/LLaVA-OneVision-2-Data)

### [NEO](https://github.com/EvolvingLMMs-Lab/NEO) (ICLR 2026)

NEO is a family of native vision-language models. Pixel and word representations sit in one dense network. The ICLR 2026 paper reports that, with 390 million image-text examples, the model learns visual perception from scratch and narrows the gap with strong modular vision-language models. The repository README also lists later models and training code in the same series.

[Paper](https://arxiv.org/abs/2510.14979) · [Models](https://huggingface.co/collections/Paranioar/neo1-0)

### [OneVision-Encoder](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder)

OneVision-Encoder is a vision encoder built around codec-style patch selection. The technical report describes selection of the high-entropy regions of an input, a range it reports as 3.1% to 25%, and a shared 3D rotary position embedding for the resulting irregular token layout. Training uses a cluster-discrimination objective over more than one million semantic concepts. When the encoder is placed in a language model, the report compares it with Qwen3-ViT and SigLIP2 on 16 image, video, and document benchmarks and reports higher scores with fewer visual tokens.

[Paper](https://arxiv.org/abs/2602.08683) · [Post](https://www.lmms-lab.com/posts/onevision_encoder/) · [Models](https://huggingface.co/collections/lmms-lab-encoder/onevision-encoder)

### [Otter](https://github.com/EvolvingLMMs-Lab/Otter) (IEEE TPAMI 2025)

Otter is a multimodal model based on OpenFlamingo. It is trained on MIMIC-IT, a dataset of 2.8 million multimodal in-context instruction-response pairs in which images or video are part of the context. The release studies instruction following and in-context learning for vision-language tasks.

[Paper](https://arxiv.org/abs/2305.03726) · [Journal version](https://doi.org/10.1109/tpami.2025.3571946) · [MIMIC-IT paper](https://arxiv.org/abs/2306.05425) · [Model](https://huggingface.co/luodian/OTTER-Image-MPT7B) · [Dataset](https://huggingface.co/datasets/pufanyi/MIMICIT)

### [LongVA](https://github.com/EvolvingLMMs-Lab/LongVA) (TMLR 2025)

LongVA studies long-context transfer from language to vision. The project reports that extending the language backbone's context lets the model take 2,000 frames, or more than 200,000 visual tokens. The TMLR paper reports state-of-the-art Video-MME and MLVU results among models around 7 billion parameters at the time of publication, using denser frame sampling, and introduces V-NIAH, a visual needle-in-a-haystack probe.

[Paper](https://arxiv.org/abs/2406.16852) · [Post](https://www.lmms-lab.com/posts/longva/) · [Models](https://huggingface.co/collections/lmms-lab/longva)

### [RelateAnything](https://github.com/EvolvingLMMs-Lab/RelateAnything)

Relate Anything takes an image, uses the Segment Anything model to produce object masks, and predicts relationships between those objects. It builds on panoptic scene graph generation (ECCV 2022).

[Demo](https://huggingface.co/spaces/mmlab-ntu/relate-anything-model) · [PSG dataset](https://psgdataset.org/)

## Reasoning and reinforcement learning

### [OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal)

OpenR1-Multimodal is a public study of the R1 training pattern on multimodal models. It adds multimodal training with Group Relative Policy Optimization (GRPO) on top of open-r1 and TRL, and releases about 8,000 multimodal reinforcement-learning examples, trained Qwen2-VL models, and the training scripts.

[Models](https://huggingface.co/lmms-lab/Qwen2-VL-2B-GRPO-8k) · [Data](https://huggingface.co/datasets/lmms-lab/multimodal-open-r1-8k-verified) · [Training logs](https://api.wandb.ai/links/libo0013/lz60ml8h)

### [OpenMMReasoner](https://github.com/EvolvingLMMs-Lab/OpenMMReasoner) (CVPR 2026)

OpenMMReasoner publishes a two-stage recipe for multimodal reasoning: supervised fine-tuning, then reinforcement learning. The paper describes an 874,000-example cold-start set with step-by-step checks and a 74,000-example reinforcement-learning set. It reports an 11.6% improvement over Qwen2.5-VL-7B-Instruct across nine multimodal reasoning benchmarks.

[Paper](https://arxiv.org/abs/2511.16334) · [Project page](https://evolvinglmms-lab.github.io/OpenMMReasoner/) · [Post](https://www.lmms-lab.com/posts/openmmreasoner/) · [Model](https://huggingface.co/OpenMMReasoner/OpenMMReasoner-RL) · [Data](https://huggingface.co/collections/lmms-lab/openmmreasoner)

### [MMSearch-R1](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) (ACL 2026)

MMSearch-R1 is an end-to-end reinforcement-learning framework that trains a multimodal model to decide when to call image and text search tools, and how to use the results across multiple turns.

[Paper](https://arxiv.org/abs/2506.20670) · [Post](https://www.lmms-lab.com/posts/mmsearch_r1/) · [Model](https://huggingface.co/lmms-lab/MMSearch-R1-7B) · [Data](https://huggingface.co/datasets/lmms-lab/FVQA)

### [LongVT](https://github.com/EvolvingLMMs-Lab/LongVT) (CVPR 2026)

LongVT trains a model to inspect long videos with a cropping tool. The model looks across the video, uses its temporal grounding to select a clip and resample frames, and repeats that loop until the answer is tied to the retrieved frames. The paper describes this as thinking with long videos through native tool calling.

[Paper](https://arxiv.org/abs/2511.20785) · [Project page](https://evolvinglmms-lab.github.io/LongVT/) · [Post](https://www.lmms-lab.com/posts/longvt/) · [Models](https://huggingface.co/collections/lmms-lab/longvt) · [Data](https://huggingface.co/datasets/longvideotool/LongVT-Parquet) · [Demo](https://huggingface.co/spaces/longvideotool/LongVT-Demo)

## Evaluation

### [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

lmms-eval is an evaluation toolkit for large multimodal models across text, image, video, and audio. The repository documents more than 100 tasks and more than 30 model backends, and the README is translated into 17 languages. The project describes its aims as reproducible runs, faster evaluation, and statistics such as confidence intervals and paired comparisons. A public site offers a hosted way to submit evaluation jobs.

[Documentation](https://docs.lmms-lab.com/docs/latest) · [PyPI](https://pypi.org/project/lmms-eval) · [Hosted evaluation](https://eval.lmms-lab.com/)

### [Multimodal SAE](https://github.com/EvolvingLMMs-Lab/multimodal-sae) (ICCV 2025)

This project studies sparse autoencoders inside multimodal models. The ICCV 2025 paper presents an automatic interpretation pipeline in which features learned on a smaller model are described by a larger one, and shows that those features can steer model outputs. The reported analysis uses LLaVA-NeXT.

[Paper](https://arxiv.org/abs/2411.14982) · [Models and data](https://huggingface.co/collections/lmms-lab/multimodal-sae)

## Training frameworks

### [lmms-engine](https://github.com/EvolvingLMMs-Lab/lmms-engine)

lmms-engine is a training codebase for multimodal models. The repository documents Fully Sharded Data Parallel (FSDP2), Ulysses sequence parallelism, tensor parallelism, expert parallelism, the Muon optimizer, Liger kernels, and sequence packing. Published examples include Qwen2.5-VL, Qwen3-VL, BAGEL, and WanVideo, among other models.

[Documentation](https://lmms-engine.readthedocs.io/en/latest/) · [PyPI](https://pypi.org/project/lmms-engine) · [Docker](https://hub.docker.com/r/kcz358/lmms-engine/tags)

## Datasets

### [EgoLife](https://github.com/EvolvingLMMs-Lab/EgoLife) (CVPR 2025)

EgoLife records a week in which six people lived together, using AI glasses and synchronized third-person video. The paper describes about 300 hours of egocentric, multiview, multimodal daily-life video. The release includes EgoGPT, for clip-level understanding, and EgoRAG, for question answering over longer stretches with a hierarchical memory.

[Paper](https://arxiv.org/abs/2503.03803) · [Project page](https://egolife-ai.github.io/) · [Data](https://huggingface.co/collections/lmms-lab/egolife)

## The Harness

The public site and documentation describe The Harness, an agent runtime. In that description, a person states a task in ordinary language, a language model writes short programs, and the runtime executes those programs in an environment the agent can observe. Documented environments include a computer desktop and a background browser, along with a terminal interface, skills, and packages.

The GitHub repository linked from the site is not publicly readable. On PyPI, `the-harness` 0.0.0 describes itself as a placeholder with no functionality, and its project page says the first functional release is still in preparation.

[Site](https://harness.lmms-lab.com/) · [Documentation](https://harness.lmms-lab.com/docs/) · [PyPI record](https://pypi.org/project/the-harness/)
