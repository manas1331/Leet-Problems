import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
  #using shape function to calculate rows(shape[0] and columns[0])
    return[players.shape[0],players.shape[1]]
