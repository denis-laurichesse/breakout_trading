from ib_insync import IB, CFD, util
from datetime import timedelta
import time

ib = IB().connect('127.0.0.1', 7496, clientId=1)
c  = CFD('XAUUSD'); ib.qualifyContracts(c)

bars, end = [], ''
while True:
    chunk = ib.reqHistoricalData(c, end, '1 W', '5 mins', 'MIDPOINT', True, 1)
    if not chunk: break
    bars[:0] = chunk
    end = (chunk[0].date - timedelta(minutes=5)).strftime('%Y%m%d %H:%M:%S')
    time.sleep(0.5)

util.df(bars)[['date', 'open', 'high', 'low', 'close']].to_csv('XAUUSD_5min.csv.gz', index=False, compression='gzip')

ib.disconnect()
