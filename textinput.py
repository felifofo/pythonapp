from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import mysql.connector as sql

class MyApp(App):
    def build(self):
        layout=GridLayout(cols=1)
        self.username=TextInput(text="enter the username")
        self.password=TextInput(text="enter the password")
        submit=Button(text="submit", on_press=self.submit)

        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(submit)

        return layout

    def submit(self,obj):
        un=self.username.text
        pw=self.password.text
        con=sql.connect(host="localhost", user="root", password="", database="uno")
        cur=con.cursor()
        query="INSERT INTO users(username,password) VALUES(%s,%s)"
        val=(un,pw)
        cur.execute(query,val)
        con.commit()
        con.close()

if __name__=="__main__":
    MyApp().run()
