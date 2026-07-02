#Main program for industrial monitoring

import json
from src.service import *
from src.report_manager import ReportManager

config = start_aplication()
report_manager = ReportManager(config)
report_manager.generate_csv_report()
report_manager.generate_excel_report()
report_manager.generate_summary()

shutdown_aplication()

