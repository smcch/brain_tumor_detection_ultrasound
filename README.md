# 🧠 Real-Time Brain Tumor Detection in Intraoperative Ultrasound using YOLO11

> From Model Training to Deployment in the Operating Room  
> *Santiago Cepeda, Olga Esteban-Sinovas, et al.*  
> Under review in *Computers in Biology and Medicine*

---

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
├── checkpoints(yolo11n.pt)    # Trained model weights
├── LICENSE
└── README.md

💡 Getting Started
1. Clone the repo

git clone https://github.com/your-username/RealTime-BrainTumor-Detection-YOLO11.git
cd RealTime-BrainTumor-Detection-YOLO11


2. Install dependencies

conda create -n yolobrain python=3.10
conda activate yolobrain
pip install -r requirements.txt

3. Run real-time inference

python inference_real_time.py

🧪 Model Performance Summary (YOLO11n)
Metric	Value
mAP@50	0.94
mAP@50-95	0.68
Latency	30.3 ms
FPS	25.98
Model size	5.23 MB
Params	2.59 M
🧠 About the Project

This work was developed by the GEIBAC Group,
Specialized Group in Biomedical Imaging and Computational Analysis at IBioVALL – University of Valladolid.
🔒 License

This repository is licensed under a non-commercial research-only license.
See the LICENSE file for terms.

    Contact us for licensing or collaboration requests:
    📧 scepedac@saludcastillayleon.es

📝 Citation

If you use this code or model in your research, please cite our preprint:

@article{Cepeda2025YOLO11,
  title={Real-Time Brain Tumor Detection in Intraoperative Ultrasound Using YOLO11: From Model Training to Deployment in the Operating Room},
  author={Cepeda, Santiago and Esteban-Sinovas, Olga and others},
  journal={Computers in Biology and Medicine},
  note={Under Review},
  year={2025}
}

📽️ Demo Video and Image


https://github.com/user-attachments/assets/335fdf47-0ff3-4257-a274-80b429b9732c


▶️ Demo video from OR deployment 

