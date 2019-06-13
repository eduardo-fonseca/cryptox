import time
from threading import Thread

import cpxAPIS
import cpxDBFunctions


if __name__ == "__main__":

   
        t1 = Thread(target=cpxDBFunctions.db_input_bitstamp)
        t1.start()
        
        t2 = Thread(target=cpxDBFunctions.db_input_gemini)
        t2.start()
        
        t3 = Thread(target=cpxDBFunctions.db_input_cexio)
        t3.start()
        
        t4 = Thread(target=cpxDBFunctions.db_input_okcoin)
        t4.start()
        
        t5 = Thread(target=cpxDBFunctions.db_input_hitbtc)
        t5.start()
        
        t6 = Thread(target=cpxDBFunctions.db_input_poloniex)
        t6.start()
        
        t7 = Thread(target=cpxDBFunctions.db_input_bitfinex)
        t7.start()
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()