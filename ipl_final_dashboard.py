# Save this file exactly as: launch_my_dashboard.py

import os
import subprocess
import webbrowser
import time
import sys  # <--- CRITICAL: This grabs your exact active Anaconda environment path!

# 1. Point to your exact project folder
target_folder = r"C:\Users\Admin\OneDrive\Desktop\material\IPL_Hacathon"
os.chdir(target_folder)

print("🚀 Initializing the Streamlit Web Server Engine using Anaconda Path...")

# 2. sys.executable forces Windows to use the EXACT Python engine running Spyder
process = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", "ipl_final_dashboard.py", "--server.port=8505", "--server.headless=true"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# 3. Give the background server 4 seconds to spin up completely
time.sleep(4)

# 4. Safety Check: If the server crashed or encountered a code typo, print the error
poll = process.poll()
if poll is not None:
    print("\n❌ Error: Streamlit server failed to start.")
    print("📋 Technical details below:")
    stdout, stderr = process.communicate()
    print(stderr)
else:
    print("🌐 Server active! Launching your interactive web browser dashboard now...")
    
    # 5. Force your computer's default web browser to open the exact local host link
    webbrowser.open("http://localhost:8505")

    print("\n" + "="*50)
    print("✨ DASHBOARD LOADED SUCCESSFULLY IN YOUR BROWSER!")
    print("👉 Check your web browser window (Chrome/Edge) to view it.")
    print("👉 Keep this Spyder console open while using the app to keep the server alive.")
    print("="*50)# Save this file exactly as: launch_my_dashboard.py

import os
import subprocess
import webbrowser
import time
import sys  # <--- CRITICAL: This grabs your exact active Anaconda environment path!

# 1. Point to your exact project folder
target_folder = r"C:\Users\Admin\OneDrive\Desktop\material\IPL_Hacathon"
os.chdir(target_folder)

print("🚀 Initializing the Streamlit Web Server Engine using Anaconda Path...")

# 2. sys.executable forces Windows to use the EXACT Python engine running Spyder
process = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", "ipl_final_dashboard.py", "--server.port=8505", "--server.headless=true"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# 3. Give the background server 4 seconds to spin up completely
time.sleep(4)

# 4. Safety Check: If the server crashed or encountered a code typo, print the error
poll = process.poll()
if poll is not None:
    print("\n❌ Error: Streamlit server failed to start.")
    print("📋 Technical details below:")
    stdout, stderr = process.communicate()
    print(stderr)
else:
    print("🌐 Server active! Launching your interactive web browser dashboard now...")
    
    # 5. Force your computer's default web browser to open the exact local host link
    webbrowser.open("http://localhost:8505")

    print("\n" + "="*50)
    print("✨ DASHBOARD LOADED SUCCESSFULLY IN YOUR BROWSER!")
    print("👉 Check your web browser window (Chrome/Edge) to view it.")
    print("👉 Keep this Spyder console open while using the app to keep the server alive.")
    print("="*50)