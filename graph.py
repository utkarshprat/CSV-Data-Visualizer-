import pandas as pd
import matplotlib.pyplot as plt


# Load CSV
def ld(f):
    try:
        d = pd.read_csv(f)
        print(f"CSV '{f}' loaded successfully.")
        return d
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


# Plot columns
def plt_d(d, x, y):
    try:
        if x not in d.columns:
            print(f"Column '{x}' not found in dataset.")
            return

        for c in y:
            if c in d.columns:
                plt.figure(figsize=(10, 6))
                plt.plot(d[x], d[c], marker='o', label=c)
                plt.title(f"{c} vs {x}", fontsize=16)
                plt.xlabel(x, fontsize=12)
                plt.ylabel(c, fontsize=12)
                plt.legend()
                plt.grid()
                plt.show()
            else:
                print(f"Column '{c}' not found in dataset.")
    except Exception as e:
        print(f"Error plotting data: {e}")
