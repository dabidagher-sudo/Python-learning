#Report Manager
from src.service import *
from datetime import datetime
from openpyxl import Workbook

class ReportManager:
    def __init__(self,config):
        self.config=config
        self.report_folder= self.config["report_folder"]

    def generate_csv_report(self):
        loginfo_print("Generating CSV report...")
    
    def generate_summary(self):
        loginfo_print("Generating KPI summary...")

    def create_report_name(self, file_ext):
        return f"{self.report_folder}/KPI_report_{datetime.now().strftime('%Y_%m_%d_%H_%M')}.{file_ext}"
    
    def generate_excel_report(self):
        workbook = Workbook()

        sheet = workbook.active
        sheet.title = "Summary"

        sheet["A1"] = "Industrial Monitor KPI Report"
        sheet["A3"] = "Generated at"
        sheet["B3"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sheet["A5"] = "Total Machines"
        sheet["B5"] = 0

        sheet["A6"] = "Total Alarms"
        sheet["B6"] = 0

        sheet["A7"] = "Critical Alarms"
        sheet["B7"] = 0

        workbook.create_sheet(title="Alarm Summary")
        sheet2 = workbook["Alarm Summary"]

        sheet2["A3"] = "Alarm Type"
        sheet2["B3"] = "Count"

        sheet2["A4"] = "Machine Stopped"
        sheet2["B4"] = 0

        sheet2["A5"] = "Critical Temperature Alarm"
        sheet2["B5"] = 0


        filename = self.create_report_name("xlsx")

        workbook.save(filename)
        loginfo_print("Excel report generated: "+ filename)




