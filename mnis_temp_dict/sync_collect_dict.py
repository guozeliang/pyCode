import uuid
from pdbc_conn import oracleCon

if __name__ == '__main__':
    hisOrclConn = oracleCon('MOBILESERVICE/MOBILESERVICE@192.168.1.4:1521/histest')
    hisData = hisOrclConn.queryData("select t.class_code,t.vital_code,t.vital_signs,t.unit,t.dept_code from nurse_temperature_item_dict t")
    print(hisData[0])
    # 创建一个列表，后期批量插入
    list_line = []
    appOrclConn = oracleCon('mnis_user/mnis_user@192.168.1.2:1521/orcl')
    cursorObj = appOrclConn.db.cursor()
    for row in hisData:
        val0 = str(uuid.uuid4())
        val1 = row[4]
        val2 = row[1]
        val3 = row[2]
        if row[3] is None:
            val4 = ''
        else:
            val4 = row[3]
        val5 = row[0]
        # H 主要 D辅助
        if val5 == 'A':#主要护理项目
            val6 = 'S'
            val7 = 'H'
        elif val5 == 'B':#辅助护理项目
            val6 = 'S'
            val7 = 'D'
        elif val5 == 'C':#主要护理事件
            val6 = 'E'
            val7 = 'H'
        elif val5 == 'D':#辅助护理事件
            val6 = 'E'
            val7 = 'D'
        elif val5 == 'E':#其它护理项目
            val6 = 'S'
            val7 = 'H'
        else:
            val6 = ''
            val7 = ''
        list_line.append((val0,val1,val2,val3,val4,val5,val6,val7))
        print("val0:%s,val1:%s,val2:%s,val3:%s,val4:%s,val5:%s,val6:%s,val7:%s" % (val0,val1,val2,val3,val4,val5,val6,val7))
    # 执行批量插入
    cursorObj.executemany('insert into mnis_t_sign_collect_dict_bak (NID_ID, WARD_CODE, ITEM_CODE, ITEM_NAME, ITEM_UNIT, CLASS_CODE,ITEM_CLASS,ITEM_ATTRIBUTE) values(:1,:2,:3,:4,:5,:6,:7,:8)', list_line)
    # 提交事务
    appOrclConn.db.commit()
