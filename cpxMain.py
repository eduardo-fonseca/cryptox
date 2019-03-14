import time
from threading import Thread

import cpxAPIS
import cpxDBFunctions


if __name__ == "__main__":


		t1 = Thread(target=cpxDBFunctions.db_input_gemini)
		t1.start()

		t2 = Thread(target=cpxDBFunctions.db_input_cexio)
		t2.start()

		t4 = Thread(target=cpxDBFunctions.db_input_btcbolsa)
		t4.start()

		t7 = Thread(target=cpxDBFunctions.db_input_bitfinex)
		t7.start()

		t1.join()
		t2.join()
		t4.join()
		t7.join()