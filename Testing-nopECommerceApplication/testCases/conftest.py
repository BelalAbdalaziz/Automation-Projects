import pytest
from selenium import webdriver
#======================================================================
#=============== To Run Project on several browsers ===================
#======================================================================
# 1) Add --browser option to CLI  
def pytest_addoption(parser):
    parser.addoption("--browser")
# 2) Get value which is after --browser       --> @pytest.fixture()
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
# 3) setup browser (You must know this is first method will run into test project)  --> @pytest.fixture()
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser ............... ")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser ............... ")
    else:
        driver = webdriver.Edge()
        print("Launching Edge Browser ............... ")
    return driver
#==================================================================
#===================== To Creat HTML Reports ======================
#==================================================================
#0) Title Of Html Report
def pytest_html_report_title(report):
    report.title = "nopCommerce Testing Report "
# 1) To modify the Environment section after tests are run
from pytest_metadata.plugin import metadata_key
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["Project Name"] = "nopCommerce"
    session.config.stash[metadata_key]["Module Name "] = "Customer"
    session.config.stash[metadata_key]["Tester "] = "Belal Abdalaziz"

#2) To delete/Modify Environment info to to html report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
#3) To Insert Duration to each test case    
import datetime
def pytest_html_duration_format(duration):
    duration_timedelta = datetime.timedelta(seconds=duration)
    time = datetime.datetime(1, 1, 1) + duration_timedelta
    return time.strftime("%H:%M:%S")
#4) Modifying Result Table
'''
#add Column
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')
#Add Row Related to column
def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(1, f'<td class="col-time">{datetime.datetime.now(datetime.UTC)}</td>')
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
'''
#===================== To Append New Logs With old Logs in the same log file ======================
import shutil
# 1) Creat backub from old file 
def pytest_configure(config):
    log_file = config.rootpath / config.getini("log_file")
    if log_file.is_file():
        config._backup = log_file.with_name(".log.bak")
        shutil.copy(log_file, config._backup)

# 2) merge backub with new log file
@pytest.hookimpl(trylast=True)
def pytest_unconfigure(config):
    log_file = config.rootpath / config.getini("log_file")
    if log_file.is_file():
        log_backup = getattr(config, "_backup", None)
        if log_backup and log_backup.is_file():
            log_file.write_text(log_backup.read_text() + log_file.read_text())
            log_backup.unlink()