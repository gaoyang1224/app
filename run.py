import pytest
from common.handle_path import REPORT_DIR

pytest.main(['-s', '-v', '--alluredir={}'.format(REPORT_DIR)])
