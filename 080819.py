class logger:
    log = {}
    
    def __init__(self):
        self.log["count"] = 0

    def record(self,order_id):
        self.log[str(self.log["count"])] = order_id
        self.log["count"] += 1

    def get_last(self,i):
        return self.log[str(self.log["count"] - i)]

