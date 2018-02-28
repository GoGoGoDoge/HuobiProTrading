import HuobiServices as hs
import datetime
import sys
import time

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python3 TradingInfo.py btcusdt 5min")
    symbol = sys.argv[1]
    period = sys.argv[2]
    waitTime = 60
    if period == '5min':
        waitTime = 300

    start_time = str(datetime.datetime.now())
    start_time = start_time.replace(":", "-").replace(" ", "-").split(".")[0]
    filename = symbol + "_" + start_time + ".csv"
    with open(filename, 'a') as f:
        f.write("time, open, close, low, high, amount, vol\n")
    try:
        while True:
            result = hs.get_kline(symbol, period, 2)
            data = result['data'][-1]
            cur_time = datetime.datetime.fromtimestamp(int(result['ts'])/1000).strftime('%Y-%m-%d %H:%M:%S')
            str_open = str(data['open'])
            str_close = str(data['close'])
            str_low = str(data['low'])
            str_high = str(data['high'])
            str_amount = str(data['amount'])
            str_vol = str(data['vol'])
            with open(filename, 'a') as f:
                data_info = cur_time + "," + str_open + "," + str_close + "," + str_low + "," + str_high + "," + str_amount + "," + str_vol + "\n"
                f.write(data_info)

    except KeyboardInterrupt:
        pass
