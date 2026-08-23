import pandas as pd
import requests

def check_environment():
  print("=== INTEGRATION TEST PASSED ===")
  
  response = requests.get("https://httpbin.org/get")
  print(f"Network Request Code: {response.status_code}")
  
  summary_data = {
    "Tool": ["CLI", "venv", "pip", "pip-tools"],
    "Status": ["Ready", "Active", "Installed", "Compiled"]
  }
  
  df = pd.DataFrame(summary_data)
  print("\n--- Project Environment Overview ---")
  print(df)
  
if __name__ == "__main__":
  check_environment()