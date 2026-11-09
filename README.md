# Master Practical Examination: AI & Machine Learning in Bioinformatics

**Course Code:** `02BMSBI24365` — AI and Machine Learning in Bioinformatics (Practical)  
**Institution:** Garden City University (GCU), School of Sciences, Department of Life Sciences  
**Programme:** Master of Science in Bioinformatics (Semester III / 25MSBI)  
**Examination Duration:** **1.5 Hours (90 Minutes)** | **Total Marks:** **50 Marks**  
**Assessment Tier:** **Tier 1: No AI** (Closed-book, unaided individual examination)  

---

## 🚀 Quick Launch in Google Colab

Students can open the examination notebook directly in Google Colab with one click:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BunnyBoss/GCU-AIML-Practical-Exam-2026/blob/main/final_practical_exam.ipynb)

*(Note: Ensure you are logged into Google Colab with your official university Google account).*

1. Click the badge above (or navigate to `File -> Open notebook -> GitHub` and enter `BunnyBoss/GCU-AIML-Practical-Exam-2026`).
2. Run **Cell 1** to initialize the clinical dataset environment.

---

## 📦 Package Requirements & Installation

### Option 1: In Google Colab
All required data science packages (`numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`) are pre-installed by default in Google Colab. Simply execute the cells. If you ever need to reinstall dependencies, execute:
```bash
!pip install -r requirements.txt
```

### Option 2: Local VS Code / Conda Environment
If executing locally on your laptop:
1. Activate your Python 3.10 virtual environment or course Conda environment:
   ```bash
   conda activate gcu-aiml-bioinfo
   ```
2. Install the required package dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `final_practical_exam.ipynb` in VS Code or Jupyter Lab, select your Python kernel, and proceed.

---

## 📁 Repository Structure

```text
├── final_practical_exam.ipynb    # Master Student Examination Notebook (50 Marks)
├── exam_data_loader.py           # Background clinical data generation & ingestion engine
├── requirements.txt              # Standardized Python package dependencies
├── .gitignore                    # Git hygiene (ignores checkpoints and cache)
└── README.md                     # Student instructions and deployment guide
```

---

## 📝 Examination Structure & Instructions

The examination consists of **25 independent questions** across three clinical & computational scenarios:

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             MASTER PRACTICAL EXAMINATION STRUCTURE (50 MARKS)                    │
├────────────┬──────────────────────────────────────────────────────────────┬────────────┬─────────┤
│ Scenario   │ Problem Domain & Paradigm                                    │ Structure  │ Marks   │
├────────────┼──────────────────────────────────────────────────────────────┼────────────┼─────────┤
│ Scenario 1 │ Liquid Biopsy Early Cancer Detection (Binary Classification) │ 10 Qs @ 2M │ 20 M    │
│ Scenario 2 │ Pharmacogenomic Drug Sensitivity Prediction (Regression)     │ 10 Qs @ 2M │ 20 M    │
│ Scenario 3 │ Neural Network Foundations (ANN Architecture & Dynamics)     │ 5 Qs @ 2M  │ 10 M    │
├────────────┼──────────────────────────────────────────────────────────────┼────────────┼─────────┤
│ Total      │ 25 Completely Independent Questions (2 Tiny Coding + 23 Th)  │ 90 Minutes │ 50 M    │
└────────────┴──────────────────────────────────────────────────────────────┴────────────┴─────────┘
```

### Guidelines for Candidates
* **100% Question Independence:** Every question is self-contained. An issue in one question will not prevent you from answering subsequent questions.
* **Minimal Code Burden:** There are only two 1–2 line coding tasks in the entire exam (Question 1.5 and Question 2.5). Scenario 3 is strictly theoretical.
* **Saving & Submission:**
  1. Click **Kernel $\to$ Restart and Run All Cells** to ensure all code outputs and scores are fully rendered.
  2. Save a personal backup: **File $\to$ Save a copy in Drive**.
  3. Download your completed file: **File $\to$ Download $\to$ Download .ipynb**.
  4. Rename the downloaded file as `[RegisterNumber]_AIML_Final_Exam.ipynb` (e.g., `25MSBI104_AIML_Final_Exam.ipynb`) and upload it to the designated course examination portal.
