import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
  # Table_Header Info
    header_names=['student_id','age']
  # Printing the final Table after the changes
    final_dataframe=pd.DataFrame(student_data,columns=header_names)
    return(final_dataframe)
