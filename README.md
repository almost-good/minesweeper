# Minesweeper
**Minesweeper** is a *puzzle-type text-based game* which runs directly in the terminal. The objective is to flag all mines in the shortest amount of time. The player can choose the desired difficulty from the predefined options or customize the game rules directly. The entire app can be accessed as a guest or as a registered user. If the user chooses to register, they will gain access to various gameplay information and be able to change their status.

## **Table of Contents**

- [Developer's Note](#developers-note)
- [How to Play](#how-to-play)
- [UX - User Experience Design](#ux---user-experience-design)
- [Logic](#logic)
- [Data Model](#data-model)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)


## **How to Play**
**Minesweeper** is a *single-player puzzle text-based game*. The objective is to *flag all mines* in the shortest amount of time. The fields of the game grid have three different states: **hidden, displayed and flagged**.<br><br>
A **hidden state** means the field did not receive any action yet. It's free to select for manipulation: *to be displayed or flagged*.<br>
The **displayed field** shows the number of mines surrounding that specific field. If the player selects and displays the field which indicates there are no mines nearby, *then all adjacent fields will be displayed*, until we get to the indicator that there is a mine nearby in either number or flag format. The displayed field cannot receive any action.<br>
The **flagged field** is an indicator of potential mine. When the user suspects there is a mine under the hidden field, they should flag it, otherwise, if the field is selected, and there is indeed a mine, it will be automatic loss. Flagged fields can be unflagged. This is important because there are only *so many flags available as there are mines on the grid*.<br><br>
If the user set all of their flags and did not win the game, it means some of the flags might not be positioned correctly. When all the correct fields are flagged the game is won. The game can also be won if the number of hidden fields is equal to mine count, there are no non-mine options left anyway. If you accidentally display a bomb, the game is instantly lost and the player will see the actual mine placements.

**Commands**
- Display a field: 
  - **row-value, col-value**
  - Correct examples:
    > *3,4*
    >
    > *3, 4*
    >
    > *3 , 4*
  - Incorrect examples:
    > *r3, 4*
    >
    > *3 4*
- Flag a mine: 
  - **flag-keyword, row-value, col-value**
  - Correct examples:
    > *flag, 3,4*
    >
    > *Flag , 3 , 4*
    >
    > *FLaG      , 3, 4*
  - Incorrect examples:
    > *f lag, 3,4*
    >
    > *flag3, 4*
    >
    > *mflag, 3, 4*
- Unflag a mine: 
  - Same as flag a mine.
  - **flag-keyword, row-value, col-value**

### **Game Modes**
The player can choose between easy, normal, hard and fun modes.<br>
All modes except the fun one come with a predefined number of grid rows, columns and mines.

#### **Easy mode**
  > *Num of rows:*
  >
  > *Num of cols:*
  >
  > *Num of mines:*

#### **Normal mode**
  > *Num of rows:*
  >
  > *Num of cols:*
  >
  > *Num of mines:*

#### **Hard mode**
  > *Num of rows:*
  >
  > *Num of cols:*
  >
  > *Num of mines:*

#### **Fun mode**
- Fun mode allows players to customize the game. The player can select a number of rows, columns and mines they wish to play with, but is at the same time restricted with minimum and maximum values they can select.
  > *Num of rows:*
  >
  > *Num of cols:*
  >
  > *Num of mines:*


Back to [Table of Contents](#table-of-contents)


## **Developer's Note**


Back to [Table of Contents](#table-of-contents)


## **UX - User Experience Design**


Back to [Table of Contents](#table-of-contents)


## **Logic**


Back to [Table of Contents](#table-of-contents)


## **Data Model**


Back to [Table of Contents](#table-of-contents)


## **Features**


Back to [Table of Contents](#table-of-contents)


## **Testing**


Back to [Table of Contents](#table-of-contents)


## **Bugs**


Back to [Table of Contents](#table-of-contents)


## **Technologies Used**


Back to [Table of Contents](#table-of-contents)


## **Deployment**


Back to [Table of Contents](#table-of-contents)


## **Credits**


Back to [Table of Contents](#table-of-contents)