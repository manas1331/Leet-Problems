import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
  # Select data of the particular student_id 
    return students.loc[students['student_id']==101,['name','age']]
