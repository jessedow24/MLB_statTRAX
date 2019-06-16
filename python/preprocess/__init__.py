'''
Define and access a list of dates on which MLB games were played.
Use these dates to query raw stats for each batter for each game.
'''

from preprocess import service, model

save_obj = model.StoreData()
path = save_obj.get_path()
read_obj = model.ReadData(path)
read_obj.set_raw_stats_df()
read_obj.update_raw_stats_df()
save_obj.save(read_obj.get_raw_stats_df())

   




