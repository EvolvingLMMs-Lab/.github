# LMMs-Lab: Building Multimodal Intelligence

We are a group of researchers, with a focus on large multimodal models (LMMs). We wish to bring insights to community with our research. 

Here're a few of our projects.

## [LMMS-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval)

<p align="center">
    <img src="https://i.postimg.cc/KvkLzbF9/WX20241212-014400-2x.png" width="60%">
</p>

We're on an exciting journey toward creating Artificial General Intelligence (AGI), much like the enthusiasm of the 1960s moon landing. This journey is powered by advanced large language models (LLMs) and large multimodal models (LMMs), which are complex systems capable of understanding, learning, and performing a wide variety of human tasks.

To gauge how advanced these models are, we use a variety of evaluation benchmarks. These benchmarks are tools that help us understand the capabilities of these models, showing us how close we are to achieving AGI. To address this challenge, we introduce lmms-eval, an evaluation framework meticulously crafted for consistent and efficient evaluation of LMM.

## [LLaVA-NeXT](https://llava-vl.github.io/blog/2024-05-10-llava-next-stronger-llms/)

<p align="center">
    <img src="./assets/llava-next.png" width="75%">
</p>

We expanded the LLaVA-NeXT series with recent stronger open LLMs, reporting our findings on more capable language models:
We maintain an efficient training strategy like previous LLaVA models. We supervised finetuned our model on the same data as in previous LLaVA-NeXT 7B/13B/34B models. Our current largest model LLaVA-NeXT-110B is trained on 128 H800-80G for 18 hours.

With stronger LLMs support, LLaVA-NeXT achieves consistently better performance compared with prior open-source LMMs by simply increasing the LLM capability. It catches up to GPT4-V on selected benchmarks.

We report detailed ablations, including architectural modifications, enlarged visual tokens, and varied training strategies, to explore potential improvements in LLaVA-NeXT's performance.

## [LLaVA-NeXT-Video](https://llava-vl.github.io/blog/2024-04-30-llava-next-video/)

<p align="center">
    <img src="./assets/llava-next-video.png" width="100%">
</p>

We explore LLaVA-NeXT's capabilities in video understanding tasks, highlighting its strong performance. Key improvements include:

**SoTA Performance!** Without seeing any video data, LLaVA-Next demonstrates strong zero-shot modality transfer ability, outperforming all the existing open-source LMMs (e.g., LLaMA-VID) that have been specifically trained for videos. Compared with proprietary ones, it achieves comparable performance with Gemini Pro on NextQA and ActivityNet-QA.

**Strong length generalization ability** Despite being trained under the sequence length constraint of a 4096-token limit, LLaVA-Next demonstrates remarkable ability to generalize to longer sequences. This capability ensures robust performance even when processing long-frame content that exceeds the original token length limitation.

**DPO pushes performance** DPO with AI feedback on videos yields significant performance gains.

