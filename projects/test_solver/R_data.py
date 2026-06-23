import pandas as pd
import os

def analyze_resistances(start_index=1, end_index=47):
    """
    Reads each periphery file (p1.csv to p47.csv), extracts all resistor values,
    prints the value of R0 and the sum of all resistances (R0 + R1 + ...).
    Automatically handles slight column header differences and avoids SettingWithCopy warnings.
    """

    base_path = os.path.join("..", "..", "models", "Abel_ref2")

    print(f"\n--- Resistance Summary for Peripheries p{start_index}–p{end_index} ---\n")

    for i in range(start_index, end_index + 1):
        filename = os.path.join(base_path, f"p{i}.csv")

        if not os.path.exists(filename):
            print(f"[p{i:02d}] File not found. Skipping.")
            continue

        try:
            # Read CSV, skipping first "data of edges" line
            df = pd.read_csv(filename, skiprows=1, header=0)

            # Normalize column names (remove spaces, lowercase)
            df.columns = df.columns.str.strip().str.lower()

            # Identify resistance column (parameter)
            param_col = next((col for col in df.columns if 'parameter' in col), None)
            if param_col is None:
                print(f"[p{i:02d}] No parameter column found.")
                continue

            # Filter only resistor rows — make a copy to avoid warnings
            resistors = df[df['type'].str.strip().str.lower() == 'resistor'].copy()

            if resistors.empty:
                print(f"[p{i:02d}] No resistors found.")
                continue

            # Convert resistance column to numeric
            resistors.loc[:, param_col] = pd.to_numeric(resistors[param_col], errors='coerce')

            # Extract R0 value (if exists)
            r0_row = resistors[resistors['name'].str.strip().str.upper() == 'R0']
            r0_value = float(r0_row[param_col].iloc[0]) if not r0_row.empty else None

            # Compute total resistance
            total_resistance = resistors[param_col].sum()

            # Display result
            if r0_value is not None:
                print(f"[p{i:02d}]  R0 = {r0_value:.3e} Ω,   R_total = {total_resistance:.3e} Ω")
            else:
                print(f"[p{i:02d}]  R0 not found,   R_total = {total_resistance:.3e} Ω")

        except Exception as e:
            print(f"[p{i:02d}] Error reading {filename}: {e}")

    print("\n--- Analysis Complete ---\n")


# Run it
if __name__ == "__main__":
    analyze_resistances(start_index=1, end_index=47)
