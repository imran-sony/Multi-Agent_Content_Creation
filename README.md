# 📸 Multi-Agent System for Automated Instagram Content Creation
Using CrewAI + LLMs + Segmind Image Generation

This project implements a complete multi-agent pipeline that automatically researches a topic, writes Instagram captions, reviews the content, and generates high-quality image prompts which are then turned into final visuals using an external text-to-image API.

Built with CrewAI for orchestration and LLMs for agent intelligence.

🚀 Features
✔ 1. Multi-Agent Workflow

The system uses four specialized agents:

Agent	Responsibility
🧭 Research Agent	Gathers accurate information, stats, and angles related to the topic
✍️ Writer Agent	Creates short & long captions, hashtags, and CTAs
🕵️ Reviewer Agent	Refines and approves the final content
🎨 Image Prompt Agent	Creates professional text-to-image prompts


✔ 2. Automated Instagram Post Package

For any topic (e.g., “AI in Healthcare”, “Future of Electric Cars”), the system outputs:

📌 Short caption

📝 Long caption

🔖 Final approved hashtags

🎯 Call-to-action (CTA)

🎨 Three high-quality image prompts


