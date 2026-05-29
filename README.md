# 🏏 IPL CRUNCH '26 — Machine Learning Match Outcome Predictor

An end-to-end data analytics and predictive machine learning project built to decode historical IPL match logs and forecast team victories using structural feature engineering. 

---

## 🚀 Project Overview
This project processes raw nested historical match records (1,239 entries) to evaluate the true impact of environmental, historical, and tactical match variables on the final outcome of an Indian Premier League fixture. Rather than relying on superficial statistics, we leveraged a **Random Forest Classifier** to reveal hidden patterns across match parameters.

---

## 🎯 Key Analytical Insights & Breakthroughs

### 1. The Coin Flip Reality (Toss Statistics)
* **The Stat:** Historically, winning the toss is a near-perfect neutral event (**50.61%** win rate). 
* **The Strategy:** Teams electing to field first historically win **53.77%** of the time, leading to a strong bias toward chasing.

### 2. The AI Myth Buster (Feature Importance Results)
When training an advanced machine learning model using all environmental variables together, the model exposed a massive disconnect between popular cricket narratives and real predictive weights:
* **Team Squad Strength (41.1% combined weight):** `Team 1` (22.2%) and `Team 2` (18.9%) dictate the foundational baseline of a match.
* **Tournament Season Era (19.5% weight):** Critical feature capturing squad transitions across different mega-auction cycles.
* **Match Venue (17.9% weight):** Pitch conditions and stadium dimensions significantly sway outcomes.
* **THE REVELATION — Toss Decision (3.6% weight):** The AI officially proved that simply choosing to *bat* or *field* first holds almost **zero independent predictive power**, debunking the popular narrative that winning the toss and chasing gives a team an automatic ticket to victory.

---

## 📊 AI Model Architecture & Feature Weights

Our trained Random Forest Classifier produced the following Feature Importance Matrix:

![IPL Feature Importance Matrix](feature_importance.png

<img width="3000" height="1800" alt="feature_importance" src="https://github.com/user-attachments/assets/d5295974-65b4-461b-8adc-5ac31d82da0b" />
---

 
## 🎮 Interactive AI Match Simulator (Console CLI Application)

To bring the machine learning engine to life and demonstrate real-world utility, the repository features a standalone, interactive console-based simulator (**`predict_cli.py`**). This utility allows users, evaluators, and judges to simulate custom match scenarios directly within the terminal window without requiring a heavy browser-based frontend deployment.

### ⚙️ How to Launch the Simulator:
Simply execute the Python script using your native command prompt terminal or the Spyder IPython console:
```bash
python predict_cli.py
*"The expected output window after running the block of code would be featuring like this:"
═══════════════════════════════════════════════════════
               🔮 AI SIMULATION REPORT               
═══════════════════════════════════════════════════════
 ⚔️  MATCHUP: Mumbai Indians vs Chennai Super Kings
 🏟️  VENUE:   Wankhede Stadium | 📅 ERA: 2024
 🪙  TOSS:    Mumbai Indians elected to field first
───────────────────────────────────────────────────────
 🏆 AI PREDICTED WINNER:  👉 Mumbai Indians 👈
 📊 MODEL CONFIDENCE:      📈 54.85%
═══════════════════════════════════════════════════════



## 🛠️ Tech Stack & Technical Pipeline

* **Language:** Python 3.13 (Anaconda Environment)
* **Core Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`
* **Model Pipeline:** 1. **Data Preprocessing:** Handled missing target parameters and flattened structural features.
  2. **Feature Encoding:** Applied `LabelEncoder` across high-cardinality categorical variables (`team1`, `team2`, `venue`, `season`).
  3. **Data Partitioning:** Split data matrix into an 80% Training and 20% Testing segment.
  4. **Ensemble Training:** Trained a `RandomForestClassifier` (150 estimators, max_depth=12) to optimize multi-class prediction capabilities.

---
---

## 🔮 Future Roadmap & Strategic Scalability

To push the multi-class predictive boundary beyond the baseline accuracy of **44.35%**, the next phase of development will implement the following systemic features:
1. **Live Form Dynamics:** Engineer moving average parameters tracking individual team win-streaks and head-to-head match form over their trailing 5 matches.
2. **Granular Player Metrics:** Incorporate structural feature inputs tracking team-level squad composition values, such as total historical runs/wickets for active playing XI selections at specific venues.
3. **Advanced Boosting Architectures:** Benchmark the ensemble Random Forest baseline model against gradient-boosted structural architectures like `XGBoost` or `LightGBM` to manage non-linear boundary constraints.

## 📈 Final Model Metrics
* **Baseline Accuracy:** Successfully achieved a classification predictive accuracy of **43.55%** across over 20 unique high-cardinality historical classification output options—performing significantly better than a random baseline guess (~5%).

---

## 👥 Authors & Team Details
* **Developer Name:** Rishabh Bhardwaj  
* **Institution:** Vellore Institute of Technology (VIT)
