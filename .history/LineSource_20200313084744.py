class LineSource:
    reference_client = ""
    reference_sap = ""
    designation = ""
    capacity = -1
    cnt_product_pack = -1
    buy_price = -1.0
    sell_price = -1.0
    barcode = -1
    is_empty = True
    is_title = False

    def __init__(self, ref_client, ref_sap, designation, capacity, cnt_product_pack, buy_price, sell_price, barcode):
        if designation != "" or ref_client == "" or ref_sap == "" or barcode == "" or capacity == "" or cnt_product_pack == "" or buy_price == "" or sell_price == "":
            self.is_empty = False
            if designation != "" and (ref_client == "" and ref_sap == "" and barcode == "" and capacity == "" and cnt_product_pack == "" and buy_price == "" and sell_price == ""):
                self.is_title = True
                self.designation = designation
            else:
                self.reference_client = ref_client
                self.reference_sap = ref_sap
                self.designation = designation
                if capacity.isdigit():
                    self.capacity = int(capacity)
                if cnt_product_pack.isdigit():
                    self.cnt_product_pack = int(cnt_product_pack)
                if buy_price.isdigit():
                    self.buy_price = float(buy_price)
                if sell_price.isdigit():
                    self.sell_price = float(sell_price)
                if barcode.isdigit():
                    self.barcode = int(barcode)
        
