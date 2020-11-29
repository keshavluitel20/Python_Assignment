def exchange_char(str):
    return str[-1:] + str[1:-1] + str[:1]


print(exchange_char('Insight'))
