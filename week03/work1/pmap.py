
# 命令行选项、参数和子命令解析器
import argparse
# 使用多线程、多进程
import concurrent.futures as futuresObj
import util
import logger


class HostScanner:
    """
        num: 并发数
        mode: 扫描方式 ping/tcp
        host: 指定地址
        store: 保存结果为json
        future: 使用运行方式 多线程/多进程
        runtime: 计算运行耗时
    """
    def __init__(self, num, mode, host, store, future, runtime):   
        try:
            ip_range = util.parse_ip_range(host)

            self.ip_start = ip_range[0]
            self.ip_end = ip_range[1]
            self.num = num
            self.mode = mode
            self.future = future
            self.runtime = runtime
            
            self.logger = logger.Logger(store > 0)

            self.task_gen = self.task_generator()
        except Exception as e:
            self.logger.rp_logger.error(e)
    def task_generator(self):
        if self.mode == 'tcp':
            for int32_ip in range(self.ip_start, self.ip_end + 1):
                str_ip = util.int2ip(int32_ip)
                for port in range(1, 65535 + 1):
                    yield util.is_port_open, str_ip, port
        else:
            for int32_ip in range(self.ip_start, self.ip_end + 1):
                yield util.ping_host, util.int2ip(int32_ip)

    def run(self):
        try:
            pool = futuresObj.ProcessPoolExecutor
            if self.future == 'thread':
                pool = futuresObj.ThreadPoolExecutor

            with pool(max_workers=self.num) as executor:
                futures = {}
                for t in self.task_gen:
                    func = t[0]
                    args = list(t)
                    args.pop(0)
                    # 记录耗时
                    if self.runtime:
                        future = executor.submit(util.measure_time, func, *args)
                    else:
                        future = executor.submit(func, *args)

                    futures[future] = t

                for f in futuresObj.as_completed(futures):
                    tt = futures[f]
                    ip = tt[1]
                    port = 0
                    if len(tt) == 3:
                        port = tt[2]
                    r = f.result()
                    self.logger.log(ip, port, r[0], r[1])
        except Exception as e:
            self.logger.rp_logger.error(e)

def create_parser():
    """定义接收命令的参数"""
    parser = argparse.ArgumentParser(description='using the host scanner')
    parser.add_argument('-n', type=int, default=2, help='specify the number of concurrent')
    parser.add_argument('-f', type=str, choices=['ping', 'tcp'], default='ping', help='specify test mode')
    parser.add_argument('-ip', type=str, help='ip address supports 192.168.0.1-192.168.0.100', required=True)
    parser.add_argument('-w', action='count', default=0, help='store scan results')
    parser.add_argument('-m', type=str, choices=['proc', 'thread'], default='proc', help='specifies to use the multi process or multi thread model')
    parser.add_argument('-v', action='count', default=0, help='print scanner takes time to run', required=False)
    args = parser.parse_args()
    return args
    
if __name__ == '__main__':
    parser = create_parser()
    scanner = HostScanner(parser.n, parser.f, parser.ip, parser.w, parser.m, parser.v)
    scanner.run()
    

