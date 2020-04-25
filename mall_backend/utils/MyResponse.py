"""
restful 统一返回JSON数据格式 ----
"""

class MyResponse(ResponseBase):
    def __init__(self,code,msg,data):
        self.code = code
        self.msg = msg
        self.data = data

        super().__init__()

    def