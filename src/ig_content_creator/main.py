# src/ig_content_creator/main.py
import json
from ig_content_creator.crew import IGContentCreatorCrew
from ig_content_creator.image_client import SegmindClient
import os

def run(topic: str):
    inputs = {"topic": topic}
    crew = IGContentCreatorCrew().crew()

    result = crew.kickoff(inputs=inputs)

    research_out = result.get("research_task")  
    write_out = result.get("write_task")
    review_out = result.get("review_task")
    prompt_out = result.get("prompt_task")


    package = {
        "topic": topic,
        "research": research_out,
        "draft": write_out,
        "reviewed": review_out,
        "prompts": prompt_out
    }
    os.makedirs("output", exist_ok=True)
    with open("output/final_package.json", "w", encoding="utf-8") as f:
        json.dump(package, f, indent=2, ensure_ascii=False)


    prompts = prompt_out.get("prompts", []) if prompt_out else []
    if prompts:
        sg = SegmindClient()
        images = sg.generate_from_prompts(prompts, width=1024, height=1024, samples=1)

        for i, img_bytes in enumerate(images):
            with open(f"output/image_{i+1}.png", "wb") as imf:
                imf.write(img_bytes)
    print("Done. Outputs in /output")

if __name__ == "__main__":
    topic = "AI in Healthcare"  
    run(topic)
