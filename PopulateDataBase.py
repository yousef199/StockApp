import _sqlite3
import alpaca_trade_api as tradeapi
import ApiConfig

connection = _sqlite3.connect('app.db')
cursor = connection.cursor()

api = tradeapi.REST(ApiConfig.API_KEY, ApiConfig.SECRET_KEY, base_url='https://paper-api.alpaca.markets') # or use ENV Vars shown below
assets = api.list_assets()
for asset in assets:
    if (asset.status == 'active' and asset.tradable):
        cursor.execute("""
                    INSERT INTO stock (symbol, company)
                    VALUES (?, ?)
            """, (asset.symbol, asset.name))

#Hi

connection.commit()