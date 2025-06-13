# 🔍 Anomaly Detection with Teachable Machine

A lightweight image anomaly detection app built with [Teachable Machine](https://teachablemachine.withgoogle.com/), [TensorFlow](https://www.tensorflow.org/), and [Streamlit](https://streamlit.io/). Upload or scan product images to classify them as **Normal** or **Anomaly** using a custom-trained deep learning model.

---

## 🚀 Live Demo
Coming soon (deploy using [Streamlit Cloud](https://streamlit.io/cloud))

---

## 📸 Features

- ✅ Image classification from uploaded files
- ✅ Bonus: Real-time camera anomaly detection using OpenCV
- ✅ TensorFlow model trained using Teachable Machine
- ✅ Clean, responsive UI built with Streamlit

---

## 🛠️ Installation

```bash
git clone https://github.com/mJ2210/anomaly-detection-teachable-machine.git
cd anomaly-detection-teachable-machine
pip install -r requirements.txt
streamlit run app.py

📦 Requirements
Here are the exact dependencies used in this project:

streamlit
tensorflow==2.13.0
opencv-python
numpy
Pillow
typing-extensions==4.10.0
These are listed in requirements.txt for easy setup.

📁 Folder Structure
anomaly-detection-teachable-machine/
├── app.py                # Streamlit application
├── model.h5              # Trained model exported from Teachable Machine
├── test_images/          # Folder with sample test images
├── requirements.txt      # Python dependencies
└── README.md             # Project overview


🙌 Credits
Google Teachable Machine

TensorFlow

Streamlit

OpenCV

⭐ Star this repo if you found it useful!


Let me know if you want:
- This saved in a downloadable `README.md`
- Help deploying on **Streamlit Cloud**
- GitHub Actions to auto-run tests or deploy
