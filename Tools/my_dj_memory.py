# Created by Traburiss on 2016/3/16
import sqlite3


class MyDjMemory(object):
    __DB_NAME = "DJ.DB"
    __TABLE_NAME = "dj_memory_table"
    connect = None
    cursor = None

    def insert(self, face_state, next_step, win_times, lose_times):
        self.open()
        self.cursor.execute('INSERT INTO ' + self.__TABLE_NAME + ' (face_state,next_step ,win_times,lose_time) VALUES(?, ?, ?, ?)', [face_state, next_step, win_times, lose_times])
        self.close()

    def search(self):
        self.open()
        value = self.cursor.execute("select * from " + self.__TABLE_NAME).fetchall()
        self.close()
        return value

    def search_by_face_state(self, face_state):
        self.open()
        value = self.cursor.execute("select * from " + self.__TABLE_NAME + " WHERE face_state = ?", [face_state]).fetchall()
        self.close()
        return value

    def open(self):
        self.connect = sqlite3.connect(self.__DB_NAME)
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute('create table '+ self.__TABLE_NAME +' (id integer primary key AUTOINCREMENT, face_state varchar(9), next_step integer, win_times integer, lose_time integer)')
        except:
            pass

    def close(self):
        self.cursor.close()
        self.connect.commit()
        self.connect.close()
