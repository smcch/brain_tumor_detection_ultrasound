# 🧠 Real-Time Brain Tumor Detection in Intraoperative Ultrasound

This repository contains the official implementation of the method described in:

Cepeda S, Esteban-Sinovas O, Romero R, et al. **“Real-time brain tumor detection in intraoperative ultrasound: From model training to deployment in the operating room.”**  Computers in Biology and Medicine. 2025;193:110481. doi:10.1016/j.compbiomed.2025.110481

https://www.sciencedirect.com/science/article/pii/S0010482525008327

---
![graphical_abstract](https://github.com/user-attachments/assets/b8f7b0f0-95a3-4ca1-b562-1652a6c94007)

## 🚀 Overview

This repository contains the code and model checkpoint for **real-time detection of brain tumors** using intraoperative ultrasound (ioUS) and the **YOLO11** architecture.  
The system was prospectively tested in the operating room to evaluate feasibility and integration into the surgical workflow.

> ⚠️ **Disclaimer**: This software is intended for **research purposes only** and **is not approved for clinical use**.

---

## 🔍 Highlights

- Real-time brain tumor detection with 2D ioUS images
- Trained on a multicenter dataset of **1,732 annotated images**
- Prospective validation in **20 brain tumor surgeries**
- Achieves **mAP@50 = 0.95** and **FPS = 34.16** with YOLO11s
- Designed for efficient deployment on low-cost consumer-grade hardware

---

## 📁 Repository Structure

```bash
📦 RealTime-BrainTumor-Detection-YOLO11
├── inference_real_time.py     # Real-time inference script (optimized for OR)
├── inference_off_line_save.py # Offline inference from a recorded ultrasound video, saving the results with overlaid predictions
├── checkpoints(detect_s.pt)    # Trained model weights
├── LICENSE
└── README.md
```

---
## 💡 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/RealTime-BrainTumor-Detection-YOLO11.git
cd RealTime-BrainTumor-Detection-YOLO11
```

### 2. Install dependencies

```bash
conda create -n yolobrain python=3.10
conda activate yolobrain
pip install -r requirements.txt
```

### 3. Run real-time inference
🖥️ Setup Example

- Connect your ultrasound machine to your computer using a USB video capture card.
- Identify the correct camera index (e.g., 2) for the virtual camera.
- Place the trained YOLO11 model in the same directory (e.g., detect-s.pt).

Run the script:
```bash
python inference_real_time.py
```

---
🎞️ inference_off_line_save.py

Performs offline detection on a recorded ultrasound video. It processes each frame, applies our trained model, and saves a new video with overlaid predictions.

✅ Features

- Frame-by-frame processing with prediction overlay
- Saves annotated video in .mp4 format
- GPU acceleration supported
- Optional live display during processing

🛠️ Setup

Edit the script to define:
```bash
video_path = 'path/to/your_ultrasound_video.mp4'
output_video_path = 'path/to/save_annotated_video.mp4'
```
Then run:
```bash
python inference_off_line_save.py
```

## 🧪 Model Performance Summary (YOLO11s)

| Metric       | Value    |
|--------------|----------|
| mAP@50       | 0.95     |
| mAP@50-95    | 0.65     |
| Latency      | 24.9 ms  |
| FPS          | 34.16    |
| Model size   | 18.3 MB  |
| Parameters   | 9.43 M   |

---

## 🧠 About the Project

This work was developed by the [GEIBAC Group](https://geibac.uva.es),  
Specialized Group in Biomedical Imaging and Computational Analysis at IBioVALL – University of Valladolid.

---

## 🔒 License

This repository is licensed under a **non-commercial research-only license**.  
See the LICENCE file for terms.

> Contact us for licensing or collaboration requests:  
📧 [scepedac@saludcastillayleon.es](mailto:scepedac@saludcastillayleon.es)

---

## 📝 Citation

If you use this code or model in your research, please cite:

```bibtex
@article{CEPEDA2025110481,
title = {Real-time brain tumor detection in intraoperative ultrasound: From model training to deployment in the operating room},
journal = {Computers in Biology and Medicine},
volume = {193},
pages = {110481},
year = {2025},
issn = {0010-4825},
doi = {https://doi.org/10.1016/j.compbiomed.2025.110481},
url = {https://www.sciencedirect.com/science/article/pii/S0010482525008327},
author = {Santiago Cepeda and Olga Esteban-Sinovas and Roberto Romero and Vikas Singh and Prakash Shett and Aliasgar Moiyadi and Ilyess Zemmoura and Giuseppe Roberto Giammalva and Massimiliano {Del Bene} and Arianna Barbotti and Francesco DiMeco and Timothy R. West and Brian V. Nahed and Ignacio Arrese and Roberto Hornero and Rosario Sarabia},
}

@software{yolo11_ultralytics,
  author = {Glenn Jocher and Jing Qiu},
  title = {Ultralytics YOLO11},
  version = {11.0.0},
  year = {2024},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

---

## 📽️ Demo
▶️ Demo video from OR deployment

![MOVIE-0001_detect_s](https://github.com/user-attachments/assets/5cdf6cf6-f96a-4d67-8725-94f8adffd689)

