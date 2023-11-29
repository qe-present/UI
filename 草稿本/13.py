import requests
from faker import Faker
import pandas as pd


# df=pd.read_csv('station.csv',index_col='name')
class Ticket:
    def __init__(self,train_date,from_station,to_station):
        self.url = 'https://kyfw.12306.cn/otn/leftTicket/query'
        self.station=pd.read_csv('station.csv',index_col='name')
        self.params = {
            'leftTicketDTO.train_date': f'{train_date}',
            'leftTicketDTO.from_station': f'{self.get_code(from_station)}',
            'leftTicketDTO.to_station': f'{self.get_code(to_station)}',
            'purpose_codes': 'ADULT',
        }
        self.headers = {
            'User-Agent': Faker().user_agent(),
            'Cookie': f'_jc_save_toStation={self.get_code(to_station)};',
        }
    def get_code(self,name):
        return self.station.loc[name,'code']
    def send_request(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        json_data = response.json()
        return json_data['data']['result']
    def parse(self,data):
        for i in data:
            t = i.split('|')
            train_no = t[2]  # 火车参数
            che = t[3]  # 车次
            startcode = t[4]  # 出发地代号
            endcode = t[5]  # 目的地代号
            from_station_no = t[16]  # 发车地代号
            to_station_no = t[17]  # 终点代号
            seat_types = t[35]  # 座位类型
            starttime = t[8]  # 出发时间
            endtime = t[9]  # 到站时间
            duration_time = t[10]  # 持续时间
            special_shop_seat = t[32] or t[25] or '--'  # 商务座/特等座，二者数据所处位置不一样
            first_seat = t[31] or '--'  # 一等座
            second_seat = t[30] or '--'  # 二等座
            high_sleep = t[21] or '--'  # 高级软卧
            soft_sleep = t[23] or '--'  # 软卧
            dong_sleep = t[33] or '--'  # 动卧
            hard_sleep = t[28] or '--'  # 硬卧
            sort_seat = t[24] or '--'  # 软座
            hart_seat = t[29] or '--'  # 硬座
            no_seat = t[26] or '--'  # 站票
            print(che)

    @staticmethod
    def start(date,start_station,end_station):
        ticket=Ticket(train_date=date,from_station=start_station,to_station=end_station)
        data=ticket.send_request()
        ticket.parse(data)
Ticket.start('2023-11-12','北京','上海')
