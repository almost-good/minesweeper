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


### **First time user**

> *I want to play the game quickly to see if it's worth my time.*
>
> *I want to be informed how to play the game, in a simple manner.*
>
> *I want the gameplay to be clean, without interruptions.*
>
> *I want to select the difficulty of the game.*
>
> *I want to see the game result, together with my score.*
>
> *I want to know what I did wrong if the game is lost.*
>
> *I want to be able to quit the game.*

### **Returning user**

> *I want to be able to register.*
>
> *I want to be able to log in.*
>
> *I want my password to be stored securely.*
>
> *I want to see my top scores.*
>
> *I want to see how many wins, losses and total games I have.*
>
> *I want to see how much time I spent playing.*
>
> *I want to set the status in case I climb to the main leaderboard.*
>
> *I want to see the top scores overall.*
>
> *I want to customize the game mode.*


Back to [Table of Contents](#table-of-contents)


## **Logic**

The real-life application is moulded according to the created flowcharts. 
The flowcharts depict the flow of the app but also allow for an insight into the logic behind.

### **Flow of the app**

Displays the flow of the app as a whole, from start until the point the app is exited.
The flowchart serves as a general guideline on how the app is constructed, structured and what it will include.

<br>
<details>
<summary>Flowchart</summary>

![Flowchart](./assets/docs/flowchart/flow-app.png)
</details>
<br>

### **Flow of the game**

Displays the flow of the game. The flow starts from the **"play game"** selection, goes over difficulty modes, the game, it's results and finally to the game menu itself. 
The flowchart will help with visualising how the gameplay should look, mainly from the player's point of view.

<br>
<details>
<summary>Flowchart</summary>

![Flowchart](./assets/docs/flowchart/flow-game.png)
</details>
<br>

### **Additional flows**

Additional flows are flows of special commands and functions.

**Input validation** is a function that appears on numerous occasions. It's one of the most important functions as it ensures the values taken from the user are, in fact valid. Validation was taken out of the main flow, to ensure the flowchart's tidiness and readability.<br>

**Menu, Exit and Help commands** are global commands of the app. They can be accessed from almost every part of the app, even if the input was intended for a different purpose.
- **Menu** jumps instantly to the main menu, even if mid-game.
- **Exit** exits the app completely.
- **Help** displays the commands for that specific part of the program. 
  - *The reason behind the help is:* The commands are initially shown at the top of the screen, but as the user interacts with the page, commands are pushed further away. The user can forget how to properly enter commands and if they do, they can simply enter **"help"** and commands will be reprinted.

<br>
<details>
<summary>Flowchart</summary>

![Flowchart](./assets/docs/flowchart/flow-helper.png)
</details>
<br>

### **Logic of the game**

The logic of the game includes insight into how the game functions behind the scenes.

<br>
<details>
<summary>Flowchart</summary>

![Flowchart](./assets/docs/flowchart/logic-game.png)
</details>
<br>

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