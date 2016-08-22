import sys
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils

def test_ls():
    result = h2o.ls()
    print(result)

if __name__ == "__main__":
    pyunit_utils.standalone_test(test_ls)
else:
    test_ls()
