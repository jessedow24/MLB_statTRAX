from process import batter_processing
import preprocess

batter_raw = preprocess.read_obj.get_raw_stats_df()

batter_clean_obj = batter_processing.RawBatter(batter_raw)
batter_clean_obj.process_batter()
batter_clean = batter_clean_obj.get_processed_batter()
batter_clean.sort_values(['NAME', 'DATE'], ascending=[False, True], inplace=True)

batter_stats_obj = batter_processing.CleanBatter(batter_clean)
batter_stats_obj.set_output()
batter_stats = batter_stats_obj.get_output()