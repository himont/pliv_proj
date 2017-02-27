# pliv_proj
This project is for automation of Plivo apis. Though requirements are as per following link 
https://docs.google.com/document/d/1iaQl6Q4v97HxiQ2FnE6-T0vM-zrsgPJ4xsVOATyfcR4/edit

Planned it in such a way that many more cases of any api can be added

### Steps to setup:
> git clone https://github.com/himont/pliv_proj.git
> cd pliv_proj
> git clone https://github.com/tungwaiyip/HTMLTestRunner.git
> touch HTMLTestRunner/__init__.py
> create virtual environment, activate it and do 'pip install -r requirements.txt'
> sudo mkdir /var/log/api_automation
> sudo chmod -R 777 /var/log/api_automation

### To execute:
For now created a sample runner which will execute assignment along with couple of other test cases. Need to execute following command to start execution.
* python test_runner.py

### Test Report and logs:
- Test report is generated in HTML format at TestReports folder.
- Every test report has timestamp in its name.
- Logging of the entire test flow is done at /var/log/api_automation/automation.log.
- Logs keep on rotating every day
