"""Download the Tanawpamana images from Hugging Face into dataset/images/.

Usage (from the repository root):
    pip install huggingface_hub
    python download_images.py
"""
import os

from huggingface_hub import snapshot_download

HF_DATASET_REPO = "thelionlies/tanawpamana-dataset"
HF_REVISION = "v1.0"  # the image set used in the paper

DATASET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")

if __name__ == "__main__":
    snapshot_download(repo_id=HF_DATASET_REPO, repo_type="dataset", revision=HF_REVISION,
                      allow_patterns=["images/*.jpg"], local_dir=DATASET_DIR)
    n = len([f for f in os.listdir(os.path.join(DATASET_DIR, "images")) if f.endswith(".jpg")])
    print(f"{n} images in {os.path.join(DATASET_DIR, 'images')}")
