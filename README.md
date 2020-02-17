<h1 align="center">Welcome to GRADESK 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/sidbmw/ECOR1051-MOD2/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>


# Introduction

GRADESK is an organizational program requested by Mr. Roller to meet his
need for a marking software with a higher degree of accuracy for the spectrum of marks
between 3+ and 4++. The program he currently uses is called Mark Manager (MaMa),
our client finds it to be dissatisfactory because he is not able to use marks like 4-- or
4/4+ in MaMa and finds it to be very difficult to work around. GRADESK seeks to
address this issue by increasing the marking options in the 3+ to 4++ range to include
the in-between marks and on all other aspects mirror the functions of MaMa. These
other functionalities include managing classes, managing students in a class, adding
marks of an assignment for the whole class, and displaying all the marks a student has
received as an online evidence record. This program is targeted toward teachers
teaching courses with high academic averages, as they can use GRADESK to its
maximum potential.

## Software platforms and API's used

* Windows 10: As both of us already had Windows 10 installed, we did not bother
installing a Linux Distro. Reflecting back on this decision, we should have developed on
a Linux Distro as it’s far more reliable than Windows and less resource intensive. There
were times where 8Gb of RAM simply wasn’t enough when running PyCharm,
sqldeveloper, Github Desktop and a browser. <br />


* Oracle Database 11g Express Edition: Database used to store all data for this program <br />
* SQL Developer: Used to write GRADESK_CREATE.sql <br />
* SQLPlus <br />
* Python 3.71 (64 bit) - Python 3.72 (64 bit) <br />
* Pycharm Professional: Main IDE used to write python code <br />
* PySimpleGUI (Tk) 3.9.0 - 3.22.0: Tool used to create Python GUI's <br />
* cx_Oracle: Plugin for connecting python with database <br />


* Atom: Used in the beginning to write python code <br />
* Teletype: Plugin for atom <br />
* Git (GitHub Desktop) <br />

