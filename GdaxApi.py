import gdax

class GdaxApi(object):
    public_client = gdax.PublicClient()

    def get_val(self,val):
        res = (self.public_client.get_product_ticker(product_id=val))
        return float(res[u'price'])