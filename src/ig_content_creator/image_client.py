# src/ig_content_creator/image_client.py
import os
from typing import List

try:
    from segmind import Segmind
    SEGMINd_AVAILABLE = True
except Exception:
    SEGMINd_AVAILABLE = False
    import requests

SEGMIND_API_KEY = os.getenv("SEGMIND_API_KEY")
SEGMIND_BASE_URL = "https://api.segmind.com/v1/generate"  

class SegmindClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or SEGMIND_API_KEY
        if not self.api_key:
            raise ValueError("Set SEGMIND_API_KEY in env")

    def generate_from_prompts(self, prompts: List[str], width=1024, height=1024, samples=1) -> List[bytes]:
        """
        Send prompts to Segmind and return raw image bytes as list.
        Adjust the exact payload per Segmind model docs: this is a guidance template.
        """
        headers = {"Authorization": f"Bearer {self.api_key}"}
        images = []
        for prompt in prompts:
            payload = {
                "model": "stable-diffusion-3.5-large-txt2img", 
                "prompt": prompt,
                "width": width,
                "height": height,
                "samples": samples
            }
            if SEGMINd_AVAILABLE:

                client = Segmind(api_key=self.api_key)

                res = client.text2img(model=payload["model"], prompt=prompt, width=width, height=height)

                for b64 in res.images:
                    import base64
                    images.append(base64.b64decode(b64))
            else:
                r = requests.post(SEGMIND_BASE_URL, json=payload, headers=headers, timeout=60)
                r.raise_for_status()
                data = r.json()

                import base64
                images.append(base64.b64decode(data["images"][0]))
        return images
