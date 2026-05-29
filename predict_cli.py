# Save this file exactly as: predict_cli.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

print("🏏 Loading IPL Historical Dataset and Initializing AI Engine...")
df = pd.read_csv('ipl_matches_clean.csv').dropna(subset=['winner'])

# 1. Re-fit Encoders exactly like your training pipeline
features = ['team1', 'team2', 'venue', 'season', 'toss_winner', 'toss_decision']
encoders = {}
for col in features + ['winner']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# 2. Train the production Random Forest model
X = df[features]
y = df['winner']
model = RandomForestClassifier(n_estimators=150, max_depth=12, random_state=42)
model.fit(X, y)

def get_user_choice(item_list, item_name):
    print(f"\n--- Select {item_name} ---")
    for i, item in enumerate(item_list):
        print(f"[{i}] {item}")
    while True:
        try:
            choice = int(input(f"Enter the number for {item_name}: "))
            if 0 <= choice < len(item_list):
                return item_list[choice]
        except ValueError:
            pass
        print("❌ Invalid selection. Try again.")

# 3. Interactive Menu Interface Loop
unique_teams = sorted(list(encoders['team1'].classes_))
unique_venues = sorted(list(encoders['venue'].classes_))
unique_seasons = sorted(list(encoders['season'].classes_))

print("\n" + "="*50)
print("🎯 WELCOME TO THE IPL AI MATCH PREDICTOR SIMULATOR")
print("="*50)

t1 = get_user_choice(unique_teams, "Team 1 (Home/Batting First)")
# Remove Team 1 from options for Team 2 to prevent playing against itself
remaining_teams = [team for team in unique_teams if team != t1]
t2 = get_user_choice(remaining_teams, "Team 2 (Away/Bowling First)")
venue = get_user_choice(unique_venues, "Match Venue Stadium")
season = get_user_choice(unique_seasons, "Tournament Season/Era")
toss_w = get_user_choice([t1, t2], "Toss Winner")
toss_d = get_user_choice(['bat', 'field'], "Toss Decision")

# 4. Transform user text strings into the exact numbers the AI understands
input_data = pd.DataFrame([{
    'team1': encoders['team1'].transform([t1])[0],
    'team2': encoders['team2'].transform([t2])[0],
    'venue': encoders['venue'].transform([venue])[0],
    'season': encoders['season'].transform([season])[0],
    'toss_winner': encoders['toss_winner'].transform([toss_w])[0],
    'toss_decision': encoders['toss_decision'].transform([toss_d])[0]
}])

# 5. Compute Prediction and Class Probabilities
pred_encoded = model.predict(input_data)[0]
pred_team = encoders['winner'].inverse_transform([pred_encoded])[0]

probs = model.predict_proba(input_data)[0]
classes = encoders['winner'].classes_

# Extract confidence score for the predicted team
pred_idx = np.where(classes == pred_team)[0][0]
confidence = probs[pred_idx] * 100

# 6. Print Out a Beautiful Prediction Card Report
print("\n" + "═"*55)
print("               🔮 AI SIMULATION REPORT               ")
print("═"*55)
print(f" ⚔️  MATCHUP: {t1} vs {t2}")
print(f" 🏟️  VENUE:   {venue} | 📅 ERA: {season}")
print(f" 🪙  TOSS:    {toss_w} elected to {toss_d} first")
print("─"*55)
print(f" 🏆 AI PREDICTED WINNER:  👉 {pred_team} 👈")
print(f" 📊 MODEL CONFIDENCE:      📈 {confidence:.2f}%")
print("═"*55)