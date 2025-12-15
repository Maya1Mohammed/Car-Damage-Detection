# Car Damage Detection System

## Project Overview

This project implements an **AI-based Car Damage Detection System** that analyzes vehicle images to:

* Detect damages on various car parts
* Identify the **damaged part** of the vehicle (e.g., bumper, door, hood)
* Serve as a foundation for **insurance assessment, repair estimation, and automation workflows**

The system is designed using **computer vision and deep learning techniques**, with a modular pipeline that can be extended to include pricing and car classification models.

---

## System Architecture

The project follows a **multi-stage AI pipeline**:

1. **Damage Detection (Object Detection)**

   * Detects damaged regions on the car
   * Identifies the damaged part
   * Typically implemented using **YOLO** or similar object detection models

2. **Car Classification (Optional / Extendable)**

   * Classifies the car brand, model, and year

3. **Damage Cost Prediction (Future Extension)**

   * Uses detected damage + car details to estimate repair cost

---

## Repository Structure

```
Car-Damage-Detection/
│
├── Media/                 # Dataset (images, annotations)
├── Model/               # Trained models / model definitions
├── Weights/            # Jupyter notebooks for training & experiments
├── requirements.txt      # Python dependencies
└── README.md
```

## Dataset Description

* Images of cars with **various types of damage**
* Annotated with:

  * Damage presence
  * Damaged part (e.g., front bumper, rear door)

The dataset can be extended to include **healthy (undamaged) cars** so the pipeline stops early when no damage is detected.

---

## Technologies Used

* **Python**
* **OpenCV**
* **YOLO (You Only Look Once)** for object detection
* **Jupyter Notebook** for experimentation

---

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Maya1Mohammed/Car-Damage-Detection.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run inference on an image:

   ```bash
   python scripts/detect_damage.py --image path_to_image
   ```

4. View results in the `results/` folder

---

## Example Output

* Bounding boxes around damaged areas
* Labels indicating damaged parts
* Confidence scores for predictions

<img width="1000" height="666" alt="run" src="https://github.com/user-attachments/assets/948c25b8-d20a-4fb1-9d65-4d298f0d45b9" />

---

## Author

**Maya Mohammed**

This project was developed as part of an exploration into **computer vision and AI-based damage assessment**.
