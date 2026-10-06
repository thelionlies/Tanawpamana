# Tanawpamana

A dataset and benchmark for evaluating vision-language models on Philippine cultural heritage sites.

- **Tanawpamana Dataset**: 499 images of Philippine cultural heritage sites with metadata from the
  NCCA Talapamana registry (Philippine Registry of Heritage): names, locations, heritage category,
  and official designations.
- **Tanawpamana Benchmark**: 4,046 four-option multiple-choice questions testing recognition of
  the sites and knowledge about them.

## Contents

```
dataset/
  Tanawpamana.csv            site information, one row per site (499)
  Tanawpamana_license.csv    source, author and license of every image
  images/                    one image per site, {ID}.jpg (hosted on Hugging Face)
benchmark/
  recognition/               4 recognition tasks (.jsonl)
  knowledge/                 5 knowledge tasks (.jsonl)
download_images.py           downloads the images from Hugging Face into dataset/images/
```

## Benchmark tasks

| Task | File | Questions | The model is asked to… |
|---|---|---|---|
| Image-to-Name (Easy / Hard) | `recognition/image_to_name_{easy,hard}.jsonl` | 499 / 481 | pick the site's name from its image |
| Name-to-Image (Easy / Hard) | `recognition/name_to_image_{easy,hard}.jsonl` | 499 / 481 | pick the site's image from its name |
| General Information | `knowledge/gen_info.jsonl` | 365 | identify the site described by a historical fact |
| Short Description | `knowledge/short_desc.jsonl` | 481 | identify the site from its heritage category and area |
| Location (Text) | `knowledge/location_text.jsonl` | 499 | give the area (Metro Manila, Luzon, Visayas, Mindanao) of a named site |
| Location (Image) | `knowledge/location_image.jsonl` | 499 | give the area of the site in an image |
| Designation | `knowledge/designation.jsonl` | 242 | identify the site that holds a given official designation |

Easy and Hard differ in how similar the wrong options are to the correct one.

Each line of a `.jsonl` file is one question with `id`, `prompt`, `options` (A–D), `answer`,
`answer_label`, and `metadata`; image questions also have an `image` field. Image paths
(e.g. `images/TP00042.jpg`) are relative to the `dataset/` folder.

## Getting the images

The images are hosted on Hugging Face:
[thelionlies/tanawpamana-dataset](https://huggingface.co/datasets/thelionlies/tanawpamana-dataset).

```bash
pip install huggingface_hub
python download_images.py   # downloads the 499 images (Hugging Face tag v1.0) into dataset/images/
```

## Known issues

- **Location tasks.** The four options are always in the same order (Metro Manila, Luzon, Visayas,
  Mindanao), so the answer distribution follows the area distribution: always answering "Luzon"
  scores 34.7%, not 25%.
- **Designation task.** Designation labels reflect the Talapamana registry as of early 2026 and may
  become outdated as the registry is updated.
- Question IDs are unique but not continuous (some numbers are skipped).

## Licenses

**Images.** Each image keeps the license of its source; see `dataset/Tanawpamana_license.csv`
(`IMAGE_SOURCE`, `IMAGE_SOURCE_URL`, `IMAGE_AUTHOR`, `IMAGE_LICENSE`, `IMAGE_LICENSE_URL`,
`IMAGE_MODIFICATIONS`). Most images are from Wikimedia Commons under CC BY-SA, CC BY, CC0 or
public domain. All images were cropped where needed to remove overlaid text, resized so the
longer side is at most 1,024 px, and stripped of embedded metadata. Images credited to Philippine
government agencies are works of the Government of the Philippines (RA 8293, Sec. 176) and are
provided for non-commercial use.

**Everything else.** The metadata created for this dataset and the benchmark questions are released
under the
[Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) (see `LICENSE`).
Site descriptions in `dataset/Tanawpamana.csv` are taken from the NCCA Talapamana registry.

## Citation

If you use Tanawpamana, please cite:

```bibtex
@inproceedings{deleon2026tanawpamana,
  title     = {Tanawpamana: Benchmarking Vision-Language Models on Philippine Cultural Heritage Sites},
  author    = {De Leon, Ivan Yuri and Ouchi, Hiroki and Sakti, Sakriani},
  booktitle = {Proceedings of the 29th Conference of the Oriental COCOSDA (O-COCOSDA 2026)},
  year      = {2026},
  note      = {To appear}
}
```
