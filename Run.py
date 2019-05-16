from spiderLib import RuleAndParamConf
import time


if __name__ == '__main__':
    while True:
        time_start = int(time.time())
        RuleAndParamConf.RuleAndParamConf().pengpai()
        RuleAndParamConf.RuleAndParamConf().rmw()
        RuleAndParamConf.RuleAndParamConf().xlcj()
        RuleAndParamConf.RuleAndParamConf().ke()
        RuleAndParamConf.RuleAndParamConf().zgjj()
        RuleAndParamConf.RuleAndParamConf().zgkj()
        time_end = int(time.time())
        time_cost = time_end - time_start
        f = open('./companyName/timeCost.txt', 'a')
        f.write(str(time_cost)+',')
        f.close()
        time.sleep(60)


