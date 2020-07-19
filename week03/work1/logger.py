import json
import logging
import logging.handlers
import os
import time

class Logger:
  def __init__(self, record_to_json):
    # 1. 创建logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 2. 创建一个handler，用于写入日志文件
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    if not os.path.isdir('./logs'):
        os.mkdir('./logs')
    log_path = os.path.dirname(os.getcwd()) + '/work1/logs/'
    log_name = log_path + rq + '.log'
    logfile = log_name
    fh = logging.FileHandler(logfile, mode='w')
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    # 3. 定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    self.rp_logger = logger

    if record_to_json:
      record_logger = logging.getLogger('file_logger')
      record_logger.setLevel(logging.INFO)
      json_formatter = logging.Formatter('%(asctime)s: %(message)s')
      if not os.path.isdir('./logs'):
        os.mkdir('./logs')
      record_handler = logging.handlers.RotatingFileHandler('logs/result.json', maxBytes=20)
      record_handler.setFormatter(json_formatter)
      
      record_logger.addHandler(record_handler)
      self.record_logger = record_logger
    
    
  def log(self, ip, port, result, elapsed):
    msg = f'ip={ip}'
    if port != 0:
      msg = f' {msg} port={port}'
    msg = f' {msg} result={result}'
    if elapsed >= 0:
      msg = f' {msg} elapsed={elapsed}'
    self.logger.info(msg)
    if self.record_logger is not None:
      d = {'time': time.time(), 'ip': ip}
      if port != 0:
        d['port'] = port
      if elapsed >= 0:
        d['elapsed'] = elapsed
      self.record_logger.info(json.dumps(d))
