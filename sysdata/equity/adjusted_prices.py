from sysdata.base_data import baseData
from sysobjects.equity_adjusted_prices import equityAdjustedPrices

USE_CHILD_CLASS_ERROR = "You need to use a child class of equityAdjustedPricesData"

class equityAdjustedPricesData(baseData):
    def __repr__(self):
        return USE_CHILD_CLASS_ERROR
    
    def keys(self):
        return self.get_list_of_instruments()
    
    def get_adjusted_prices(self, instrument_code: str) -> equityAdjustedPrices:
        if self.is_code_in_data(instrument_code):
            adjusted_prices = self._get_adjusted_prices_without_checking(
                instrument_code)
        else:
            adjusted_prices = equityAdjustedPrices.create_empty()
        
        return adjusted_prices
    
    def __getitem__(self, instrument_code: str) -> equityAdjustedPrices:
        return self.get_adjusted_prices(instrument_code)
    
    def delete_adjusted_prices(self, instrument_code: str, are_you_sure: bool = False):
        if are_you_sure:
            if self.is_code_in_data(instrument_code):
                self._delete_adjusted_prices_without_any_warning_be_careful(
                    instrument_code
                )
                self.log.info(
                    "Deleted adjusted price data for %s" %instrument_code,
                    instrument_code=instrument_code,
                )
            
            else:
                self.log.warning("Tried to delete non existent adjusted prices for %s"
                                 %instrument_code,
                                 instrument_code=instrument_code,)
        
        else:
            self.log.error(
                "You need to call delete_adjusted_prices with a flag to be sure",
                instrument_code=instrument_code,
            )
    
    def is_code_in_data(self, instrument_code: str) -> bool:
        if instrument_code in self.get_list_of_instruments():
            return True
        else:
            return False
        
    def add_adjusted_prices(self,
        instrument_code: str,
        adjusted_prices_data: equityAdjustedPrices,
        ignore_duplication: bool = False,
    ):
        if self.is_code_in_data(instrument_code):
            if ignore_duplication:
                pass
            else:
                self.log.error(
                    "There is already %s in the data, you have to delete it first"
                    % instrument_code,
                    instrument_code=instrument_code,
                )
        
        self._add_adjusted_prices_without_checking_for_existing_entry(
            instrument_code, adjusted_prices_data
        )

        self.log.info(
            "Added data for instrument %s" % instrument_code,
            instrument_code=instrument_code,
        )
    
    def _add_adjusted_prices_without_checking_for_existing_entry(
            self, instrument_code: str, adjusted_price_data: equityAdjustedPrices
    ):
        raise NotImplementedError(USE_CHILD_CLASS_ERROR)

    def get_list_of_instruments(self) -> list:
        raise NotImplementedError(USE_CHILD_CLASS_ERROR)
    
    def _delete_adjusted_prices_without_any_warning_be_careful(
            self, instrument_code: str
    ):
        raise NotImplementedError(USE_CHILD_CLASS_ERROR)
    
    def _get_adjusted_prices_without_checking(
            self, instrument_code: str
    ) -> equityAdjustedPrices:
        raise NotImplementedError(USE_CHILD_CLASS_ERROR)