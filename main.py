import sqlite3 as sql


def list_to_str(row):
    ret = '('
    for item in row:
        if(type(item) == int):
            ret += str(item)
        elif(type(item) == str):
            ret += '\'%s\'' % item
        else:
            ret += str(item)
        ret += ','
    return ret[:-1]+')'


if __name__ == '__main__':

    source_path = str(input('Source browser profile address: '))
    destination_path = str(input('Destination browser profile address: '))


    conn1 = sql.connect(source_path)
    c1 = conn1.cursor()
    cursor = c1.execute('select * from keywords;')

    output_table = [['Short Name', 'Keyword', 'URL']]
    record_num = 0
    insert_values = []
    for row in cursor:
        print([row[1], row[2], row[4]])
        insert_values.append(list_to_str(row))
        record_num += 1

    conn1.close()

    print('%d records in total.' % record_num)


    insert_values_str = ''
    for i in range(0, len(insert_values)-1):
        insert_values_str += insert_values[i]+','
    insert_values_str += insert_values[-1]

    yn = input('Continue to import(Y/n)?')
    if('n' not in yn and 'N' not in yn):
        conn2 = sql.connect(destination_path)
        c2 = conn2.cursor()
        c2.execute('insert or ignore into keywords values %s;' % insert_values_str)
        print('Insert succeeded!')
        conn2.commit()
        conn2.close()
