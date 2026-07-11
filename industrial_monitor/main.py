#Main program for industrial monitoring

import json
from src.service import *
from src.report_manager import ReportManager
from src.sqlite_data_source import SQLiteDataSource



config = start_aplication()
data_source = SQLiteDataSource(config["database_file"])
report_manager = ReportManager(config,data_source)
report_manager.generate_csv_report()
report_manager.generate_excel_report()
report_manager.generate_summary()



shutdown_aplication()

