import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = os.path.join(PROJECT_PATH, 'config', 'config.ini')
YAML = os.path.join(PROJECT_PATH, 'config', 'config.yml')
CASE_INI = os.path.join(PROJECT_PATH, 'case.ini')
CORE = os.path.join(PROJECT_PATH, 'core')
TEST_CASE = os.path.join(PROJECT_PATH, 'test_case')
BASE_CASE_DATA = os.path.join(PROJECT_PATH, 'test_data', 'base_case_data')
CSV_CASE_DATA = os.path.join(PROJECT_PATH, 'test_data', 'csv_case_data')
TEST_PHOTO = os.path.join(PROJECT_PATH, 'test_data', 'test_photo')
TEST_LOG = os.path.join(PROJECT_PATH, 'test_log')
TEST_REPORT = os.path.join(PROJECT_PATH, 'test_report')
UTILS = os.path.join(PROJECT_PATH, 'utils')
