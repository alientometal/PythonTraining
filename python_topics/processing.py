import pandas as pd
from layout_config import LAYOUT_MAPPING, COLUMNS_MAPPING

class ProcessFile():
    def __init__(self, filename):
        self._filename = filename
        
        self.clean_data()
    
    def clean_data(self):
    
        def _read_file():
            with open(self._filename, "r") as Pfile:
                self.string = Pfile.read()  
            
            return  
        
        def _get_layout():
            get_interval = lambda target_string, interval: target_string[interval[0] -1:interval[1]] 
            self.layout = {key:get_interval(self.string, interval) for key, interval in LAYOUT_MAPPING.items()}
            
            return
    
        def _process_layout():
            self.layout_df = pd.DataFrame.from_dict(self.layout, orient="index").T
            self.layout_df[["OPERATION DATE", "VALUATION DATE"]] = self.layout_df[["OPERATION DATE", "VALUATION DATE"]].apply(pd.to_datetime)
            self.layout_df.rename(columns=COLUMNS_MAPPING, inplace=True)
            return
        
        def _set_final_dataframe():
            self.transaction_df = self.layout_df['PORTFOLIO_ID', 'TRADE_DATE', 'SETTLE_DATE', 'AMOUNT'].copy()
            self.transaction_df
            return
        
        # main function(clean_data)
        _read_file()
        _get_layout()
        _process_layout()
        _set_final_dataframe()
        
        return
    
