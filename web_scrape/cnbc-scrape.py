import cnbc

json_resp = cnbc.list_symbol_news(symbol='AAPL',
                                  api_key='f3c7547811mshb7e5680d6a29edcp1387fcjsncb14f156c54a')

print(json_resp)