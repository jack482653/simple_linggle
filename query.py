#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import shelve

tags = {'CC', 'CD', 'DT', 'EX', 'FW',
        'IN', 'JJ', 'JJR', 'JJS', 'LS',
        'MD', 'NN', 'NNS', 'NNP', 'NNPS',
        'PDT', 'POS', 'PRP', 'PRP$', 'RB',
        'RBR', 'RBS', 'RP', 'SYM', 'TO',
        'UH', 'VB', 'VBD', 'VBG', 'VBN',
        'VBP', 'WBZ', 'WDT', 'WP', 'WP$', 'WRB'}

# db = shelve.open('db.dat', 'r')


def deal_query(query):
    print 'Query content: ' + query
    query = query.decode('utf-8')
    q_list = query.split(' ')
    q = []
    # check which type query
    if '_' in q_list:
        print 'Query type: _'
    elif '*' in q_list:
        print 'Query type: *'
    elif 1 in [1 if e in tags else 0 for e in q_list]:
        print 'Query type: Part of Speech'
    else:
        # case 1: ?
        if 1 in [1 if e[0] == u'?' else 0 for e in q_list]:
            print 'Query type: ?'
            # check if any word's first charactor is '?'
            q = [' '.join([e[1:] if e[0] == u'?' else e for e in q_list]),
                 ' '.join([e for e in q_list if e[0] != u'?'])]
        # case 2: |
        if '|' in q_list:
            print 'Query type: |'
            index = q_list.index(u'|')
            z = [e for e in q_list if e != u'|']
            q = [' '.join([e for j, e in enumerate(z) if j != index]),
                 ' '.join([e for j, e in enumerate(z) if j != (index-1)])]
    if q:
        return q
    else:
        return [query]


def query_result2(database, q):
    result = {}
    print 'Subquery: {}'.format(q)
    for e in q:
        try:
            result[e] = database[e.encode('utf-8')][:10]
        except Exception, ex:
            result[e] = [['None', 'None', 0]]
    return result


def query_result3(cur, q):
    result = {}
    print 'Subquery: {}'.format(q)
    for e in q:
        query_str ='select * from pair where query=?'
        r_set = cur.execute(query_str, (e.encode('utf-8'),)).fetchmany(10)
        if not r_set:
            result[e] = [['None', 'None', 0]]
        else:
            x = lambda d: list(d[1:])
            result[e] = map(x, r_set)
    return result
