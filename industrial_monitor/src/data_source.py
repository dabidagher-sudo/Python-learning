#Data Source

class DataSource:

    def get_total_records(self):
        raise NotImplementedError
    
    def get_total_alarms(self):
        raise NotImplementedError
    
    def get_critical_alarms(self):
        raise NotImplementedError
    
    def get_alarm_summary(self):
        raise NotImplementedError
    
    def get_factory_inventory(self):
        raise NotImplementedError

