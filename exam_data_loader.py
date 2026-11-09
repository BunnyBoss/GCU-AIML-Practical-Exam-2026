"""
exam_data_loader.py
===================
Background Data Loader & Preprocessing Engine for Master Practical Exam
Course: 02BMSBI24365 — AI and Machine Learning in Bioinformatics
Department of Life Sciences, Garden City University (GCU)

This module generates and provides self-contained, leak-free, pre-partitioned
clinical datasets for Scenario 1 (Liquid Biopsy) and Scenario 2 (Drug Response).
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_exam_datasets(random_state=42):
    """
    Generates and returns leak-free, pre-partitioned clinical cohorts
    for Scenario 1 (Classification) and Scenario 2 (Regression).

    Returns:
    --------
    X_train, y_train, X_test, y_test : Scenario 1 (Liquid Biopsy cfDNA)
    X_train_drug, y_train_drug, X_test_drug, y_test_drug : Scenario 2 (Drug IC50)
    """
    np.random.seed(random_state)

    # =========================================================================
    # SCENARIO 1: Liquid Biopsy cfDNA Early Cancer Detection (N = 500)
    # =========================================================================
    N_cfdna = 500
    cfdna_conc = np.random.exponential(scale=15.0, size=N_cfdna) + 5.0
    cancer_latent = (cfdna_conc > 22.0).astype(int)
    short_frag = np.random.normal(loc=0.20 + 0.15 * cancer_latent, scale=0.04, size=N_cfdna)
    aberrant_motif = np.random.normal(loc=0.08 + 0.07 * cancer_latent, scale=0.02, size=N_cfdna)
    age = np.random.randint(40, 80, size=N_cfdna)

    # Latent probability model
    p_cancer = 1.0 / (1.0 + np.exp(-(0.08 * cfdna_conc + 12.0 * short_frag + 15.0 * aberrant_motif - 6.5)))
    y_cfdna = (p_cancer > 0.50).astype(int)

    # Calibrate to exactly 20% oncology prevalence (100 cancer, 400 control)
    if y_cfdna.sum() != 100:
        top_indices = np.argsort(p_cancer)[::-1]
        y_cfdna = np.zeros(N_cfdna, dtype=int)
        y_cfdna[top_indices[:100]] = 1

    X_cfdna = pd.DataFrame({
        'cfdna_concentration': np.round(cfdna_conc, 2),
        'short_fragment_ratio': np.round(np.clip(short_frag, 0.05, 0.60), 3),
        'aberrant_motif_freq': np.round(np.clip(aberrant_motif, 0.01, 0.30), 3),
        'patient_age': age
    })

    # 80/20 Stratified Partition
    X_train, X_test, y_train, y_test = train_test_split(
        X_cfdna, y_cfdna, test_size=0.20, random_state=random_state, stratify=y_cfdna
    )

    # =========================================================================
    # SCENARIO 2: Pharmacogenomic Drug Sensitivity IC50 (N = 200)
    # =========================================================================
    N_drug = 200
    kinase_expr = np.random.normal(loc=10.0, scale=2.5, size=N_drug)
    efflux_pump = np.random.normal(loc=5.0, scale=1.5, size=N_drug)
    dna_repair = np.random.normal(loc=8.0, scale=2.0, size=N_drug)
    doubling_time = np.random.normal(loc=36.0, scale=8.0, size=N_drug)

    # Linear response model with biological noise
    log_ic50 = (
        4.2
        - 1.8 * ((kinase_expr - 10.0) / 2.5)
        + 2.4 * ((efflux_pump - 5.0) / 1.5)
        + 0.6 * ((dna_repair - 8.0) / 2.0)
        + np.random.normal(0, 0.4, N_drug)
    )

    X_drug = pd.DataFrame({
        'target_kinase_expression': np.round(kinase_expr, 2),
        'efflux_transporter_activity': np.round(efflux_pump, 2),
        'dna_repair_capacity': np.round(dna_repair, 2),
        'cell_doubling_time': np.round(doubling_time, 1)
    })
    y_drug = np.round(log_ic50, 2)

    # 80/20 Partition
    X_train_drug, X_test_drug, y_train_drug, y_test_drug = train_test_split(
        X_drug, y_drug, test_size=0.20, random_state=random_state
    )

    print("=" * 78)
    print("✓ EXAMINATION ENVIRONMENT INITIALIZED SUCCESSFULLY")
    print(f"  • Scenario 1 (Liquid Biopsy cfDNA): {len(X_train)} Train samples, {len(X_test)} Test samples")
    print(f"  • Scenario 2 (Pharmacogenomic IC50): {len(X_train_drug)} Train samples, {len(X_test_drug)} Test samples")
    print("=" * 78)

    return (
        X_train, y_train, X_test, y_test,
        X_train_drug, y_train_drug, X_test_drug, y_test_drug
    )

if __name__ == "__main__":
    load_exam_datasets()
