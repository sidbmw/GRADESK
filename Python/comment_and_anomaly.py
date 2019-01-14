import PySimpleGUI as sg
import cx_Oracle
from input_checker import check_string as check_string


def do_it(student_id, mark):
    # con = cx_Oracle.connect('EOM/EOM@127.0.0.1/xe')
    # cur = con.cursor(scrollable=True)
    sg.ChangeLookAndFeel('DarkBlue')

    layout = [[sg.Text('Comments', font=("Helvetica", 11), text_color='white', justification='left')],
              [sg.InputText(size=(25, 0))],  # 250 char limit
              [sg.Text('      Mark as anomaly'), sg.Checkbox('')],
              [sg.Button('Delete this assignment', button_color=('black', 'orange'), key='delete')],
              [sg.Text('')],
              [sg.Button('Save', button_color=('black', 'orange'), key='save')]]

    window = sg.FlexForm('Class selection ', auto_size_text=True, default_element_size=(40, 1)).Layout(layout)

    while True:
        event, values = window.Read()

        if event == 'delete':
            cur.execute("select * from EOM_MARKS")
            for row in cur:  # problem "cx_Oracle.InterfaceError: not a query"
                cur.execute("UPDATE EOM_MARKS SET DELETED_FLAG=:v_delete WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                            v_delete='Y', v_id=student_id, v_mark=mark)
                print('1')
            con.commit()
            sg.Popup('All marks associated with ' + mark + " has been deleted")
            break

        if event == 'save':
            comments = values[0]
            if check_string(comments, 'str', 250):
                if values[1]:  # anomaly
                    cur.execute("select * from EOM_MARKS")
                    for row in cur:  # problem "cx_Oracle.InterfaceError: not a query"
                        cur.execute("UPDATE EOM_MARKS SET COMMENTS=:v_comment, ANOMALY=:v_anomaly "
                                    "WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                                    v_comment=comments, V_anomaly='Y', v_id=student_id, v_mark=mark)
                        print('2')
                    con.commit()

            cur.execute("UPDATE EOM_MARKS SET COMMENTS = :v_comment WHERE STUDENT_ID=:v_id AND TASK=:v_mark",
                        v_comment=comments, v_id=student_id, v_mark=mark)
            con.commit()

        if event is None:
            break
    window.Close()


do_it(1, 'T1')
