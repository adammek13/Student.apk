from flet import * 
import sqlite3 

conn=sqlite3.connect("dato.db",check_same_thread=False) 
cursor=conn.cursor() 



cursor.execute(""" CREATE TABLE IF NOT EXISTS student(      
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     stdname TEXT,
     stdphone TEXT,
     stdaddress TEXT,
     stdmathematique INTEGER,    
     stdfrench INTEGER,
     stdenglish INTEGER,
     stddrawing INTEGER,
     stdphyisqus INTEGER,
     stdchemistry INTEGER                                    
 )""")

conn.commit() 

def main(page:Page):
    page.title= 'StudengManager'
    page.scroll= 'auto'
    page.window.top=1
    page.window.left=960
    page.window.width=39
    page.window.height=740
    page.bgcolor='white'
    page.theme_mode=ThemeMode.LIGHT

    

    tabe_name='student'
    query=f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result=cursor.fetchone()
    row_count=result[0]
    row_count=str(row_count)
    
    def add(e):
        cursor.execute("INSERT INTO STUDENT(stdname,stdphone,stdaddress,stdphysics,stdmathematique,stdfrench,stdenglish,stdchemistry,stddrawing) VALUES(?,?,?,?,?,?,?,?,?)",(tname.value,tphone.value,taddress.value,mathematique.value,physics.value,chemistry.value,drawing.value,french.value,english.value))
        conn.commit()

    def show(e):
        c=conn.cursor()
        c.execute("SELECT * FROM student")
        users=c.fetchall()
        for user in users:
            print(user)


        if not users =="":
            keys=['id','stdname','stdphone','stdaddress','stdmathematique','stdphysics','stdenglish','stdfrench','stdchemistry','stddrawing']
            result=[dict(zip(keys,values)) for values in users]
            print(users)
            for x in result:
              page.add(
                 Card(
                      color="white",
                      content=Container(
                         content=Column([
                           Row([
                              Text("Full Name:"+x["stdname"],color="black")
                           ],alignment=MainAxisAlignment.CENTER),
                           

                           Row([
                            Text("Phone:"+str(x["stdphone"]),color="black")
                            
                           ],alignment=MainAxisAlignment.CENTER),

                           Row([
                               Text("Address:" +x["stdaddress"],color="black")
                           ],alignment=MainAxisAlignment.CENTER),

                           Row([
                           Text("English:"+str(x["stdenglish"]),color="black"),
                           Text("Mathematique:"+str(x["stdmathematique"]),color="black"),
                           Text("Physics"+str(x["stdphysics"]),color="black"),
                           ],alignment=MainAxisAlignment.CENTER),

                           

                           Row([
                           Text("French:"+str(x["stdfrench"]),color="black"),
                           Text("Chemstry:"+str(x["stdchemistry"]),color="black"),
                           Text("Drawing"+str(x["stddrawing"]),color="black"),
                           ],alignment=MainAxisAlignment.CENTER)


                          ])
                      )
                 )
              )


              page.update()


    
    tname=TextField(label='Student full Name', icon=icons.PERSON,height=38)
    tphone=TextField(label='Student Phone Number', icon=icons.PHONE,height=38)
    taddress=TextField(label='Student Adress', icon=icons.LOCATION_CITY,height=38)
   



   
    marktext=Text("Marks student", text_align="center",weight="bold",)
    mathematique=TextField(label="Math",width=110,height=38)
    french=TextField(label="French",width=110,height=38)
    physics=TextField(label="Physics",width=110,height=38)
    english=TextField(label="English",width=110,height=38)
    chemistry=TextField(label="Chemistry",width=110,height=38)
    drawing=TextField(label="Drawing",width=110,height=38)
    
    


    add_buuton=ElevatedButton(
         "Add New Student",
         width=170,
         style=ButtonStyle(bgcolor="blue",color="white",padding=15),
         on_click=add
    )


    
    
    show_buuton=ElevatedButton(
         "Display students",
         width=170,
         style=ButtonStyle(bgcolor="blue",color="white",padding=15),
         on_click=show
    )


    page.add(
        Row([
            Image(src="apk.img.png",width=280)
        ],alignment=MainAxisAlignment.CENTER),

        
        Row([
            Text("MyStudent",size=20,weight="bold",color="black")
        ],alignment=MainAxisAlignment.CENTER),

        

        
        Row([
            Text("Number of Student:",size=20,color="black"),
            Text(row_count,size=20,color="blue")
        ],alignment=MainAxisAlignment.CENTER),

            
        tname,
        tphone,
        taddress,

         
         Row([
             marktext
         ],alignment=MainAxisAlignment.CENTER),
        
        Row([
             mathematique,french,physics
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            english,chemistry,drawing
        ],alignment=MainAxisAlignment.CENTER),
         
        Row([
            add_buuton,show_buuton
        ],alignment=MainAxisAlignment.CENTER),
        
    )

    

    page.update()
app(main)
    
