import PySimpleGUI as sg
import cx_Oracle

from input_checker import check_string as check_string


def do_it(student_id, mark):
    con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
    cur = con.cursor(scrollable=True)
    cur.execute("select COMMENTS from EOM_MARKS where STUDENT_ID=:student_id and TASK=:mark",
                               student_id=student_id, mark=mark)
    old_comments = cur.fetchone()
    print(old_comments)

    layout = [[sg.Text('Comments', font=("Helvetica", 11), text_color='white', justification='left')],
              [sg.InputText(old_comments, size=(250, 0))],
              [sg.Text('      Mark as anomaly'), sg.Checkbox('')],
              [sg.Button('Delete this assignment', button_color=('black', 'orange'), key='_delete_')],
              [sg.Text('')],
              [sg.Button('Save', button_color=('black', 'orange'), key='_save_')]]

    window = sg.Window('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    while True:

        event, values = window.Read()
        # print(event, values)
        if event is None or event == 'Exit':
            window.Close()

            if event == '_delete_':
                cur.execute("UPDATE EOM_MARKS SET DELETED_FLAG=:v_delete WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                            v_delete='Y', v_id=student_id, v_mark=mark)
                print('1')
                con.commit()
                sg.Popup('All marks associated with ' + mark + " has been deleted")
                break

            if event == '_save_':
                comments = values[0]
                if values[1]:  # anomaly
                    cur.execute("UPDATE EOM_MARKS SET COMMENTS=:v_comment, ANOMALY=:v_anomaly WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                                v_comment=comments, V_anomaly='Y', v_id=student_id, v_mark=mark)
                    print('2')
                    con.commit()

        con.commit()
