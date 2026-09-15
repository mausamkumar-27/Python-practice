import os

print("--- 🔍 Aapke Project ka Scanner Shuru ho gaya hai ---")

# 1. Dekhte hain current folder mein total kitni files hain
all_files = os.listdir()

# 2. Sirf .py (Python) files ko dhoondh kar alag karte hain
python_files = [f for f in all_files if f.endswith(".py")]

print(f"Total files in folder: {len(all_files)}")
print(f"Aapne abhi tak kitni Python (.py) files bana li hain: {len(python_files)}")

print("\nYeh rahi aapki kuch recent files ki list:")
for file in python_files[:5]:  # Pehli 5 files dikhayega
    print(f" 👉 {file}")

# 3. Ek magic trick: Ek sath 3 nayi practice files auto-generate karte hain!
print("\n--- 🪄 Magic Trick: Auto-creating files ---")
for i in range(1, 4):
    dummy_filename = f"auto_practice_{i}.py"
    if not os.path.exists(dummy_filename):
        with open(dummy_filename, "w") as f:
            f.write("# Yeh file os module ne auto-generate ki hai\nprint('Auto file working!')")
        print(f"Created: {dummy_filename}")

print("\nApne VS Code ka left sidebar check karo, wahan nayi files aagyi hongi!")