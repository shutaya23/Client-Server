# Client-Server
使用Python透過Socket連線讓Server和Client建立溝通並傳送訊息

Server:
使不間斷聆聽
建立socket，socket指定某個可用位址(IP/Port)
設定最大連接數
連線client，c_socket存放本次連線、addr存放位址資訊
輸出連接的次數和IP、位置和接收到的字串

Client:
建立socket，指定要用的位址(IP/Port)
封裝存送資料
回傳的資料
輸出連接開始訊息、接收server成功回傳的訊息

