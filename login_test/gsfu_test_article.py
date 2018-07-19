from logger import Logger
import time
from test_one_api import testApi
myLogger = Logger(logger="finish").getlog()

if __name__ == '__main__':
    start = time.time()
    endUrl = '/app/phpatientarticle/appuseagreement?aArticleCategoryId=47DE670DABEA41838356283C6E212435'
    while True:
        test = testApi()
        test.startTest(endUrl)
        myLogger.info(time.time() - start)
        myLogger.info('---------end----------')