# The vision...
![20181111_174710](https://user-images.githubusercontent.com/46163555/71789369-b9927700-2ff8-11ea-9cea-dae039c9387f.jpg)

# User Guide

## Class selection

The home page of GRADESK, this is the first interface you will encounter after
you launch the program. On here all of the classes will be listed with information about
it like class name, period number, and school year. From here the user can initiate four
actions by pressing a corresponding button, access the class, add another class, edit
the selected class and its students, and if need be deleting the selected class.

![image](https://user-images.githubusercontent.com/16989022/71627118-bc3b3980-2bbe-11ea-89e7-2948625f34d7.png)
```
Figure 1.0
```
*only one class can be selected at a time, the program default it to the last class
(bottommost class)

## Add Class

If you choose to add a new class to the database, press the ‘Add Class’ button
on the class selection interface. In the next interface, you can enter the course code,
period number, and active year of the new class. There is an input checker in place,
course code needs to be eight or fewer characters long (should be in the format of
ICS4U-01), and the period number needs to be between 1 and 4. Once satisfied, press
‘Add Course’.

![image](https://user-images.githubusercontent.com/16989022/71627122-c3fade00-2bbe-11ea-8801-c69e2a5a9a4b.png)
```
Figure 2.0 (adding the new class ICS4U-02)
```

The next interface (figure 2.1) will ask you for the number of students you want in
the newly created class. Input needs to be an integer. Press ‘Ok’ to advance to the next
step or press ‘Cancel’ to skip the next step.

![image](https://user-images.githubusercontent.com/16989022/71627125-c78e6500-2bbe-11ea-9418-5563e7512729.png)
```
Figure 2.1
```
On this interface (figure 2.2), you will find a number of empty text boxes aligned
under first names and last names. Each row represents one student and you can add all
the students in your newly added class into database here. Press ‘Add students’ to
finish adding a new class.

![image](https://user-images.githubusercontent.com/16989022/71627134-da089e80-2bbe-11ea-86b3-9eb3c9626e28.png)
```
Figure 2.2
```

## Edit Class

First, select the class you want to edit, then press the ‘Edit Class’ button at the
bottom. The edit class interface (figure 3.0) is very similar to the add class interface, but
instead of blank text boxes, they will be filled with current information about the class
that you selected. Same input restrictions apply as the add class interface, press ‘Edit
Course’ to make changes. If you wish to edit the students in that class, press ‘Go to Edit
Students’, otherwise press ‘x’ to exit editing.

![image](https://user-images.githubusercontent.com/16989022/71627144-e2f97000-2bbe-11ea-81be-99287b6ce218.png)
```
Figure 3.0 (Editing the class ICS4U-02)
```
The edit student interface (figure 3.1) is also very similar to it add counterpart but
also having the current student data in the text boxes. You can edit the students’ first
and last names (here changing John Doe to John Wick) or delete students (deleting
Albert Schmidt) by checking the box on the same row as their name, be sure to press
the ‘Save’ button to save your changes. If you wish to add new students to the class,
press ‘Add students’ (same process as in add class).

![image](https://user-images.githubusercontent.com/16989022/71627149-e68cf700-2bbe-11ea-9e5f-5d47af2cb71a.png)
```
Figure 3.1
```
## Access a class

To view a student’s marks, click access on the class that he/she belongs to. It will
bring you to an interface like this (will not have the colorful section if that student does
not have a mark yet). Here you can see all the marks the student had received on his
assessments. Clicking on ‘Next Student’ will bring you to the next student in
alphabetical order, ‘Previous student’ brings you to the previous student in alphabetical
order.

![image](https://user-images.githubusercontent.com/16989022/71627154-ea207e00-2bbe-11ea-850a-4da24f33943a.png)

Pressing ‘Print report will open up automatically generated HTML file in your
default browser showing all of the student's marks (figure 4.1). This file can be printed
by hitting “Ctrl + P” and can also be saved.


![image](https://user-images.githubusercontent.com/16989022/71627156-ec82d800-2bbe-11ea-81a6-f543b00cb061.png)
```
Figure 4.1
```
Pressing the ‘Exit’ button will close the python interface and will lead you back to the
class selection screen.


## Add assignment

Press the ‘Add assignment’ button on the grid interface, it will present you with
two options (figure 5.0), to add one assessment for the current student or to add one
assessment for the whole class.

![image](https://user-images.githubusercontent.com/16989022/71627159-ef7dc880-2bbe-11ea-933b-8e15f1c68a73.png)
```
Figure 5.0
```
No matter which button you press, you will come to an interface (figure 5.1)
asking for information about the new assessment like the type of assessment (test,
project, quiz, etc), the name of the assessment, and the number of expectations/marks
it has. Name of assignment will only take a name in the format of a letter, a number, and
the number of expectations can only take an integer.

![image](https://user-images.githubusercontent.com/16989022/71627161-f1478c00-2bbe-11ea-8814-d22a5273f6e1.png)
```
Figure 5.1
```
Next up you will be brought to the actual marking interfaces, there is one version
for the single student and another version for the whole class. The single student's
version will have ‘Finish Marking’ instead of ‘Next Student’ button like on the whole
class version. On both versions, you will find sets of text boxes asking for expectation
and mark, expectations only accept a letter and a number, while marks take anything
that can be found on the grid (refer to 4.0). Once you are done entering the marks and


expectations, press ‘Finish Marking’ or ‘Next student’. For whole class version, you will
then need to mark this assessment for the next student (all expectations are preserved
and already filled in).

![image](https://user-images.githubusercontent.com/16989022/71627161-f1478c00-2bbe-11ea-8814-d22a5273f6e1.png)
![image](https://user-images.githubusercontent.com/16989022/71627164-f4427c80-2bbe-11ea-8b7f-91ea7a7e6e99.png)
```sh
Figure 5.2 (for the whole class),   Figure 5.3 (for a single student)
```

## Editing marks and adding comments

You can edit marks and add comments by clicking on a mark on the grid (refer to
4.0) if it has a mark on it. The comments and anomaly interface (figure 6.0) will pop up
and here you can see the previous comment and edit it in the text box, mark that one
assessment for this student as an anomaly by checking the checkbox or delete this
assessment for this student by pressing the ‘Delete this assignment’ button. Save all
changes by pressing the ‘Save’ button.

![image](https://user-images.githubusercontent.com/16989022/71627169-fb698a80-2bbe-11ea-820c-f6fc9f8f7cf4.png)
```
Figure 6.0
```
You can edit the assignment’s marks by pressing the ‘Edit’ button, it will bring
you to an interface similar to that of the marking interfaces (refer to 5.2 and 5.3) (figure
6.1). All of the marks for the student on that assignment (in this case T2) will be shown
in the text boxes. Input restrictions are the same as the marking interfaces, and you can
save your changes by pressing ‘Finish Marking’.

![image](https://user-images.githubusercontent.com/16989022/71627172-fd334e00-2bbe-11ea-9097-f1a737eae33a.png)
```
Figure 6.1
```

# Diagram of code flow
![image](https://user-images.githubusercontent.com/16989022/71627173-01f80200-2bbf-11ea-9dbd-990594d1b25d.png)

