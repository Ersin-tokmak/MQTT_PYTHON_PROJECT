





                    ########################333### (TR)   İKİ TANE DENEME KODUM VAR    (ING) THERE ARE TWO CODES I TRIED AT THE BEGINNING  ^###########################################3    



###   Necassary library       pyside2 , paho






# import os
# import sys
# from PySide2.QtCore import*
# from PySide2.QtGui import *
# from PySide2.QtWidgets import*
# from PySide2 import *
# import paho.mqtt.client as paho
# from paho import mqtt
# # import source_paho
# # from paho.mqtt import client as mqtt_client

# from MQTT_WİNDOW_ui import *


# class UIfunctions(QMainWindow, Ui_MainWindow):


#     def __init__(self) -> None :
#         super().__init__()
#         self.setupUi(self)
        # self.broker = BROKER_URL_ADRESS
        # self.port = PORT_NUB
        # self.topic = TOPİC
        # self.topic_sub = TOPİC_SUBSC_VALUE
        # self.client_id = CLİENDİD
        # self.username = YOUR USERNAME
        # self.password = YOURPASSWORD
#         # self.deviceID ="B7004F5D-A389-4A2A-AB81-381052B0D6C1"
#         # self.payload=self.lineEdit.text()

#         self.lab=[self.label]
#         # self.send_btn.clicked.connect(self.publ)
#         self.client = paho.Client(client_id=self.client_id, userdata=None, protocol=paho.MQTTv5)


#         self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
#         # buraya username ve password u girmeniz gerek
#         self.client.username_pw_set(self.username, self.password)
#         #buraya cluster URL yi girmeniz gerekiyor ve port numarasını
#         self.client.connect(host=self.broker, port=self.port)

#         self.client.on_connect = self.on_connect
#         self.client.on_subscribe = self.on_subscribe
#         self.client.on_message = self.on_message

#         self.client.on_publish =self.on_publish
#         self.send_btn.clicked.connect(self.client.on_publish)

#         self.client.subscribe(topic=self.topic_sub, qos=0)
#         # self.client.publish(topic=self.topic, payload=self.payload, qos=0)

#         # self.send_btn.clicked.connect(self.on_publish)
#         # self.client.loop_forever()

#     def on_connect(self,client, userdata, flags, rc, properties=None):
#         print("bağlanmak için deniyor %s." % rc)


#     def on_publish(self):
#         print("1.adim")
#         payload = self.lineEdit.text()  # lineEdit'den değeri alın
#         mid = self.client.publish(topic=self.topic, payload=payload, qos=0)
#         print("mid: " + str(mid))


#     def on_subscribe(self,client, userdata, mid, granted_qos, properties=None):

#         print("2.adim")
#         print("Subscribed: " + str(mid) + " " + str(granted_qos))

#     def on_message(self,client, userdata, msg):

#         print("burasi çaliyor")
#         print("3.adim")
#         print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
#         print("4.adim")
#         self.lab[0].setText(
#                             f"<html><head/><body><p><span style=' font-weight:600;'>deger : </span> {str(msg.payload)} </p></body></html>"
#                         )




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     appUI = UIfunctions()
#     appUI.show()
#     sys.exit(app.exec_())



######################3---------------------------------------------------------------------------------------########################




# import os
# import sys
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
# from PySide2 import *
# import paho.mqtt.client as paho
# from paho import mqtt

# from MQTT_WİNDOW_ui import *


# class UIfunctions(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
        # self.broker = BROKER_URL_ADRESS
        # self.port = PORT_NUB
        # self.topic = TOPİC
        # self.topic_sub = TOPİC_SUBSC_VALUE
        # self.client_id = CLİENDİD
        # self.username = YOUR USERNAME
        # self.password = YOURPASSWORD

