from nba_api.stats.endpoints import playergamelog
import pandas as pd



gamelog_bron = playergamelog.PlayerGameLog(player_id='2544', season = '2018')

df_bron_games_2018 = gamelog_bron.get_data_frames()

# If you want all seasons, you must import the SeasonAll parameter
from nba_api.stats.library.parameters import SeasonAll

gamelog_bron_all = playergamelog.PlayerGameLog(player_id='2544', season = SeasonAll.all)

df_bron_games_all = gamelog_bron_all.get_data_frames()
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# print(df_bron_games_all)