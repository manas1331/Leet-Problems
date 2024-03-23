# Printing the first three rows
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
  # Prints the first three rows
    return employees.head(3)