#         self.lab = [self.label]
#         self.client = paho.Client(client_id=self.client_id, userdata=None, protocol=paho.MQTTv5)
#         self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
#         self.client.username_pw_set(self.username, self.password)
#         self.client.connect(host=self.broker, port=self.port)
#         self.client.on_connect = self.on_connect
#         self.client.on_subscribe = self.on_subscribe
#         self.client.on_message = self.on_message
#         self.client.on_publish = self.on_publish

#         self.send_btn.clicked.connect(self.publish_message)  # Butona bağlantı eklendi

#         self.client.subscribe(topic=self.topic_sub, qos=0)

#     def on_connect(self, client, userdata, flags, rc, properties=None):
#         print("bağlanmak için deniyor %s." % rc)

#     def on_publish(self, client, userdata, mid):
#         print("1.adim")
#         print("mid: " + str(mid))

#     def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
#         print("2.adim")
#         print("Subscribed: " + str(mid) + " " + str(granted_qos))

#     def on_message(self, client, userdata, msg):
#         print("burasi çaliyor")
#         print("3.adim")
#         print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
#         print("4.adim")
#         payload = msg.payload.decode("utf-8")  # Payload'ı uygun bir şekilde çözümle
#         self.lab[0].setText(
#             f"<html><head/><body><p><span style='font-weight:600;'>deger : </span>{payload}</p></body></html>"
#         )
#     def publish_message(self):
#         payload = self.lineEdit.text()  # lineEdit'den değeri alır
#         self.client.publish(topic=self.topic, payload=payload, qos=0)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     appUI = UIfunctions()
#     appUI.show()
#     sys.exit(app.exec_())


#######################################-------------------------------------------------------###################################################

import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import *
import paho.mqtt.client as paho
from paho import mqtt

from MQTT_WİNDOW_ui import *


class UIfunctions(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        ######## (TR) KODU ÇALIŞTIRIRKEN BU ALT KISMI AÇMALISINIZ   (ING) YOU MUST OPEN THIS SECTION WHEN RUNNING THE CODE ^#######
        
        # self.broker = BROKER_URL_ADRESS
        # self.port = PORT_NUB
        # self.topic = TOPİC
        # self.topic_sub = TOPİC_SUBSC_VALUE
        # self.client_id = CLİENDİD
        # self.username = YOUR USERNAME
        # self.password = YOURPASSWORD



        self.lab = [self.label]
        self.client = paho.Client(client_id=self.client_id, userdata=None, protocol=paho.MQTTv5)
        self.client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        self.client.username_pw_set(self.username, self.password)
        self.client.connect(host=self.broker, port=self.port)
        self.client.on_connect = self.on_connect
        self.client.on_subscribe = self.on_subscribe
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

        self.send_btn.clicked.connect(self.publish_message)  # Butona bağlantı eklendi
        self.conect_btn.clicked.connect(self.on_connect)
        self.client.subscribe(topic=self.topic_sub, qos=0)

    def on_connect(self, client, userdata, flags, rc, properties=None):
        print("bağlanmak için deniyor %s." % rc)

    def on_publish(self, client, userdata, mid):
        print("1.adim")
        print("mid: " + str(mid))

    def on_subscribe(self, client, userdata, mid, granted_qos, properties=None):
        print("2.adim")
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    def on_message(self, client, userdata, msg):
        print("3.adim")
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        print("4.adim")
        payload = msg.payload.decode("utf-8")  # Payload'ı uygun bir şekilde çözümle
        self.lab[0].setText(
            f"<html><head/><body><p><span style='font-weight:600;'>deger : </span>{payload}</p></body></html>"
        )
        
    def publish_message(self):
        payload = self.lineEdit.text()  # lineEdit'den değeri alır
        self.client.publish(topic=self.topic, payload=payload, qos=0)
        
    def subscribe(self):
        self.client.subscribe(topic=self.topic,qos=0)
        
        print("Abone oldu")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appUI = UIfunctions()
    appUI.show()
    sys.exit(app.exec_())