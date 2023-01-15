import os
import pytest

# if __name__ == '__main__':
#     pytest.main()
#     os.system("pytest --alluredir ./result --allure-features='qualityPlatform'")
pytest.main(["--alluredir=result/allure-results", "--junitxml=result/xml-report/result.xml"])
