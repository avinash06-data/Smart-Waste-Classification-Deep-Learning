\# Smart Waste Classification using Deep Learning ♻️



\## Project Overview

A deep learning project that classifies waste images into two categories using a Convolutional Neural Network (CNN):

\- Organic Waste

\- Recyclable Waste



The application uses Streamlit to provide an easy interface for uploading images and viewing predictions.



\## Features

\- Image classification using CNN.

\- Organic and recyclable waste detection.

\- Image upload through Streamlit.

\- Prediction confidence display.

\- Trained using TensorFlow and Keras.



\## Technologies Used

\- Python

\- TensorFlow and Keras

\- CNN

\- NumPy

\- Matplotlib

\- Scikit-learn

\- Streamlit

\- Pillow



\## Model Architecture

\- Conv2D (32 filters) + MaxPooling

\- Conv2D (64 filters) + MaxPooling

\- Conv2D (128 filters) + MaxPooling

\- Flatten

\- Dense (128 neurons)

\- Dropout (0.5)

\- Sigmoid output layer



\## Model Performance

| Metric | Result |

|---|---:|

| Training Accuracy | 95.31% |

| Validation Accuracy | 81.25% |



\*Performance is based on a small validation dataset. Results may vary on unseen images.\*



\## Project Structure

```text

Smart\_Waste\_Classification/

├── app/

│   └── app.py

├── models/

│   └── waste\_classifier.keras

├── notebooks/

│   └── Waste\_Classification.ipynb

├── outputs/

├── requirements.txt

└── README.md

```



\## Installation and Setup



\### 1. Clone the repository

```bash

git clone https://github.com/avinash06-data/Smart-Waste-Classification-Deep-Learning.git

```



\### 2. Open the project folder

```bash

cd Smart-Waste-Classification-Deep-Learning

```



\### 3. Create a virtual environment

```bash

python -m venv waste\_env

```



\### 4. Activate the environment (Windows)

```bash

waste\_env\\Scripts\\activate

```



\### 5. Install dependencies

```bash

pip install -r requirements.txt

```



\### 6. Run the application

```bash

streamlit run app/app.py

```



\## Dataset

The training dataset is not included in this repository. The model is already trained and saved in the `models` folder.



\## Author

\*\*Avinash Helkar\*\*



GitHub: https://github.com/avinash06-data



\---

If you find this project useful, consider giving it a ⭐ on GitHub!

