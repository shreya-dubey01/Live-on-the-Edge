# Live-on-the-Edge
A real-time, privacy-first Vision-Language Model (VLM) navigation assistant for the visually impaired on a Raspberry Pi 5 (currently testing), entirely on edge.

By "squeezing" a 3-billion parameter Vision-Language Model (VLM) onto a Raspberry Pi 5, this project provides real-time spatial awareness and navigational advice without relying on the cloud.

<H2> Phase 1 (Current Progress) </H2>

Established the core inference engine and refined the model's "agentic" behavior to filter out environmental noise.
Key Technicalities:
- Model Selection & Quantization: Integrated Qwen2.5-VL-3B via Ollama, utilizing 4-bit GGUF quantization to fit high-level spatial reasoning into <2.5GB of RAM.
- Semantic Noise Filtering: Developed a specialized system prompt using Few-Shot Prompting to force the model to ignore non-hazards (posters, wall art) and focus exclusively on ground-level obstacles.
- Safety Heuristics: Implemented a Brightness Threshold check (Mean Pixel Intensity) to prevent model hallucinations ("Ghost Stairs") in low-light conditions or when the camera shutter is closed.
- Feedback: Established a structured output format: [Object] at [Position]. [Advice]. (e.g., "Chair at center. Veer left to bypass.").

System Prompt:
                                "You are 'Live on the Edge', a blind navigation assistant. "
                                "Identify ONLY ground-level obstacles (chairs, stairs, people). "
                                "Ignore walls, posters, or lights. If clear, say 'Path clear.' "
                                "Structure: [Object] at [Position]. [Advice]. "
                                "Examples: "
                                "'Chair at center. Veer left to bypass.' "
                                "'Person at right. Stay left to avoid.' "
                                "Constraint: Exactly 10 words total."

<img width="879" height="268" alt="image" src="https://github.com/user-attachments/assets/46043d51-3799-4526-a97a-a8b8d3537a49" />
