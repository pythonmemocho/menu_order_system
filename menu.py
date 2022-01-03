#クラスを作成
class Menu:
    #名前、値段、画像を初期値に設定
    def __init__(self,name,price,image) -> None:
        self.name = name,
        self.price = price,
        self.image = image
    
    #品名を取り出すメソッド
    #インスタンス化した値がタプルに入っているため取り出しが必要
    def get_name(self):
        return self.name[0]
    
    #値段を取り出すメソッド
    #品名と同じ理由で取り出しが必要
    def get_price(self):
        return self.price[0]
    
    #小計を計算するメソッド
    def getTotalPrice(self,ordercount):
        ordercount = int(ordercount)
        total = ordercount * self.price[0]
        return total
    
