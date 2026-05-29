# Save this file exactly as: ipl_ml_advanced.py

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Establish workspace path environment
target_folder = r"C:\Users\Admin\OneDrive\Desktop\material\IPL_Hacathon"
os.chdir(target_folder)

print("🔄 Loading dataset for Advanced Feature Engineering...")
df = pd.read_csv('ipl_matches_clean.csv')

# Drop any blank row values across our expanded metrics list
df = df.dropna(subset=['team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'venue', 'season'])

# 2. Fit Categorical Label Encoders
le_team = LabelEncoder()
all_teams = pd.concat([df['team1'], df['team2'], df['toss_winner'], df['winner']]).unique()
le_team.fit(all_teams)

# Encode our core team structures
df['encoded_team1'] = le_team.transform(df['team1'])
df['encoded_team2'] = le_team.transform(df['team2'])
df['encoded_toss_winner'] = le_team.transform(df['toss_winner'])

# Encode our strategic toss decision matrix
le_decision = LabelEncoder()
df['encoded_toss_decision'] = le_decision.fit_transform(df['toss_decision'])

# --- ADVANCED FEATURES: Add Venue and Season tracking to help the model learn trends ---
le_venue = LabelEncoder()
df['encoded_venue'] = le_venue.fit_transform(df['venue'])

le_season = LabelEncoder()
df['encoded_season'] = le_season.fit_transform(df['season'].astype(str))

# 3. Update the Feature Array (X) with our new environmental layers
X = df[['encoded_team1', 'encoded_team2', 'encoded_toss_winner', 'encoded_toss_decision', 'encoded_venue', 'encoded_season']]
y = le_team.transform(df['winner'])

# 4. Partition data matrix (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize and train our upgraded Random Forest Model
print("🤖 Training the Advanced Match Predictor Model...")
# Tuning hyperparameters (n_estimators and max_depth) to find stronger decision splits
model = RandomForestClassifier(n_estimators=150, max_depth=12, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate accuracy metrics
y_pred = model.predict(X_test)
advanced_accuracy = accuracy_score(y_test, y_pred)

print("\n" + "="*40)
print(f"🎯 UPGRADED AI MODEL PERFORMANCE")
print(f"📊 Advanced Predictive Model Accuracy: {advanced_accuracy * 100:.2f}%")
print(f"📈 Net improvement over basic model: {(advanced_accuracy - 0.4435)*100:+.2f}%")
print("="*40)