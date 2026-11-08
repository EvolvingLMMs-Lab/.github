# LMMs-Lab

LMMs-Lab researches large multimodal models that see, hear, and act, and that learn from feedback on their actions. The public work includes open models, training recipes, evaluation, and datasets.

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

## Models and training

### [LLaVA-OneVision](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-2)

LLaVA-OneVision is an open series for image, video, and spatial understanding. Version 1.5 releases training data, code, and models. Version 2.0 uses OneVision-Encoder with native-resolution inputs and codec-style visual tokens for long video.

1.5: [Paper](https://arxiv.org/abs/2509.23661) · [Post](https://www.lmms-lab.com/posts/llava_onevision_1_5/) · [Models and data](https://huggingface.co/collections/lmms-lab/llava-onevision-15) · [Reinforcement-learning code](https://github.com/EvolvingLMMs-Lab/LLaVA-OneVision-1.5-RL)

2.0: [Paper](https://arxiv.org/abs/2605.25979) · [Project page](https://evolvinglmms-lab.github.io/LLaVA-OneVision-2/) · [Post](https://www.lmms-lab.com/posts/llava_onevision_2/) · [Model](https://huggingface.co/lmms-lab-encoder/LLaVA-OneVision-2-8B-Instruct) · [Data](https://huggingface.co/datasets/mvp-lab/LLaVA-OneVision-2-Data)

### [NEO](https://github.com/EvolvingLMMs-Lab/NEO) (ICLR 2026)

NEO is a family of native vision-language models that encode pixels and words in one dense network. The models learn visual perception from scratch.

[Paper](https://arxiv.org/abs/2510.14979) · [Models](https://huggingface.co/collections/Paranioar/neo1-0)

### [OneVision-Encoder](https://github.com/EvolvingLMMs-Lab/OneVision-Encoder)

OneVision-Encoder is a vision encoder that selects and encodes the high-entropy regions of an image or video. The technical report compares it with Qwen3-ViT and SigLIP2 and reports higher scores with fewer visual tokens.

[Paper](https://arxiv.org/abs/2602.08683) · [Post](https://www.lmms-lab.com/posts/onevision_encoder/) · [Models](https://huggingface.co/collections/lmms-lab-encoder/onevision-encoder)

### [Otter](https://github.com/EvolvingLMMs-Lab/Otter) (IEEE TPAMI 2025)

Otter is a multimodal model based on OpenFlamingo, trained on MIMIC-IT. MIMIC-IT is a dataset of multimodal in-context instructions over images and video, and Otter studies instruction following and in-context learning.

[Paper](https://arxiv.org/abs/2305.03726) · [Journal version](https://doi.org/10.1109/tpami.2025.3571946) · [MIMIC-IT paper](https://arxiv.org/abs/2306.05425) · [Model](https://huggingface.co/luodian/OTTER-Image-MPT7B) · [Dataset](https://huggingface.co/datasets/pufanyi/MIMICIT)

### [LongVA](https://github.com/EvolvingLMMs-Lab/LongVA) (TMLR 2025)

LongVA transfers long context from a language model to vision. The release can take long videos, on the order of 2,000 frames, without separate long-video training.

[Paper](https://arxiv.org/abs/2406.16852) · [Post](https://www.lmms-lab.com/posts/longva/) · [Models](https://huggingface.co/collections/lmms-lab/longva)

### [RelateAnything](https://github.com/EvolvingLMMs-Lab/RelateAnything)

Relate Anything takes an image, uses Segment Anything to produce object masks, and predicts relationships between those objects. It builds on panoptic scene graph generation (ECCV 2022).

[Demo](https://huggingface.co/spaces/mmlab-ntu/relate-anything-model) · [PSG dataset](https://psgdataset.org/)

## Reasoning and reinforcement learning

### [OpenR1-Multimodal](https://github.com/EvolvingLMMs-Lab/open-r1-multimodal)

OpenR1-Multimodal applies Group Relative Policy Optimization to multimodal models, using open-r1 and TRL. It releases training examples, Qwen2-VL models, and the training scripts.

[Models](https://huggingface.co/lmms-lab/Qwen2-VL-2B-GRPO-8k) · [Data](https://huggingface.co/datasets/lmms-lab/multimodal-open-r1-8k-verified) · [Training logs](https://api.wandb.ai/links/libo0013/lz60ml8h)

### [OpenMMReasoner](https://github.com/EvolvingLMMs-Lab/OpenMMReasoner) (CVPR 2026)

OpenMMReasoner is an open recipe for multimodal reasoning in two stages: supervised fine-tuning, then reinforcement learning. The release includes data, models, and training code.

[Paper](https://arxiv.org/abs/2511.16334) · [Project page](https://evolvinglmms-lab.github.io/OpenMMReasoner/) · [Post](https://www.lmms-lab.com/posts/openmmreasoner/) · [Model](https://huggingface.co/OpenMMReasoner/OpenMMReasoner-RL) · [Data](https://huggingface.co/collections/lmms-lab/openmmreasoner)

### [MMSearch-R1](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) (ACL 2026)

MMSearch-R1 trains a multimodal model, with reinforcement learning, to decide when to call image and text search and how to use the results across turns.

[Paper](https://arxiv.org/abs/2506.20670) · [Post](https://www.lmms-lab.com/posts/mmsearch_r1/) · [Model](https://huggingface.co/lmms-lab/MMSearch-R1-7B) · [Data](https://huggingface.co/datasets/lmms-lab/FVQA)

### [LongVT](https://github.com/EvolvingLMMs-Lab/LongVT) (CVPR 2026)

LongVT trains a model to answer questions about long videos by cropping to relevant clips and inspecting those frames more closely. It repeats that loop until the answer is tied to the retrieved video.

[Paper](https://arxiv.org/abs/2511.20785) · [Project page](https://evolvinglmms-lab.github.io/LongVT/) · [Post](https://www.lmms-lab.com/posts/longvt/) · [Models](https://huggingface.co/collections/lmms-lab/longvt) · [Data](https://huggingface.co/datasets/longvideotool/LongVT-Parquet) · [Demo](https://huggingface.co/spaces/longvideotool/LongVT-Demo)

## Evaluation

### [lmms-eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

lmms-eval evaluates large multimodal models on text, image, video, and audio. The repository covers a large set of tasks and model backends, and a public site accepts hosted evaluation jobs.

[Documentation](https://docs.lmms-lab.com/docs/latest) · [PyPI](https://pypi.org/project/lmms-eval) · [Hosted evaluation](https://eval.lmms-lab.com/)

### [Multimodal SAE](https://github.com/EvolvingLMMs-Lab/multimodal-sae) (ICCV 2025)

Multimodal SAE studies sparse autoencoders inside multimodal models. A larger model interprets features learned in a smaller one, and those features can steer the model's outputs.

[Paper](https://arxiv.org/abs/2411.14982) · [Models and data](https://huggingface.co/collections/lmms-lab/multimodal-sae)

## Training frameworks

### [lmms-engine](https://github.com/EvolvingLMMs-Lab/lmms-engine)

lmms-engine is a training codebase for multimodal models. It supports sharded data parallel, sequence parallelism, and expert parallelism, with examples for Qwen2.5-VL, Qwen3-VL, BAGEL, and WanVideo.

[Documentation](https://lmms-engine.readthedocs.io/en/latest/) · [PyPI](https://pypi.org/project/lmms-engine) · [Docker](https://hub.docker.com/r/kcz358/lmms-engine/tags)

## Datasets

### [EgoLife](https://github.com/EvolvingLMMs-Lab/EgoLife) (CVPR 2025)

EgoLife records one week of daily life from six people wearing AI glasses, together with synchronized third-person video. The release includes EgoGPT for clip-level understanding and EgoRAG for question answering over longer stretches.

[Paper](https://arxiv.org/abs/2503.03803) · [Project page](https://egolife-ai.github.io/) · [Data](https://huggingface.co/collections/lmms-lab/egolife)

## The Harness

The Harness is an agent runtime with a public website and documentation. Those docs describe a task stated in ordinary language, short programs written by a language model, and execution in an environment the agent can observe, including a computer desktop and a background browser. Explore the public site and documentation.

[Site](https://harness.lmms-lab.com/) · [Documentation](https://harness.lmms-lab.com/docs/)
