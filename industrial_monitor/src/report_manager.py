#Report Manager
from src.service import loginfo_print
from datetime import datetime

class ReportManager:
    def __init__(self,config):
        self.config=config
        self.report_folder= self.config["report_folder"]

    def generate_csv_report(self):
        loginfo_print("Generating CSV report...")
    
    def generate_summary(self):
        loginfo_print("Generating KPI summary...")

    def create_report_name(self):
        return f"KPI_report_{datetime.now().strftime('%Y_%m_%d_%H_%M')}.csv"

